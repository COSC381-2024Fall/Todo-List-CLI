from TodoList import TodoList

def print_menu():
    print("\nTo-Do List CLI App")
    print("1. Add task")
    print("2. List tasks")
    print("3. Delete task")
    print("4. Add/Update a due date to a task")
    print("5. Quit")


def main():
    todo_list = TodoList()

    while True:
        try: 
            print_menu()
            choice = input("\nEnter your choice (1-5): ")

            if choice == '1':
                task = input("Enter the task: ")
                todo_list.add_task(task)

            elif choice == '2':
                todo_list.list_tasks()

            elif choice == '3':
                task_number = int(input("Enter task number to delete: "))
                todo_list.delete_task(task_number)

            elif choice == '4':
                task_number = int(input("Enter task number to update: "))
                due_date = input("Enter a due date for the task: ")
                todo_list.add_task_date(task_number, due_date)

            elif choice == '5':
                print("Exiting To-Do List CLI App. Goodbye!")
                break

            else:
                print("Invalid choice! Please choose a valid option.")

        except ValueError:
            print("Invalid input! Please enter a number.")


if __name__ == '__main__':
    main()
