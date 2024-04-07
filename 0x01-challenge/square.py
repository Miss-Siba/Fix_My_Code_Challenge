#!/usr/bin/python3

class Square:
    """A class representing a square."""

    def __init__(self, side_length=0):
        """
        Initialize a Square instance.

        Args:
            side_length (int): The length of each side of the square.
        """
        self.side_length = side_length

    def area_of_my_square(self):
        """Calculate the area of the square."""
        return self.side_length ** 2

    def PermiterOfMySquare(self):
        """Calculate the perimeter of the square."""
        return self.side_length * 4

    def __str__(self):
        """Return a string representation of the square."""
        return "{}".format(self.side_length)


if __name__ == "__main__":
    s = Square(side_length=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
