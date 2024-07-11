import math
# https://docs.python.org/3/library/math.html

circle_radius = int(input("Enter radius of the circle: "))
circle_area = math.pi * (circle_radius * circle_radius)

# :.2f limits the calculation to 2 decimal places
# print(f"The area of the circle with radius {circle_radius} is: {circle_area:.2f}")
print(f"The area of the circle with radius {circle_radius} is: {round(circle_area, 2)}")

#---------------------------------------------------------------------------------------
triangle_base = int(input("Enter the base of the triangle: "))
triangle_height = int(input("Enter the height of the triangle: "))

triangle_area = ((triangle_height * triangle_base) // 2)

# print(f"The area of the triangle with base {triangle_base} and height {triangle_height} is: {triangle_area:.2f}")
print(f"The area of the triangle with base {triangle_base} and height {triangle_height} is: {round(triangle_area, 2)}")
#---------------------------------------------------------------------------------------
rect_length = int(input("Enter the length of the rectangle: "))
rect_breadth = int(input("Enter the breadth of the rectangle: "))

rect_area = (rect_breadth * rect_length)

# print(f"The area of the rectangle with length {rect_length} and breadth {rect_breadth} is: {rect_area:.2f}")
print(f"The area of the rectangle with length {rect_length} and breadth {rect_breadth} is: {round(rect_area, 2)}")

## another way to restrict the decimal to 0, 1, 2 spaces
# round(number, num_digits)
# round(circle_area, 2)
# {round(triangle_area, 2)}
# {round(rect_area, 2)}

