# Author: Erik Bobinski
# Date: 9/18/2024
# Description: sums all odd integers within random bounds [ [1-10], [11-20] ]
import random

lowerBound = random.randint(1,10)
upperBound = random.randint(11,20)
print(f"Randomly generated interval to compute odd sum: [{lowerBound}, {upperBound}]\n")
oddSum = 0

for num in range(lowerBound, upperBound + 1):
    if num % 2 == 0: # even
        continue
    else: # odd
        print(f"{num} is odd, including in sum")
        oddSum += num

print(f"The final odd sum is {oddSum}")

