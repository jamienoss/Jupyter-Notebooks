
#devPath = "/Users/jnoss/dev/astropy/build/lib.macosx-10.6-x86_64-3.5/astropy/"
#import importlib.util
#spec = importlib.util.spec_from_file_location("astropy", devPath+'setup_package.py')
#astropy = importlib.util.module_from_spec(spec)
#spec.loader.exec_module(astropy)
import sys
sys.path.insert(0, '/Users/jnoss/dev/astropy/build/lib.macosx-10.6-x86_64-3.5/')
import astropy
print(astropy.version)

import astropy.convolution as astroconv
import scipy.ndimage.filters as sciconv
import scipy.signal as scisig
#from scipy.ndimage.filters import convolve
import numpy as np
import gc
import time
#import gputools

iLength = 10000
jLength = iLength
image = np.random.random((iLength, jLength))

size = 11#1
ker = astroconv.Gaussian2DKernel(20,x_size=size,y_size=size)
#ker = np.random.random((iLength+1, jLength+1))

#smoothed = scisig.fftconvolve(image, ker)#.array, mode='same')
#smoothed = astroconv.convolve_fft(image, ker, allow_huge=True)#, boundary='wrap')
#image[50, 50] = np.nan
#smoothed = sciconv.convolve(image, ker.array, mode='reflect')
astroconv.convolve(image, ker, boundary=None, nan_treatment='interpolate')


#smoothed = sciconv.convolve(image, ker)
#smoothed = astroconv.convolve(image, ker)


#smoothed = gputools.convolve(image, ker.array)

#quote, rem = scisig.deconvolve(image, ker)

#gc.collect()
#time.sleep(60)
