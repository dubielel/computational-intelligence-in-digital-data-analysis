import gymnasium as gym
from tqdm import tqdm

from lab4.agents.q_learning_agent import QLearningAgent


env = gym.make("envs/GuessNumberEnv-v0", algorithm="QLearning", render_mode="human")
agent = QLearningAgent(env.observation_space['agent'], env.action_space)

# Train the agent
num_episodes = 1000
for episode in tqdm(range(num_episodes)):
    observation = env.reset()
    done = False
    while not done:
        action = agent.choose_action()
        next_observation, reward, done, _, _ = env.step(action)
        agent.update_q_table(action, reward)
        observation = next_observation
    agent.decay_exploration_rate()

# Test the trained agent
observation = env.reset()
done = False
while not done:
    action = agent.choose_action()
    next_observation, reward, done, _, _ = env.step(action)
    observation = next_observation
    env.render()