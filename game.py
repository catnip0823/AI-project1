from config import *
from util import *
from food import *
from snake import *
from state import *
from MDP import *
from q_learning import *
from greedy import *
import numpy as np
# import time
translate = [K_RIGHT, K_DOWN, K_LEFT, K_UP]
translate_MDP = [K_UP, K_DOWN, K_LEFT, K_RIGHT]
all_time1 = []
all_time2 = []

class Game:
    def __init__(self):
        self.exit_flag = False
        self.screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
        pygame.init()
        self.font = pygame.font.SysFont("arial", 28)
        self.clock = pygame.time.Clock()
        self.list_action = None
        self.last_action = None

    def render(self,snake1, snake2,food, font, score1, score2):
        self.screen.fill(BG_COLOR, (0, 0, COLNUM*LEN+BLOCK_SIZE*LEN, ROWNUM*LEN))
        pygame.draw.line(screen, FONT_COLOR, ((COLNUM)*LEN,0), ((COLNUM)*LEN,ROWNUM*LEN))
        snake1.draw_snake(1)
        snake2.draw_snake(2)
        food.draw_food()
        text1 = font.render(" Score1: " + str(score1), True, FONT_COLOR)
        text2 = font.render(" Score2: " + str(score2), True, FONT_COLOR)
        screen.blit(text1,((COLNUM*LEN),20 * 1))
        screen.blit(text2,((COLNUM*LEN),20 * 2))
        pygame.display.update()


    def play(self):
        # one epoch  
        q_learn = Q_learning()
        
        for epoch in range(epochs):
            snake1 = Snake(self.screen) # keyboard
            snake2 = Snake(self.screen) # MDP
            snake1_action = Snake_Action(snake1)
            snake2_action = Snake_Action(snake2)
            food = Food(screen, snake1, snake2)
            
            
            while not self.exit_flag:
                # start_2 = time.time()
                mdp_state = MDP(snake1, snake2, food)
                mdp_state.iteration(food, snake1, snake2)
                self.last_action = self.list_action
                self.list_action = mdp_state.get_policy(snake2.head, food, self.last_action)
                # end_2 = time.time()
                # all_time2.append(end_2 - start_2)

                if (auto_flag == False):
                    # start keyboard
                    for event in pygame.event.get():
                        if event.type == KEYDOWN:
                            snake1_action.keyboard_action(event)
                    # end keyboard
                else:
                    feature_state = State(snake1, snake2, food)
                    pygame.event.get()
                    # start_1 = time.time()
                    action = mainGreedy(feature_state, food, snake1)
                    end_1 = time.time()
                    # all_time1.append(end_1 - start_1)
                    # snake1_action.AI_action(action)


                snake2_action.AI_action(translate_MDP[self.list_action])
                
                self.check_exit(snake1, snake2, food)
                self.render(snake1, snake2, food, self.font, snake1.score, snake2.score)
                self.clock.tick(5000)
            self.exit_flag = False
            print("game over!")
            # print('greedy', sum(all_time1)/len(all_time1))
            # print('MDP',sum(all_time2)/len(all_time2))
            print('greedy:', snake1.score)
            print('MDP:', snake2.score)
                    

    def check_exit(self, snake1, snake2, food):
        for snake in [snake1, snake2]:
            if snake.head in food.pos:
                food.be_eatten(food.pos.index(snake.head), snake1, snake2)
                snake.eat_food()

            if snake.head[0] < 0 or snake.head[0] >= COLNUM * LEN or snake.head[1] < 0 or snake.head[1] >= ROWNUM * LEN:
                snake.dead()
                self.exit_flag = True
            
            for b in snake.body:
                if b == snake.head:
                    snake.dead()
                    self.exit_flag = True

        for b in snake1.body:
            if b == snake2.head:
                snake2.dead()
                self.exit_flag = True

        for b in snake2.body:
            if b == snake1.head:
                snake1.dead()
                self.exit_flag = True

        if snake1.head == snake2.head:
            snake1.dead()
            snake2.dead()
            self.exit_flag = True

