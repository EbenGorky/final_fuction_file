from tkinter import *
from matplotlib import pyplot as plt
from math import *
import numpy

def damped_oscillations(m,b,k):
    try:
        x = numpy.linspace(0,100,1000)
        y = []
        for i in x:
            y.append(e**(-b*i/2*m)*cos(((k/m - (b**2/4*m**2))**(1/2))*i))
        plt.plot(x,y)
        plt.show()
    except:
        print('hello world!')
        x = numpy.linspace(0,100,1000)
        y = []
        for i in x:
            y.append(e**(-b*i/2*m)*cos(((k/m + (b**2/4*m**2))**0.5)*i))
        plt.plot(x,y)
        plt.show()

def sum_of_sin_wav(n):
    a = list()
    w = Toplevel()
    for i in range(n):
        Label(w,text = 'enter the function of {i}st function').grid(row = 0,column = 0)
        e = Entry(w)
        e.grid(row = 0,column = 0   )
        a.append(e.get())
    print(a)
