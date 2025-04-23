def calculate_total_and_grade(marks1, marks2, marks3):
    total = marks1 + marks2 + marks3
    average = total / 3
    
    def grade(marks):
        if marks <= 39:
            return "F"
        elif 40 <= marks <= 44:
            return "P"
        elif 45 <= marks <= 49:
            return "C"
        elif 50 <= marks <= 54:
            return "B"
        elif 55 <= marks <= 59:
            return "B+"
        elif 60 <= marks <= 69:
            return "A"
        elif 70 <= marks <= 79:
            return "A+"
        elif 80 <= marks <= 100:
            return "O"
        else:
            return "NA"
    
    grade1 = grade(marks1)
    grade2 = grade(marks2)
    grade3 = grade(marks3)
    
    if marks1 <= 39 or marks2 <= 39 or marks3 <= 39:
        status = "Fail"
    else:
        status = "Pass"
    
    return total, average, status, grade1, grade2, grade3

marks1 = float(input("Enter marks for subject 1: "))
marks2 = float(input("Enter marks for subject 2: "))
marks3 = float(input("Enter marks for subject 3: "))

total, average, status, grade1, grade2, grade3 = calculate_total_and_grade(marks1, marks2, marks3)

print(f"Total: {total}")
print(f"Average: {average}")
print(f"Status: {status}")
print(f"Grades: Subject 1: {grade1}, Subject 2: {grade2}, Subject 3: {grade3}")
