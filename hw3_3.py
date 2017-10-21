import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

N = [2**15]

stepsize = 1.15
np.random.seed()

for n in N:
    n = int(n)
    
    S = np.zeros(n)
    xx = np.zeros(n+1)
    yy = np.zeros(n+1)    
    rejected = 0
    x, y = 0, 0
    
    for i in range(n):        
        dx = np.random.uniform(-stepsize,stepsize)
        dy = np.random.uniform(-stepsize,stepsize)
        x = x + dx
        y = y + dy
        
        if abs(x) > 1 or abs(y) > 1:
            x = x - dx
            y = y - dy
            rejected += 1
        if (x**2 + y**2) < 1:
            S[i] = 4
        xx[i] = x
        yy[i] = y
        
    iters = int(np.log(len(S))/np.log(2))
    SS = np.copy(S)
    errors = np.array([])
    varss = np.array([])
    for p in range(1,iters+1):
        size = len(S)
        SS = np.array([])
        midpoint = int(size / 2)
        for j in range(midpoint):
            SS = np.append(SS, np.sum(S[2*j:2*j + 2]) / 2)
        S = np.copy(SS)
        print(p)
        print(np.mean(S))
        print(np.sqrt(np.var(S) / n))
        print()
        varss = np.append(varss, np.var(S)/n)
        errors = np.append(errors, 1 / (n - 1) * np.sum(S**2- (np.mean(S))**2 )/n)

plt.plot(np.sqrt(varss) - np.sqrt(errors))
plt.plot(np.sqrt(errors))



