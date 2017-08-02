import matplotlib.pyplot as plt
import numpy as np

def plotGrid(g,fig):
    ax = fig.gca()
    a = np.where(g==2)[0]
    b = np.where(g==2)[1]
    ax.plot(b,-a,'ro',markersize=15)
    
    a = np.where(g==1)[0]
    b = np.where(g==1)[1]
    ax.plot(b,-a,'bo',markersize=30)
    



