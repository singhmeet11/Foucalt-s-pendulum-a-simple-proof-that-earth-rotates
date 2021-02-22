# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 11:32:21 2020


"""

import matplotlib.pyplot as plt

import numpy as np
from matplotlib.animation import FuncAnimation 
from IPython import display



#defining the constants  and initialising t
g=9.8 
L=67
R=0.01   #anguluar speed of earth
lamda=0   #longitude
k_1=1
k_2=1              
t=0

#definied the figure
fig, ax= plt.subplots()
ax.set_xlim(-5,5)
ax.set_ylim(-5,5)
#this is the line that FuncAnimation will modify for animation
line, =ax.plot([],[],'o')
plt.grid()

#defined the function
def pendulum(A):
    t = A
    a_=1j*(np.sqrt(g/L)*t)
    a=np.exp(a_)


    b_=1j*((-1)*np.sqrt(g/L)*t)
    b=np.exp(b_)

    c_=1j*(R*np.sin(lamda)*(-1)*t)
    
    c=np.exp(c_)
    u=(k_1*a+k_2*b)*c
    
    x=u.real
    y=u.imag
    
    
    
    line.set_xdata(x)
    line.set_ydata(y)
   
    return line,
    
#this is the main part, in which the FuncAnimation will use to plot the command
animation = FuncAnimation(fig, pendulum, frames = np.arange(0,100,0.1),interval=100)
animation.save('Foucalt_pendulum_equator.mp4',fps=30, extra_args=['-vcodec', 'libx264'])

