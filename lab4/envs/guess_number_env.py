# fmt: off

# %%
# Declaration and Initialization
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# Our custom environment will inherit from the abstract class
# ``gymnasium.Env``. You shouldn’t forget to add the ``metadata``
# attribute to your class. There, you should specify the render-modes that
# are supported by your environment (e.g. ``"human"``, ``"rgb_array"``,
# ``"ansi"``) and the framerate at which your environment should be
# rendered. Every environment should support ``None`` as render-mode; you
# don’t need to add it in the metadata. In ``GridWorldEnv``, we will
# support the modes “rgb_array” and “human” and render at 4 FPS.
#
# The ``__init__`` method of our environment will accept the integer
# ``size``, that determines the size of the square grid. We will set up
# some variables for rendering and define ``self.observation_space`` and
# ``self.action_space``. In our case, observations should provide
# information about the location of the agent and target on the
# 2-dimensional grid. We will choose to represent observations in the form
# of dictionaries with keys ``"agent"`` and ``"target"``. An observation
# may look like ``{"agent": array([1, 0]), "target": array([0, 3])}``.
# Since we have 4 actions in our environment (“right”, “up”, “left”,
# “down”), we will use ``Discrete(4)`` as an action space. Here is the
# declaration of ``GridWorldEnv`` and the implementation of ``__init__``:

import numpy as np

import gymnasium as gym
from gymnasium import spaces


class GuessNumberEnv(gym.Env):
    metadata = {"render_modes": ['human'], "render_fps": 1}

    def __init__(self, algorithm, render_mode=None, min_number=1, max_number=100):
        self.algorithm = algorithm

        self._agent_number = None
        self._target_number = None

        self.min_number = min_number  # The number which is the lower threshold for the numbers range
        self.max_number = max_number  # The number which is the upper threshold for the numbers range 

        # Observations are dictionaries with the agent's and the target's numbers.
        self.observation_space = spaces.Dict(
            {
                "agent": spaces.Discrete(max_number - min_number + 1),
                "target": spaces.Discrete(max_number - min_number + 1),
            }
        )

        # The action in this env is a number from the range [min_number, max_number]
        self.action_space = spaces.Discrete(max_number - min_number + 1)

        assert render_mode is None or render_mode in self.metadata["render_modes"]
        self.render_mode = render_mode

        """
        If human-rendering is used, `self.window` will be a reference
        to the window that we draw to. `self.clock` will be a clock that is used
        to ensure that the environment is rendered at the correct framerate in
        human-mode. They will remain `None` until human-mode is used for the
        first time.
        """
        self.window = None
        self.clock = None

    # %%
    # Constructing Observations From Environment States
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #
    # Since we will need to compute observations both in ``reset`` and
    # ``step``, it is often convenient to have a (private) method ``_get_obs``
    # that translates the environment’s state into an observation. However,
    # this is not mandatory and you may as well compute observations in
    # ``reset`` and ``step`` separately:

    def _get_obs(self):
        return {"agent": self._agent_number, "target": self._target_number}

    # %%
    # We can also implement a similar method for the auxiliary information
    # that is returned by ``step`` and ``reset``. In our case, we would like
    # to provide the manhattan distance between the agent and the target:

    def _get_info(self):
        diff = self._target_number - self._agent_number
        match self.algorithm:
            case "QLearning":
                """
                When `self._target_number` is greater than chosen return 1
                When `self._target_number` is less than chosen return -1
                When `self._target_number` is equal to chosen return 0
                """
                return {'distance': np.sign(diff)}
            case "SARSA":
                """
                When `self._target_number` is less than chosen return -2
                When `self._target_number` is greater than chosen return -1
                When `self._target_number` is equal to chosen return 0
                """
                if diff < 0:
                    return {'distance': -2, 'message': f'Chosen number ({self._agent_number}) is too big'}
                elif diff > 0:
                    return {'distance': -1, 'message': f'Chosen number ({self._agent_number}) is too small'}
                else:
                    return {'distance': 0, 'message': f'Correctly guessed number ({self._agent_number})!'}

    # %%
    # Oftentimes, info will also contain some data that is only available
    # inside the ``step`` method (e.g. individual reward terms). In that case,
    # we would have to update the dictionary that is returned by ``_get_info``
    # in ``step``.

    # %%
    # Reset
    # ~~~~~
    #
    # The ``reset`` method will be called to initiate a new episode. You may
    # assume that the ``step`` method will not be called before ``reset`` has
    # been called. Moreover, ``reset`` should be called whenever a done signal
    # has been issued. Users may pass the ``seed`` keyword to ``reset`` to
    # initialize any random number generator that is used by the environment
    # to a deterministic state. It is recommended to use the random number
    # generator ``self.np_random`` that is provided by the environment’s base
    # class, ``gymnasium.Env``. If you only use this RNG, you do not need to
    # worry much about seeding, *but you need to remember to call
    # ``super().reset(seed=seed)``* to make sure that ``gymnasium.Env``
    # correctly seeds the RNG. Once this is done, we can randomly set the
    # state of our environment. In our case, we randomly choose the agent’s
    # location and the random sample target positions, until it does not
    # coincide with the agent’s position.
    #
    # The ``reset`` method should return a tuple of the initial observation
    # and some auxiliary information. We can use the methods ``_get_obs`` and
    # ``_get_info`` that we implemented earlier for that:

    def reset(self, seed=None, options=None):
        # We need the following line to seed self.np_random
        super().reset(seed=seed)

        # Choose the agent's number uniformly at random
        self._agent_number = self.np_random.integers(self.min_number, self.max_number, dtype=int)

        # We will sample the target's number randomly until it does not coincide with the agent's number
        self._target_number = self._agent_number
        while self._target_number == self._agent_number:
            self._target_number = self.np_random.integers(self.min_number, self.max_number, dtype=int)

        observation = self._get_obs()
        info = self._get_info()

        return observation

    # %%
    # Step
    # ~~~~
    #
    # The ``step`` method usually contains most of the logic of your
    # environment. It accepts an ``action``, computes the state of the
    # environment after applying that action and returns the 5-tuple
    # ``(observation, reward, terminated, truncated, info)``. See
    # :meth:`gymnasium.Env.step`. Once the new state of the environment has
    # been computed, we can check whether it is a terminal state and we set
    # ``done`` accordingly. Since we are using sparse binary rewards in
    # ``GridWorldEnv``, computing ``reward`` is trivial once we know
    # ``done``.To gather ``observation`` and ``info``, we can again make
    # use of ``_get_obs`` and ``_get_info``:

    def step(self, action):
        # An episode is done if the agent has reached the target
        self._agent_number = action
        observation = self._get_obs()
        info = self._get_info()

        reward = info["distance"]
        terminated = not info["distance"]

        return observation, reward, terminated, False, info

    # %%
    # Rendering
    # ~~~~~~~~~

    def render(self):
        # if self.render_mode == "rgb_array":
        #     return self._render_frame()

        match self.render_mode:
            case "human":
                print(f"Agent number: {self._agent_number}, Target number: {self._target_number}, Reward: {self._get_info()['distance']}")
                return
