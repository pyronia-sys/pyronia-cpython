import os
import sys
import json
from statistics import median, mean, stdev
from collections import OrderedDict

runs = 25

depth = ['0', '25', '50', '75', '100']
fsize = ['1K', '10K', '100K', '1M', '10M']

stats = OrderedDict()
for s in fsize:
    f = open('data/open-latency-'+s+'-pyr.csv', "r")
    latency_data = [l.strip() for l in f.readlines()]
    f.close()

    depths = OrderedDict()
    for t in latency_data:
        expt = t.split(", ")
        d = expt[0].strip()
        lat = float(expt[1].strip())
        if depths.get(d) == None:
            depths[d] = []
        depths[d].append(lat)

    for dep in depth:
        expt_stats = OrderedDict()
        if stats.get(dep) == None:
            stats[dep] = OrderedDict()
        lats = depths[dep]

        expt_stats['min'] = min(lats)
        expt_stats['mean'] = mean(lats)
        expt_stats['median'] = median(lats)
        expt_stats['max'] = max(lats)
        expt_stats['stddev'] = stdev(lats)

        stats[dep][s] = expt_stats

for d, expt in stats.items():
    means = []
    for s, st in expt.items():
        means.append(st['mean'])
    stats[d]['mean'] = mean(means)
    stats[d]['stddev'] = stdev(means)

outfile = 'open-latency-pyr_stats.txt'
f = open(outfile, "w+")
json.dump(stats, f, indent=4)
f.close()
