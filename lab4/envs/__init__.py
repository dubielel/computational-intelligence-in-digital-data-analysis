from lab4.envs.guess_number_env import GuessNumberEnv
from gymnasium.envs.registration import register

register(
    id="envs/GuessNumberEnv-v0",
    entry_point="envs:GuessNumberEnv",
    max_episode_steps=300,
)