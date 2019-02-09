import numpy as np
import matplotlib.pyplot as plt
import json
from collections import OrderedDict

lvls = ['1', '25', '50', '75', '100']

nosi_data = dict()
with open('open-latency-nosi_stats.txt', 'r') as fp:
    nosi_data = json.load(fp, object_pairs_hook=OrderedDict)

pyr_data = dict()
with open('open-latency-pyr_stats.txt', 'r') as fp:
    pyr_data = json.load(fp, object_pairs_hook=OrderedDict)

nosi_values = [ v['mean'] for k, v in nosi_data.items() ]
nosi_stddevs = [ v['stddev'] for k, v in nosi_data.items() ]

pyr_values = [ v['mean'] for k, v in pyr_data.items() ]
pyr_stddevs = [ v['stddev'] for k, v in pyr_data.items() ]

line, caps, bars = plt.errorbar(
    lvls,  # X
    nosi_values, # Y
    yerr=nosi_stddevs,     # Y-errors
    fmt="r-", # format line like for plot()
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
    fmt="b--", # format line like for plot()
    linewidth=2,   # width of plot line
    elinewidth=0.5,# width of error bar line
    ecolor='k',    # color of error bar
    capsize=5,     # cap length for error bar
    capthick=0.5   # cap thickness for error bar
    )

plt.setp(line,label="Pyronia (no stack inspection)")#give label to returned line
plt.setp(line2,label="Pyronia")#give label to returned line
plt.legend()      #Set label location
#plt.xticks([1,2,3,4])               #get only ticks we want
plt.yscale("log")
plt.xlabel('# call stack levels')
plt.ylabel('time in microseconds')
plt.savefig('open-latency.pdf')
