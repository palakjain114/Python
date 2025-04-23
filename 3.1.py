def count_vowels(vow):
    vowels = "aeiouAEIOU"
    count = 0
    for char in vow:
        if char in vowels:
            count += 1
    return count


vow = input("Enter a string")
print("Number of vowels:", count_vowels(vow))
