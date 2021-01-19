from itertools import count
import math
import random

"""
Contains class representing an asteroid called Asteroid.
"""


class Asteroid:
    """Represents an asteroid with its circumference in metres, position, velocity.

    Both position and velocity are vectors with x y z coordinates that are measured in metres per second"""
    id_counter = count(1)

    def __init__(self, circumference: float, position: tuple, velocity: tuple):
        """
        Initialize a new asteroid, with an incrementing id for each created asteroid starting with 1.

        :precondition:  Circumference must be a positive number, position and velocity must be tuples with 3 numbers.
        :postcondition: Initialize an object with float circumference, tuple with 3 numbers for position and velocity.
        :param circumference: A float
        :param position: A tuple with 3 numbers
        :param velocity: A tuple with 3 numbers
        """
        self.__circumference = circumference
        self.__position = position
        self.__velocity = velocity
        self.handle_identifier(self)

    @staticmethod
    def handle_identifier(self):
        """
        Initializes the identifier of this object starting with 1, and incrementing by 1 for each created object.
        :return: none
        """
        self.__id = next(self.id_counter)

    @staticmethod
    def calculate_circumference(radius):
        """
        Return circumference of asteroid in metres given a radius in metres
        :param radius: A number
        :return: Circumference calculated from radius.
        """
        return 2 * radius * math.pi

    @staticmethod
    def generate_random_position():
        """
        Generates random position of asteroid with a max range of 100.
        :return: Tuple with three numbers.
        """
        return random.randrange(100), random.randrange(100), random.randrange(100)

    @staticmethod
    def generate_random_velocity():
        """
        Generates random velocity of asteroid with a maximum of 5.
        :return: Tuple with three numbers.
        """
        return random.randrange(5), random.randrange(5), random.randrange(5)

    @staticmethod
    def generate_random_asteroid():
        """
        Return an asteroid instance with random circumference, position, and velocity.

        Position has max of 100 in each axis, and velocity with a max of 5 in each, circumference has a max of 25.133.
        :return: Random Asteroid instance.
        """
        radius = random.randrange(1, 4)
        return Asteroid(Asteroid.calculate_circumference(radius),
                        Asteroid.generate_random_position(),
                        Asteroid.generate_random_velocity())

    def move(self) -> tuple:
        """
        Move asteroid by adding the vector of velocity to position, print new and old position, return the new position.

        :return: Tuple of the new position.
        """
        old_position = self.__position
        self.__position = tuple(map(sum, zip(self.__position, self.__velocity)))
        print(f"Asteroid {self.__id} Moved! Old Pos: {old_position} -> New Pos: {self.__position}")
        return self.__position

    def get_circumference(self) -> float:
        """
        :return: Returns the circumference as a float.
        """
        return self.__circumference

    def set_circumference(self, circumference: float):
        """
        Sets the circumference to the parameter.
        :param circumference: A float.
        :return: none
        """
        self.__circumference = circumference

    def get_position(self) -> tuple:
        """
        Returns the position as a tuple with three floats representing x y z.
        :return: A tuple with three floats.
        """
        return self.__position

    def set_position(self, position: tuple):
        """
        Sets the position.
        :param position: Tuple with three floats representing x y z.
        :return: none.
        """
        self.__position = position

    def get_velocity(self) -> tuple:
        """
        Returns the velocity as a tuple with three floats representing x y z.
        :return: A tuple with three floats.
        """
        return self.__velocity

    def set_velocity(self, velocity: tuple):
        """
        Sets the velocity.
        :param velocity: Tuple with three floats representing x y z.
        :return: none.
        """
        self.__velocity = velocity

    circumference = property(get_circumference, set_circumference)

    velocity = property(get_velocity, set_velocity)

    position = property(get_position, set_position)

    def __repr__(self):
        """
        :return: string representation of this object instance.
        """
        return f"Asteroid ID: {self.__id} Circumference: {self.__circumference:} " \
               f"Position: {self.__position} Velocity: {self.__velocity}"

    def __str__(self) -> str:
        """
        :return: string of this Asteroid's information
        """
        return f"Asteroid {self.__id} is currently at {self.__position} and moving at {self.__velocity} " \
               f"metres per second. It has a circumference of {self.__circumference:_})"
