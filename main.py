import time
import pygame
import sys
import random
import time
from pygame import mixer
size = 40
Back_Ground = (0, 220, 0)
width = 750
height = 450


class Apple:
    def __init__(self, parent_screen):
        self.image = pygame.image.load("resources/apple.jpg")
        self.parent_screen = parent_screen
        self.x = size*3
        self.y = size*3

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()
    # logic for apple random position

    def move(self):
        self.x = random.randint(0, 17)*size
        self.y = random.randint(0, 9)*size


class Snake:
    def __init__(self, parent_screen, length):
        # adding block in pygame
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load('resources/block.jpg').convert()
        self.x = [size]*length
        self.y = [size]*length
        self.direction = "up"
    # logic of increasing length of snake

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def draw(self):
        # drawing a block function
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
            pygame.display.flip()
    # logic of snake movement in game

    def move_up(self):
        self.direction = "up"

    def move_down(self):
        self.direction = "down"

    def move_left(self):
        self.direction = "left"

    def move_right(self):
        self.direction = "right"
    # this is a logic of snake walking automatically

    def walk(self):
        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]
        if self.direction == "up":
            self.y[0] -= size
        if self.direction == "down":
            self.y[0] += size
        if self.direction == "left":
            self.x[0] -= size
        if self.direction == "right":
            self.x[0] += size

        self.draw()


class Game:
    def __init__(self):
        # python initialization
        pygame.init()
        self.background_music()
        # creating  screen for pygame
        self.surface = pygame.display.set_mode((width, height))
        # initialization mixer
        pygame.mixer.init()
        # filling surface
        # rgb is red green and blue
        self.surface.fill((0, 220, 0))
        # adding backgroung img
        self.background_img()
        # adding snake in Game
        self.snake = Snake(self.surface, 1)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()
    # logic of snake colliding with apple

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2+size:
            if y1 >= y2 and y1 < y2+size:
                return True
        return False

    def background_music(self):
        pygame.mixer.music.load("resources/bg_music_1.mp3")
        pygame.mixer.music.play()

    def background_img(self):
        bg = pygame.image.load("resources/background.jpg")
        self.surface.blit(bg, (0, 0))

    def play_sound(self, sound):
        ding = pygame.mixer.Sound(f"resources/{sound}.mp3")
        pygame.mixer.Sound.play(ding)

    def play(self):
        self.background_img()
        self.snake.walk()
        self.apple.draw()
        self.show_score()
        # self.Level_up()
        pygame.display.update()  # update is for updating the score ok
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.play_sound("ding")
            self.snake.increase_length()
            self.apple.move()

        # snake colliding with itself gameover logic
        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.play_sound("crash")
                raise "Game Over"

        # snake boundaries error problem
        if (self.snake.x[0] < 0 or self.snake.x[0] > width) or (self.snake.y[0] < 0 or self.snake.y[0] > height):
            raise "hit the boundry error"

    def reset_game(self):
        self.snake = Snake(self.surface, 1)
        self.apple = Apple(self.surface)

    def show_score(self):
        font = pygame.font.SysFont('arial', 32)

        score = font.render(
            f"Score:{self.snake.length-1}", True, (255, 255, 255))
        self.surface.blit(score, (630, 5))  # means image draw karwaraha hu !

    def show_game_over(self):
        self.background_img()
        font = pygame.font.SysFont('arial', 32)
        line1 = font.render(
            f"Game Over and Your Score is :{self.snake.length-1}", True, (255, 255, 255))

        self.surface.blit(line1, (150, 180))  # means image draw karwaraha hu !
        line2 = font.render(
            f"To Play again Press Enter and Exit press Close", True, (255, 255, 255))

        self.surface.blit(line2, (120, 210))  # means image draw karwaraha hu !
        pygame.mixer.music.pause()

        pygame.display.flip()

    def run(self):
        # creating a game loop
        running = True
        pause = False
        while running:
            # creating a event for loop
            for event in pygame.event.get():
                # checking event type and key in it
                if event.type == pygame.KEYDOWN:
                    # if pause==True:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.unpause()  # unpause in built in method chalu karta hai
                        pause = False
                    if event.key == pygame.K_UP:
                        self.snake.move_up()
                    if event.key == pygame.K_DOWN:
                        self.snake.move_down()
                    if event.key == pygame.K_LEFT:
                        self.snake.move_left()
                    if event.key == pygame.K_RIGHT:
                        self.snake.move_right()
                elif event.type == pygame.QUIT:
                    running = False

            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset_game()

            if self.snake.length-1 <= 10:
                time.sleep(0.3)
            elif self.snake.length-1 > 15 and self.snake.length-1 < 25:
                time.sleep(0.2)
            elif self.snake.length-1 > 30:
                time.sleep(0.1)


if __name__ == "__main__":  # it is simple help us to create a module
    # game object
    game = Game()  # Game class
    game.run()  # game is running for object self
