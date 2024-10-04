# Author: Erik Bobinski
# Date: 10/4/2024
# Description: Generates a plot of temp vs time for three cities, each temp is randomized b/w [10-30] inclusively

import matplotlib.pyplot as plt
import random

# stores [1 thru 12] inclusively
time = [num for num in range(1,13)]

# Los Angeles
la = [random.randint(10,30) for _ in range(12)]
plt.plot(time, la)

# New York
ny = [random.randint(10,30) for _ in range(12)]
plt.plot(time, ny)

# Baltimore
ba = [random.randint(10,30) for _ in range(12)]
plt.plot(time, ba)

plt.title("Temp vs Time")

plt.xlabel("Time")
plt.ylabel("Temp")

plt.legend(["la", "ny", "ba"])

plt.show()
