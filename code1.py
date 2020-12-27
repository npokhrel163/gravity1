
from pylab import *
import matplotlib.pyplot as plt
def list_generator1():
     time1 = linspace(0,5,50)
     yi= int(input("what is the initial height of your trajectory? "))
     g = 9.8
     vi = int(input("What is the initial velocity of the particle? "))
     list1 = []
     for a in time1:
        y_coordinate = yi + vi*a - (1/2)*g*(a**2)  #formula for calculating the trajectory
        list1.append(y_coordinate)
     for heights in list1:
        a = list1.index(heights)
        if heights <0:
            list1[a] = 0
     
     print(time1)
     print(list1)
     figure()
     plot(time1, list1)
     xlabel("time")
     ylabel("height")
     plt.show()

list_generator1()