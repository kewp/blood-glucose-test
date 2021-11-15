import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

'''
A, nu, k = 10, 4, 2

def f(x, A, nu, k):
    return A * np.exp(-k*x) * np.cos(2*np.pi * nu * x)

xmax, nx = 0.5, 8
x = np.linspace(0, xmax, nx)
y = f(x, A, nu, k)
'''
x = [0,30,50,82,97,108,119,136,146,156]
y = [4.7,4.8,5.4,5.9,6.3,6.3,6.3,6.3,6.0,6.3]

f_nearest = interp1d(x, y, kind='nearest')
f_linear  = interp1d(x, y)
f_cubic   = interp1d(x, y, kind='cubic')

x2 = np.linspace(0, 156, 100)
plt.plot(x, y, 'o', label='data points')
#plt.plot(x2, f(x2, A, nu, k), label='exact')
plt.plot(x2, f_nearest(x2), label='nearest')
plt.plot(x2, f_linear(x2), label='linear')
plt.plot(x2, f_cubic(x2), label='cubic')

plt.title('Blood glucose after eating low-carb granola')
plt.ylabel('mmol/L')
plt.xlabel('Minutes from eating')

plt.legend()

plt.show()
