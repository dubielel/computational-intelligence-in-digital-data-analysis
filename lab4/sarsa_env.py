import gymnasium as gym

from lab4.agents.sarsa_agent import SARSAAgent

env_sarsa = gym.make("envs/GuessNumberEnv-v0", algorithm="SARSA", render_mode="human")
agent = SARSAAgent(env_sarsa.observation_space, env_sarsa.action_space)

# Train the agent
agent.train(env_sarsa, episodes=1000)

# Test the agent
observation = env_sarsa.reset()
done = False
while not done:
    action = agent.choose_action(observation)
    observation, reward, done, _, _ = env_sarsa.step(action)
    env_sarsa.render()
