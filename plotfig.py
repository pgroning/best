
import matplotlib.pyplot as plt
import math

fig = plt.figure()
ax = fig.add_subplot(111)
x = xrange(0,11)
y = [xx**2 for xx in x]
p = ax.plot(x, y, 'b')
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_title('XY point plot')
fig.show()
