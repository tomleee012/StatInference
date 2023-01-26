import numpy as np
from matplotlib import pyplot as plt

# Simulate the correlation coefficient rho from example 
def SimuRho(mean=np.array([0, 0]), var=1):
    rhos = np.linspace(-1, 1, 41)

    # simulate the data X and Y first
    nRep = 2 ** 10 # the number of simulations
    nSize = 2 ** 15

    RhoHats = [] # store the simulation result of rho
    RhoTildes = [] # store the simulation result of rho

    for r in rhos:
        # VarMat = np.array([[var, r], [r, var]])
        RhoHatResult = [] # store the simulation result of rho
        RhoTildeResult = [] # store the simulation result of rho
        for i in range(nRep):
            xdata = np.random.normal(loc=mean[0], scale=np.sqrt(var), size=nSize)
            ydata = [r * d for d in xdata] + np.sqrt(1 - r**2) * np.random.normal(loc=mean[1], scale=np.sqrt(var), size=nSize)
            RhoHatResult.append(np.corrcoef(xdata, ydata)[0][1])

            RhoTildeResult.append( np.mean( [a * b for a,b in zip(xdata, ydata)] ) )

        RhoHats.append(np.var(RhoHatResult) + (np.mean(RhoHatResult) - r) ** 2) # variance + bias squared
        RhoTildes.append(np.var(RhoTildeResult) + (np.mean(RhoTildeResult) - r) ** 2)

    plt.plot(rhos, RhoHats, 'b')
    plt.plot(rhos, RhoTildes, 'r')
    plt.show()

    return RhoHats, RhoTildes


if __name__ == "__main__":
    rhohats, rhotildes = SimuRho()
    # print(rhohats)
    # print(rhotildes)
