import numpy as np
from matplotlib import pyplot as plt

# convergence in probability
def ConProb(nRep: int):
    ds


#  Stochastic convergence
def StoCon():
    nRep = 2 * 12 # number of simulations
    nSize = [2 ** i for i in range(5)] # number of sample size

    X = np.random.choice([-1, 1], 1)[0] # the value of X
    Xn = []

    for iRep in range(nRep):
        ds

    
    for n in nSize:
        In = np.random.binomial(n=1, p=1/n**2) # In ~ Bern(1/j**2)
        Xn.append( n * In + X * (1 - In)) # representation
        
    plt.plot([i for i in range(1, nSize)], Xn, 'b')
    plt.plot([i for i in range(1, nSize)], [X for i in range(1, nSize)], 'r')
    plt.show()

if __name__ == "__main__":
    results = StoCon()
