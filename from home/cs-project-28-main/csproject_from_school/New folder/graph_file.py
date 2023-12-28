from matplotlib import pyplot as plt
#import math
import numpy

def cr_fun(rhs):
    with open('sa.py','w') as fp:
        fp.write(f"def f(x):\n\treturn {rhs}")

import sa

def draw_graph(fun,start_value = 0,ending_value = 100,density = 1000):
    #cr_fun(fun)
    x = numpy.linspace(start_value,ending_value,density)
    y = []
    for i in x:
        y.append(sa.f(i))
    plt.plot(x,y)
    plt.show()

draw_graph('x**3',start_value=-100,ending_value=100)