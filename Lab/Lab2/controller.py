from Lab.Lab2.asteroid import Asteroid
from datetime import datetime
import time


class Controller:
    def __init__(self):
        self.list_of_asteroids = []
        i = 0
        while i <= 99:
            self.list_of_asteroids.append(Asteroid.generate_random_asteroid())
            i += 1

    def simulate(self, seconds: int):
        print("Simulation Start Time: ", datetime.now())
        time.sleep((1000000 - datetime.now().microsecond) / 1000000)
        print("\n Moving Asteroids!\n -----------------")
        i = 0
        while i != seconds:
            for asteroid in self.list_of_asteroids:
                asteroid.move()
                print(self.list_of_asteroids[i])
            time.sleep(1)
            i += 1


def main():
    controller = Controller()
    controller.simulate(11)


if __name__ == "__main__":
    main()
