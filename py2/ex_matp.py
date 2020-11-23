import matplotlib.pyplot as plt
import numpy as np


data1 = [10,15,19,20,25]
# plt.plot(data1)
plt.show()

x=np.arange(-4.5,4.5,0.5)    #arange(start,args,kwargs)
y=2*x**2
plt.plot(x,y)
plt.show()

