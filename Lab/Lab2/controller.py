from Lab.Lab2.asteroid import Asteroid


class Controller:
    def __init__(self):
        self.list_of_asteroids = []
        i = 0
        while i <= 99:
            self.list_of_asteroids.append(Asteroid.generate_random_asteroid())
            i += 1