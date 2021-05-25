# This program supports (x, y, label) formatted csv data.
# argv[1] : Imported csv file.
# argv[2] : Exported png file.

import csv, pprint, sys, math
import numpy as np
import matplotlib.pyplot as plt

ifile = sys.argv[1]
if ifile.endswith('.csv'):
    ext = '.csv'
    delimeter = ','
if ifile.endswith('.txt'):
    ext = '.txt'
    delimeter = ' '

with open(ifile) as f:
    reader = csv.reader(f, delimiter=delimeter)
    l = [row for row in reader]

x = [float(i[0]) for i in l] 
y = [float(i[1]) for i in l]
value = [float(i[2]) for i in l]

plt.scatter(x, y, s=5, c=value, cmap='jet', vmin=0, vmax=1)
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.xticks([-1, -0.5, 0, 0.5, 1], ["-1", "-0.5", "0", "0.5", "1"])
plt.yticks([-1, -0.5, 0, 0.5, 1], ["-1", "-0.5", "0", "0.5", "1"])
plt.title(ifile.replace(ext, ''))
plt.colorbar()
plt.savefig(sys.argv[2])