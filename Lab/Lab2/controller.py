"""This module implements a Controller class for Asteroid class"""


from Lab.Lab2.asteroid import Asteroid
from datetime import datetime
import time


class Controller:
    """
    This class simulates 100 asteroids.
    """
    def __init__(self):
        """
        Initialize a new Controller, and fills it with 100 randomly generated Asteroids.
        """
        self.list_of_asteroids = []
        i = 0
        while i <= 99:
            self.list_of_asteroids.append(Asteroid.generate_random_asteroid())
            i += 1

    def simulate(self, seconds: int):
        """
        Simulate asteroid movement for all Asteroids once per second for specified amount of seconds.

        :param seconds: An integer greater than 0.
        :precondition: seconds must be an int greater than 0
        """
        print("Simulation Start Time: ", datetime.now())
        time.sleep((1000000 - datetime.now().microsecond) / 1000000)  # delays by until start of next second.
        print("\n Moving Asteroids!\n -----------------")
        i = 0
        while i != seconds:
            for asteroid in self.list_of_asteroids:
                asteroid.move()
                print(asteroid)
            time.sleep(1)
            i += 1


def main():
    controller = Controller()
    controller.simulate(11)


if __name__ == "__main__":
    main()
