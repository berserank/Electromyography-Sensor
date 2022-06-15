from pylab import *
import numpy as np
import scipy.signal as sp

H=sp.lti([0.00442,0],polymul([0.0006125678,1],[0.0316,1]))
W,S,phi=H.bode()
figure(0)
xlabel('frequency')
ylabel('Magnitude')
xlim(0.01,10**4)
title('Magnitude plot')
semilogx(W,S)
show()
figure(1)
semilogx(W,phi)
xlabel('frequency')
ylabel('Phase')
xlim(0.01,10**4)
title('Phase plot')
show()