def are_points_on_line(x1, y1, x2, y2, x3, y3):
    area = (x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))
    if area == 0:
        return "The points are on the same straight line."
    else:
        return "The points are not on the same straight line."

x1, y1 = map(int, input("Enter coordinates of first point (x1 y1): ").split())
x2, y2 = map(int, input("Enter coordinates of second point (x2 y2): ").split())
x3, y3 = map(int, input("Enter coordinates of third point (x3 y3): ").split())

result = are_points_on_line(x1, y1, x2, y2, x3, y3)
print(result
