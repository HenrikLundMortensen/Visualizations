import matplotlib.pyplot as plt
import numpy as np

def plotGrid(g,fig):
    # Rotate grid, such that the view is correct
    rotg = np.rot90(g,3)
    
    # Find Ag index and pair them in a list
    indexAg = np.where(rotg==1)
    PairsAg = list( [indexAg[0][i],  indexAg[1][i] ] for i in range(len(indexAg[0])))
    
    # Find O index and pair them in a list
    indexO = np.where(rotg==2)
    PairsO = list( [indexO[0][i],  indexO[1][i] ] for i in range(len(indexO[0])))

    # Define the shearing matrix
    shearMat = np.array([[1, 0.5],[0,1]])

    # Multiply all coordinate pairs with the shearing matrix
    CoordsAg = np.array(list( np.dot(shearMat,i) for i in PairsAg)).T
    CoordsO = np.array(list( np.dot(shearMat,i) for i in PairsO)).T

    # Plot
    ax = fig.gca()
    ax.plot(CoordsAg[0],CoordsAg[1],'bo',markersize=30)
    ax.plot(CoordsO[0],CoordsO[1],'ro',markersize=15)

    # Make it look right
    ax.set_facecolor((0.9,0.8,1))
    ax.set_xlim([-1,8])
    ax.set_ylim([-1,5])
    # plt.xticks([])
    # plt.yticks([])



