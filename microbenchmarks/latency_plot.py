import numpy as np
import matplotlib.pyplot as plt
import json
from collections import OrderedDict

lvls = ['1', '25', '50', '75', '100']

nopyr_data = dict()
with open('connect-latency-nopyr_stats.txt', 'r') as fp:
    nopyr_data = json.load(fp, object_pairs_hook=OrderedDict)

nosi_data = dict()
with open('connect-latency-nosi_stats.txt', 'r') as fp:
    nosi_data = json.load(fp, object_pairs_hook=OrderedDict)

pyr_data = dict()
with open('connect-latency-pyr_stats.txt', 'r') as fp:
    pyr_data = json.load(fp, object_pairs_hook=OrderedDict)

nopyr_values = [ v['mean'] for k, v in nopyr_data.items() ]
nopyr_stddevs = [ v['stddev'] for k, v in nopyr_data.items() ]

nosi_values = [ v['mean'] for k, v in nosi_data.items() ]
nosi_stddevs = [ v['stddev'] for k, v in nosi_data.items() ]

pyr_values = [ v['mean'] for k, v in pyr_data.items() ]
pyr_stddevs = [ v['stddev'] for k, v in pyr_data.items() ]

line, caps, bars = plt.errorbar(
    lvls,  # X
    nopyr_values, # Y
    yerr=nopyr_stddevs,     # Y-errors
    fmt="r-", # format line like for plot()
    linewidth=2,   # width of plot line
    elinewidth=0.5,# width of error bar line
    ecolor='k',    # color of error bar
    capsize=5,     # cap length for error bar
    capthick=0.5   # cap thickness for error bar
    )

line1, caps1, bars1 = plt.errorbar(
    lvls,  # X
    nosi_values, # Y
    yerr=nosi_stddevs,     # Y-errors
    fmt="b--", # format line like for plot()
    linewidth=2,   # width of plot line
    elinewidth=0.5,# width of error bar line
    ecolor='k',    # color of error bar
    capsize=5,     # cap length for error bar
    capthick=0.5   # cap thickness for error bar
    )

line2, caps2, bars2 = plt.errorbar(
    lvls,  # X
    pyr_values, # Y
    yerr=pyr_stddevs,     # Y-errors
    fmt="g:", # format line like for plot()
    linewidth=2,   # width of plot line
    elinewidth=0.5,# width of error bar line
    ecolor='k',    # color of error bar
    capsize=5,     # cap length for error bar
    capthick=0.5   # cap thickness for error bar
    )

'''
plt.setp(line,label="open()")#give label to returned line
plt.setp(line1,label="open()+Pyronia (no SI)")#give label to returned line
plt.setp(line2,label="open()+Pyronia")#give label to returned line
'''
plt.setp(line,label="connect()")#give label to returned line
plt.setp(line1,label="connect()+Pyronia (no SI)")#give label to returned line
plt.setp(line2,label="connect()+Pyronia")#give label to returned line

plt.legend()      #Set label location
#plt.xticks([1,2,3,4])               #get only ticks we want
plt.yscale("log")
plt.xlabel('# call stack levels')
plt.ylabel('time in microseconds')
plt.savefig('connect-latency.pdf')
