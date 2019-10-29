__author__ = "Aylin Nadine Okandan"

import numpy as np
import random
import math
import matplotlib.pylab as plt

pi = [] #saves every value of pi in a list
index = [] #saves the values 10 to 10000 in a list

for i in range(10, 10000): #for-loop for the iteration from 10 to 10000
    index.append(i)
    p_all = 0 #number of all points
    p_circle = 0 #number of points which is within the circle with r=0.5
    for j in range(i): #for-loop to generate i times a random number
        p_all = p_all + 1
        x = random.uniform(0, 0.5) #generates a random point within the square
        y = random.uniform(0, 0.5)
        distance = math.sqrt(x**2 + y**2) #calculates the distance between the position of the generated point and the middle of the circle
        if distance <= 0.5: #if the distance is smaller or is r=0.5, then the point is within the circle
            p_circle = p_circle + 1 
    #quotient of the points within the circle and all points, multiplied by 4 (because of the ratio between the area of the circle and the area of the square
    pi.append(p_circle*4/p_all)      

#Monte-Carlo plot
plt.hlines(np.pi, 0, 10000, label=r'$\pi$', zorder=1) #graph for comparison with pi in the foreground    
plt.plot(index, pi, label='calculated 'r'$\pi$', zorder=0)
plt.legend(loc=1)
plt.xlabel('size of iteration')
plt.ylabel('calculated value of 'r'$\pi$')
plt.show()
