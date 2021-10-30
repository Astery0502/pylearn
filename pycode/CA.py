# code for a kind of cellular automata from automation python 

import time, random, copy
width = 60
height = 20

# Create a list of list for the cells:
nextcells =[]
for x in range(width):
    column = [] # create a new column
    for y in range(height):
        if random.randint(0,1) == 0:
            column.append('#') # Add a living cell.
        else:
            column.append(' ') # Add a dead cell.
    nextcells.append(column) #nextcells is a list of column lists.

while True: 
    print('\n\n\n\n\n
