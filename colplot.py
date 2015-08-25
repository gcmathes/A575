import matplotlib.pyplot as plt
import os
import numpy as np
import pylab as pyl

direct = '/kochab/gcmathes'

os.chdir(direct)

filename = raw_input('Name of file: ')

infile = open(filename, 'r')

EW = []

for line in infile:
    columns = line.split()
    EW.append(float(columns[0]))

del EW[-1]

plt.hist(EW, bins=21)
plt.title('Number of objects per EW bin')
plt.xlabel('EW')
plt.ylabel('Number')

pyl.xlim([0, 0.22])
plt.show()
