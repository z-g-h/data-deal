import math
import numpy as np
import matplotlib.pyplot as plt

Q  = np.array([13.97,13.02,12.04,11,10,7.99,5.98,4,2.05,0])
P_in = np.array([-9.33,-8.04,-6.81,-5.52,-4.35,-2.44,-0.99,0.02,0.72,0.93])*10**3
P_out = np.array([0.074,0.121,0.166,0.207,0.243,0.296,0.329,0.352,0.366,0.379])*10**6
n = 2578
N = np.array([0.943,0.935,0.927,0.919,0.894,0.802,0.772,0.650,0.463,0.317])
rho = 10**3
g=9.81

u1 = Q/(3600*math.pi*(42*10**-3)**2/4)
u2 = Q/(3600*math.pi*(39*10**-3)**2/4)
H = (P_out-P_in)/(rho*g) + (u2**2-u1**2)/(2*g)
eta = H*Q*rho*g/(3600*N*1000)*100
np.set_printoptions(precision=3, suppress=True)
print(u1)
print(u2)
print(H)
print(eta)
 
a = np.array([1.88,1.69,1.61,1.5,1.37])
plt.plot(a)
#plt.plot(Q,eta)
#plt.plot(Q,N)
plt.show()
