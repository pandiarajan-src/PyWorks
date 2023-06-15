# You are required to write the code to calculate Euclidean distance
# to store in the variable dist
import math

# Assume that we have the following variables already defined:
# xp, yp and xq, yq
xp, yp = 5, 8
xq, yq = 9, 11

# Here we calculate dx and dy
dx = xq - xp
dy = yq - yp
# You are required to use the above variables to calculate 
# the euclidean distance and store the result in the variable dist
dist = math.sqrt((dx ** 2) + (dy ** 2)) # equl to (((dx**2) + (d**2))**0.5)
print(f"distance: {dist}")