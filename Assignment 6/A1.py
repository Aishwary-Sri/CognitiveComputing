import numpy as np
import matplotlib.pyplot as plt

m = float(input("Enter value: "))
x = np.linspace(-10,10,400)
y1 = m * x**2
y2 = m * np.sin(x)
plt.figure()
plt.plot(x,y1,"r-",label="m*x^2")
plt.plot(x,y2,"b--",label="m*sin(x)")
plt.legend()
plt.grid(True)
plt.title("Q1: Functions")
plt.show()
