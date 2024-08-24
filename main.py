import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.monitor import Monitor
import os

# create a larger custom map for FrozenLake
custom_map = [
    'SFFFFHFFFF',
    'FFFHFHHFFF',
    'FFFFFHHFFF',
    'FHFFFFHHFF',
    'FFFFFHFFFF',
    'FFFHFFFFHF',
    'FFHHFFFFFH',
    'FHFFFHHFFF',
    'FFFFHFFFFF',
    'FFFHFFFFFG'
]

# custom FrozenLake environment
env = gym.make(
    'FrozenLake-v1',
    desc=custom_map,
    is_slippery=True,
    render_mode='human'
)

# Wrap the environment with a Monitor wrapper to record results
env = Monitor(env)

# Wrap the environment in a DummyVecEnv to support parallel environments (even though we only have one here)
env = make_vec_env(lambda: env, n_envs=1)

# Specify the path for saving/loading the model
model_path = "ppo_frozenlake.zip"

# Check if the model already exists
if os.path.exists(model_path):
    # Load the existing model
    model = PPO.load(model_path, env=env)
    print(f"Model loaded from {model_path}")
else:
    # Create a new model if no saved model is found
    model = PPO(
        "MlpPolicy",
        env,
        learning_rate=0.0003,
        n_steps=2048,
        batch_size=64,
        n_epochs=10,
        gamma=0.99,
        clip_range=0.1,
        ent_coef=0.01,  # Increase entropy to encourage exploration
        verbose=1
    )
    print("No existing model found, training from scratch")

# Train the model with a higher number of timesteps
model.learn(total_timesteps=10000)

# Save the model after training
model.save(model_path)
print(f"Model saved at {model_path}")

# Test the trained model
obs = env.reset()
for _ in range(1000):
    action, _states = model.predict(obs)
    obs, reward, done, info = env.step(action)
    env.render()
    if done:
        obs = env.reset()

env.close()
