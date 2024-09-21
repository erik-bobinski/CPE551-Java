# Author: Erik Bobinski
# Date: 9/18/2024
# Description: Simulates batting in baseball, and tells you 
# the result based on the distance the ball was hit
import random

ballDistance = random.randint(0,450)

if ballDistance == 0:
    print(f"Ball travelled {ballDistance}, strike!")
elif 1 <= ballDistance <= 9:
    print(f"Ball travelled {ballDistance} ft, batter bunted the ball and made it to first base.")
elif 10 <= ballDistance <= 134:
    print(f"Ball travelled {ballDistance} ft, batter hit the ball into the infield.")
elif 135 <= ballDistance <= 400:
    print(f"Ball travelled {ballDistance} ft, the batter hit the ball into the outfield.")
else:
    print(f"Ball travelled {ballDistance} ft, homerun!")
