#coding:utf-8
#一条蛇，qlearning
import sys
import pygame
import random
import time
from pygame.locals import *
import numpy as np

auto_flag = True # false if 键盘输入, true if AI

ROWNUM = 30
COLNUM = 50
LEN = 20 #block
CELLNUM = ROWNUM * COLNUM
SCREEN_SIZE = (COLNUM*LEN+5*LEN,ROWNUM*LEN)
BG_COLOR = (0,0,0)
FONT_COLOR = (255,255,255)
HEAD_COLOR = (188,50,88)
SNAKE_COLOR = (100,50,80)
FOOD_COLOR = (55,100,155)
# OVER_COLOR = (55,88,211)
OVER_COLOR = (255,0,0)

class Food():
    def __init__(self):
        self.pos=[random.randint(0, COLNUM-1)*LEN,random.randint(0, ROWNUM-1)*LEN]
        # self.pos=[0,110]
    def draw_food(self):
        pygame.draw.rect(screen,FOOD_COLOR,(self.pos[0],self.pos[1],LEN,LEN))

    def be_eatten(self):
        self.pos=[random.randint(0, COLNUM-1)*LEN,random.randint(0, ROWNUM-1)*LEN]

class Snake():
    def __init__(self):
        self.length=4
        self.head=[random.randint(4,COLNUM-4)*LEN,random.randint(4,ROWNUM-4)*LEN]
        self.body=[
                    [self.head[0]-1*LEN,self.head[1]],
                    [self.head[0]-2*LEN,self.head[1]],
                    [self.head[0]-3*LEN,self.head[1]],
                  ]

    def draw_snake(self):
        pygame.draw.rect(screen,HEAD_COLOR,(self.head[0],self.head[1],LEN,LEN))
        for grid in self.body:
            pygame.draw.rect(screen,SNAKE_COLOR,(grid[0],grid[1],LEN,LEN))

    def insert_head_and_del_last(self,new_head):
        del self.body[-1]
        self.body.insert(0,self.head)
        self.head = new_head

    def insert_head(self,new_head):
        self.body.insert(0,self.head)
        self.head = new_head

    def turn(self,event):
        # turn left or turn right
        if self.head[0] == self.body[0][0]:
            if event.key == K_LEFT:
                new_head = [self.head[0]-LEN,self.head[1]]
                self.insert_head_and_del_last(new_head)
            if event.key == K_RIGHT:
                new_head = [self.head[0]+LEN,self.head[1]]
                self.insert_head_and_del_last(new_head)

        #turn up or turn down
        if self.head[1] == self.body[0][1]:
            if event.key == K_UP:
                new_head = [self.head[0],self.head[1]-LEN]
                self.insert_head_and_del_last(new_head)
            if event.key == K_DOWN:
                new_head = [self.head[0],self.head[1]+LEN]
                self.insert_head_and_del_last(new_head)

    def auto_turn(self, action):
        if self.head[0] == self.body[0][0]:
            if action == K_LEFT:
                new_head = [self.head[0]-LEN,self.head[1]]
                self.insert_head_and_del_last(new_head)
            if action == K_RIGHT:
                new_head = [self.head[0]+LEN,self.head[1]]
                self.insert_head_and_del_last(new_head)

        #turn up or turn down
        if self.head[1] == self.body[0][1]:
            if action == K_UP:
                new_head = [self.head[0],self.head[1]-LEN]
                self.insert_head_and_del_last(new_head)
            if action == K_DOWN:
                new_head = [self.head[0],self.head[1]+LEN]
                self.insert_head_and_del_last(new_head)

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

    def eat_food(self):
        # move towards the left
        if self.head[0] < self.body[0][0]:
            new_head = [self.head[0]-LEN,self.head[1]]
            self.insert_head(new_head)
            self.length=self.length+1

        # move towards the right
        elif self.head[0] > self.body[0][0]:
            new_head = [self.head[0]+LEN,self.head[1]]
            self.insert_head(new_head)
            self.length=self.length+1

        # move upward
        elif self.head[1] < self.body[0][1]:
            new_head = [self.head[0],self.head[1]-LEN]
            self.insert_head(new_head)
            self.length=self.length+1

        # move downward
        elif self.head[1] > self.body[0][1]:
            new_head = [self.head[0],self.head[1]+LEN]
            self.insert_head_and_del_last(new_head)
            self.length=self.length+1




