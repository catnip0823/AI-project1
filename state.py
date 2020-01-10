from config import *

class State():
    def __init__(self, snake1, snake2, food):
        # (0, 0), (0, 1) not (9, 9)
        self.state = {}
        self.q_learning_state = []

        for i in range(-1,COLNUM+1):
            for j in range(-1,ROWNUM+1):
                if [LEN*i, LEN*j] == snake1.head:
                    self.state[(i, j)] = 'my_head'
                    self.q_learning_state.append(((i, j), 'my_head'))
                elif [LEN*i, LEN*j] == snake2.head:
                    self.state[(i, j)] = 'enemy_head'
                    self.q_learning_state.append(((i, j), 'enemy_head'))
                elif [LEN*i, LEN*j] in snake1.body:
                    self.state[(i, j)] = 'my_body'
                    self.q_learning_state.append(((i, j), 'my_body'))
                elif [LEN*i, LEN*j] in snake2.body:
                    self.state[(i, j)] = 'enemy_body'
                    self.q_learning_state.append(((i, j), 'enemy_body'))
                elif [LEN*i, LEN*j] in food.pos:
                    self.state[(i, j)] = 'food'
                    self.q_learning_state.append(((i, j), 'food'))
                elif i == -1:
                    self.state[(i, j)] = 'wall'
                    self.q_learning_state.append(((i, j), 'wall'))
                elif i == COLNUM:
                    self.state[(i, j)] = 'wall'
                    self.q_learning_state.append(((i, j), 'wall'))
                elif j == -1:
                    self.state[(i, j)] = 'wall'
                    self.q_learning_state.append(((i, j), 'wall'))
                elif j == ROWNUM:
                    self.state[(i, j)] = 'wall'
                    self.q_learning_state.append(((i, j), 'wall'))
                else:
                    self.state[(i, j)] = 'None'
        self.q_learning_state = tuple(self.q_learning_state)

    def get_state(self, food, snake1, snake2):
        for i in range(5):
            x = food.pos[i-1]
        y_1 = snake1.head
        z_1 = snake1.body
        if y_1[0] == z_1[0][0]:
            if y_1[1] > z_1[0][1]:
                direction_1 = 3
            if y_1[1] < z_1[0][1]:
                direction_1 = 1
        if y_1[1] == z_1[0][1]:
            if y_1[0] > z_1[0][0]:
                direction_1 = 0
            if y_1[0] < z_1[0][0]:
                direction_1 = 2            
        y_2 = snake2.head
        z_2 = snake2.body
        if y_2[0] == z_2[0][0]:
            if y_2[1] > z_2[0][1]:
                direction_2 = 3
            if y_2[1] < z_2[0][1]:
                direction_2 = 1
        if y_2[1] == z_2[0][1]:
            if y_2[0] > z_2[0][0]:
                direction_2 = 0
            if y_2[0] < z_2[0][0]:
                direction_2 = 2
        size = LEN
        return (x[0] <= y_2[0], x[1] >= y_2[1], x[0] == y_2[0], x[1] == y_2[1], direction_1, direction_2, [x[0] - size, x[1]] in z_2, [x[0] + size, x[1]] in z_2, [x[0], x[1] - size] in z_2, [x[0], x[1] + size] in z_2)

        # print(self.state)
        # print(len(self.state))