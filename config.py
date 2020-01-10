import pygame


ROWNUM = 15
COLNUM = 15
epochs = 1

LF = 0.8 #learning rate
DF = 0.6 #discount rate

LEN = 50
BLOCK_SIZE = 4
CELLNUM = ROWNUM * COLNUM
SCREEN_SIZE = (COLNUM * LEN + BLOCK_SIZE * LEN, ROWNUM * LEN)
FOOD_NUM = 5


BG_COLOR = (0,0,0)
FONT_COLOR = (255,255,255)
HEAD_COLOR = [(188,50,88), (254,249,55)]
SNAKE_COLOR = [(100,50,80), (237,230,142)]
FOOD_COLOR = (55,100,155)
OVER_COLOR = (255,0,0)

screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
auto_flag = True # false if 键盘输入, true if AI
