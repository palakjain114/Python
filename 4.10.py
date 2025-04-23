def fibonacci_series(n):
    fib_series = [0, 1]  
    for _ in range(n - 2):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]  

n = int(input("Enter the number of Fibonacci numbers to generate: "))

print("Fibonacci Series:", fibonacci_series(n))
