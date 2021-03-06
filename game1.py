# autor: MolokovAlex
# lisence: GPL
# version 0.0.1

# Игра "Поймай шарик"
# Суть игры проста: в случайном месте появляется на короткое время шарик, и мы должны успеть щелкнуть по нему мышкой.



import pygame
from pygame.draw import *       # Это позволит вместо pygame.draw.rect(...) писать просто rect(...).
from random import randint

def new_ball() -> list:
    '''рисует новый шарик 
    вход:
    нет
    выход:
    список с координатами центра и радиуса шарика
    position [x_position, y_position, radius]
    '''
    position = []
    x_position = randint(100, 400)
    y_position = randint(100, 400)
    radius = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x_position, y_position), radius)
    position = x_position, y_position, radius
    return position

def hitClickMouse(mouse_position: list, ballPositionAndRadius: list)-> bool:
    ''' определяет попадание клика мыши в круг 
    вход:
    mouse_position: list    список с координатами клика мыщи
    ballPositionAndRadius: list      список с координатами центра мяча
    выход:
    hit-> bool логический тип - попал True или не попал False
    '''
    hit = False
    mouse_Xposition_click = 0
    mouse_Yposition_click = 0
    ballXPositionAndRadius = 0
    ballYPositionAndRadius = 0
    ballRadius = 0
    mouse_Xposition_click, mouse_Yposition_click = mouse_position
    ballXPositionAndRadius, ballYPositionAndRadius, ballRadius = ballPositionAndRadius
    katetX = abs(mouse_Xposition_click-ballXPositionAndRadius)
    katetY = abs(mouse_Yposition_click-ballYPositionAndRadius)
    length = (katetX**2 + katetY**2)**0.5
    if length < ballRadius:
        hit = True
    # такой if подойдет только для квадратов
    #if (ball_Xposition-ball_radius<mouse_Xposition_click<ball_Xposition+ball_radius) and \
    #                 (ball_Yposition-ball_radius<mouse_Yposition_click<ball_Yposition+ball_radius):
                    
    return hit

def showScore(scoreUser: int)-> None:
    ''' определяет попадание клика мыши в круг 
    вход:
    scoreUser: int    целочисленный, очки, набранные игроком
    выход:
    None
    '''
    font  = pygame.font.Font(None, 20)
    text = font.render("Score: ", True, (180,0,0))
    text2 = font.render(str(score), True, (180,0,0))
    screen.blit(text, [20,20])
    screen.blit(text2, [70,20])


FPS = 1                     # максимальный FPS, быстрее которого программа работать не будет
X_window = 500              # размеры окна игры
Y_window = 500
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
ball_position_and_radius = []
score = 0

# После импорта библиотеки, необходимо её инициализировать:
pygame.init()
# И создать окно:
screen = pygame.display.set_mode((X_window, Y_window))

# после чего, чтобы они отобразились на экране, экран нужно обновить:
pygame.display.update()
# Эту же команду нужно будет повторять, если на экране происходят изменения.

clock = pygame.time.Clock()         # добавление небольшой задержки в главный цикл программы, чтобы не заставлять ее работать 
                                    # "вхолостую", постоянно считывая события, которых, скорее всего, нет. 
                                    # Для этого в pygame есть специальный модуль time. До начала главного цикла создаем объект Clock

# Нужно создать основной цикл, в котором будут отслеживаться
# происходящие события.
finished = False
while not finished:
    clock.tick(FPS)                          # Здесь 30 - это максимальный FPS, быстрее которого программа работать не будет.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:                          #  если нажата кнопка мыши
            if (event.button == 1) and (hitClickMouse(event.pos, ball_position_and_radius)):     #  она левая и произошло попадание в шарик
                score +=1
    ball_position_and_radius = new_ball()
    showScore(score)
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
    