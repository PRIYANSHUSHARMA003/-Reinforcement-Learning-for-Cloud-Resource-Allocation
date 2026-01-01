import gymnasium as gym
from gymnasium import spaces
import numpy as np

class CloudEnv(gym.Env):
    def __init__(self):
        super().__init__()

        self.action_space = spaces.MultiDiscrete([11, 11])

        self.observation_space = spaces.Box(
            low=0,
            high=100,
            shape=(4,),
            dtype=np.float32
        )

        self.total_cpu = 100
        self.total_memory = 100

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)

        self.available_cpu = self.total_cpu
        self.available_memory = self.total_memory

        self.task_cpu = np.random.randint(1, 20)
        self.task_memory = np.random.randint(1, 20)

        state = np.array([
            self.available_cpu,
            self.available_memory,
            self.task_cpu,
            self.task_memory
        ], dtype=np.float32)

        return state, {}

    def step(self, action):
        cpu_alloc, mem_alloc = action

        if cpu_alloc >= self.task_cpu and mem_alloc >= self.task_memory:
            reward = 10
            latency = 1
        else:
            reward = -5
            latency = 5

        reward += (cpu_alloc / self.total_cpu) + (mem_alloc / self.total_memory)

        self.task_cpu = np.random.randint(1, 20)
        self.task_memory = np.random.randint(1, 20)

        terminated = False
        truncated = False

        state = np.array([
            self.available_cpu,
            self.available_memory,
            self.task_cpu,
            self.task_memory
        ], dtype=np.float32)

        info = {"latency": latency}

        return state, reward, terminated, truncated, info
