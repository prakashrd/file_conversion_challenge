import json
import csv
import argparse
from typing import Tuple, List


def argument_parser():
    p = argparse.ArgumentParser(
        description="converts a fixed width windows-1252 encoded file to delimited utf-8 file"
    )
    p.add_argument(
        "-s",
        "--specs",
        required=False,
        type=str,
        help="spec.json file path",
        default="./data/spec.json"
    )
    p.add_argument(
        "-f",
        "--fixed_width_file",
        required=False,
        type=str,
        help="fixed width input file path",
        default="./data/fixed_width.dat"
    )
    p.add_argument(
        "-o",
        "--delimited_output_file",
        required=False,
        type=str,
        help="fixed width input file path",
        default="./output/delimited_output.csv"
    )
    args = p.parse_args()

    return args.specs, args.fixed_width_file, args.delimited_output_file


def parse_for_specs(specs_file) -> Tuple[any, any, any, any, any]:
    try:
        with open(specs_file) as fp:
            d = json.load(fp)
            return (
                    d['ColumnNames'],
                    d['Offsets'],
                    d['FixedWidthEncoding'],
                    d['IncludeHeader'],
                    d['DelimitedEncoding']
                )

    except KeyError as e:
        print(f'key error: {e}')
        raise e


def parse_row(row='', offset_lens=None) -> List[str]:
    pos = 0
    ret = []

    for offset in offset_lens:
        ret.append(row[pos:pos+offset].strip())
        pos += offset

    return ret


def parse_and_generate_output(specs_file, input_file, delimited_file):
    columns, offsets, fixed_width_encoding, include_header, delimited_encoding = parse_for_specs(specs_file)
    offsets_int = [int(o) for o in offsets]

    try:
        with open(delimited_file, 'w', encoding=delimited_encoding, newline='') as fp:
            csv_writer = csv.writer(fp, delimiter=';')

            with open(input_file, 'r', encoding=fixed_width_encoding) as input_fp:
                if include_header:
                    csv_writer.writerow(columns)

                for row in input_fp.readlines():
                    if len(row) == 0:
                        continue
                    csv_writer.writerow(parse_row(row, offsets_int))

    except ValueError as ve:
        print(f"exception in opening file: {ve}")
        raise ve
    except LookupError as le:
        print(f'problem reading the file: {le}')
        raise le
    except Exception as e:
        print(f"error while parsing and writing: {e}")
        raise e


if __name__ == '__main__':
    try:
        specs, fixed_width_file, output_file = argument_parser()
        parse_and_generate_output(specs, fixed_width_file, output_file)
    except Exception as err:
        print(f'error with parsing and converting: {err}')
