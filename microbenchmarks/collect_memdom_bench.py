# Run 25 trials for a given application, and collect the memdom metadata allocation data for each run

import os
import sys
import subprocess

runs = 25

depth = ['50']
fsize = ['1K', '10K', '100K', '1M', '10M']

for d in depth:
    for s in fsize:
        for x in range (0, runs):
            subprocess.call(['../load_python_profile'])
            f = open('data/open-micro-'+d+'-'+s+'-memdom-nosi.data', "a+")
            subprocess.call(['../pyronia_build/python', 'test_modules/run_syscall_latency_bench.py', d, s], stdout=f)
            f.close()
            print('Finished run '+str(x+1)+' for file open micro depth '+str(d)+', file size '+s)
