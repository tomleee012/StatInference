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
def ConQM(nRep: int, nEps: int, X: list, Xn: list) -> list:
    return [0, 0, 0]

#  Stochastic convergence
def StoCon():
    nRep = 2 * 17 # number of simulations
    nLen = 5
    nSize = [2 ** i for i in range(nLen)] # number of sample size

    nEps = 4 # number of epsilons
    ProbResult = [[] * nEps for i in range(nLen)] # there are 3 epsilons
    QMResult = [[] * nEps for i in range(nLen)] # there are 3 epsilons
    
    for i in range(nLen):
        n = nSize[i]
        X = []
        Xn = []

        for iRep in range(nRep):
            X.append(np.random.choice([-1, 1], 1)[0]) # the value of X

            In = np.random.binomial(n=1, p=1/n**2) # In ~ Bern(1/n**2)
            Xn.append(n * In + X[iRep] * (1 - In)) # representation

        ProbResult[i] = ConProb(nRep, nEps, X, Xn)
        QMResult[i]   = ConQM(nRep, nEps, X, Xn)

    ProbVis = [[] * nLen for i in range(nEps)]

    for i in range(nEps):
        ProbVis[i] = [ProbResult[j][i] for j in range(nLen)]

    plt.plot(nSize, ProbVis, 'r')
    plt.title(f'The line graph of probability vs number of samples')
    plt.xlabel('Number of samples')
    plt.ylabel(r'$ P(| X - X_n | > \epsilon) $')
    plt.show()


if __name__ == "__main__":
    StoCon()