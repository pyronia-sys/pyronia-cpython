#!/bin/bash
## Runs 6 latency experiments for single python file reads, with varying
## file sizes

python file_read.py 1K >> data/file-read-latency.csv
python file_read.py 10K >> data/file-read-latency.csv
python file_read.py 100K >> data/file-read-latency.csv
python file_read.py 1M >> data/file-read-latency.csv
python file_read.py 10M >> data/file-read-latency.csv
python file_read.py 100M >> data/file-read-latency.csv
