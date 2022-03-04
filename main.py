# Snake Tutorial Using Pygame
import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox


class cube(object):
    rows = 20
    w = 500

    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface, eyes=False):
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(surface, self.color, (i * dis + 1, j * dis + 1, dis - 2, dis - 2))
        if eyes:
            centre = dis // 2
            radius = 3
            circleMiddle = (i * dis + centre - radius, j * dis + 8)
            circleMiddle2 = (i * dis + dis - radius * 2, j * dis + 8)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle, radius)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle2, radius)

        # This class is defined for snake design and its movement


class snake(object):
    body = []
    turns = {}

    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()
            # It will manage the keys movement for the snake
            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                    # Snake when hit the boundary wall
        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body) - 1:
                    self.turns.pop(p)
            else:
                if c.dirnx == -1 and c.pos[0] == c.rows - 1:
                    c.pos = (0, c.pos[1])
                elif c.dirny == 1 and c.pos[1] >= c.rows - 1:
                    c.pos = (c.pos[0], 0)
                elif c.dirny == -1 and c.pos[1] == 0:
                    continue
                else:
                    break
        return (x, y)


# Using Tkinter function to display message
def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass

    # main() function


def main():
    global width, rows, s, snack
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    s = snake((255, 0, 0), (10, 10))
    snack = cube(randomSnack(rows, s), color=(0, 255, 0))
    flag = True

    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        s.move()
        if s.body[0].pos == snack.pos:
            s.addCube()
            snack = cube(randomSnack(rows, s), color=(0, 255, 0))

        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z: z.pos, s.body[x + 1:])):
                print('Score: \n', len(s.body))
                message_box('You Lost!\n', 'Play again...\n')
                s.reset((10, 10))
                break

        redrawWindow(win)

    pass


class Station:
    def __init__(self, name, capacity=5, size=25):
        self.__capacity = capacity
        self.__size = size
        self.__name = name

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, x):
        self.__size = x

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, x):
        self.__capacity = x

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, x):
        self.__name = x


class Game_map:
    def __init__(self):
        a = Station('a')
        b = Station('b')
        c = Station('c')
        d = Station('d')
        self.__stations = [a, b, c, d]
        self.__graph = {self.__stations[0]: [self.__stations[1], self.__stations[2]],
                        self.__stations[1]: [self.__stations[2], self.__stations[3]]}

    def spawn(self):
        pass

    @property
    def graph(self):
        return self.__graph

    @property
    def stations(self):
        return self.__stations

    @graph.setter
    def graph(self, x):
        self.__graph = x

    @stations.setter
    def stations(self, x):
        self.__stations = x


class Train:
    def __init__(self, game_map, size=25, capacity=0):
        self.__game_map = game_map
        self.__curr_station = game_map.stations[0]
        self.__size = size
        self.__capacity = capacity

    def go_to_station(self):
        for station in self.__game_map.graph[self.__curr_station]:
            print(station.name, end=' ')
        key = int(input())
        self.__curr_station = self.__game_map.graph[self.__curr_station][key]

    def loading(self):
        print('на станции сейчас столько грузов:', self.__curr_station.capacity)
        print('в поезде сейчас столько груза:', self.capacity)
        kolvo = int(input('введите сколько товара забрать со станции: '))
        while kolvo < 0 or self.__curr_station.scapacity - kolvo < 0:
            print('на станции сейчас столько грузов:', self.__curr_station.capacity)
            print('в поезде сейчас столько груза:', self.capacity)
            kolvo = int(input('введите сколько товара забрать со станции: '))
        if self.__capacity + kolvo <= self.__size:
            self.__capacity += kolvo
            self.__curr_station.capacity -= kolvo
        else:
            buf = self.__size - self.__capacity
            self.__capacity = self.__size
            self.__curr_station.capacity += -buf + kolvo

    def unloading(self):
        print('на станции сейчас столько грузов:', self.__curr_station.capacity)
        print('в поезде сейчас столько груза:', self.capacity)
        kolvo = int(input('введите сколько товара выгрузить на станцию: '))
        while kolvo < 0 or self.__capacity - kolvo < 0:
            print('на станции сейчас столько грузов:', self.__curr_station.capacity)
            print('в поезде сейчас столько груза:', self.capacity)
            kolvo = int(input('введите сколько товара выгрузить на станцию: '))
        self.__capacity -= kolvo
        self.__curr_station.capacity += kolvo
        # self.__curr_station.capacity(self.__curr_station.capacity + kolvo)

    @property
    def curr_station(self):
        return self.__curr_station

    @property
    def capacity(self):
        return self.__capacity


if __name__ == '__main__':
    x = Game_map()
    train = Train(x)
    train.go_to_station()
    print(train.curr_station.name)
    train.loading()
    print(train.curr_station.capacity)
    print(train.capacity)
    train.unloading()
    print(train.curr_station.capacity)
    print(train.capacity)
