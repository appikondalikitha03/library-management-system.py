tasks = []

while True:
    print("\n===== TASK MANAGEMENT SYSTEM =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append({"task": task, "completed": False})
        print("Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            print("\nTasks:")
            for i, task in enumerate(tasks, start=1):
                status = "✓ Completed" if task["completed"] else "✗ Pending"
                print(f"{i}. {task['task']} - {status}")

    elif choice == "3":
        if not tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task['task']}")
            try:
                num = int(input("Enter task number to mark as completed: "))
                tasks[num - 1]["completed"] = True
                print("Task marked as completed!")
            except:
                print("Invalid task number.")

    elif choice == "4":
        if not tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task['task']}")
            try:
                num = int(input("Enter task number to delete: "))
                deleted = tasks.pop(num - 1)
                print(f"Deleted task: {deleted['task']}")
            except:
                print("Invalid task number.")

    elif choice == "5":
        print("Exiting Task Management System...")
        break

    else:
        print("Invalid choice! Please enter 1-5.")