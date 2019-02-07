import numpy as np
import matplotlib.pyplot as plt
import json

nopyr_data = dict()
pyr_data = dict()
with open('app_latency_pyr.data', 'r') as fp:
    pyr_data = json.load(fp)
with open('app_latency_nopyr.data', 'r') as fp:
    nopyr_data = json.load(fp)

ind = np.arange(4)  # the x locations for the groups
width = 0.34  # the width of the bars

# gather pyr and no_pyr lists
pyr_means = [ float(a[0])/1000000.0 for a in pyr_data['mean'] ]
pyr_e2e_means = [ float(a[1])/1000000.0 for a in pyr_data['mean'] ]
pyr_stddev = [ float(a[0])/1000000.0 for a in pyr_data['stddev'] ]
pyr_e2e_stddev = [ float(a[1])/1000000.0 for a in pyr_data['stddev'] ]

nopyr_means = [ float(a[0])/1000000.0 for a in nopyr_data['mean'] ]
nopyr_e2e_means = [ float(a[1])/1000000.0 for a in nopyr_data['mean'] ]
nopyr_stddev = [ float(a[0])/1000000.0 for a in nopyr_data['stddev'] ]
nopyr_e2e_stddev = [ float(a[1])/1000000.0 for a in nopyr_data['stddev'] ]

fig, ax = plt.subplots()
rects1 = ax.bar(ind - 0.75*width, nopyr_means, width/2, yerr=nopyr_stddev,
                color='SkyBlue', edgecolor='black', label='Main-only', hatch='o')
rects2 = ax.bar(ind - width/4, nopyr_e2e_means, width/2, yerr=nopyr_e2e_stddev,
                color='SkyBlue', edgecolor='black', label='Application', hatch='/')
rects3 = ax.bar(ind + width/4, pyr_means, width/2, yerr=pyr_stddev,
                color='IndianRed', edgecolor='black', label='Main-only w/ Pyronia')
rects4 = ax.bar(ind + 0.75*width, pyr_e2e_means, width/2, yerr=pyr_e2e_stddev,
                color='IndianRed', edgecolor='black', label='Application w/ Pyronia', hatch='*')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_yscale('log')
ax.set_ylabel('time in seconds')
ax.set_title('IoT main module and application execution times')
ax.set_xticks(ind)
ax.set_xticklabels(('hello', 'twitterPhoto', 'alexa', 'plant_watering'))

plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

fig.savefig('apps-latency.pdf')

'''
def autolabel(rects, xpos='center'):
    """
    Attach a text label above each bar in *rects*, displaying its height.

    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """

    xpos = xpos.lower()  # normalize the case of the parameter
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                '{}'.format(height), ha=ha[xpos], va='bottom')


autolabel(rects1, "left")
autolabel(rects2, "right")
'''
