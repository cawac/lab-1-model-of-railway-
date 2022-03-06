import time
from time import *


class Station:
    def __init__(self, name, posx, posy, capacity=5, size=25, ):
        self.__posx = posx
        self.__posy = posy
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
        b = Station('b', 140, 140)
        c = Station('c', 40, 140)
        d = Station('d', 140, 40)
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
        sleep(3)

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
        sleep(1)

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
        sleep(1)
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
