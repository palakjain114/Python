def is_valid_triangle(angle1, angle2, angle3):
    if angle1 + angle2 + angle3 == 180:
        return True
    else:
        return False

angle1 = float(input("Enter the first angle of the triangle: "))
angle2 = float(input("Enter the second angle of the triangle: "))
angle3 = float(input("Enter the third angle of the triangle: "))

if is_valid_triangle(angle1, angle2, angle3):
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")
