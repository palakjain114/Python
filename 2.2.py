def s(a, b, c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    else:
        return c

def l(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

a= float(input("Enter first number: "))
b= float(input("Enter second number: "))
c= float(input("Enter third number: "))

smallest = s(a, b, c)
largest = l (a, b, c)

print("Smallest number: ", smallest)
print("Largest number: ", largest)
   
   
