"""This module implements the Asteroid class representing an asteroid."""


from itertools import count
import math
import random


class Asteroid:
    """Represents an asteroid with its circumference in metres, position, velocity.

    Both position and velocity are vectors with x y z coordinates that are measured in metres per second"""
    id_counter = 0

    def __init__(self, circumference, position, velocity):
        """
        Initialize a new asteroid, with an incrementing id for each created asteroid starting with 1.

        :precondition:  Circumference must be a positive integer, position and velocity must be tuples with 3 integers.
        :param circumference: A float
        :param position: A tuple with 3 integers
        :param velocity: A tuple with 3 integers
        """
        self.__circumference = circumference
        self.__position = position
        self.__velocity = velocity
        self.__id = self.increment_id()

    @classmethod
    def increment_id(cls):
        """
        Increments static variable for asteroid id by 1, and returns new asteroid id.
        :return: New id.
        """
        Asteroid.id_counter += 1
        return Asteroid.id_counter

    @staticmethod
    def calculate_circumference(radius):
        """
        Return circumference of asteroid in metres given a positive radius in metres.
        :param radius: A positive integers
        :precondition: Radius must be a positive integers.
        :return: Circumference calculated from radius.
        """
        if radius > 0:
            return 2 * radius * math.pi

    @staticmethod
    def generate_random_position():
        """
        Generates random position of asteroid with a max range of 100.
        :return: Tuple with three integers.
        """
        return random.randrange(100), random.randrange(100), random.randrange(100)

    @staticmethod
    def generate_random_velocity():
        """
        Generates random velocity of asteroid with a maximum of 5.
        :return: Tuple with three integers.
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

    def move(self):
        """
        Move asteroid by adding the vector of velocity to position, print new and old position, return the new position.

        :return: Tuple of the new position.
        """
        old_position = self.__position
        self.__position = tuple(map(sum, zip(self.__position, self.__velocity)))
        print(f"Asteroid {self.__id} Moved! Old Pos: {old_position} -> New Pos: {self.__position}")
        return self.__position

    def get_circumference(self):
        """
        :return: Returns the circumference as a number.
        """
        return self.__circumference

    def set_circumference(self, circumference):
        """
        Sets the circumference to the parameter.
        :param circumference: A positive integers.
        :precondition: Circumference must be a positive number.
        """
        if circumference > 0:
            self.__circumference = circumference

    def get_position(self):
        """
        Returns the position as a tuple with three integers representing x y z.
        :return: A tuple with three floats.
        """
        return self.__position

    def set_position(self, position):
        """
        Sets the position.
        :param position: Tuple with three integers representing x y z.
        :precondition: Position must be tuple with three integers.
        :return: none.
        """
        if isinstance(position, tuple) & len(position) == 3 & all(element.is_integer() for element in position):
            self.__position = position

    def get_velocity(self):
        """
        Returns the velocity as a tuple with three integers representing x y z.
        :return: A tuple with three floats.
        """
        return self.__velocity

    def set_velocity(self, velocity):
        """
        Sets the velocity.
        :param velocity: Tuple with three integers representing x y z.
        :return: none.
        """
        if isinstance(velocity, tuple) & len(velocity) == 3 & all(element.is_integer() for element in velocity):
            self.__position = velocity

    circumference = property(get_circumference, set_circumference)

    velocity = property(get_velocity, set_velocity)

    position = property(get_position, set_position)

    def __repr__(self):
        """
        :return: string representation of this object instance.
        """
        return f"Asteroid ID: {self.__id} Circumference: {self.__circumference:} " \
               f"Position: {self.__position} Velocity: {self.__velocity}"

    def __str__(self):
        """
        :return: string of this Asteroid's information
        """
        return f"Asteroid {self.__id} is currently at {self.__position} and moving at {self.__velocity} " \
               f"metres per second. It has a circumference of {self.__circumference:_})"
