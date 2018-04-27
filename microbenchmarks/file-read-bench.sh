#!/bin/bash
## Runs 5 latency experiments for single python file reads, with varying
## file sizes

cd test_modules/
python run_file_latency_bench.py 0 10K >> ../data/file-read-latency-stack-depth-10K.csv
python run_file_latency_bench.py 25 10K >> ../data/file-read-latency-stack-depth-10K.csv
python run_file_latency_bench.py 50 10K >> ../data/file-read-latency-stack-depth-10K.csv
python run_file_latency_bench.py 75 10K >> ../data/file-read-latency-stack-depth-10K.csv
python run_file_latency_bench.py 100 10K >> ../data/file-read-latency-stack-depth-10K.csv
python run_file_latency_bench.py 0 10M >> ../data/file-read-latency-stack-depth-10M.csv
python run_file_latency_bench.py 25 10M >> ../data/file-read-latency-stack-depth-10M.csv
python run_file_latency_bench.py 50 10M >> ../data/file-read-latency-stack-depth-10M.csv
python run_file_latency_bench.py 75 10M >> ../data/file-read-latency-stack-depth-10M.csv
python run_file_latency_bench.py 100 10M >> ../data/file-read-latency-stack-depth-10M.csv
