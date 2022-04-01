import random
import time
import pygame
import typing

width: int = 860
height: int = 600
bg = pygame.image.load("back.jpg")


class Station:
    def __init__(self, name: str, posx: int, posy: int, size: int, capacity: int):
        self.__name = name
        self.__posx = posx
        self.__posy = posy
        self.__size = size
        self.__capacity = capacity

    @property
    def size(self) -> int:
        return self.__size

    @property
    def capacity(self) -> int:
        return self.__capacity

    @capacity.setter
    def capacity(self, value: int) -> None:
        self.__capacity = value

    @property
    def name(self) -> str:
        return self.__name

    @property
    def posx(self) -> int:
        return self.__posx

    @posx.setter
    def posx(self, new_posx: int) -> None:
        self.__posx = new_posx

    @property
    def posy(self) -> int:
        return self.__posy

    @posy.setter
    def posy(self, new_posy: int) -> None:
        self.__posy = new_posy


def is_touch(x1: int, y1: int, x2: int, y2: int) -> bool:
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 < 60


def is_clicked(x1: int, y1: int, x2: int, y2: int) -> bool:
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 < 20


class Game_map:
    def __init__(self):
        self.__stations = [Station('a', 100, 100, 25, random.randint(2, 8))]
        for i in range(1, random.randint(11, 14)):
            generate(self)
        self.__graph = {}
        for station_start in self.__stations:
            self.__graph[station_start] = []
        for station_start in self.__stations:
            for j in range(random.randint(1, len(self.__stations) // 2)):
                new_station = random.choice(self.__stations)
                if new_station not in self.__graph[station_start]:
                    self.__graph[station_start].append(new_station)
                    self.__graph[new_station].append(station_start)

    def spawn(self) -> None:
        random.choice(self.__stations).capacity += 5

    @property
    def graph(self) -> dict:
        return self.__graph

    @property
    def stations(self) -> typing.List[Station]:
        return self.__stations

    def is_overload(self) -> bool:
        for statione in self.__stations:
            if statione.capacity >= statione.size:
                return True
        else:
            return False


def generate(mapa: Game_map) -> None:
    x = random.randint(30, width - 50)
    y = random.randint(30, height - 30)
    for i in mapa.stations:
        if is_touch(i.posx, i.posy, x, y):
            generate(mapa)
            return
    mapa.stations.append(Station(chr(97 + len(mapa.stations)), x, y, 25, random.randint(2, 8)))


class Train:
    def __init__(self, game_map: Game_map) -> None:
        self.__game_map = game_map
        self.__curr_station = game_map.stations[0]
        self.__posx = float(self.__curr_station.posx)
        self.__posy = float(self.__curr_station.posy)

    def go_to_station(self, x: int, y: int) -> None:
        for key in self.__game_map.graph[self.__curr_station]:
            if is_clicked(x, y, key.posx, key.posy):
                start = self.__curr_station
                self.__curr_station = key
                end = key
                # self.__cosa = abs(start.posx - end.posx) / (
                # (start.posx - end.posx) ** 2 + (start.posy - end.posy) ** 2) ** 0.5
                first_time = time.time()
                while time.time() - first_time <= 3:
                    pygame.time.delay(50)
                    self.__posx += (end.posx - start.posx) / 45
                    self.__posy += (end.posy - start.posy) / 45
                    draw_window(self, self.__game_map)
                self.__posx = self.__curr_station.posx
                self.__posy = self.__curr_station.posy

    def loading(self, x: int, y: int) -> None:
        if is_clicked(x, y, self.__curr_station.posx, self.__curr_station.posy):
            self.__curr_station.capacity -= 1
            draw_window(self, self.__game_map)

    @property
    def curr_station(self) -> Station:
        return self.__curr_station

    @property
    def curr_station(self) -> Station:
        return self.__curr_station

    @property
    def posx(self) -> float:
        return self.__posx

    @property	
    def posy(self) -> float:
        return self.__posy

    

def draw_window(the_Thomas: Train, railway: Game_map) -> None:  # draw display
    win.blit(bg, (0, 0))
    for start in railway.graph:  # drawing railways
        for end in railway.graph[start]:
            pygame.draw.aaline(win, (255, 202, 0),
                               [start.posx, start.posy],
                               [end.posx, end.posy])
    for station in railway.stations:  # drawing stations
        j = 0
        pygame.draw.circle(win, (255, 159, 0),
                           (station.posx, station.posy), 20)
        f1 = pygame.font.Font(None, 24)
        text1 = f1.render(station.name, True,
                          (15, 79, 168))
        win.blit(text1, (station.posx - 10, station.posy - 10))
        for i in range(station.capacity):  # drawing goods
            if i % 5 == 0:
                j += 1
            pygame.draw.rect(win, (225, 0, 93),
                             (station.posx + 21 + i % 5 * 7, station.posy - 30 + j * 7, 5, 5))
    pygame.draw.rect(win, (133, 122, 238), (the_Thomas.posx, the_Thomas.posy, 10, 10))
    pygame.display.update()  # update display


if __name__ == '__main__':
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption('train model')
    win = pygame.display.set_mode((width, height))
    railway_map = Game_map()
    train = Train(railway_map)
    first_time = time.time()
    while not railway_map.is_overload():
        pygame.time.delay(50)
        draw_window(train, railway_map)
        if (time.time() - first_time) > 1:
            railway_map.spawn()
            first_time = time.time()
        key = 0
        ev = pygame.event.get()
        for event in ev:
            # handle MOUSEBUTTONUP
            if railway_map.is_overload():
                break
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                key = event.button
                if key == 1:
                    train.loading(x, y)
                elif key == 3:
                    train.go_to_station(x, y)
    if railway_map.is_overload():
        print('ПОТРАЧЕНО')

    pygame.quit()
