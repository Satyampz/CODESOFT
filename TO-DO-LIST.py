def main():
    tasks = []

    while True:
        print("######## TO-DO-LIST ########")
        print("1. Add Tasks in TO-DO-LIST")
        print("2. Show Added Tasks TO-DO-LIST")
        print("3. Mark Task as Done")
        print("4. Exit from TO-DO-LIST")

        choice = input("Enter your choice: ")

        if choice == '1':
            print()
            n_tasks = int(input("How many task you want to add: "))
            
            for i in range(n_tasks):
                task = input("Enter the task: ")
                tasks.append({"task": task, "done": False})
                print("Task added!!!\n")

        elif choice == '2':
            print("\nTasks:")
            for index, task in enumerate(tasks):
                status = "Done" if task["done"] else "Not Done"
                print(f"{index + 1}. {task['task']} - {status}")

        elif choice == '3':
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("Task marked as done!")
            else:
                print("Invalid task number.")

        elif choice == '4':
            print("Exiting the TO-DO-LIST.")
            break

        else:
            print("Invalid Choice Enter, Please try again.")

if __name__ == "__main__":
    main()
