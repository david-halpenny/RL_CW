from abc import ABC, abstractmethod
from collections import defaultdict
import random
from typing import List, Dict, DefaultDict
from gymnasium.spaces import Space
from gymnasium.spaces.utils import flatdim
import numpy as np


class Agent(ABC):
    """Base class for Q-Learning agent

    **ONLY CHANGE THE BODY OF THE act() FUNCTION**

    """

    def __init__(
        self,
        action_space: Space,
        obs_space: Space,
        gamma: float,
        epsilon: float,
        **kwargs
    ):
        """Constructor of base agent for Q-Learning

        Initializes basic variables of the Q-Learning agent
        namely the epsilon, learning rate and discount rate.

        :param action_space (int): action space of the environment
        :param obs_space (int): observation space of the environment
        :param gamma (float): discount factor (gamma)
        :param epsilon (float): epsilon for epsilon-greedy action selection

        :attr n_acts (int): number of actions
        :attr q_table (DefaultDict): table for Q-values mapping (OBS, ACT) pairs of observations
            and actions to respective Q-values
        """

        self.action_space = action_space
        self.obs_space = obs_space
        self.n_acts = flatdim(action_space)

        self.epsilon: float = epsilon
        self.gamma: float = gamma

        self.q_table: DefaultDict = defaultdict(lambda: 0)

    def act(self, obs: int) -> int:
        """Implement the epsilon-greedy action selection here

        **YOU MUST IMPLEMENT THIS FUNCTION FOR Q2**

        :param obs (int): received observation representing the current environmental state
        :return (int): index of selected action
        """
        ### PUT YOUR CODE HERE ###
        max_q = -float("inf")
        best_action = -1
        ties = []
        # get best action
        for action in range(self.n_acts):
            if self.q_table[(obs, action)] > max_q:
                max_q = self.q_table[(obs, action)]
                best_action = action
                ties = []
            elif self.q_table[(obs, action)] == max_q:
                ties.append(action)
                if best_action != -1: # check current best action isn't default
                    ties.append(best_action)
        if len(ties) > 0:
            best_action = random.choice(ties) # choose randomly if there is a tie
        # assign probabilities and randomly choose action to take
        probabilities = np.zeros(self.n_acts)
        for action in range(self.n_acts):
            if action == best_action:
                probabilities[action] = 1 - self.epsilon + (self.epsilon / self.n_acts)
            else:
                probabilities[action] = self.epsilon / self.n_acts

        action = np.random.choice(self.n_acts, p=probabilities)
        
        # raise NotImplementedError("Needed for Q2")
        ### RETURN AN ACTION HERE ###
        return action

    @abstractmethod
    def schedule_hyperparameters(self, timestep: int, max_timestep: int):
        """Updates the hyperparameters

        This function is called before every episode and allows you to schedule your
        hyperparameters.

        :param timestep (int): current timestep at the beginning of the episode
        :param max_timestep (int): maximum timesteps that the training loop will run for
        """
        ...

    @abstractmethod
    def learn(self):
        ...


class QLearningAgent(Agent):
    """Agent using the Q-Learning algorithm"""

    def __init__(self, alpha: float, **kwargs):
        """Constructor of QLearningAgent

        Initializes some variables of the Q-Learning agent, namely the epsilon, discount rate
        and learning rate alpha.

        :param alpha (float): learning rate alpha for Q-learning updates
        """

        super().__init__(**kwargs)
        self.alpha: float = alpha

    def learn(
        self, obs: int, action: int, reward: float, n_obs: int, done: bool
    ) -> float:
        """Updates the Q-table based on agent experience

        **YOU MUST IMPLEMENT THIS FUNCTION FOR Q2**

        :param obs (int): received observation representing the current environmental state
        :param action (int): index of applied action
        :param reward (float): received reward
        :param n_obs (int): received observation representing the next environmental state
        :param done (bool): flag indicating whether a terminal state has been reached
        :return (float): updated Q-value for current observation-action pair
        """
        ### PUT YOUR CODE HERE ###
        if done:
            q = self.q_table[(obs, action)] + self.alpha * (reward - self.q_table[(obs, action)]) # the value of q(n_obs, a) is 0 for all a
        else:
            q = self.q_table[(obs, action)] + self.alpha * (reward + self.gamma * max([self.q_table[(n_obs, a)] for a in range(self.n_acts)]) - self.q_table[(obs, action)])
        self.q_table[(obs, action)] = q
        # raise NotImplementedError("Needed for Q2")
        return self.q_table[(obs, action)]

    def schedule_hyperparameters(self, timestep: int, max_timestep: int):
        """Updates the hyperparameters

        **DO NOT CHANGE THE PROVIDED SCHEDULING WHEN TESTING PROVIDED HYPERPARAMETER PROFILES IN Q2**

        This function is called before every episode and allows you to schedule your
        hyperparameters.

        :param timestep (int): current timestep at the beginning of the episode
        :param max_timestep (int): maximum timesteps that the training loop will run for
        """
        self.epsilon = 1.0 - (min(1.0, timestep / (0.20 * max_timestep))) * 0.99


class MonteCarloAgent(Agent):
    """Agent using the Monte-Carlo algorithm for training"""

    def __init__(self, **kwargs):
        """Constructor of MonteCarloAgent

        Initializes some variables of the Monte-Carlo agent, namely epsilon,
        discount rate and an empty observation-action pair dictionary.

        :attr sa_counts (Dict[(Obs, Act), int]): dictionary to count occurrences observation-action pairs
        """
        super().__init__(**kwargs)
        self.sa_counts = {}

    def learn(
        self, obses: List[int], actions: List[int], rewards: List[float]
    ) -> Dict:
        """Updates the Q-table based on agent experience

        **YOU MUST IMPLEMENT THIS FUNCTION FOR Q2**

        :param obses (List(int)): list of received observations representing environmental states
            of trajectory (in the order they were encountered)
        :param actions (List[int]): list of indices of applied actions in trajectory (in the
            order they were applied)
        :param rewards (List[float]): list of received rewards during trajectory (in the order
            they were received)
        :return (Dict): A dictionary containing the updated Q-value of all the updated state-action pairs
            indexed by the state action pair.
        """
        updated_values = {}
        ### PUT YOUR CODE HERE ###
        G = 0
        for i in range(len(obses) - 1, -1, -1):
            G = self.gamma * G + rewards[i]
            if (obses[i], actions[i]) not in self.sa_counts:
                self.sa_counts[(obses[i], actions[i])] = 0
            self.sa_counts[(obses[i], actions[i])] += 1
            self.q_table[(obses[i], actions[i])] += (1 / self.sa_counts[(obses[i], actions[i])]) * (G - self.q_table[(obses[i], actions[i])]) # incremental average formula
            updated_values[(obses[i], actions[i])] = self.q_table[(obses[i], actions[i])]

        # raise NotImplementedError("Needed for Q2")
        return updated_values

    def schedule_hyperparameters(self, timestep: int, max_timestep: int):
        """Updates the hyperparameters

        **DO NOT CHANGE THE PROVIDED SCHEDULING WHEN TESTING PROVIDED HYPERPARAMETER PROFILES IN Q2**

        This function is called before every episode and allows you to schedule your
        hyperparameters.

        :param timestep (int): current timestep at the beginning of the episode
        :param max_timestep (int): maximum timesteps that the training loop will run for
        """
        self.epsilon = 1.0 - (min(1.0, timestep / (0.9 * max_timestep))) * 0.8
