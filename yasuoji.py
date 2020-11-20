import numpy as np
import math


T0 = np.array([19.9,21.0,20.6,21.8,22.2])+273
T1 = np.array([31.5,40.4,47.8,49.5,52.2])+273
p0 = 0.1*10**6
p1 = np.array([0.2,0.3,0.4,0.5,0.6])*10**6
n = np.array([537,535,535,534,531])
H = np.array([7.9,6.8,6.5,5.4,5.1])*10**3
D = 19.05
C = np.array([0.981,0.978,0.977,0.977,0.975])
Q = 1128.53*10**(-6)*C*D**2*T0*np.sqrt(H/(p0*T1))
print("Q=",Q)
lamda_t = np.array([0.99,0.96,0.94,0.94,0.93])
lamda_p = np.array([0.96,0.96,0.96,0.96,0.96])
lamda_l = np.array([0.99,0.98,0.98,0.97,0.96])
Ap = math.pi/4*0.153**2
Vs = Ap*0.114
alpha = 1.64*10**(-4)/Vs
print("alpha=",alpha)
epsilo = np.array([2,3,4,5,6])
lamda_v = 1-alpha*(np.power(epsilo,1/1.2)-1)
print("lamda_v=",lamda_v)
V = 2*n*lamda_l*lamda_p*lamda_t*lamda_v*Vs
print("V=",V)
error = np.abs(V-Q)/V*100
print("error=",error)
print("T0=",T0)
print("T1=",T1)
print("H=",H)
print("p0=",p0)
print(Vs)