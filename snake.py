from config import *
import random
import pygame
from pygame.locals import *

class Snake():
    def __init__(self, screen):
        self.length=4
        self.head=[random.randint(4,COLNUM-4)*LEN,random.randint(4,ROWNUM-4)*LEN]
        self.body=[
                    [self.head[0]-1*LEN, self.head[1]],
                    [self.head[0]-2*LEN, self.head[1]],
                    [self.head[0]-3*LEN, self.head[1]],
                  ]
        self.score = 0
        self.screen = screen
    
    def insert_head_and_del_last(self, new_head):
        del self.body[-1]
        self.body.insert(0,self.head)
        self.head = new_head
    
    def insert_head(self,new_head):
        self.body.insert(0, self.head)
        self.head = new_head
    
    def insert_tail(self,new_tail):
        self.body.append(new_tail)

    def draw_snake(self, type):
        pygame.draw.rect(self.screen,HEAD_COLOR[type - 1],(self.head[0],self.head[1],LEN,LEN))
        for grid in self.body:
            pygame.draw.rect(self.screen,SNAKE_COLOR[type - 1],(grid[0],grid[1],LEN,LEN))

    def eat_food(self):
        # move towards the left
        if self.body[-1][0] < self.body[-2][0]:
            new_tail = [self.body[-1][0]+LEN, self.body[-1][1]]
            # new_head = [self.head[0]-LEN,self.head[1]]
            self.insert_tail(new_tail)
            # self.insert_head(new_head)
            self.length=self.length+1
            self.score=self.score+100

        # move towards the right
        elif self.body[-1][0] > self.body[-2][0]:
            new_tail = [self.body[-1][0]-LEN, self.body[-1][1]]
            self.insert_tail(new_tail)
            # new_head = [self.head[0]+LEN,self.head[1]]
            # self.insert_head(new_head)
            self.length=self.length+1
            self.score=self.score+100

        # move upward
        elif self.body[-1][1] < self.body[-2][1]:
            new_tail = [self.body[-1][0], self.body[-1][1]-LEN]
            self.insert_tail(new_tail)
            # new_head = [self.head[0],self.head[1]-LEN]
            # self.insert_head(new_head)
            self.length=self.length+1
            self.score=self.score+100

        # move downward
        elif self.body[-1][1] > self.body[-2][1]:
            new_tail = [self.body[-1][0], self.body[-1][1]+LEN]
            self.insert_tail(new_tail)
            # new_head = [self.head[0],self.head[1]+LEN]
            # self.insert_head_and_del_last(new_head)
            self.length=self.length+1
            self.score=self.score+100
    
    def move(self):
        # move towards the left
        if self.head[0] < self.body[0][0]:
            new_head = [self.head[0]-LEN,self.head[1]]
            self.insert_head_and_del_last(new_head)

        # move towards the right
        elif self.head[0] > self.body[0][0]:
            new_head = [self.head[0]+LEN,self.head[1]]
            self.insert_head_and_del_last(new_head)

        # move upward
        elif self.head[1] < self.body[0][1]:
            new_head = [self.head[0],self.head[1]-LEN]
            self.insert_head_and_del_last(new_head)

        # move downward
        elif self.head[1] > self.body[0][1]:
            new_head = [self.head[0],self.head[1]+LEN]
            self.insert_head_and_del_last(new_head)

    def dead(self):
        self.score=self.score-1000


class Snake_Action():
    def __init__(self, snake):
        self.snake = snake

    def insert_head_and_del_last(self, new_head):
        del self.snake.body[-1]
        self.snake.body.insert(0,self.snake.head)
        self.snake.head = new_head

    def insert_head(self,new_head):
        self.snake.body.insert(0,self.snake.head)
        self.snake.head = new_head

    def keyboard_action(self,event): # keyboard
        # turn left or turn right
        if self.snake.head[0] == self.snake.body[0][0]:
            if event.key == K_LEFT:
                new_head = [self.snake.head[0]-LEN,self.snake.head[1]]
                self.insert_head_and_del_last(new_head)
            elif event.key == K_RIGHT:
                new_head = [self.snake.head[0]+LEN,self.snake.head[1]]
                self.insert_head_and_del_last(new_head)

        #turn up or turn down
        if self.snake.head[1] == self.snake.body[0][1]:
            if event.key == K_UP:
                new_head = [self.snake.head[0],self.snake.head[1]-LEN]
                self.insert_head_and_del_last(new_head)
            elif event.key == K_DOWN:
                new_head = [self.snake.head[0],self.snake.head[1]+LEN]
                self.insert_head_and_del_last(new_head)

    def AI_action(self, action): # AI
        if self.snake.head[0] == self.snake.body[0][0]:
            if action == K_LEFT:
                new_head = [self.snake.head[0]-LEN,self.snake.head[1]]
                self.insert_head_and_del_last(new_head)
            elif action == K_RIGHT:
                new_head = [self.snake.head[0]+LEN,self.snake.head[1]]
                self.insert_head_and_del_last(new_head)
            else:
                self.snake.move()

        #turn up or turn down
        
        elif self.snake.head[1] == self.snake.body[0][1]:
            if action == K_UP:
                new_head = [self.snake.head[0],self.snake.head[1]-LEN]
                self.insert_head_and_del_last(new_head)
            elif action == K_DOWN:
                new_head = [self.snake.head[0],self.snake.head[1]+LEN]
                self.insert_head_and_del_last(new_head)
            else:
                self.snake.move()

    