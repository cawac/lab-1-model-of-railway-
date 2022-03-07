import random
import time
import pygame


class Station:
    def __init__(self, name, posx, posy, size=25, ):
        self.__posx = posx
        self.__posy = posy
        self.__capacity = random.randint(1,7)
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

    @property
    def posx(self):
        return self.__posx

    @posx.setter
    def posx(self, new_posx):
        self.__posx = new_posx

    @property
    def posy(self):
        return self.__posy

    @posy.setter
    def posy(self, new_posy):
        self.__posy = new_posy


class Game_map:
    def __init__(self):
        a = Station('a', 40, 40)
        b = Station('b', 240, 240)
        c = Station('c', 240, 40)
        d = Station('d', 40, 240)
        e = Station('e', 360, 120)
        f = Station('f', 360, 360)
        self.__stations = [a, b, c, d, e, f]
        self.__graph = {self.__stations[0]: [self.__stations[1], self.__stations[2]],
                        self.__stations[1]: [self.__stations[0], self.__stations[3], self.__stations[4]],
                        self.__stations[2]: [self.__stations[0], self.__stations[5]],
                        self.__stations[3]: [self.__stations[1]],
                        self.__stations[4]: [self.__stations[1], self.__stations[5]],
                        self.__stations[5]: [self.__stations[2], self.__stations[4]]}

    def spawn(self):
        self.__stations[random.randint(0, 5)].capacity += 5

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

    def check_overloading(self):
        for statione in self.__stations:
            if statione.capacity >= statione.size:
                return False
            else:
                return True


class Train:
    def __init__(self, game_map, size=25, capacity=0):
        self.__game_map = game_map
        self.__curr_station = game_map.stations[0]
        self.__size = size
        self.__capacity = capacity

    def go_to_station(self, win):
        # buffer = win
        for statione in self.__game_map.graph[self.__curr_station]:
            print(statione.name, end=' ')
        key = int(input())
        self.__curr_station = self.__game_map.graph[self.__curr_station][key]
        first_time1 = time.time()
        # while time.time() - first_time1 <= 2:
        #     buffer
        time.sleep(2)

    def loading(self):
        print('на станции сейчас столько грузов:', self.__curr_station.capacity)
        print('в поезде сейчас столько груза:', self.capacity)
        kolvo = int(input('введите сколько товара забрать со станции: '))
        while kolvo < 0 or self.__curr_station.capacity - kolvo < 0:
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
        time.sleep(kolvo)

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
        time.sleep(kolvo)
        # self.__curr_station.capacity(self.__curr_station.capacity + kolvo)

    @property
    def curr_station(self):
        return self.__curr_station

    @property
    def capacity(self):
        return self.__capacity


# def menu(x, train):
#     first_time = time.time()
#     if ((time.time() - first_time) > 20):
#         x.spawn()
#         first_time = time.time()
#     print(f'Поезд на [' + train.curr_station.name + '] станции')
#     print('Что сделать?')
#     key = input('(1) Следующая станция\n(2) Загрузить поезд\n(3) Разгрузить поезд\n')
#     if key == '1':
#         train.go_to_station()
#         print('едем...')
#         time.sleep(2)
#     elif key == '2':
#         train.loading()
#         print('загружаю...')
#         time.sleep(3)
#     elif key == '3':
#         train.unloading()
#         print('разгружаю...')
#         time.sleep(3)
#     if x.check_overloading()
#         print('ПОТРАЧЕНО')


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('train model')
    win = pygame.display.set_mode((500, 500))
    x = Game_map()
    train = Train(x)
    first_time = time.time()
    # train.go_to_station()
    # print(train.curr_station.name)
    # train.loading()
    # print(train.curr_station.capacity)
    # print(train.capacity)
    # train.unloading()
    # print(train.curr_station.capacity)
    # print(train.capacity)
    run = True
    while x.check_overloading():
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for start in x.graph:
            for end in x.graph[start]:
                pygame.draw.aaline(win, (255, 255, 255),
                                   [start.posx, start.posy],
                                   [end.posx, end.posy])
        for station in x.stations:
            j = 0
            pygame.draw.circle(win, (140, 200, 10),
                               (station.posx, station.posy), 20)
            capacity = station.capacity
            for i in range(capacity):
                if i % 5 == 0:
                    j += 1
                pygame.draw.rect(win, (200, 200, 200),
                                 (station.posx + 21 + i % 5 * 7, station.posy - 30 + j * 7, 5, 5))
        pygame.display.update()

        if ((time.time() - first_time) > 20):
            x.spawn()
            first_time = time.time()
        print(f'Поезд на [' + train.curr_station.name + '] станции')
        print('Что сделать?')
        key = input('(1) Следующая станция\n(2) Загрузить поезд\n(3) Разгрузить поезд\n')
        if key == '1':
            print('едем...')
            train.go_to_station(win)
        elif key == '2':
            print('загружаю...')
            train.loading()
        elif key == '3':
            print('разгружаю...')
            train.unloading()
        if x.check_overloading():
            print('ПОТРАЧЕНО')
        win.fill((0, 0, 0))
    pygame.quit()