#!/usr/bin/python3

class square():
    
    side_length = 0

    
    def __init__(self, side_length):
        self.side_length = side_length

    def area_of_my_square(self):
        """ Area of the square """
        return self.side_length ** 2

    def PermiterOfMySquare(self):
        return self.side_length * 4

    def __str__(self):
        return f"Square with side length {self.side_length}"

if __name__ == "__main__":

    s = square(side_length = 9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
