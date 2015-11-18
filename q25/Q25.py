import matplotlib.pyplot as plt
import isochrones as iso
import numpy as np


log_age = 9.

zp01 = iso.read("zp01.dat")
zp1_temp = []
zp1_mbol = []
zp1_intimf = []
zp1_diff = [0]

for i in range(0, len(zp01['age'])):
    if zp01['age'][i] == log_age:
        zp1_temp.append(zp01['logte'][i])
        zp1_mbol.append(zp01['mbol'][i])
        zp1_intimf.append(zp01['intimf'][i])

for j in range(1, len(zp1_intimf)):
    zp1_diff.append(10 ** (abs(zp1_intimf[j] - zp1_intimf[j-1])))
fig, ax2 = plt.subplots()

number_bins = 30
xbin_width = (max(zp1_temp) - min(zp1_temp)) / float(number_bins)
ybin_width = (max(zp1_mbol) - min(zp1_temp)) / float(number_bins)

xedges = [min(zp1_temp)]
yedges = [min(zp1_mbol)]

for j in range(1, 30):
    xedges.append(xedges[j-1] + xbin_width)
    yedges.append(xedges[j-1] + ybin_width)
#for k in range(0, len(zp1_diff)):
#    for x in range(0, number_bins):
#        for y in range(0, number_bins):
           # extent=(xedges[0], xedges[-1], yedges[0], yedges[-1])
zp1_temp = zp1_temp[::-1]
zp1_mbol = zp1_mbol[::-1]

plt.figure(1)
hist1, yedges, xedges = np.histogram2d(zp1_mbol, zp1_temp, bins=20, range= [[min(zp1_mbol), max(zp1_mbol)], [min(zp1_temp), max(zp1_temp)]], weights=zp1_diff)
plt.imshow(hist1, interpolation='nearest', origin="lower")
plt.gca().invert_xaxis()
plt.gca().invert_yaxis()
plt.colorbar()
plt.show()

'''
ax2.scatter(zp1_temp, zp1_mbol, c=zp1_diff, cmap='jet', s=60, vmin=min(zp1_diff), vmax=max(zp1_diff), linewidth=0.2)
ax2.invert_yaxis()
ax2.invert_xaxis()


ax3.scatter(zp0_temp, zp0_mbol, marker='o', s= 12, linewidth=0, facecolor='b')
ax3.scatter(zp2_temp, zp2_mbol, marker='o', s= 12, linewidth=0, facecolor='g')
ax3.scatter(zp4_temp, zp4_mbol, marker='o', s= 12, linewidth=0, facecolor='r')
ax3.invert_yaxis()

ax3.set_xlabel("log $T_e$")
ax3.set_ylabel("Bolometric Magnitude")

ax4.scatter(zp01['logte'], zp01['mbol'], c=zp01['age'], cmap='jet', vmin=min(zp01['age']), vmax=max(zp01['age']), linewidth=0.2)

plt.subplots_adjust(hspace = 0, wspace = 0)
ax4.set_xlabel("log $T_e$")
'''
plt.show()

'''
temp 
grab
bolmag
metal
age
'''
