#coding:utf-8
#五颗豆，两条蛇，AI蛇是random
import sys
import pygame
import random
import time
from pygame.locals import *

auto_flag = True # false if 键盘输入, true if AI

ROWNUM = 30
COLNUM = 50
LEN = 20
BLOCK_SIZE = 10
CELLNUM = ROWNUM * COLNUM
SCREEN_SIZE = (COLNUM*LEN+BLOCK_SIZE*LEN,ROWNUM*LEN)
BG_COLOR = (0,0,0)
FONT_COLOR = (255,255,255)
HEAD_COLOR1 = (188,50,88)
HEAD_COLOR2 = (254,249,55)
SNAKE_COLOR1 = (100,50,80) # red & 键盘输入
SNAKE_COLOR2 = (237,230,142) # yellow & AI
FOOD_COLOR = (55,100,155)
# OVER_COLOR = (55,88,211)
OVER_COLOR = (255,0,0)

FOOD_NUM = 5

class Food():
    def __init__(self):
        self.pos = []
        for i in range(FOOD_NUM):
            self.pos.append([])
            self.pos[i]=[random.randint(0, COLNUM-1)*LEN,random.randint(0, ROWNUM-1)*LEN]
        # self.pos=[0,110]
    def draw_food(self):
        for i in range(FOOD_NUM):
            pygame.draw.rect(screen,FOOD_COLOR,(self.pos[i][0],self.pos[i][1],LEN,LEN))

    def be_eatten(self, index):
        self.pos[index]=[random.randint(0, COLNUM-1)*LEN,random.randint(0, ROWNUM-1)*LEN]

class Snake():
    def __init__(self):
        self.length=4
        self.head=[random.randint(4,COLNUM-4)*LEN,random.randint(4,ROWNUM-4)*LEN]
        self.body=[
                    [self.head[0]-1*LEN,self.head[1]],
                    [self.head[0]-2*LEN,self.head[1]],
                    [self.head[0]-3*LEN,self.head[1]],
                  ]
        self.score = 0

    def draw_snake(self, type):
        if type == 1:
            pygame.draw.rect(screen,HEAD_COLOR1,(self.head[0],self.head[1],LEN,LEN))
        if type == 2:
            pygame.draw.rect(screen,HEAD_COLOR2,(self.head[0],self.head[1],LEN,LEN))
        for grid in self.body:
            if type == 1:
                pygame.draw.rect(screen,SNAKE_COLOR1,(grid[0],grid[1],LEN,LEN))
            if type == 2:
                pygame.draw.rect(screen,SNAKE_COLOR2,(grid[0],grid[1],LEN,LEN))

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
            self.score=self.score+100

        # move towards the right
        elif self.head[0] > self.body[0][0]:
            new_head = [self.head[0]+LEN,self.head[1]]
            self.insert_head(new_head)
            self.length=self.length+1
            self.score=self.score+100

        # move upward
        elif self.head[1] < self.body[0][1]:
            new_head = [self.head[0],self.head[1]-LEN]
            self.insert_head(new_head)
            self.length=self.length+1
            self.score=self.score+100

        # move downward
        elif self.head[1] > self.body[0][1]:
            new_head = [self.head[0],self.head[1]+LEN]
            self.insert_head_and_del_last(new_head)
            self.length=self.length+1
            self.score=self.score+100

    def dead(self):
        self.score=self.score-1000


def draw_screen():
    screen.fill(BG_COLOR, (0, 0, COLNUM*LEN+BLOCK_SIZE*LEN, ROWNUM*LEN))
    # pygame.draw.line(screen, FONT_COLOR, (0,(ROWNUM)*LEN), (COLNUM*LEN,(ROWNUM)*LEN))
    pygame.draw.line(screen, FONT_COLOR, ((COLNUM)*LEN,0), ((COLNUM)*LEN,ROWNUM*LEN))

def draw_scores(font,scores,flag):
    text = font.render(" Score" + str(flag) + ": " + str(scores), True, FONT_COLOR)
    screen.blit(text,((COLNUM*LEN),20*flag))

