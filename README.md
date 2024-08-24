# FrozenLake-PPO-with-Custom-Map
This project is a work-in-progress implementation of a reinforcement learning agent trained to navigate a custom version of the FrozenLake environment using the Proximal Policy Optimization (PPO) algorithm from the Stable-Baselines3 library. The environment is a larger, more complex FrozenLake map designed to challenge the agent with additional obstacles and hazards.

# Project Overview

  Environment: The project uses a custom 10x10 FrozenLake map with slippery surfaces and additional holes (H cells) to navigate.
    
  Algorithm: Proximal Policy Optimization (PPO), a popular reinforcement learning algorithm, is used to train the agent.
  
# Libraries:
  gymnasium: To create and customize the FrozenLake environment.
  stable-baselines3: To implement and train the PPO algorithm.
  Monitor: To record the results and performance of the agent during training.

# Features

  Custom Map: A larger, more challenging FrozenLake map with complex paths and hazards.
    
  Model Saving and Loading: The model is saved after training, allowing you to load and continue training or testing from the last checkpoint.
    
  Training: The agent is trained over 10,000 timesteps, with a focus on exploration to successfully navigate the map.
    
  Testing: After training, the model is tested on the environment, and the agent's performance is rendered.

# Installation

To run this project, you need to have Python installed along with the required libraries. You can install the dependencies using pip:

    pip install gymnasium stable-baselines3

# How to Run

  Clone the repository.
    
  Ensure that the required libraries are installed.
  
  Run the Python script.

The script will either load a previously saved model or train a new one if no model is found. After training, the model will be saved and tested on the custom FrozenLake environment.

# Custom Map

The custom map used in this project is a 10x10 grid with the following layout:

    SFFFFHFFFF
    FFFHFHHFFF
    FFFFFHHFFF
    FHFFFFHHFF
    FFFFFHFFFF
    FFFHFFFFHF
    FFHHFFFFFH
    FHFFFHHFFF
    FFFFHFFFFF
    FFFHFFFFFG

   S: Starting point
  
  F: Frozen surface (safe to walk on)
  
  H: Hole (leads to failure)
  
  G: Goal

# Training Parameters

  Learning Rate: 0.0003
  Timesteps: 10,000
  n_steps: 2048
  Batch Size: 64
  n_epochs: 10
  Gamma: 0.99
  Clip Range: 0.1
  Entropy Coefficient: 0.01

Notes

  This project is still in development, and improvements or changes may be made to the environment or training process.
  The environment's complexity may cause some agents to fail frequently, especially during early stages of training.
