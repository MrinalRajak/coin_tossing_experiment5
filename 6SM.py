

# 6:Find the probability distribution P(n) for throwing a sum 'n'
# with two dices. Plot P(n) as a function of 'n'.
# (Answer should be first analitically calculated and then numerically verified).


import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randint

P= lambda n: [sum(randint(6,size=n)) for i in range(trial)]
markers=['o']
n , trial = 2 , 10000

for i in range(1):
    x,y=np.unique(P(n),return_counts=True)
    x=x/n
    y=y/np.max(y)
    plt.plot(x,y,marker=markers[i])
    n=n*10

plt.xlabel('n')
plt.ylabel('P(n)')
plt.legend(['n=2'])
plt.show()
