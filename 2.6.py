def count_digits(number):
    return len(str(abs(number)))

num = int(input("Enter a number: "))

digit_count = count_digits(num)

print(f"The number {num} has {digit_count} digits.")
