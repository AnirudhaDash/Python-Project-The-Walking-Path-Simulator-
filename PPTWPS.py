import numpy as np
import matplotlib.pyplot as plt

# Function to perform a random walk
def random_walk(steps=1000):
    # Create an array of -1 and 1 randomly selected for each step
    steps_array=np.random.choice([-1, 1], size=steps)
    
    # Calculate position by summing up steps over time
    position=np.cumsum(steps_array)
    
    return position  # Return the positions array

# Function to plot the random walk path
def plot_random_walk(position):
    plt.figure(figsize=(10, 6))   # Set plot size
    
    # Plot the position over steps
    plt.plot(position, label='Random Walk Path')
    
    # Add title and labels to the plot
    plt.title('Random Walk Simulation')
    plt.xlabel('Step')
    plt.ylabel('Position')
    
    # Add a grid and a legend
    plt.grid(True)
    plt.legend()
    plt.show()  # Show the plot

# Run the random walk and plot it
if __name__=="__main__":
    steps=1000                        # Number of steps
    position=random_walk(steps)        # Run the random walk function
    plot_random_walk(position)           # Plot the result