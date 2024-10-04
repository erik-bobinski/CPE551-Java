# Author: Erik Bobinski
# Date: 10/4/2024
# Description: Generates 8x8 matrix of simulated cosmic ray muon detectors (CRMDs)
# with randomly generated capture rates from [0-500]
import random

# dimensions of square map, should be held constant
DIM = 8

# 8x8 matrix
map = [ [0 for i in range(DIM)] for j in range(DIM)]


#iterate thru elements, in rand int between [0-500] inclusively
for row in range(DIM):
    for col in range(DIM):
        map[row][col] = random.randint(0,500)

# coordinates for relevant capture rates in `map`
xMax = 0
yMax = 0
rateMax = 0 # set to lowest max val possible to be overwritten below
rateMin = 500 # set to greatest min val possible to be overwritten below

# search for max and min in `map`
for row in range(DIM):
    for col in range(DIM):
        if map[row][col] > rateMax:
            rateMax = map[row][col]
            xMax = col + 1
            yMax = row + 1  
        elif map[row][col] < rateMin:
            rateMin = map[row][col]

# Display highest capture rate
print(f"The highest capture rate is {rateMax}, at ({xMax}, {yMax})")

# Display lowest capture rate
print(f"The lowest capture rate is {rateMin}\n")

# Display `map`
print("CRMD capture rate map:\n")
for row in map:
    print(" ".join(f"{cell:3}" for cell in row)) 
    # `f"{cell:3}"` ensures each cell occupies three character, with right-padding if necessary
    # `" ".join` joins the formatted strings with a space b/w them
