'''Learn standard plot'''
import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
plt.plot(X, np.sin(X))       # Plot the sine of each x point
plt.show()                   # Display the plot
