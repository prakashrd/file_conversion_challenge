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
#### Run the container
<pre><code>docker run -d --name my_test file-conversion-challenge</code></pre>
#### get the container instance id to view the generated
<pre><code>jai-mac:file_conversion_challenge jai$ docker ps -a
CONTAINER ID        IMAGE                       COMMAND                  CREATED             STATUS                     PORTS               NAMES
432dd7061125        file-conversion-challenge   "python file_convers…"   6 seconds ago       Exited (0) 5 seconds ago                       my_test</code></pre>
#### copy the output from container
the program takes the default values  [specs.json](data/spec.json) and [fixed_width_file](data/fixed_width.dat)
generates the delimited file to `output` directory
<pre><code>jai-mac:file_conversion_challenge jai$ docker cp 432dd7061125:/app/output/ ~/
jai-mac:file_conversion_challenge jai$ ls -l ~/output/
total 8
-rw-r--r--  1 jai  staff  1040 24 Aug 13:25 delimited_output.csv
jai-mac:file_conversion_challenge jai$ wc -l ~/output/delimited_output.csv 
      10 /Users/jai/output/delimited_output.csv
jai-mac:file_conversion_challenge jai$ head -n 1 ~/output/delimited_output.csv 
f1;f2;f3;f4;f5;f6;f7;f8;f9;f10
jai-mac:file_conversion_challenge jai$ 
</code></pre>

### Usage without Docker
- `python file_conversion.py`
- The solution accepts the following *optional* parameters
    - `-s` specs.json file path by default takes `data/specs.json`
    - `-f` fixed width file path by default takes `data/fixed_width.dat`
    - `-o` output path for generated delimited file by default writes to `output/delimited_output.csv`
 - `python file_conversion.py -f ./data/specs.json -s ./data/fixed_width.dat -o output/delimited.csv`
 
### ToDo
1. document passing files as arguments through docker
1. mount docker output directory on to host 
    