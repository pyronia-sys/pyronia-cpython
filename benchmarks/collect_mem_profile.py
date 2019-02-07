# Run 25 trials for a given application, and collect the end-to-end memory usage for  each run                         

import os
import sys
import subprocess

runs = 25

app = sys.argv[1]

dirs = app.split('/')
app_name = dirs[-1].strip()[:-3]

for x in range (0, runs):
    #subprocess.call(['./load_python_profile'])
    subprocess.call(['mprof', 'run', '-o', app_name+'/mprofile_'+app_name+'-'+str(x)+'-nopyr.dat', '../pyronia_build/python', os.path.abspath(app)])
    print('Finished run '+str(x+1)+' for app '+app)
