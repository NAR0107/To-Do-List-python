def main():
    tasks = []

    while True:
        print("\n ---- ^_^ To-Do List ^_^ ----")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")

        choice = input("Select the option  : ")

        if choice == '1':
            print()
            n_tasks = int(input("How may tasks do you want to add: "))

            for i in range(n_tasks):
                task = input("Enter the task: ")
                tasks.append({"task": task, "complete": False})
                print("Task added!")

        elif choice == '2':
            print("\nTasks:")
            for index, task in enumerate(tasks):
                status = "complete" if task["complete"] else "Not Yet Complted"
                print(f"{index + 1}. {task['task']} - {status}")

        elif choice == '3':
            task_index = int(input("Enter the task number to mark as complete: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["complete"] = True
                print("Task marked as completed!")
            else:
                print("Invalid task number.")

        elif choice == '4':
            print("Exit from the To-Do List.")
            break

        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()