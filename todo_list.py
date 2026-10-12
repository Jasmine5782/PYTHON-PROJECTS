while True:
    print("==== TO-DO LIST ====")
    print("1. Add Tasks")
    print("2. View Tasks")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        print("Add Task Selected")
        task = input("Enter a task: ")
        if task == "":
            print("Task cannot be empty")
        else:
            with open("task.txt", "a") as file:
                file.write(task + "\n")
            print("Task saved successfully")

    elif choice == "2":
        print("View Task selected")
        with open("task.txt", "r") as file:
            content = file.read()

            if content == " ":
                print("No task saved yet")
            else:
                print(content)

    elif choice == "3":
        print("Goodbye")
        break
    else:
        print("Invalid Choice")


    