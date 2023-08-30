##nsphere.py
#Claire Landgraf
#The purpose of this program is to plot the volume of an n-sphere over a range of n and a range of radii.

import math
import matplotlib.pyplot as plt

graphType = input('Please input 1 for 3D, 2 for x = R, and 3 for x = n:')
if graphType == '1':
    #Create scatter plot
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    #Loop through n from 0 to 50
    for n in range(51):
        #Loop through R from 1 to 2
        for i in range(21):
            R = 0.05*i + 1
            #Define volume of n-sphere
            V = math.pi**(float(n/2)) * (R)**n / math.gamma(float(n/2) + 1)
            #Add point to scatterplot
            ax.scatter(n,R,V,'p')

    #Format plot
    ax.set_xlabel('n')
    ax.set_ylabel('R')
    ax.set_zlabel('V')
    ax.set_title('Volume (V) of n-sphere over both dimensions (n) and radius (R)')
    
elif graphType == '2': 
    for n in range(51):
        R = []
        V = []
        for i in range(21):
            R.append(0.05*i + 1)
            V.append(math.pi**(float(n/2)) * (0.05*i+1)**n / math.gamma(float(n/2) + 1))
        plt.plot(R,V)
    plt.xlabel('R')
    plt.ylabel('V')
    plt.title('Volume (V) of n-sphere over radius (R) for a range of dimensions (n)')
        
else:
    for i in range(21):
        R = 0.05*i + 1
        n = []
        V = []
        for j in range(51):
            n.append(j)
            V.append(math.pi**(float(j/2)) * (R)**j / math.gamma(float(j/2) + 1))
        plt.plot(n,V)
    plt.xlabel('n')
    plt.ylabel('V')
    plt.title('Volume (V) of n-sphere over dimension (n) for a range of radii (R)')
        

#Display plot
plt.show()

