import sys
import pygame
import random
import time
from pygame.locals import * 
from config import *

def draw_screen():
    screen.fill(BG_COLOR, (0, 0, COLNUM*LEN+BLOCK_SIZE*LEN, ROWNUM*LEN))
    pygame.draw.line(screen, FONT_COLOR, ((COLNUM)*LEN,0), ((COLNUM)*LEN,ROWNUM*LEN))

def draw_scores(font,scores,flag):
    text = font.render(" Score" + str(flag) + ": " + str(scores), True, FONT_COLOR)
    screen.blit(text,((COLNUM*LEN),20 * flag))

def draw_all(food, snake1, snake2, scores1, scores2):
    draw_screen()
    snake1.draw_snake(1)
    snake2.draw_snake(2)
    food.draw_food()
    # draw_scores(font,scores1,1)
    # draw_scores(font,scores2,2)
