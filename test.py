from plotGrid import *
import matplotlib.pyplot as plt
import time


fig = plt.figure()

g = np.array([[0,0,1,1,1],[2,1,2,1,1],[2,1,1,2,1],[0,1,1,1,0],[0,0,2,2,0]])
plotGrid(g,fig)
plt.pause(.001)
plt.draw()
print('Moving on')

time.sleep(3)
g = np.array([[0,0,1,1,1],[2,1,2,1,1],[2,1,1,2,1],[0,1,1,1,0],[0,0,2,2,2]])
plotGrid(g,fig)
plt.draw()
print('Ending')
plt.show()






