import os
import sys
import json
from statistics import median, mean, stdev
from collections import OrderedDict

runs = 25

depth = ['0', '25', '50', '75', '100']
fsize = ['1K', '10K', '100K', '1M', '10M']

stats = OrderedDict()
for d in depth:
    #size_expt = OrderedDict()
    #for s in fsize:
    expt_stats = OrderedDict()
    f = open('data/connect-micro-'+d+'-memdom-nosi.data', "r")

    memdom_data = [l.strip() for l in f.readlines()]
    f.close()

    total_memdoms = []
    total_interp_doms = []
    mins = []
    means = []
    medians = []
    maxs = []
    for r in range(0, runs):
        num_si_doms = int(memdom_data[1])
        start_idx = 3
        total_interp_doms.append(int(memdom_data[start_idx-1])+num_si_doms)
        total_memdoms.append(int(memdom_data[0])+total_interp_doms[r])
        memdom_allocs = [ int(a) for a in memdom_data[start_idx:start_idx+total_memdoms[r]] ]
        memdom_data = memdom_data[total_memdoms[r]+start_idx:]

        mins.append(min(memdom_allocs))
        means.append(mean(memdom_allocs))
        medians.append(median(memdom_allocs))
        maxs.append(max(memdom_allocs))

    expt_stats['min'] = mean(mins)
    expt_stats['mean'] = mean(means)
    expt_stats['median'] = mean(medians)
    expt_stats['max'] = mean(maxs)
    expt_stats['stddev'] = stdev(means)
    expt_stats['total_doms'] = mean(total_memdoms)
    expt_stats['interp_doms'] = mean(total_interp_doms)

    stats[d] = expt_stats

outfile = 'connect-memdom-nosi_stats.txt'
f = open(outfile, "w+")
json.dump(stats, f, indent=4)
f.close()
