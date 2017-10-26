import numpy as np
from scipy.stats import cauchy
import matplotlib.pyplot as plt

alfa = 30
beta = 10
samples = [10, 100, 1000]

for n in samples:

    xx = cauchy.rvs(loc=alfa, scale=beta, size=n) 
    alfas = np.linspace(10, 50, n)
    likelihoods = np.zeros(len(alfas))
    
    for a in range(len(alfas)):
        total = np.sum(np.log(cauchy.pdf(xx, loc=alfas[a], scale=beta)))
        likelihoods[a] = total
        
    plt.title("Estimates of " + r'$\alpha$' + " with " + str(n) + " samples")
    plt.xlabel("Estimated " + r'$\alpha$')
    plt.ylabel("Likelihood, normalized units")    
    plt.plot(alfas, likelihoods/np.abs(np.max(likelihoods)), ".", label=n)
best_like = np.sum(np.log(cauchy.pdf(xx, loc=alfa, scale=beta)))
plt.plot(alfa, best_like / np.abs(np.max(best_like)), 'r*', label="True value")
plt.grid()
plt.legend(loc=4)