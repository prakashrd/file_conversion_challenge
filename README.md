#File Conversion Challenge
Converts a fixed width file to a delimited csv text file.

## Overview

### Requirements
1. Install [Docker 2.3.0.4 or above](https://docs.docker.com/get-docker/)
1. Optional [Python 3.7 or above](https://www.python.org/downloads/) 

### Inputs
1. specs.json
1. fixed_width.dat file

### Usage with Docker
#### Build Docker Image
<pre><code>docker build -t file-conversion-challenge .</code></pre>
#### Run the container with mount 
The following runs the docker image `file-conversion-challenge` and mounts the docker output directory
on host directory which will have extracted delimited file
<pre><code>docker run -d --name my_test -v ~/my_output:/app/output file-conversion-challenge</code></pre>

the program takes the default values  [specs.json](data/spec.json) and [fixed_width_file](data/fixed_width.dat)
generates the delimited file to `output` directory which will be mounted to `~/my_output/`
<pre><code>jai-mac:file_conversion_challenge jai$ ls -l ~/my_output/
total 8
-rw-r--r--  1 jai  staff  1040 24 Aug 13:25 delimited_output.csv
jai-mac:file_conversion_challenge jai$ wc -l ~/my_output/delimited_output.csv 
      10 /Users/jai/output/delimited_output.csv
jai-mac:file_conversion_challenge jai$ head -n 3 ~/my_output/delimited_output.csv 
f1;f2;f3;f4;f5;f6;f7;f8;f9;f10
row1£;12ERokpycGTl;3Pl;2h;13lUODFxmpDRE;7RTHvLc;10YLXagLva;13RSdcdylHldT;20EwhTiEAyBoRuoKUnOj;13ESLvoMugZWp
row2£;12DnywieKRFu;3yx;2w;13pxxGYoockCQ;7MYZTQf;10WKMiqISg;13HTpEmFDquZa;20KVVFbAKOITBomkHWqW;13cjaWsxVjYCc
jai-mac:file_conversion_challenge jai$ 
</code></pre>

### Usage without Docker
- `python file_conversion.py`
- The solution accepts the following *optional* parameters
    - `-s` specs.json file path by default takes `data/specs.json`
    - `-f` fixed width file path by default takes `data/fixed_width.dat`
    - `-o` output path for generated delimited file by default writes to `output/delimited_output.csv`
 - `python file_conversion.py -f ./data/specs.json -s ./data/fixed_width.dat -o output/delimited.csv`
 A sample output snippet
 <pre><code>f1;f2;f3;f4;f5;f6;f7;f8;f9;f10
row1£;12ERokpycGTl;3Pl;2h;13lUODFxmpDRE;7RTHvLc;10YLXagLva;13RSdcdylHldT;20EwhTiEAyBoRuoKUnOj;13ESLvoMugZWp
row2£;12DnywieKRFu;3yx;2w;13pxxGYoockCQ;7MYZTQf;10WKMiqISg;13HTpEmFDquZa;20KVVFbAKOITBomkHWqW;13cjaWsxVjYCc
row3£;12RxxFgEifGe;3Gc;2c;13soqOuFGGcrD;7qkiuYD;10sTzLkLVD;13DNpCoBxISBl;20NNKhQGyXlGFkBgvQLM;13fqCGLOYIRdv
row4£;12SgYVITGXRD;3rI;2M;13PvnrQygyXAT;7ZICpuE;10eqrtVufp;13SkMFYBgNngu;20JyMistPZCKKPsSQsWZ;13UOHJCRapmVu
row5£;12hViTcnwhac;3NE;2W;13MIFdaetQwfd;7ycrpxC;10lKiDeTWt;13SvzUCyzcJqf;20QeuBWaXudLicMIMJRF;13NCBiASLrHWZ
row6£;12utAfEEeKGj;3zv;2j;13SLJIttlVSwB;7nbjXwr;10zovxgWyW;13HnTznuwaGkh;20HCVQyXSgyYunnJooza;13DrcjBRzzVQn
row7£;12MGfsDmXOlS;3pz;2j;13PJSvZCjrmbE;7jtVgzh;10nhjDUrTy;13WHazUJNuWKv;20xkSKzdoLEDHpMgvWbP;13YiHIwxsEEXx
row8£;12DADjXIAhow;3bR;2P;13tjlEhFoKMkz;7KKDhja;10FyGPpkaS;13WKJagjwENIj;20oLWHWjrrmeqHFmrAja;13snMiSRbhMae
row9£;12TiuKiYiKrh;3DE;2f;13yfAZmbUcyhg;7DRmNng;10MZLdFzmS;13YiRXHVxszfQ;20dkXGAiSLwPeTXxTgXn;13tPlFNucSJEE
row10;£12PvGYecUTK;A3T;U2;G13YsWgAimozO;n7TcotP;o10toQWHtE;f13yvALbYAjmM;R20PiXPpwSZIBqPnPZcE;g13MfEQwLcIUL</code></pre>

### ToDo
1. document passing files as arguments through docker
1. add logger     