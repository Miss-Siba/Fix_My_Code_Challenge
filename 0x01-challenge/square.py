#!/usr/bin/python3
""" Defines a squre class """


class square():
    """Class representing a square."""

    def __init__(self, side_length):
        """
        Initialize a Square instance with a given side length.

        Args:
            side_length (int): The length of each side of the square.
        """
        self.side_length = side_length

    def area_of_my_square(self):
        """ Area of the square """
        return self.side_length ** 2

    def PermiterOfMySquare(self):
        """
        Calculate the perimeter of the square.

        Returns:
            int: The perimeter of the square.
        """
        return self.side_length * 4

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: A string describing the square.
        """
        return f"Square with side length {self.side_length}"


if __name__ == "__main__":

    s = square(side_length=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
