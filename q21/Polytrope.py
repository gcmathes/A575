import matplotlib.pyplot as plt
import numpy 

#Program : Use Runge-Kutta shooting method to solve our differential equation.
#Be setting y = theta and z = dtheta / dxi = y'. 

#I'm going to need this calculation a lot, so I define it as a function. It's
#done by solving the Lane-Emden equation for d2theta / dxi2, which is my z'. 
def zprime(y,z,xi,n):
    z_p = (-1.0 * y ** n) - (2.0 * (z / xi))
    return z_p

#Lets set up boundary conditions. y = 1 @ xi_0. Also, z = 0 @ xi_0. Also, we 
#know y = 0 @ xi_1, which is the last entry. 

n = 2.75 #My polytropic index.
y = 1.0
z = (-1.0)*0.000333333225 #Solved the expanded Lane-Emden given in the problem for 
                #xi = 0.001 to get my initial condition here. Took the 
xi = 0.001      #derivative of the series in order to get my dtheta / dxi.

y_tot = []
z_tot = []
xi_tot = []
xi2_tot = []

steps = 0.001

#With all my constants / boundaries in line, time to begin the Runge-Kutta
#I want to run these steps until theta is 0, then it stops.
#The first and last shots should be the widest, so the middle go as my step 
#size divided by 2. Each degree depends on the results of the previous step
#The limit I use here for theta is based on letting it run forever. After this
#point, theta goes negative and we cannot run anymore.

while y > 0.000035:
    k1 = steps * z
    l1 = steps * zprime(y,z,xi,n)
    k2 = steps * (z + (l1 / 2.0))
    l2 = steps * zprime(y + (k1 / 2.0), z + (l1 / 2.0), xi + (steps / 2.0), n)
    k3 = steps * (z + (l2 / 2.0))
    l3 = steps * zprime(y + (k2 / 2.0), z + (l2 / 2.0), xi + (steps / 2.0), n)
    k4 = steps * (z + l3)
    l4 = steps * zprime(y + k3, z + l3, xi + steps, n)
    
#Now I want to weight the inner steps to create a 'mountain' effect as the 
#Runge-Kutta naturally overshoots the real values.

    y += (1.0/6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
    z += (1.0/6.0) * (l1 + 2.0 * l2 + 2.0 * l3 + l4)

#Finally, output the results of this loop to my arrays. 
    xi_tot.append(xi)
    xi2_tot.append(xi ** 2.0)
    y_tot.append(y)
    z_tot.append(z)
    xi += steps
#These equations were taken from the notes
rho_rat = xi_tot[-1] / ((-1.0) * 3.0 * z_tot[-1])

N_1 = ((4.0 * 3.1415926) ** (1.0 / n)) / (n + 1.0)
N_2 = (-1.0) * (xi_tot[-1]) ** ((n + 1.0) / (n - 1.0))

N_final = N_1 * (N_2 * z_tot[-1]) ** ((1.0 - n) / n)

W = ((4.0 * 3.1415926 * (n + 1.0) * (z_tot[-1] ** 2))) ** (-1.0)

bigsig = ((-1.0) * (n + 1.0) * xi_tot[-1] * z_tot[-1]) ** (-1.0)

print "Final Xi value = " + str(xi_tot[-1])
print "rho_c / rho_mean = " + str(rho_rat)
print "N_n = " + str(N_final)
print "W = " + str(W)
print "Capital Sigma = " + str(bigsig)

#This completes the first five columns of the table. After this, I have all the 
#information I need to compute the remaining density, pressure, and temp.
#Let's load up some solar values!

X = 0.7
Z = 0.02

mu = (X * 2.0 + (1 - X - Z) * 0.75 + Z / 2) ** (-1.0)
Msun = 1.99 * (10 ** 33)
Rsun = 6.96 * (10 ** 10)
G = 6.67 * (10 ** -8)
amu = 1.67 * (10 ** -24)
k = 1.38 * (10 ** -16)

rho_c = ((-1.0) * xi_tot[-1] / (3.0 * z_tot[-1])) * (3.0 * Msun) / (4.0 * 3.1415926 * (Rsun ** 3)) 

P_c = W * G * (Msun ** 2) / (Rsun ** 4)

T_c = bigsig * G * Msun * mu * amu / (k * Rsun)

print "rho_c = " + str(rho_c)
print "P_c = " + str(P_c)
print "T_c = " + str(T_c)

'''
Here's the output of my code:

Final Xi value = 6.034
rho_c / rho_mean = 34.9351592073
N_n = 0.354952053503
W = 6.40200821313
Capital Sigma = 0.767612612769
rho_c = 49.2265593816
P_c = 7.20628203484e+16
T_c = 10935386.6427

All units are in CGS
'''

#This completes part a. of the assignment. Now, I will plot my results
#These just make new arrays for raising all values to a power for plotting.

q = []
for j in range(0, len(xi2_tot)):
    temp = xi2_tot[j] * z_tot[j] / (xi2_tot[-1] * z_tot[-1])
    q.append(temp)

yn_tot = []
for b in range(0, len(y_tot)):
    temp = y_tot[b] ** n
    yn_tot.append(temp)

yn2_tot = []
for e in range(0, len(y_tot)):
    temp = y_tot[e] ** (n + 1.0)
    yn2_tot.append(temp)

plt.plot(xi_tot, y_tot, color = 'r', linewidth = 2.5, label = "n = 1")
plt.plot(xi_tot, yn_tot, color = 'b', linewidth = 2.5, label = "n = 2.75")
plt.plot(xi_tot, yn2_tot, color = 'g', linewidth = 2.5, label = "n = 3.75")
plt.plot(xi_tot, q, color = 'k', linewidth = 2.5, label = "q")
plt.title('Part b : Values of Theta with different polytrope values')
plt.xlabel('Xi Values')
plt.ylabel('Theta Values')
plt.legend()

plt.show()

#The first three all show different polytrope values of theta, which represents
#the ratio of density to central density. One at n = 1, the second at my 2.75 value,
#and the last one is a higher index by n + 1. q, instead of a ratio of densities,
#is a ratio of mass interior to the total mass. 
