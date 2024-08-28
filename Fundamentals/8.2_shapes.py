#1.---------------------------------------------------------------------------------------
"""Define the rectangle, circle, and triangle area calculations as functions"""
import math

# https://docs.python.org/3/library/math.html


def circle_area(radius):
    area = math.pi * radius ** 2
    return area


radius = float(input("Enter the radius of the circle: "))
area = circle_area(radius)
print(f"The area of the circle with radius {radius} is: {round(area, 2)}")


#---------------------------------------------------------------------------------------


def triangle_area(base, height):
    area = ((triangle_height * triangle_base) // 2)
    return area


triangle_base = float(input("Enter the base of the triangle: "))
triangle_height = float(input("Enter the height of the triangle: "))
area = triangle_area(triangle_height, triangle_base)
# print(f"The area of the triangle with base {triangle_base} and height {triangle_height} is: {triangle_area:.2f}")
print(f"The area of the triangle with base {triangle_base} and height {triangle_height} is: {round(area, 2)}")


#---------------------------------------------------------------------------------------

def rectangle_area(rect_length, rect_width):
    rect_area = (rect_width * rect_length)
    return rect_area


rect_length = float(input("Enter the length of the rectangle: "))
rect_width = float(input("Enter the width of the rectangle: "))
rect_area = rectangle_area(rect_length, rect_width)
# print(f"The area of the rectangle with length {rect_length} and breadth {rect_breadth} is: {rect_area:.2f}")
print(f"The area of the rectangle with length {rect_length} and breadth {rect_width} is: {round(rect_area, 2)}")


## another way to restrict the decimal to 0, 1, 2 spaces
# round(number, num_digits)
# round(circle_area, 2)
# {round(triangle_area, 2)}
# {round(rect_area, 2)}


#2.--------------------------------------------------------------------------------------
"""Function named square_parameter that takes side length of a Square and returns 
the perimeter P = 2(l + w)"""


def square_perimeter(side_length):
    perimeter = 4 * side_length
    return perimeter


side_length = float(input("Enter the length of one of the Square's sides: "))
perimeter = square_perimeter(side_length)
# print(f"The area of the rectangle with length {rect_length} and breadth {rect_breadth} is: {rect_area:.2f}")
print(f"The perimeter of the square with side length {side_length} is: {round(perimeter, 2)}")


#3. ---------------------------------------------------------------------------------------
"""Function named circle_details that takes radius and prints both circumference & area C= 2πr"""


def circle_details(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius

    print(f"Radius: {radius}")
    print(f"Circumference: {round(circumference, 2)}")
    print(f"Area: {round(area, 2)}")


radius = float(input("Enter the radius of the circle: "))
circle_details(radius)


#4.---------------------------------------------------------------------------------------
"""Function named geometry that takes the side length of a square and the radius of a circle.
Should print which shape has a larger perimeter/circumference & which has larger area"""


def geometry(side_length, radius):
    square_perimeter = 4 * side_length
    circle_circumference = 2 * math.pi * radius
    square_area = side_length ** 2
    circle_area = math.pi * radius ** 2

    if square_perimeter > circle_circumference:
        print("The Square Perimeter is larger than the circumference")
    elif circle_circumference > square_perimeter:
        print("The Circle circumference is larger than the square perimeter")
    else:
        print("They are the same")


side_length = float(input("Enter the side length of the square: "))
radius = float(input("Enter the radius of the circle: "))
geometry(side_length, radius)
