def factorial(x):
    return 1 if x == 0 else x * factorial(x - 1)

n = int(input("Enter n: "))
r = int(input("Enter r: "))
nCr = factorial(n) // (factorial(r) * factorial(n - r))
nPr = factorial(n) // factorial(n - r)
print("nCr:", nCr)
print("nPr:", nPr)
