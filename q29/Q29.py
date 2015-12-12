import numpy as np
import numpy.random
import matplotlib.pyplot as plt

M_min = 0.5
M_max = 100


def random_weights(amin, amax, num, p):
    '''
    Takes a power law of dN / dM = M**p and generates a 'num' of
    random deviates in that distribution. I needed to integrate the function, then
    invert it to transform my random deviate. 

    INPUTS : Minimum and Maxmimum range, Number of Deviates, Power of dN/dM

    OUTPUTS : Array of weighted deviates between Min and Max. 
    '''
    tmin = amin ** (p+1.)
    tmax = amax ** (p+1.)
    randoms = np.random.random(num)
    invert = 1. / (p+1.)
    
    returnarray = ((tmax - tmin) * randoms + tmin) ** invert
    return returnarray
    

imf_array = random_weights(0.5, 100, 10000, -2.35)
print imf_array
print min(imf_array)
print max(imf_array)
plt.hist(imf_array, bins= np.logspace(-.3, 2, 20))
#Here I need to put my bins in log format, for easy readability.


#Then, I need to make my Salpeter power law to overlay. N = M^-1.35 because 
#dN / dM = M^-2.35, so I overlay that powerlaw for my function.
prange = 0.5 * np.arange(1, 200)
powerlaw = (prange ** -1.35) * 6 * 10 ** 3
plt.plot(prange, powerlaw)

#The rest of this is formatting the plot space.
plt.yscale('log')
plt.xscale('log')
plt.xlabel("Mass in Log Scale")
plt.ylabel("Number of Deviates")
plt.title("Log-Log Distribution of Random Deviates from 0.5 - 100 M using Salpeter IMF with 1000 points")
plt.show()
