"""
Created on Thu Feb  3 16:48:14 2022

@author: visit
"""


""" Author: CANAVAGGIO Thibault 
    Created: 24/12/2021
    Title: Méthode_d_Euler explicative
"""
import math
import numbers as np
import matplotlib as plt
plt
np
# à droite de l'équation différentielle de premier ordre 
def f(x):
    return (32/(32*x-64)**2)
# Condition Initiale
x_O =1/64
# le pas
dt= 0.1
#Intervalle de 0 jusqu'a T
T=1.8
#Subdivision
t=np.linspace(0,T,int(T/dt))
# variable pour garder en mémoire 
x=np.zeros(len(t))
# intégration de l'équation par la méthode d'Euler
x[0]=x_O
for i in range(1,len(t)):
    x[i]=x[i-1] + f(x[i-1])*dt
# Sauvegarde de la solution
np.savetxt('t.txt',t)
np.savetxt('x.txt',x)
# graph
plt.figure()
#plot solution
plt.plot(t,x,color='blue')
# Axes
plt.xlabel('t')
plt.ylabel('x(t)')
#sauvegarde graph
plt.savefig('plot.pdf')