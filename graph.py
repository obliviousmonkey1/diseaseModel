import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# Example code [subject to change]

fig, ax = plt.subplots()   # a figure with a single axes

# days on the x, infected on the y 
# we store number of infected in a list and then use the indexes + 1 for the days 
ax.plot([days],[infected_per_day])
# Track immunity 
ax.plot([days],[immune_per_day])
# Track mortality 
ax.plot([days],[dead_per_day])

ax.set(xlabel='day', ylabel='number of people',
       title='Infection tracker')
ax.grid()

fig.savefig("infection.png")
plt.show()
