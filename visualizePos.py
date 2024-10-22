import pandas as pd
import matplotlib.pyplot as plt
import imageio
import os

# Load the drone positions from CSV
data = pd.read_csv('C:/Users/upina/documents/GitHub/upekesha/drone_positions.csv')

# Define the folder where you want to save the frames and gif
save_folder = 'C:/Users/upina/documents/GitHub/upekesha/output_frames'

# Get unique time steps
time_steps = data['TimeStep'].unique()

# Prepare to store the images for creating a GIF
filenames = []

# Create a plot for each time step
for t in time_steps:
    # Filter the data for the current time step
    step_data = data[data['TimeStep'] == t]
    
    # Plot the positions of the drones
    plt.figure(figsize=(6, 6))
    plt.scatter(step_data['X'], step_data['Y'], c='blue', s=100)
    
    # Annotate the drones with their indices at each time step
    for i, row in step_data.iterrows():
        plt.text(row['X'] + 0.1, row['Y'] + 0.1, f'Drone {i}', fontsize=12)
    
    plt.xlim(-10, 1000)
    plt.ylim(-10, 1000)
    plt.title(f'Drone Simulation - Time Step {t}')
    plt.xlabel('X Position')
    plt.ylabel('Y Position')

    # Save each frame
    filename = f'frame_{t}.png'
    plt.savefig(filename)
    filenames.append(filename)
    plt.close()

# Create a GIF from the saved frames in the specified folder
gif_path = os.path.join(save_folder, 'drone_simulation.gif')
with imageio.get_writer(gif_path, mode='I', duration=0.5) as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)

# Clean up saved frames (optional)
import os
for filename in filenames:
    os.remove(filename)
