import numpy as np
import numpy.random
import matplotlib.pyplot as plt

#This program is designed to take a delta function spaced 10 pixels apart and
#slide a Gaussian function over it for all pixels, resulting in the convolution
#of these functions. I then plot the results. 

def gauss(x, mean, amp, sig):
    '''
    I'm going to need to call a Gaussian Function very often, so I made
    a quick function for it. It takes in the 3 parameters of a Gaussian,
    as well as an x coordinate, and spits out the given y value at that point.
    '''
    return amp * np.exp((-1.)*(x-mean)**2 / (2. * sig**2))

conv_array = []

for i in range(0, 8192):
    total = 0
    for j in range(0, 8192):
        delta = 0
        if j % 10 == 0:
            delta = 1.
        total += delta * gauss(j, i, 1., 5.)
    conv_array.append(total)
    print i

plt.plot(np.arange(0, 8192), conv_array)
plt.show()

#================================================
#End Part One
#Now I will attempt the same by multiplying the functions in Fourier Space
#First step is to fill an array with evenly spaced delta functions.
#================================================

delta_array = []

for k in range(0, 8192):
    if k % 10 == 0:
        delta_array.append(1.)
    else:
        delta_array.append(0.)

gauss_array = []

for i in range(0, 8192):
    gauss_array.append(gauss(float(i)-(8192./2.), 0., 1., 5.))
'''
Here, I generate a single Gaussian function over the pixel radius I define. 
It should be about zero at all places except around a mean at zero. This is
only used for doing the Fourier transform of the Gaussian, which should result
in another Gaussian in Fourier space.
'''

Fgauss_array = np.fft.fft(gauss_array)
Fdelta_array = np.fft.fft(delta_array)

Fmulti = Fdelta_array * Fgauss_array

'''
I multiply the two new arrays together because the multiplication of two 
functions in Fourier Space is the same thing as convolution of functions in
Real space. The last step is to do an inverse Fourier transform to get back to
real coordinates. Then, I just plot my results
'''

Fout = np.fft.ifft(Fmulti)

plt.plot(np.arange(0, 8192), Fout[np.arange(0, 8192)])
plt.show()

'''
Sadly, I have a spike at the center of the Gaussian I defined earlier, which is
odd. However, the rest of my function, when you zoom in, looks incredibly similar
the convolution I did without transforming it in Fourier space. 
'''