class Qlearning:
    def __init__():

        self.Q = {}
        self.discount = 0.6
        self.alpha = 0.2


    def predict(self, state):
        if (state not in self.Q.keys()):
            self.Q[state] = np.random.rand(4)
        self.prevState = state
        self.action = np.argmax(self.Q[state])
        # print(state, self.Q[state])
        return np.argmax(self.Q[state])

    def update(self, reward, state):
        if (state not in self.Q.keys()):
            self.Q[state] = np.random.rand(4)
        # self.Q[self.prevState][self.action] += self.LF * (reward + self.discount * np.max(self.Q[state]) - self.Q[self.prevState][self.action])
        # self.Q[self.prevState][self.action] += self.LF * reward
        next_q = reward + self.discount * np.max(self.Q[state])
        self.Q[self.prevState][self.action] = (1 - self.alpha) * self.Q[self.prevState][self.action] + self.alpha *  next_q

    # def join(self, mdl):
    #     res = Model()
    #     for key in mdl.Q.keys():
    #         if (key in self.Q.keys()):
    #             res.Q[key] = (self.Q[key] + mdl.Q[key]) / 2
    #         else:
    #             res.Q[key] = mdl.Q[key]
    #     return res  
class Game:
    def __init__():
        self.snake = Snake()
        self.food = Food()
        self.exit_flag = False
        

    def draw_screen():
        screen.fill(BG_COLOR, (0, 0, COLNUM*LEN+5*LEN, ROWNUM*LEN))
        # pygame.draw.line(screen, FONT_COLOR, (0,(ROWNUM)*LEN), (COLNUM*LEN,(ROWNUM)*LEN))
        pygame.draw.line(screen, FONT_COLOR, ((COLNUM)*LEN,0), ((COLNUM)*LEN,ROWNUM*LEN))

    def draw_scores(font,scores):
        text = font.render(" Scores: " + str(scores),True,FONT_COLOR)
        screen.blit(text,((COLNUM*LEN),0))

    def draw_all(food,snake,font,scores):
        draw_screen()
        snake.draw_snake()
        food.draw_food()
        draw_scores(font,scores)    

    def getState(self):
        return (self.food.pos, self.snake.head, self.snake.body)

    def check_turn(self):
        

       

def main():
    pygame.init()
    global screen
    screen = pygame.display.set_mode(SCREEN_SIZE,0,32)
    pygame.event.set_blocked(None)
    pygame.event.set_allowed((KEYDOWN,QUIT))
    pygame.display.set_caption('Retro Snaker')
    font = pygame.font.SysFont("arial",28)
    clock = pygame.time.Clock()
    text = font.render("Scores: " + str(snake.length-4),True,FONT_COLOR)
    text2=font.render('Game over!', True, OVER_COLOR)
    textobj=text2.get_rect()
    textobj.center = (COLNUM*LEN/2, ROWNUM*LEN/2)
    screen.blit(text,((COLNUM*LEN),0))
    draw_all(food,snake,font,snake.length-4)
    game = Game()
    model = Qlearning()  
    
    while True:

        if exit_flag:
            continue
        if auto_flag == False:
            for event in pygame.event.get():
                if event.type==KEYDOWN:
                    game.snake.turn(event)
                    draw_all(game.food,game.snake,font,game.snake.length-4)
                    pygame.display.flip()
                    if game.snake.head[0] == game.food.pos[0] and game.snake.head[1] == game.food.pos[1]:
                        game.food.be_eatten()
                        game.snake.eat_food()
        else:
            action = model.predict(game.getState())
            # actions = [K_LEFT, K_RIGHT, K_DOWN, K_UP]
            pygame.event.get()
            # action = random.sample(actions,1)[0]
            game.snake.auto_turn(action)
            draw_all(game.food,game.snake,font,game.snake.length-4)
            pygame.display.flip()
            if game.snake.head[0] == game.food.pos[0] and game.snake.head[1] == game.food.pos[1]:
                game.food.be_eatten()
                game.snake.eat_food()


        game.snake.move()

        if game.snake.head[0] == game.food.pos[0] and game.snake.head[1] == game.food.pos[1]:
            game.food.be_eatten()
            game.snake.eat_food()

        if game.snake.head[0] < 0 or game.snake.head[0] >= COLNUM*LEN or game.snake.head[1] < 0 or game.snake.head[1] >= ROWNUM*LEN:
            screen.blit(text2,textobj)
            pygame.display.flip()
            pygame.quit()
            exit_flag = True
            time.sleep(1)
            sys.exit()

        for b in game.snake.body:
            if b == game.snake.head:
                screen.blit(text2,textobj)
                pygame.display.update()
                pygame.quit()
                exit_flag = True
                time.sleep(1)
                sys.exit()

        draw_all(game.food,game.snake,font,game.snake.length-4)
        pygame.display.flip()
        clock.tick(8) #speed

if __name__ == '__main__':
    main()