def draw_all(food, snake1, snake2, font, scores1, scores2):
    draw_screen()
    snake1.draw_snake(1)
    snake2.draw_snake(2)
    food.draw_food()
    draw_scores(font,scores1,1)
    draw_scores(font,scores2,2)

def main():
    pygame.init()
    global screen
    screen = pygame.display.set_mode(SCREEN_SIZE,0,32)
    pygame.event.set_blocked(None)
    pygame.event.set_allowed((KEYDOWN,QUIT))
    pygame.display.set_caption('Retro Snaker')
    font = pygame.font.SysFont("arial",28)
    clock = pygame.time.Clock()
    snake1 = Snake()
    snake2 = Snake()
    food = Food()
    text = font.render("Scores1: " + str(snake1.score),True,FONT_COLOR)
    text = font.render("Scores2: " + str(snake2.score),True,FONT_COLOR)
    text2=font.render('Game over!', True, OVER_COLOR)
    textobj=text2.get_rect()
    textobj.center = (COLNUM*LEN/2, ROWNUM*LEN/2)
    screen.blit(text,((COLNUM*LEN),0))
    draw_all(food,snake1, snake2, font,snake1.score,snake2.score)
    exit_flag = False
    while True:
        if exit_flag:
            continue
        # if auto_flag == False:
        for event in pygame.event.get():
            if event.type==KEYDOWN:
                snake1.turn(event)
                draw_all(food,snake1, snake2, font,snake1.score,snake2.score)
                pygame.display.flip()
                if snake1.head in food.pos:
                    food.be_eatten(food.pos.index(snake1.head))
                    snake1.eat_food()
        # else:
        actions = [K_LEFT, K_RIGHT, K_DOWN, K_UP]
        pygame.event.get()
        action = random.sample(actions,1)[0]
        snake2.auto_turn(action)
        draw_all(food,snake1, snake2, font,snake1.score,snake2.score)
        pygame.display.flip()
        if snake2.head in food.pos:
            food.be_eatten(food.pos.index(snake2.head))
            snake2.eat_food()

        for snake in [snake1, snake2]:
            snake.move()

            if snake.head in food.pos:
                food.be_eatten(food.pos.index(snake.head))
                snake.eat_food()


            if snake.head[0] < 0 or snake.head[0] >= COLNUM*LEN or snake.head[1] < 0 or snake.head[1] >= ROWNUM*LEN:
                snake.dead()
                screen.blit(text2,textobj)
                draw_all(food,snake1, snake2, font,snake1.score,snake2.score)
                pygame.display.flip()
                pygame.display.update()
                pygame.quit()
                exit_flag = True
                time.sleep(1)
                sys.exit()

            for b in snake.body:
                if b == snake.head:
                    snake.dead()
                    screen.blit(text2,textobj)
                    draw_all(food,snake1, snake2, font,snake1.score,snake2.score)
                    pygame.display.flip()
                    pygame.display.update()
                    pygame.quit()
                    exit_flag = True
                    time.sleep(1)
                    sys.exit()
        for b in snake1.body:
            if b == snake2.head:
                snake2.dead()
                screen.blit(text2,textobj)
                draw_all(food,snake1, snake2, font,snake1.score,snake2.score)
                pygame.display.flip()
                pygame.display.update()
                pygame.quit()
                exit_flag = True
                time.sleep(1)
                sys.exit()

        for b in snake2.body:
            if b == snake1.head:
                snake1.dead()
                screen.blit(text2,textobj)
                draw_all(food,snake1, snake2, font,snake1.score,snake2.score)
                pygame.display.flip()
                pygame.display.update()
                pygame.quit()
                exit_flag = True
                time.sleep(1)
                sys.exit()
        if snake1.head == snake2.head:
            snake1.dead()
            snake2.dead()
            screen.blit(text2,textobj)
            draw_all(food,snake1, snake2, font,snake1.score,snake2.score)
            pygame.display.flip()
            pygame.display.update()
            pygame.quit()
            exit_flag = True
            time.sleep(1)
            sys.exit()

        draw_all(food,snake1, snake2, font,snake1.score,snake2.score)
        pygame.display.flip()
        snake1.score+=1
        snake2.score+=1
        clock.tick(8) #speed

if __name__ == '__main__':
    main()