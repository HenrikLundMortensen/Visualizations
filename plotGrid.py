import matplotlib.pyplot as plt
import numpy as np


g = np.array([[0,0,1,1,1],[2,1,2,1,1],[2,1,1,2,1],[0,1,1,1,0],[0,0,2,2,0]])

a = np.where(g==2)[0]
b = np.where(g==2)[1]
print(a)
print(b)

plt.plot(a,b,'ro')

a = np.where(g==1)[0]
b = np.where(g==1)[1]
print(a)
print(b)

plt.plot(a,b,'bo')

plt.show()



