# Author: Erik Bobinski
# Date: 9/11/2024
# Description: Given a duration of time, this program computes 
# the velocity, average velocity, and displacement of an object.

# Useful values:
acceleration = 5.25
initialVelocity = 8.25

# Initialize the radius:
time = 10.0

# Calculate the properties of the object:

velocity = initialVelocity + acceleration*time

averageVelocity = initialVelocity + 0.5*acceleration*time

displacement = initialVelocity*time + 0.5*acceleration*(time ** 2)


# Print the results:

print("time = ",time)

print(f"""
velocity         = {velocity}
average velocity = {averageVelocity}
displacement     = {displacement}""")

