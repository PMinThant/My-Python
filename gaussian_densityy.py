import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
def gaussian_density(x, mu, sigma):
    return (1/np.sqrt(2*np.pi*np.power(sigma, 2.))) * np.exp(-np.power(x - mu, 2.) / (2 * np.power(sigma, 2.)))

def plot_gaussian(x, mu, sigma):

    y = gaussian_density(x, mu, sigma)

    plt.plot(x, y)
    plt.title('Gaussian Probability Density Function')
    plt.xlabel('x variable')
    plt.ylabel('probability density function')
    plt.show()

def gaussian_probability(mean, stdev, x_low, x_high):
    return norm(loc = mean, scale = stdev).cdf(x_high) - norm(loc = mean, scale = stdev).cdf(x_low)
ans =gaussian_probability(50, 10, 0, 100)
print(ans)
x= 60
mu = 50
sigma = 10
ans = plot_gaussian(x, mu, sigma)
print(ans)
