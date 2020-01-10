from config import *
import random
import pygame


class Food():
    def __init__(self, screen, snake1, snake2):
        self.pos = []
        for i in range(FOOD_NUM):
            self.pos.append([])
            while True:
                temp = [random.randint(0, COLNUM-1)*LEN,random.randint(0, ROWNUM-1)*LEN]
                if temp not in snake1.body:
                    if temp not in snake2.body:
                        if temp != snake1.head:
                            if temp != snake2.head:
                                break
            self.pos[i] = temp
        self.screen = screen
        
    def draw_food(self):
        for i in range(FOOD_NUM):
            pygame.draw.rect(self.screen,FOOD_COLOR,(self.pos[i][0],self.pos[i][1],LEN,LEN))

    def be_eatten(self, index, snake1, snake2):
        while True:
            self.pos[index] = [random.randint(0, COLNUM-1)*LEN,random.randint(0, ROWNUM-1)*LEN]
            if self.pos[index] not in snake1.body:
                if self.pos[index] not in snake2.body:
                    if self.pos[index] != snake1.head:
                        if self.pos[index] != snake2.head:
                            break
