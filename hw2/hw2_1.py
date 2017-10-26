import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


N = [1e2, 1e3, 1e4]

runs = 100

for n in N:
    n = int(n)
    pis = np.zeros(runs)
    variances = np.zeros(runs)
    est_vars = np.zeros(runs)
    mean_vars = np.zeros(runs)
    
    for j in range(runs):
        S = np.zeros(n)
        xx = np.zeros(n)
        yy = np.zeros(n)
        
        for i in range(n):        
            x = np.random.uniform(-1,1)
            y = np.random.uniform(-1,1)
            xx[i] = x
            yy[i] = y
            
            if (x**2 + y**2) < 1:
                S[i] = 4
                
        pis[j] = np.mean(S)
        variances[j] = np.var(S)        
        est_vars[j] = 1 / (n - 1) * np.sum(S**2- (np.mean(S))**2 )
        mean_vars[j] = np.var(S) / n
        
   # plot_drawn()
    
    print()
    print("N =", n)
    print("Estimate of pi:")
    print(np.mean(pis))
    print("Variance of estimates of pi:")
    print(np.var(pis))
    print("Mean of variance of estimated mean (m-hat) of each run:")
    print(np.mean(mean_vars))
    print("Mean of variance of each run:")
    print(np.mean(variances))
    print("Mean of estimated variance of each run:")
    print(np.mean(est_vars))


    
    def plot_drawn():
        plt.figure()
        ax = plt.gca()
        circle = plt.Circle((0,0), 1, color="red", fill=False, zorder=5, lw=3)
        
        plt.plot(xx,yy, '.')
        plt.title("Example of " + str(n) + " points uniformly drawn")
        plt.xlabel("x")
        plt.ylabel("y")
        
        ax.add_artist(circle)
        ax.add_patch(Rectangle((-1,-1), 2, 2, lw=2, color="black", fill=False))
        plt.show()

