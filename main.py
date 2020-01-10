#coding:utf-8
#五颗豆，两条蛇，AI蛇是random
import sys
import pygame
import random
import time
from pygame.locals import *
from food import *
from snake import *
from config import *
from util import *
from state import *
from game import *

if __name__ == '__main__':
    my = Game()
    my.play()