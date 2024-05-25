# Author: Joshua Simpson
# Course: CST 305
# Date: 3/20/2024
# Description: This script explores the Lorenz attractor's chaotic behavior for different 'r' values. It calculates and plots the attractor's trajectory using NumPy for number crunching and Matplotlib for visual output, including 3D representations.

# Importing NumPy for numerical calculations
import numpy as np
# Importing Matplotlib's pyplot for plotting graphs
import matplotlib.pyplot as plt
# Importing Axes3D from mpl_toolkits for three-dimensional plotting capabilities
from mpl_toolkits.mplot3d import Axes3D  # Necessary for 3D graphing

# The Lorenz system's differential equations are encapsulated in this function
def lorenz(x, y, z, r, s=10, b=8/3):
    # Calculate the change rate of x
    x_dot = s * (y - x)
    # Calculate the change rate of y
    y_dot = r * x - y - x * z
    # Calculate the change rate of z
    z_dot = x * y - b * z
    # Outputs the calculated rates of change for x, y, and z
    return x_dot, y_dot, z_dot

# Function to solve the Lorenz equations over time and plot the results
def solve_and_plot(r):
    # Defines the simulation's time step size
    dt = 0.01
    # Specifies the total number of simulation steps
    num_steps = 10000

    # Initialize storage for the variables' values throughout the simulation
    xs = np.empty(num_steps + 1)
    ys = np.empty(num_steps + 1)
    zs = np.empty(num_steps + 1)

    # Sets the starting conditions for the simulation
    xs[0], ys[0], zs[0] = (0.5, 1, 1.5)

    # Iteratively solves the Lorenz system using the Euler method
    for i in range(num_steps):
        # Retrieves rates of change for the current step
        x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i], r=r)
        # Updates the system's state based on the current rates of change
        xs[i + 1] = xs[i] + (x_dot * dt)
        ys[i + 1] = ys[i] + (y_dot * dt)
        zs[i + 1] = zs[i] + (z_dot * dt)

    # Initiating plotting sequence for the simulation results
    # Setting up a figure for graphing with a custom size
    fig = plt.figure(figsize=(20, 5))  # This can be adjusted for different display sizes

    # Plot for X variable over time
    ax1 = fig.add_subplot(1, 4, 1)
    ax1.plot(xs, 'r-', label='X')
    ax1.set_title(f'X vs. Time (r={r})')
    ax1.legend()

    # Plot for Y variable over time
    ax2 = fig.add_subplot(1, 4, 2)
    ax2.plot(ys, 'g-', label='Y')
    ax2.set_title(f'Y vs. Time (r={r})')
    ax2.legend()

    # Plot for Z variable over time
    ax3 = fig.add_subplot(1, 4, 3)
    ax3.plot(zs, 'b-', label='Z')
    ax3.set_title(f'Z vs. Time (r={r})')
    ax3.legend()

    # Generating the 3D plot for the Lorenz attractor
    ax4 = fig.add_subplot(1, 4, 4, projection='3d')
    ax4.plot(xs, ys, zs, lw=0.5)
    ax4.set_title(f'Lorenz Attractor (r={r})')

    # Adjusts the layout for clarity and displays the plots
    plt.tight_layout()
    plt.show()

# Predefined 'r' values for simulation
r_values = [10, 19, 28]
# Looping through each 'r' value, simulating and plotting the system's behavior
for r in r_values:
    solve_and_plot(r)   # Executes the function for each specified 'r' value
