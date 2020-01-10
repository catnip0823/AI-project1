from config import *
from util import *
from food import *
from snake import *
import numpy as np


class MDP:
    def __init__(self, snake1, snake2, food):
        self.mdp_learning_state = {}
        for i in range(COLNUM):
            for j in range(ROWNUM):
                for k in range(4):
                    self.mdp_learning_state[((i, j), k)] = 0
        for i in range(-1, COLNUM+1):
            for k in range(4):
                self.mdp_learning_state[((-1, i), k)] = -99999999
                self.mdp_learning_state[((ROWNUM, i), k)] = -99999999
        for i in range(-1, ROWNUM+1):
            for k in range(4):
                self.mdp_learning_state[((i, -1), k)] = -99999999
                self.mdp_learning_state[((i, COLNUM), k)] = -99999999
                


    def get_reward(self, state, action, food, snake1, snake2):
        next_state = self.get_next_state(state, action)
        next_state = [LEN*next_state[0], LEN*next_state[1]]
        if next_state in food.pos:
            return 10000
        if next_state[0] < 0 or next_state[1] < 0 or next_state[0] > LEN*COLNUM-LEN or next_state[1] > LEN*ROWNUM-LEN:
            return -100000
        if next_state in snake1.body:
            return -100000
        if next_state in snake2.body:
            return -100000
        if next_state in snake1.head:
            return -50000
        
        return 0
    
    def judge_exit(self, state, action, food):
        next_state = state
        next_state = [LEN*next_state[0], LEN*next_state[1]]
        if next_state in food.pos:
            return -1
        if next_state[0] == -LEN or next_state[1] == -LEN or next_state[0] == LEN*COLNUM or next_state[1] == LEN*ROWNUM:
            return -1
        return 0

    def iteration(self, food, snake1, snake2):
        for k in range(20):
            previos_state = self.mdp_learning_state
            for state, action in self.mdp_learning_state.keys():
                reward = self.get_reward(state, action, food, snake1, snake2)
                # print(reward,'reward')
                next_state = self.get_next_state(state, action)
                if (next_state[0] >= -1 and next_state[1] >= -1 and next_state[0] <= COLNUM and next_state[1] <= ROWNUM):
                    max_q_next = self.get_max_q(next_state, previos_state)
                    self.mdp_learning_state[(state, action)] = reward + DF * max_q_next
        # print('hhhh',self.mdp_learning_state[((0, 14), 2)])
        


    def get_next_state(self, state, action):
        if action == 0: # up
            state = (state[0], state[1] - 1)
        if action == 1: # down
            state = (state[0], state[1] + 1)
        if action == 2: # left
            state = (state[0] - 1, state[1])
        if action == 3: # right
            state = (state[0] + 1, state[1])
        return state
    
    def get_max_q(self, state, previos_state):
        ret_value = None
        for i in range(4):
            if ret_value == None:
                ret_value = previos_state[(state, i)]
            else:
                ret_value = max(ret_value, previos_state[(state, i)])
        return ret_value
    
    def get_policy(self, start_state, food, last_action):
        start_state = (start_state[0]//LEN, start_state[1]//LEN)
        policy_list = []
        for _ in range(100):
            policy = None
            max_value = -999999999999
            for i in range(4):
                if policy_list != []:
                    if policy_list[-1] == 0 and i == 1:
                        continue
                    if policy_list[-1] == 1 and i == 0:
                        continue
                    if policy_list[-1] == 2 and i == 3:
                        continue
                    if policy_list[-1] == 3 and i == 2:
                        continue
                elif last_action != None:
                    if last_action == 0 and i == 1:
                        continue
                    if last_action == 1 and i == 0:
                        continue
                    if last_action == 2 and i == 3:
                        continue
                    if last_action == 3 and i == 2:
                        continue
                if max_value < self.mdp_learning_state[(tuple(start_state), i)]:
                    max_value = self.mdp_learning_state[(tuple(start_state), i)]
                    policy = i
            return policy
            policy_list.append(policy)
 
            if self.judge_exit(tuple(start_state), policy, food) != 0:
                break
            
            start_state = self.get_next_state(tuple(start_state), policy)
            print('start state', start_state)
            

        return policy_list



