from stable_baselines3 import PPO
from env.cloud_env import CloudEnv

# Create environment
env = CloudEnv()
print("Environment created successfully!")

# Create PPO model
model = PPO(
    "MlpPolicy",
    env,
    verbose=1
)

# Train model
model.learn(total_timesteps=10000)

# Save model
model.save("ppo_cloud_resource_model")

print("Training completed successfully!")
