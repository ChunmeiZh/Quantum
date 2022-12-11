# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 16:26:26 2022

@author: cmzha
"""

import numpy as np
import matplotlib.pylab as plt


T=1000 

k=1.38054e-23;                         #玻尔兹曼常数
h=6.626e-34;                           #普朗克常数
c=2.997925e8;                          #光速

mu=np.linspace(1e3,2.5e14,4000);
m_plank= 2*np.pi*h*np.power(mu,3)/np.power(c,3)/(np.exp(h*mu/k/T)-1);
plt.figure()
plt.plot(mu,m_plank,linewidth=2, label='Planck')
 
m_wein =2*np.pi*h*np.power(mu/c,3)*np.exp(-h*mu/k/T);

plt.plot(mu,m_wein,linewidth=2, label='Wien')
mu=np.linspace(1e3,3e13,2000);
m_raj = 2*np.pi*mu**2/np.power(c,3)*k*T;
plt.plot(mu,m_raj,linewidth=2, label='Rayleigh-Jeans')
plt.legend()
plt.xlabel('Frequency/Hz')

plt.savefig('three_formulas.png',dpi=500,bbox_inches = 'tight')

plt.figure()
lambda1=np.linspace(0,2000,2001);
lam=lambda1*1e-9;
T=3500
u_lam=8*np.pi*h*c/np.power(lam,5)/(np.exp(h*c/lam/k/T)-1)/1000;
plt.plot(lambda1,u_lam,linewidth=2)
plt.text(600,100,'T=3500K',fontsize=10)
T=4000
u_lam=8*np.pi*h*c/np.power(lam,5)/(np.exp(h*c/lam/k/T)-1)/1000;
plt.plot(lambda1,u_lam,linewidth=2)
plt.text(550,200,'T=4000K',fontsize=10)
T=4500
u_lam=8*np.pi*h*c/np.power(lam,5)/(np.exp(h*c/lam/k/T)-1)/1000;
plt.plot(lambda1,u_lam,linewidth=2)
plt.text(470,370,'T=4500K',fontsize=10)
T=5000
u_lam=8*np.pi*h*c/np.power(lam,5)/(np.exp(h*c/lam/k/T)-1)/1000;
plt.plot(lambda1,u_lam,linewidth=2)
plt.text(450,600,'T=5000K',fontsize=10)
T=5500
u_lam=8*np.pi*h*c/np.power(lam,5)/(np.exp(h*c/lam/k/T)-1)/1000;
plt.plot(lambda1,u_lam,linewidth=2)
plt.text(400,900,'T=5500K',fontsize=10)
plt.ylim(-50,1000)
plt.xlim(0,2000)
plt.ylabel(r'u($\lambda$)[kJ/nm]')
plt.xlabel(r'$\lambda$[nm]')
plt.savefig('bb_radiation.png',dpi=500,bbox_inches = 'tight')