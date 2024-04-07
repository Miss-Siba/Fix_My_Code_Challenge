#!/usr/bin/python3
"""Defines a square class"""


class Square():
    """A class representing a square."""

    def __init__(self, width=0, height=0):
        """Initialize a square instance"""
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """Calculate the area of the square."""
        return self.width * self.height

    def perimeter_of_my_square(self):
        """Calculate the perimeter of the square."""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
