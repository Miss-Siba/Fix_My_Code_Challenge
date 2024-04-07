#!/usr/bin/python3

class Square:
    """A class representing a square."""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """
        Initialize a Square instance.

        Args:
            *args: Positional arguments (not used in this example).
            **kwargs: Keyword arguments to dynamically set attributes.
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

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
