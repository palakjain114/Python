def check_area_vs_perimeter(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    
    if area > perimeter:
        return "Area is greater than Perimeter"
    elif area < perimeter:
        return "Area is smaller than Perimeter"
    else:
        return "Area is equal to Perimeter"

length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

result = check_area_vs_perimeter(length, breadth)
print(result)
