import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()   # a figure with a single axes

# days on the x, infected on the y 
# we store number of infected in a list and then use the indexes + 1 for the days 
ax.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],[1,1,1,1,2,5,10,20,80,90,140,120,90,100,70,45])
# Track immunity 
ax.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],[0,0,0,0,0,0,0,2,4,7,3,5,20,50,70,100])
# Track mortality 
ax.plot
ax.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],[0,0,0,0,0,0,0,2,4,7,3,5,8,9,10,11])

ax.set(xlabel='day', ylabel='number of people',
       title='Infection tracker')
ax.grid()

fig.savefig("infection.png")
plt.show()