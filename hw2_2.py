import numpy as np
from scipy.stats import cauchy
import matplotlib.pyplot as plt

x = cauchy.rvs(loc=30, scale=10, size=10) 
plt.hist(x, bins=50)

#test