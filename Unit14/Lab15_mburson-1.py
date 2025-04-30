import matplotlib.pyplot as plt
import numpy as np

x = np. linspace(-5,5)
y1 = 6 - x**2
y2 = 5 - x**2
y3 = 4 - x**2
y4 = 3 - x**2
y5 = 2 - x**2
y6 = 1 - x**2
y7 = 0 - x**2


plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

plt.plot(x, y1, color='red', linewidth=7, linestyle='-')

ax.plot(x,y2, color='orange', linewidth=7, linestyle='-')

plt.plot(x, y3, color='yellow', linewidth=7, linestyle='-')

ax.plot(x,y4, color='green', linewidth=7, linestyle='-')

plt.plot(x, y5, color='lightblue', linewidth=7, linestyle='-')

ax.plot(x,y6, color='blue', linewidth=7, linestyle='-')

plt.plot(x, y7, color='purple', linewidth=7, linestyle='-')


plt.show()