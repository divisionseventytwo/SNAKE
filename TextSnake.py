import time
import os
import random as rnd
import numpy as np
input('Нажмите Enter')
snake = np.zeros((16, 16))
commands = []
apple = []
SnakeLength = 0
GameOver = 0
a = 0
maxsnakelength = 3
snake[1][1] = 3
snake[1][2] = 2
snake[1][3] = 1


def random():
    f = int(rnd.randint(0, 15))
    return f


def printscreen():

    for x in range(16):
        print('                            ', end=' ')
        for y in range(16):

            if x == apple[0] and y == apple[1]:
                print('Ѽ', end='   ')
            elif snake[x][y] == max:
                print('☻', end='   ')
            elif snake[x][y]:
                print('◙', end='   ')
            else:
                print(' ', end='   ')
        print('\n')


while maxsnakelength:

    if a == 0:
        apple = [random(), random()]
        a = 1
    printscreen()
    while a:
        max = 0
        for x in range(16):
            for y in range(16):
                if snake[x][y] > max:
                    i = x
                    j = y
                    max = snake[x][y]
        if i == apple[0] and j == apple[1]:
            maxsnakelength += 1
            a = 0
        if i > apple[0]:
            for x in range(16):
                for y in range(16):
                    if snake[x][y]:
                        snake[x][y] -= 1
            if snake[i - 1][j] == 0 and i - 1 >= 0:
                snake[i - 1][j] = maxsnakelength
            elif snake[i][j - 1] == 0 and j - 1 >= 0:
                snake[i][j - 1] = maxsnakelength
            elif snake[i][j + 1] == 0 and j + 1 <= 16:
                snake[i][j + 1] = maxsnakelength
            elif snake[i + 1][j] == 0 and i + 1 <= 16:
                snake[i + 1][j] = maxsnakelength
            else:
                GameOver = 1
                break
        elif j > apple[1]:
            for x in range(16):
                for y in range(16):
                    if snake[x][y]:
                        snake[x][y] -= 1
            if snake[i][j - 1] == 0 and j - 1 >= 0:
                snake[i][j - 1] = maxsnakelength
            elif snake[i - 1][j] == 0 and i - 1 >= 0:
                snake[i - 1][j] = maxsnakelength
            elif snake[i + 1][j] == 0 and i + 1 <= 16:
                snake[i + 1][j] = maxsnakelength
            elif snake[i][j + 1] == 0 and j + 1 <= 16:
                snake[i][j + 1] = maxsnakelength
            else:
                GameOver = 1
                break
        elif i < apple[0]:
            for x in range(16):
                for y in range(16):
                    if snake[x][y]:
                        snake[x][y] -= 1
            if snake[i + 1][j] == 0 and i + 1 <= 16:
                snake[i + 1][j] = maxsnakelength
            elif snake[i][j - 1] == 0 and j - 1 >= 0:
                snake[i][j - 1] = maxsnakelength
            elif snake[i][j + 1] == 0 and j + 1 <= 16:
                snake[i][j + 1] = maxsnakelength
            elif snake[i - 1][j] == 0 and i - 1 >= 0:
                snake[i - 1][j] = maxsnakelength
            else:
                GameOver = 1
                break
        elif j < apple[1]:
            for x in range(16):
                for y in range(16):
                    if snake[x][y]:
                        snake[x][y] -= 1
            if snake[i][j + 1] == 0 and j + 1 <= 16:
                snake[i][j + 1] = maxsnakelength
            elif snake[i - 1][j] == 0 and i - 1 >= 0:
                snake[i - 1][j] = maxsnakelength
            elif snake[i + 1][j] == 0 and i + 1 <= 16:
                snake[i + 1][j] = maxsnakelength
            elif snake[i][j - 1] == 0 and j - 1 >= 0:
                snake[i][j - 1] = maxsnakelength
            else:
                GameOver = 1
                break
        SnakeLength = 0
        for x in range(16):
            for y in range(16):
                if snake[x][y]:
                    SnakeLength += 1
        if SnakeLength > maxsnakelength:
            for x in range(16):
                for y in range(16):
                    if snake[x][y]:
                        snake[x][y] -= 1
        time.sleep(0.1)
        os.system('CLS')
        printscreen()
    if GameOver:
        break
    os.system('CLS')
print('Игра окончена')
input()
