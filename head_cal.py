import numpy as np
import math

def cal_el_stress(p):
    print("椭圆应力")
    x = np.array([0,50,100,150,175,200,204.5])
    S = 4.5
    a = 200+S/2
    b = a/2
    sigma_phi = p/(2*S*b)*np.sqrt(a**4-x**2*(a**2-b**2))
    sigma_theta = sigma_phi*(2-a**4/(a**4-x**2*(a**2-b**2)))
    sigma_phi = np.append(sigma_phi,p*(200+S/2)/(2*S))
    sigma_theta = np.append(sigma_theta,p*(200+S/2)/S)

    test_strain_phi = np.array([26.8,28.7,31.3,15.3,15.3,1.3,5.1,24.9])*10**-6
    test_strain_theta = np.array([26.8,26.8,18.5,-1.9,-13.4,-21.1,0.6,24.9])*10**-6
    test_stress_phi = E/(1-mu**2)*(test_strain_phi+mu*test_strain_theta)
    test_stress_theta = E/(1-mu**2)*(test_strain_theta+mu*test_strain_phi)

    #print(test_stress_phi)
    #print(test_stress_theta)


    #print(a,b,S)
    print(sigma_phi)
    print(sigma_theta)

def cal_flat_stress(p):
    S = 35
    t = S/2
    print("平盖")
    R = 206
    mu = 0.3
    r = np.array([0,50,100,150,175,200,206])
    z = np.array([t,t,t,t,t,t,-7.5])
    sigma_r = 3*p*z*((1+mu)*R**2-(3+mu)*r**2)/(4*S**3)
    sigma_theta = 3*p*z*((1+mu)*R**2-(1+3*mu)*r**2)/(4*S**3)
    print(sigma_r)
    print(sigma_theta)

def cal_tri_stress(p):
    print("锥型")
    R1 = 212/2
    R2 = 400/2
    S =  5.5
    x = np.array([100,100+175,100+2*175,100+3*175,100+4*175,100+5*175])
    degree = math.radians(13)
    r = R1 + x*math.tan(degree)
    #print(r)
    sigma_phi = p*r/(2*S*math.cos(degree))
    sigma_theta = p*r/(S*math.cos(degree))


    print(sigma_phi)
    print(sigma_theta)

def cal_fly_stress(p):
    print("蝶形")
    S = 5
    D = 400
    r = D/2 + S/2
    r0 = 0.17*D +S/2
    R = 0.9*D + S/2
    phi0 = math.asin((r-r0)/(R-r0))
    #print(r,r0,R)

    #print(R)
    #print(r0)
    #print("phi0 =")
    #print(math.degrees(phi0))
    #print(R*math.sin(phi0))
    phi = np.array([phi0,phi0,phi0,phi0,math.radians(37.58),math.radians(74.7),math.radians(90)])
    sigma_phi = p*(r0+(R-r0)*math.sin(phi0)/np.sin(phi))/(2*S)
    sigma_theta = sigma_phi*(1-(R-r0)*math.sin(phi0)/(r0*np.sin(phi)))
    sigma_phi[0:4] = p*R/(2*S)
    sigma_theta[0:4] = p*R/(2*S)
    sigma_phi = np.append(sigma_phi,p*r/(2*S))
    sigma_theta = np.append(sigma_theta,p*r/S)
    print(sigma_phi)
    print(sigma_theta)
    



def cal_body_stress(p):
    S = 5
    R = 200
    sigma_phi = p*R/(2*S)
    sigma_theta = p*R/S

    print(sigma_phi,sigma_theta)



p = 1
E = 1.96*10**5
mu = 0.3
np.set_printoptions(precision=3, suppress=True)
cal_el_stress(p)
cal_flat_stress(p)
cal_tri_stress(p)
cal_fly_stress(p)
cal_body_stress(p)