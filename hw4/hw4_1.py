import numpy as np
import matplotlib.pyplot as plt

L = 10
n = 5
sig = 0.1
runs = 1000

all_positions = np.zeros((runs,n))

for i in range(runs):
    positions = np.random.uniform(sig, L - sig, n)
    
    while abs(pos2 - pos1) < 2*sig:
        pos1 = np.random.uniform(sig, L - sig)
        pos2 = np.random.uniform(sig, L - sig)
    positions[i] = [pos1, pos2]

plt.figure()
plt.hist([positions[:,0], positions[:,1]], label=["1", "2"], bins=25, normed=True)
plt.legend()
plt.xlabel("Position")
plt.ylabel("Relative frequency")
plt.show()
plt.close("all")