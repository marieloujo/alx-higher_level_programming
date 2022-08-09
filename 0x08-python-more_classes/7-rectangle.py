#!/usr/bin/python3
"""
    Module 0-rectangle - contain definition
    of class rectangle
"""


class Rectangle:
    """Defines an empty class Rectangle

        Attributes:
            __width (int): private attr, contain value of rectangle width
            __height (int): private attr, contain value of rectangle height

    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Class constructeur

        Args:
            width (int): passed value of rectangle width
            height (int): passed value of rectangle height
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def area(self):
        """Return the area of rectangle based
        on its width and height
        """
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of rectangele based
        on its width and height
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    @property
    def width(self):
        """Retrieve of private attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the value of __width

        Args:
            value (int): new width of square.
        """
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve of private attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the value of __height

        Args:
            value (int): new height of square.
        """
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        """returns printable string representation of the rectangle"""
        if self.__width != 0 and self.__height != 0:
            return "\n".join(str(self.print_symbol) * self.width
                             for line in range(self.height))
        return ""

    def __repr__(self):
        """returns a string representation of the rectangle for reproduction"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """prints a string when an instance has been deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")


my_rectangle_1 = Rectangle(8, 4)
print(my_rectangle_1)
print("--")
my_rectangle_1.print_symbol = "&"
print(my_rectangle_1)
print("--")

my_rectangle_2 = Rectangle(2, 1)
print(my_rectangle_2)
print("--")
Rectangle.print_symbol = "C"
print(my_rectangle_2)
print("--")

my_rectangle_3 = Rectangle(7, 3)
print(my_rectangle_3)

print("--")

my_rectangle_3.print_symbol = ["C", "is", "fun!"]
print(my_rectangle_3)

print("--")
