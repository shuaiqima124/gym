"""
Task is to copy content from the input tape to
the output tape. http://arxiv.org/abs/1511.07275
"""
import numpy as np
from gym.envs.algorithmic import algorithmic_env
from gym.envs.algorithmic.algorithmic_env import ha

class CopyEnv(algorithmic_env.AlgorithmicEnv):
    def __init__(self, base=5):
        algorithmic_env.AlgorithmicEnv.__init__(self,
                                                inp_dim=1,
                                                base=base,
                                                chars=True)
    def set_data(self):
        self.content = {}
        self.target = {}
        for i in range(self.total_len):
            val = self.random.randrange(self.base)
            self.content[ha(np.array([i]))] = val
            self.target[i] = val
        self.total_reward = self.total_len
