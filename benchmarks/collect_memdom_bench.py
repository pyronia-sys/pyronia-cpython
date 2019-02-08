# Run 25 trials for a given application, and collect the memdom metadata allocation data for each run

import os
import sys
import subprocess

runs = 25

app = sys.argv[1]

dirs = app.split('/')
app_name = dirs[-1].strip()[:-3]

for x in range (0, runs):
    subprocess.call(['../load_python_profile'])
    f = open(app_name+'/'+app_name+'-memdom-'+str(x)+'.data', "w+")
    subprocess.call(['../pyronia_build/python', os.path.abspath(app)], stdout=f)
    f.close()
    print('Finished run '+str(x+1)+' for app '+app)
