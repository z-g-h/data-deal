import numpy as np
import math

p_est1 = np.array([-121,-131,-155,-189,-234,-285,-348,-423,-505,-601,-715,-788])
p_est2 = np.array([1581,1580,1579,1570,1536,1471,1375,1242,1074,866,602,370])
delta_p = np.array([8,21,47,85,135,198,269,354,446,548,667,762])
F = np.array([0.8,1.0,1.1,1.3,1.6,1.9,2.1,2.4,2.9,3.1,3.5,3.6])
Ta = 296
pa = 0.103*10**6
n = 2202
dn = 0.099
D1 = 0.15
D2 = 0.125
L1 = 0.75
L2 = 0.6

A1 = math.pi*D1**2/4
A2 = math.pi*D2**2/4

rho_a = pa/(288.5*Ta)
Q = 63.311*dn**2*np.sqrt(rho_a*delta_p)/rho_a

pd1 = rho_a*(Q/(60*A1))**2/2
delta1 = pd1*(0.025*L1/D1)
pst1 = p_est1-delta1
p1 = pst1+pd1

pd2 = rho_a*(Q/(60*A2))**2/2
delta2 = pd2*(0.025*L2/D2)
pst2 = p_est2 + delta2
p2 = pst2 + pd2

pst = pst2-pst1
pd = pd2 - pd1
p = p2 - p1

Nsh = F*n/9550

eta = Q*p/(Nsh*6*10**4)*100
np.set_printoptions(precision=3, suppress=True)

print(pst)
