from config import *
from util import *
from food import *
from snake import *
import numpy as np


class Q_learning:
    
    def __init__(self):
        self.Q = {}
        # self.snake1 = snake1
        # self.snake2 = snake2
        # self.state = state


    def get_reward(self, food, snake2):
        i = snake2.head[0]
        j = snake2.head[1]
        food_reward = 0
        ret_value = 0
        # food.pos[0]
        
        for i in food.pos:
            ret_value += 1/(abs(i[0] - snake2.head[0]) + abs(i[1] - snake2.head[1] + 1))
            break
        return ret_value - 2
        
        # wall_reward = -10/(min(i, j, COLNUM*LEN - i, ROWNUM*LEN - j) + 1)
        # food_reward = 10000/

        return wall_reward

    def next_action(self, state):
        self.prevstate = state
        # print(state)
        # print(self.Q.keys())
        # print("st")
        # for i in self.Q:
            # print(i, self.Q[i])
        # print('end')
        # print(type(state))
        if(state not in self.Q.keys()):
            # print("miss!")
            self.Q[state] = np.array([0, 0, 0, 0])
            random_action = np.random.rand(4)  ##only one state
            self.action = np.argmax(random_action)
            return self.action
        # else:
            # print("hit!")
        self.action = np.argmax(self.Q[state])

        return self.action 

    def update(self, reward, state):
        if(state not in self.Q.keys()):
            self.Q[self.prevstate][self.action] = LF * (reward)
            return
            # print('not in')
            # self.Q[state] = np.array([0, 0, 0, 0])
        # print('privious,', self.prevstate)
        self.Q[self.prevstate][self.action] = LF * (reward + DF * np.max(self.Q[state]))