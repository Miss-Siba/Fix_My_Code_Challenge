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

    def area(self):
        """Calculate the area of the square."""
        return self.side_length ** 2

    def perimeter(self):
        """Calculate the perimeter of the square."""
        return self.side_length * 4

    def __str__(self):
        """Return a string representation of the square."""
        return f"Square with side length {self.side_length}"


if __name__ == "__main__":
    square = Square(side_length=9)
    print(square)
    print("Area:", square.area())
    print("Perimeter:", square.perimeter())
