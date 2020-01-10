import pygame
from pygame.locals import *
from config import *
import random

# total = 

def cul_dis(x1, y1, x2, y2):
    return (x1-x2)**2 + (y1-y2)**2

def mainGreedy(world_state, food, snake2):
    actions = {K_LEFT, K_RIGHT, K_DOWN, K_UP}

    snake_head = snake2.head
    snake_body = snake2.body
    headx = snake_head[0]/LEN
    heady = snake_head[1]/LEN
    food_pos = food.pos
    distance = 999999
    action = None

    unvalid = ['enemy_head', 'my_body', 'enemy_body', 'wall']
    
    if world_state.state[(max(0,headx-1),heady)] in unvalid:
        actions.discard(K_LEFT)
    if world_state.state[(min(headx+1,COLNUM-1),heady)] in unvalid:
        actions.discard(K_RIGHT)
    if world_state.state[(headx,min(heady+1,ROWNUM-1))] in unvalid:
        actions.discard(K_DOWN)
    if world_state.state[(headx,max(0,heady-1))] in unvalid:
        actions.discard(K_UP)
                

    for i in actions:
        if i == K_LEFT:
            for x2,y2 in food_pos:
                temp = cul_dis(headx-1,heady,x2/LEN,y2/LEN)
                if(temp < distance):
                    distance = temp
                    action = K_LEFT
        elif i == K_RIGHT:
            for x2,y2 in food_pos:
                temp = cul_dis(headx+1,heady,x2/LEN,y2/LEN)
                if(temp < distance):
                    distance = temp
                    action = K_RIGHT
        elif i == K_DOWN:
            for x2,y2 in food_pos:
                temp = cul_dis(headx,heady+1,x2/LEN,y2/LEN)
                if(temp < distance):
                    distance = temp
                    action = K_DOWN
        elif i == K_UP:
            for x2,y2 in food_pos:
                temp = cul_dis(headx,heady-1,x2/LEN,y2/LEN)
                if(temp < distance):
                    distance = temp
                    action = K_UP

        if snake2.head[0] == snake2.body[0][0]:
            if snake2.head[1] < snake2.body[0][1]:
                if action == K_DOWN:
                    temp_actions = actions.copy()
                    temp_actions.discard(K_DOWN)
                    temp_actions.discard(K_UP)
                    if temp_actions:
                        action = random.sample(temp_actions,1)[0]
            else:
                if action == K_UP:
                    temp_actions = actions.copy()
                    temp_actions.discard(K_DOWN)
                    temp_actions.discard(K_UP)
                    if temp_actions:
                        action = random.sample(temp_actions,1)[0]

        if snake2.head[1] == snake2.body[0][1]:
            if snake2.head[0] < snake2.body[0][0]:
                if action == K_RIGHT:
                    temp_actions = actions.copy()
                    temp_actions.discard(K_RIGHT)
                    temp_actions.discard(K_LEFT)
                    if temp_actions:
                        action = random.sample(temp_actions,1)[0]
            else:
                if action == K_LEFT:
                    temp_actions = actions.copy()
                    temp_actions.discard(K_RIGHT)
                    temp_actions.discard(K_LEFT)
                    if temp_actions:
                        action = random.sample(temp_actions,1)[0]



    return action