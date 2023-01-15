# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 11:17:32 2022

@author: Abhi
"""

import numpy as np

#rnd =np.random.rand(10)
x=np.array([0,1,2,3,4,5])
prob=np.array([0.3,0.2,0.15,0.1,0.13,0.12])
cums=np.cumsum(prob)
cums
rnd=[0.614,0.178,0.34,0.18,0.811,0.628,0.4383,0.5867,0.925,0.967]
l=[]
for d in rnd:
    if d<cums[len(cums)-1] and d>=cums[len(cums)-2]:
        l.append(5)
    elif d<cums[len(cums)-2] and d>=cums[len(cums)-3]:
        l.append(4)
    elif d<cums[len(cums)-3] and d>cums[len(cums)-4]:
        l.append(3)
    elif d<cums[len(cums)-4] and d>cums[len(cums)-5]:
        l.append(2)
    elif d<cums[len(cums)-5] and d>cums[len(cums)-6]: 
        l.append(1)
    elif d<cums[0]:
        l.append(0)
        
print(l)        


m=[]
for d in rnd:
    for i in range(0,len(cums)):
        if i==len(cums)-1:
            m.append(i)
        elif d in np.arange(cums[i],cums[i+1]):
            m.append(i)
            
print(m)        
x=np.arange(3.44,6.44,0.001)
if 4.43 in x:
    print('yes')
else:
    print('no')    
