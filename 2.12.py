import math

def check_point_in_circle(x, y, cx, cy, r):
    distance = math.sqrt(math.pow(x - cx, 2) + math.pow(y - cy, 2))
    
    if distance < r:
        return "The point lies inside the circle."
    elif distance == r:
        return "The point lies on the circle."
    else:
        return "The point lies outside the circle."

x, y = map(float, input("Enter the coordinates of the point (x y): ").split())
cx, cy = map(float, input("Enter the coordinates of the center of the circle (cx cy): ").split())
r = float(input("Enter the radius of the circle: "))

result = check_point_in_circle(x, y, cx, cy, r)
print(result)
