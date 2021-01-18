from itertools import count

"""
Contains class representing an asteroid called Asteroid.
"""

class Asteroid:
    """Represents an asteroid with its circumference in metres, position, velocity.
    Both position and velocity are vectors with x, y ,z coordinates measured in metres per second"""
    id_counter = count(1)

    def __init__(self, circumference: float, position: tuple, velocity: tuple):
        """
        Initialize a new asteroid, with an incrementing id for each created asteroid starting with 1.

        :precondition:  Circumference must be float, position and velocity must be tuples with 3 floats each.
        :postcondition: Initialize an object with float circumference, tuple with 3 floats for position and velocity.
        :param circumference: A float
        :param position: A tuple with 3 floating point numbers
        :param velocity: A tuple with 3 floating point numbers
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

    def move(self) -> tuple:
        """
        Moves the position of the asteroid by adding the vector of velocity to position and returns the new position.

        :return: Tuple of the new position.
        """
        self.__position = tuple(map(sum, zip(self.__position, self.__velocity)))
        return self.__position

    def get_circumference(self) -> float:
        """
        Returns the circumference as a float.
        :return: A float.
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

    def __str__(self) -> str:
        return f"Asteroid({self.__circumference:_}, {self.__position}, {self.__velocity}, {self.__id})"
