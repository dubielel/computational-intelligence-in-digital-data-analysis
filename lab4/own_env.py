import gymnasium as gym
from lab4.envs import GuessNumberEnv

import numpy as np
import random
from tqdm import tqdm


env = gym.make("envs/GuessNumberEnv-v0", render_mode="human")


class QLearningAgent:
    def __init__(
            self,
            observation_space,
            action_space,
            learning_rate=0.1,
            discount_factor=0.99,
            exploration_rate=1.0,
            min_exploration_rate=0.01,
            exploration_decay_rate=0.99
    ):
        self.observation_space = observation_space
        self.action_space = action_space
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.min_exploration_rate = min_exploration_rate
        self.exploration_decay_rate = exploration_decay_rate
        self.q_table = np.zeros((action_space.n,))

    def choose_action(self):
        if random.uniform(0, 1) < self.exploration_rate:
            return self.action_space.sample()  # Explore action space
        else:
            print(self.q_table)
            return np.argmax(self.q_table)  # Exploit learned values

    def update_q_table(self, action, reward):
        old_q_value = self.q_table[action]
        next_max = np.max(self.q_table)
        new_q_value = (1 - self.learning_rate) * old_q_value + self.learning_rate * (reward + self.discount_factor * next_max)
        self.q_table[action] = new_q_value

    def decay_exploration_rate(self):
        self.exploration_rate = max(self.min_exploration_rate, self.exploration_rate * self.exploration_decay_rate)


agent = QLearningAgent(env.observation_space['agent'], env.action_space)


num_episodes = 1000
for episode in tqdm(range(num_episodes)):
    observation = env.reset()
    done = False
    while not done:
        action = agent.choose_action()
        print(f'action: {action}')
        next_observation, reward, done, _, _ = env.step(action)
        agent.update_q_table(action, reward)
        observation = next_observation
    agent.decay_exploration_rate()

# Test the trained agent
observation = env.reset()
done = False
while not done:
    action = agent.choose_action()
    # print(f'Current obs: {observation} taken action: {action}')
    next_observation, reward, done, _, _ = env.step(action)
    observation = next_observation
    env.render()
