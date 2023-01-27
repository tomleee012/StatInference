import numpy as np
from matplotlib import pyplot as plt

# convergence in probability
def ConProb(nRep: int, nEps: int, X: list, Xn: list) -> list:
    epsilons = [1/10**i for i in range(nEps)]
    results = [0.0 for i in range(len(epsilons))]

    for i in range(len(epsilons)):
        eps = epsilons[i]
        for j in range(nRep):
            if np.abs(X[j] - Xn[j]) > eps:
                results[i] += 1
        results[i] /= nRep

    return results

# convergence in quadratic mean
def ConQM(nRep: int, X: list, Xn: list) -> list:
    return [0, 0, 0]

#  Stochastic convergence
def StoCon():
    nRep = 2 * 16 # number of simulations
    nLen = 5
    nSize = [2 ** i for i in range(nLen)] # number of sample size

    nEps = 3 # number of epsilons
    ProbResult = [[] * nEps for i in range(nLen)] # there are 3 epsilons
    QMResult = [[] * nEps for i in range(nLen)] # there are 3 epsilons
    
    for i in range(5):
        n = nSize[i]
        X = []
        Xn = []

        for iRep in range(nRep):
            X.append(np.random.choice([-1, 1], 1)[0]) # the value of X

            In = np.random.binomial(n=1, p=1/n**2) # In ~ Bern(1/n**2)
            Xn.append(n * In + X[iRep] * (1 - In)) # representation

        ProbResult[i] = ConProb(nRep, nEps, X, Xn)
        QMResult[i]   = ConQM(nRep, nEps, X, Xn)

    for 

    plt.plot([i for i in range(1, nSize)], Xn, 'b')
    plt.plot([i for i in range(1, nSize)], [X for i in range(1, nSize)], 'r')
    plt.show()    
        


if __name__ == "__main__":
    StoCon()

    print(ProbResult)
