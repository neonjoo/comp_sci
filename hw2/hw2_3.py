import numpy as np
import matplotlib.pyplot as plt

lower = 1 
upper = 20

def pdf_single(scale):
    x = np.random.exponential(scale=scale)
    if x < 20 and x > 1:
        return x
    return pdf_single(scale)

def norm_pdf(lower, upper, scale, size):
    """ Draws $size points from the normalized distribution"""
    xx = np.zeros(size)
    for i in range(size):
        xx[i] = pdf_single(scale)
    return xx

def pdf_x(x, lower, upper, scale):
    xx = np.zeros(len(x))
    Z = np.exp(-lower/scale) - np.exp(-upper/scale)
    for i in range(len(x)):
        if x[i] >= lower and x[i] <= upper:
            xx[i] = np.exp(-x[i]/scale) / Z / scale
        else:
            xx[i] = 0
    return xx

#samples = [10, 100, 1000]
#lambda_ = 10
#for n in samples:
#    xx = norm_pdf(lower, upper, lambda_, n)
#    lambdas = np.linspace(1, 25, n)
#    likelihoods = np.zeros(len(lambdas))
#    
#    for a in range(len(lambdas)):
#        total = np.sum(np.log(pdf_x(xx, lower, upper, lambdas[a])))
#        likelihoods[a] = total
#    
#    plt.title("Estimates of " + r'$\lambda$') ## + " with " + str(n) + " samples")
#    plt.xlabel("Estimated " + r'$\lambda$')
#    plt.ylabel("Likelihood, normalized units")    
#    plt.ylim([-1.1, -0.99])
#    plt.plot(lambdas, likelihoods/np.abs(np.max(likelihoods)), ".", label=n)
#    plt.grid()
#    plt.legend(loc=4)
    
    
    
    
samples = [10, 100, 1000]
lambda_s = [2, 20]
max_likes = np.array([])

for lambda_ in lambda_s:
    max_like = np.zeros(len(samples))
    
    for n in samples:
        xx = norm_pdf(lower, upper, lambda_, n)
        lambdas = np.linspace(1, 50, n)
        likelihoods = np.zeros(len(lambdas))
        
        for a in range(len(lambdas)):
            total = np.sum(np.log(pdf_x(xx, lower, upper, lambdas[a])))
            likelihoods[a] = total
            
        index = samples.index(n)
        max_like[index] = lambdas[np.argmax(likelihoods)]
        plt.figure()
        plt.plot(lambdas, likelihoods/np.abs(np.max(likelihoods)), ".", label=n)
        
    max_likes = np.append(max_likes, max_like)
max_likes = np.reshape(max_likes, (len(lambda_s),len(samples)))

print(max_likes)