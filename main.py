class Station:
    def __init__(self, name, scapacity = 5, size = 25):
        self.scapacity = scapacity
        self.__size = size
        self.__name = name

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, x):
        self.__size = x

    # @property
    # def scapacity(self):
    #     return self.__scapacity
    #
    # @scapacity.setter
    # def scapacity(self, x):
    #     self.__scapacity = x

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
    def __init__(self, game_map, size = 25, capacity = 0):
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
        print(self.__curr_station.scapacity)
        kolvo = int(input('kolvo tovara'))
        self.__capacity += kolvo
        self.__curr_station.scapacity = 4
        # buf = self.__curr_station.scapacity - kolvo
        # self.__curr_station.scapacity(buf)

    def unloading(self):
        print(self.__capacity)
        kolvo = int(input('kolvo tovara vigryz'))
        self.__capacity -= kolvo
        # self.__curr_station.capacity(self.__curr_station.capacity + kolvo)

    @property
    def curr_station(self):
        return self.__curr_station


if __name__ == '__main__':
    x = Game_map()
    print(x.stations[2].scapacity)
    train = Train(x)
    train.go_to_station()
    print(train.curr_station.name)
    train.loading()
    print(train.curr_station.scapacity)
    train.unloading()

    print(train.curr_station.capacity)