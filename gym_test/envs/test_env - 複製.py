import gym
from gym import error, spaces, utils
from gym.utils import seeding
import pandas as pd
import random


class TestEnv(gym.Env):
    def __init__(self):
        self.f = './dataset/clean.csv'
        self.df_xy = pd.DataFrame(pd.read_csv(self.f))
        self.ACTION_LOOKUP = {0: '1', 1: '2', 2: '3', 3: '4', 4: '5', 5: '6', 6: '7', 7: '8', 8: '9', 9: '10', 10: '11',
        11: '12', 12: '13', 13: '14', 14: '15', 15: '16', 16: '17', 17: '18', 18: '19', 19: '20', 20: '21', 21: '22', 22: '23',
        23: '24', 24: '25', 25: '26', 26: '27', 27: '28', 28: '29', 29: '30', 30: '31', 31: '32', 32: '33', 33: '34', 34: '35',
        35: '36', 36: '37', 37: '38', 38: '39', 39: '40', 40: '41', 41: '42', 42: '43', 43: '44', 44: '45', 45: '46', 46: '47',
        47: '48', 48: '0'}

        self.action_space = spaces.Discrete(len(self.ACTION_LOOKUP))
        self.observation_space = spaces.Discrete(self.df_xy.shape[0])

        self.ob = self._get_random_initial_state()
        self.episode_over = False
        self.turns = 0
        self.sum_rewards = 0.0
        self.action = 0.0
        self.current_state_index = 0
        print("action_space:",self.action_space)
        print("action_space_shape:",self.action_space.shape)
        print("observation_space:",self.observation_space)
        print("observation_space_shape:",self.observation_space)
        print("data_shape",self.df_xy.shape)
        print("ACTION_LOOKUP_len:",len(self.ACTION_LOOKUP))
        
    def step(self, predicted_action_index):
        """
                Parameters
                ----------
                action_index :
                Returns
                -------
                ob, reward, episode_over, info : tuple
                    ob (object) :
                        an environment-specific object representing your observation of
                        the environment.
                    reward (float) :
                        amount of reward achieved by the previous action. The scale
                        varies between environments, but the goal is always to increase
                        your total reward.
                    episode_over (bool) :
                        whether it's time to reset the environment again. Most (but not
                        all) tasks are divided up into well-defined episodes, and done
                        being True indicates the episode has terminated. (For example,
                        perhaps the pole tipped too far, or you lost your last life.)
                    info (dict) :
                         diagnostic information useful for debugging. It can sometimes
                         be useful for learning (for exam   ple, it might contain the raw
                         probabilities behind the environment's last state change).
                         However, official evaluations of your agent are not allowed to
                         use this for learning.
                """

        self.turns += 1
        self.predicted_action = self._take_action(predicted_action_index)
        self.reward = self._get_reward(self.predicted_action)
        self.ob = self._get_next_state()
        #if self.turns > 10 or self.sum_rewards > 2:
        if self.sum_rewards > 5:
            self.episode_over = True

        return self.ob, self.reward, self.episode_over, {}

    def reset(self):
        """
               Reset the environment and supply a new state for initial state
               :return:
               """

        self.turns = 0
        self.ob = self._get_random_initial_state()
        self.episode_over = False
        self.sum_rewards = 0.0
        return self.ob

    def render(self, mode='human', close=False):
        pass

    def _take_action(self, action_index):
        """
                Take an action correpsonding to action_index in the current state
                :param action_index:
                :return:
                """
        #print(len(self.ACTION_LOOKUP))
        self.action = action_index
        #self.action = self.ACTION_LOOKUP[action_index]
        return self.action

    def _get_random_initial_state(self):
        nrand = random.randint(0, self.df_xy.shape[0])
        self.current_state_index = nrand
        return self.df_xy.iloc[nrand]

    def _get_reward(self, predicted_action):
        """
                Get reward for the action taken in the current state
                :return:
                """
        df = self.df_xy
        labelled_action = df.iloc[self.current_state_index]['shop_tag']
        reward = 0.0
        if labelled_action == 1.0:
            if predicted_action == 1.0:
                reward = 1.0
            else:
                reward = -1.0
        elif labelled_action == 2.0:
            if predicted_action == 2.0:
                reward = 2.0
            else:
                reward = -1.0
        elif labelled_action == 3.0:
            if predicted_action == 3.0:
                reward = 1.0
            else:
                reward = -1.0
        elif labelled_action == 4.0:
            if predicted_action == 4.0:
                reward = 1.0
            else:
                reward = -1.0
        elif labelled_action == 5.0:
            if predicted_action == 5.0:
                reward = 1.0
            else:
                reward = -1.0
        elif labelled_action == 6.0:
            if predicted_action == 6.0:
                reward = 2.0
            else:
                reward = -1.0
        elif labelled_action == 7.0:
            if predicted_action == 7.0:
                reward = 1.0
            else:
                reward = -1.0
        elif labelled_action == 8.0:
            if predicted_action == 8.0:
                reward = 1.0
            else:
                reward = -1.0
        elif labelled_action == 9.0:
            if predicted_action == 9.0:
                reward = 1.0
            else:
                reward = -1.0
        elif labelled_action == 10.0:
            if predicted_action == 10.0:
                reward = 2.0
            else:
                reward = -1.0
        elif labelled_action == 11.0:
            if predicted_action == 11.0:
                reward = 1.0
            else:
                reward = -1.0
        elif labelled_action == 12.0:
            if predicted_action == 12.0:
                reward = 2.0
            else:
                reward = -1.0
        elif labelled_action == 13.0:
            if predicted_action == 13.0:
                reward = 2.0
            else:
                reward = -1.0
        elif labelled_action == 14.0:
            if predicted_action == 14.0:
                reward = 1.0
            else:
                reward = -1.0
        elif labelled_action == 15.0:
            if predicted_action == 15.0:
                reward = 2.0
            else:
                reward = -1.0
        elif labelled_action == 16.0:
            if predicted_action == 16.0:
                reward = 1.0
            else:
                reward = -1.0
        elif labelled_action == 17.0:
            if predicted_action == 17.0:
                reward = 1.0
            else:
                reward = -1.0
        elif labelled_action == 18.0:
            if predicted_action == 18.0:
                reward = 2.0
            else:
                reward = -1.0
        elif labelled_action == 19.0:
            if predicted_action == 19.0:
                reward = 2.0
            else:
                reward = -1.0
        elif labelled_action == 20.0:
            if predicted_action == 20.0:
                reward = 1.0
            else:
                reward = -1.0
        elif labelled_action == 21.0:
            if predicted_action == 21.0:
                reward = 2.0
            else:
                reward = -1.0
        elif labelled_action == 22.0:
            if predicted_action == 22.0:
                reward = 2.0
            else:
                reward = -1.0
        elif labelled_action == 23.0:
            if predicted_action == 23.0:
                reward = 1.0
            else:
                reward = -1.0
        elif labelled_action == 24.0:
            if predicted_action == 24.0:
                reward = 1.0
            else:
                reward = -1.0
        elif labelled_action == 25.0:
            if predicted_action == 25.0:
                reward = 2.0
            else:
                reward = -1.0
        elif labelled_action == 26.0:
            if predicted_action == 26.0:
                reward = 2.0
            else:
                reward = -1.0
        elif labelled_action == 27.0:
            if predicted_action == 27.0:
                reward = 1.0
            else:
                reward = -1.0
        elif labelled_action == 28.0:
            if predicted_action == 28.0:
                reward = 1.0
            else:
                reward = -1.0
        elif labelled_action == 29.0:
            if predicted_action == 29.0:
                reward = 1.0
            else:
                reward = -1.0
        elif labelled_action == 30.0:
            if predicted_action == 30.0:
                reward = 1.0
            else:
                reward = -1.0
        elif labelled_action == 31.0:
            if predicted_action == 31.0:
                reward = 1.0
            else:
                reward = -1.0
        elif labelled_action == 32.0:
            if predicted_action == 32.0:
                reward = 1.0
            else:
                reward = -1.0
        elif labelled_action == 33.0:
            if predicted_action == 33.0:
                reward = 1.0
            else:
                reward = -1.0
        elif labelled_action == 34.0:
            if predicted_action == 34.0:
                reward = 1.0
            else:
                reward = -1.0
        elif labelled_action == 35.0:
            if predicted_action == 35.0:
                reward = 1.0
            else:
                reward = -1.0
        elif labelled_action == 36.0:
            if predicted_action == 36.0:
                reward = 2.0
            else:
                reward = -1.0
        elif labelled_action == 37.0:
            if predicted_action == 37.0:
                reward = 2.0
            else:
                reward = -1.0
        elif labelled_action == 38.0:
            if predicted_action == 38.0:
                reward = 1.0
            else:
                reward = -1.0
        elif labelled_action == 39.0:
            if predicted_action == 39.0:
                reward = 2.0
            else:
                reward = -1.0
        elif labelled_action == 40.0:
            if predicted_action == 40.0:
                reward = 1.0
            else:
                reward = -1.0
        elif labelled_action == 41.0:
            if predicted_action == 41.0:
                reward = 1.0
            else:
                reward = -1.0
        elif labelled_action == 42.0:
            if predicted_action == 42.0:
                reward = 1.0
            else:
                reward = -1.0
        elif labelled_action == 43.0:
            if predicted_action == 43.0:
                reward = 1.0
            else:
                reward = -1.0
        elif labelled_action == 44.0:
            if predicted_action == 44.0:
                reward = 1.0
            else:
                reward = -1.0
        elif labelled_action == 45.0:
            if predicted_action == 45.0:
                reward = 1.0
            else:
                reward = -1.0
        elif labelled_action == 46.0:
            if predicted_action == 46.0:
                reward = 1.0
            else:
                reward = -1.0
        elif labelled_action == 47.0:
            if predicted_action == 47.0:
                reward = 1.0
            else:
                reward = -1.0
        elif labelled_action == 48.0:
            if predicted_action == 48.0:
                reward = 2.0
            else:
                reward = -1.0
        elif labelled_action == 0.0:
            if predicted_action == 0.0:
                reward = 1.0
            else:
                reward = -1.0
        
        self.sum_rewards += reward
        return reward

    def _get_next_state(self):
        """
        Get the next state from current state
        :return:
        """
        df = self.df_xy
        new_state_index = self.current_state_index + 1
        if new_state_index == self.df_xy.shape[0]:
            new_state_index = self._get_random_initial_state()
        next_state = df.iloc[new_state_index]
        self.current_state_index = new_state_index
        return next_state

    def _seed(self):
        return
