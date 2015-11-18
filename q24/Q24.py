import matplotlib.pyplot as plt
import isochrones as iso
import numpy as np

zp00 = iso.read("zp00.dat")
zp02 = iso.read("zp02.dat")
zp04 = iso.read("zp04.dat")

agetest00 = zp00['age']
agetest02 = zp02['age']
agetest04 = zp04['age']

log_age = 9.
'''
zp0 = {'temp' : zp00['logte'], 'grav' : zp00['logg'], 'mbol' : zp00['mbol'], 'z' : zp00['z'], 'age' : zp00['age']}

zp2 = {'temp' : zp02['logte'], 'grav' : zp02['logg'], 'mbol' : zp02['mbol'], 'z' : zp02['z'], 'age' : zp02['age']}

zp4 = {'temp' : zp04['logte'], 'grav' : zp04['logg'], 'mbol' : zp04['mbol'], 'z' : zp04['z'], 'age' : zp04['age']}
'''

zp0_temp = []
zp0_grav = []
zp0_mbol = []

zp2_temp = []
zp2_grav = []
zp2_mbol = []

zp4_temp = []
zp4_grav = []
zp4_mbol = []


for i in range(0, len(zp00['age'])):
    if agetest00[i] == log_age:
        zp0_temp.append(zp00['logte'][i])
        zp0_grav.append(zp00['logg'][i])
        zp0_mbol.append(zp00['mbol'][i])

for i in range(0, len(zp02['age'])):
    if agetest02[i] == log_age:
        zp2_temp.append(zp02['logte'][i])
        zp2_grav.append(zp02['logg'][i])
        zp2_mbol.append(zp02['mbol'][i])

for i in range(0, len(zp04['age'])):
    if agetest04[i] == log_age:
        zp4_temp.append(zp04['logte'][i])
        zp4_grav.append(zp04['logg'][i])
        zp4_mbol.append(zp04['mbol'][i])


zp01 = iso.read("zp01.dat")

f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')

ax1.scatter(zp0_temp, zp0_grav, marker='o', s= 12, linewidth=0, facecolor='b')
ax1.scatter(zp2_temp, zp2_grav, marker='o', s= 12, linewidth=0, facecolor='g')
ax1.scatter(zp4_temp, zp4_grav, marker='o', s= 12, linewidth=0, facecolor='r')
ax1.set_ylim([0.2, 5.2])
ax1.invert_xaxis()
ax1.invert_yaxis()
ax1.set_ylabel("log Surface Gravity")

ax2.scatter(zp01['logte'], zp01['logg'], c=zp01['age'], cmap='jet', vmin=min(zp01['age']), vmax=max(zp01['age']), linewidth=0.2)
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

plt.show()

'''
temp 
grab
bolmag
metal
age
'''
