import numpy as np
import math


E = 70*10**3
t = np.array([0.095,0.10,0.096])
L = np.array([115,114.6,167.0])
D = np.array([65.2,65.7,65.8])

Lcr = 1.17*D*np.sqrt(D/t)
Pcr = 2.59*E*t**2/(L*D*np.sqrt(D/t))
n = np.power(7.06*D**3/(t*L**2),1/4)
test_pcr = np.array([0.009,0.008,0.0045])
test_n =  np.array([5,4,4])
error_pcr = np.abs(Pcr-test_pcr)/test_pcr*100
error_n = np.abs(test_n-n)/test_n*100

print("Lcr=",Lcr)
print("Pcr=",Pcr)
print("n=",n)
print("pcr_error=",error_pcr)
print("n_error=",error_n)