import numpy as np
from tqdm import tqdm


class SARSAAgent:
    def __init__(self, observation_space, action_space, learning_rate=0.1, discount_factor=0.99, epsilon=0.1):
        self.observation_space = observation_space
        self.action_space = action_space
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = epsilon
        self.q_table = np.zeros((observation_space["agent"].n, action_space.n))

    def choose_action(self, observation):
        if np.random.rand() < self.epsilon:
            return np.random.randint(self.action_space.n)
        else:
            return np.argmax(self.q_table[observation["agent"]])

    def update_q_table(self, observation, action, reward, next_observation, next_action):
        current_q_value = self.q_table[observation["agent"], action]
        next_q_value = self.q_table[next_observation["agent"], next_action]
        td_target = reward + self.discount_factor * next_q_value
        td_error = td_target - current_q_value

        if reward == -1:
            # chosen number is too small, so update every possible [state, action] smaller than chosen number
            # so that we can avoid choosing smaller numbers than currently chosen one
            self.q_table[: observation["agent"] + 1, : action + 1] += self.learning_rate * td_error
            self.q_table[:, : action + 1] += self.learning_rate * td_error
            self.q_table[: observation["agent"] + 1, :] += self.learning_rate * td_error
            return
        if reward == -2:
            # chosen number is too big
            self.q_table[observation["agent"]:, action:] += self.learning_rate * td_error
            self.q_table[:, action:] += self.learning_rate * td_error
            self.q_table[observation["agent"]:, :] += self.learning_rate * td_error

            return

        self.q_table[observation["agent"], action] += self.learning_rate * td_error

    def train(self, env, episodes):
        for i in tqdm(range(episodes)):
            observation = env.reset()
            action = observation['agent']
            done = False
            while not done:
                next_observation, reward, done, _, info = env.step(action)
                # if i in [0, 50, 99]:
                #     print(f'{i} {info["message"]}')
                next_action = self.choose_action(next_observation)
                self.update_q_table(observation, action, reward, next_observation, next_action)
                observation = next_observation
                action = next_action
