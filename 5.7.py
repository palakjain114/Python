def stack_operations():
    stack = []
    while True:
        print("\nStack Operations:")
        print("1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            element = int(input("Enter element to push: "))
            stack.append(element)
            print(f"{element} pushed to stack")
        elif choice == 2:
            if stack:
                print(f"Popped element: {stack.pop()}")
            else:
                print("Stack is empty!")
        elif choice == 3:
            print(f"Stack: {stack}")
        elif choice == 4:
            break
        else:
            print("Invalid choice!")
