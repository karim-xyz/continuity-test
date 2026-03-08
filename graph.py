import plotext as plt
import numpy as np
from sympy import lambdify

def draw(f, s):
    g = lambdify(s, f, modules="numpy")
    x = np.linspace(-10, 10, 1000)
    y = g(x)
    
    plt.plot(x, y, color="red", marker="dot", label="f")
    
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.xticks([-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10])
    plt.yticks([-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10])

    #draw x axis (horizontal line at y=0)
    plt.horizontal_line(0, color="white")
    
    #draw y axis (vertical line at x=0)
    plt.vertical_line(0, color="white")
    
    plt.xlabel("x")
    plt.ylabel("y")
    
    #black background
    plt.clc()

    plt.show()

