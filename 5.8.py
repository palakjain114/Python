def queue_operations():
    queue = []
    while True:
        print("\nQueue Operations:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            element = int(input("Enter element to enqueue: "))
            queue.append(element)
            print(f"{element} added to queue")
        elif choice == 2:
            if queue:
                print(f"Dequeued element: {queue.pop(0)}")
            else:
                print("Queue is empty!")
        elif choice == 3:
            print(f"Queue: {queue}")
        elif choice == 4:
            break
        else:
            print("Invalid choice!")
