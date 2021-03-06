# -*- coding: utf-8 -*-
"""Assignment 8-1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qrWpd9Gh3WxYkqXcjhcqyfxkXMjScNtn
"""

# -*- coding: utf-8 -*-
"""Assignment8.ipynb
 
Automatically generated by Colaboratory.
Original file is located at
    https://colab.research.google.com/drive/1K4uGtnhOtv4P44277zg-xnL6sPEPhIgA
"""
#Code by Batharaju Ramana 
#June 28, 2021
 
import numpy as np
import matplotlib.pyplot as plt
 
#Generate line points
def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB
 
#Generating and plotting line 3x+2y = 12
A=np.array([2/3,5])
B=np.array([4,0])
AB=line_gen(A,B)
plt.plot(AB[0,:],AB[1,:],label='3x+2y=12')
 
#Generating and plotting line x=1
C=np.array([1,10])
D=np.array([1,0])
CD=line_gen(C,D)
plt.plot(CD[0,:],CD[1,:],label='x=1')
 
#Generating and plotting line y=2
E=np.array([-5,2])
F=np.array([5,2])
EF=line_gen(E,F)
plt.plot(EF[0,:],EF[1,:],label='y=2')
 
#Shading Required Region
x1=[2.70,1,1]
y1=[2,2,4.5]
plt.fill(x1,y1)
 
#Labelling points
plt.plot(1,9/2,'o',color='r')
plt.text(2,5,'A(1,9/2)')
plt.plot(1,2,'o',color='r')
plt.text(0,0.5,'B(1,2)')
plt.plot(8/3,2, 'o', color='r')
plt.text(3,2,'C(8/3,2)')
 
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')