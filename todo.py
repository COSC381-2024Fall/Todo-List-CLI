# todo.py
from TodoList import TodoList

def print_menu():
    """Prints the menu of options for the user."""
    print("\nTo-Do List CLI App")
    print("1. Add task")
    print("2. List tasks")
    print("3. Delete task")
    print("4. Add/Update a due date to a task")
    print("5. Add/Update a tag to a task")
    print("6. Delete all tasks")
    print("7. Edit task description")
    print("8. Quit")


def main():
    """Main function that runs the To-Do List CLI."""
    todo_list = TodoList()

    while True:
        try: 
            print_menu()
            choice = input("\nEnter your choice (1-8): ")

            if choice == '1':
                    task = input("Enter the task: ")
                    dateBool = input("Would you like to add a due date? 1: Yes 2: No -- ")
                    if int(dateBool) == 1:
                        due_date = input("Enter the due date: ")
                    else:
                        due_date = ""
                    todo_list.add_task(task, due_date)

            elif choice == '2':
                todo_list.list_tasks()

            elif choice == '3':
                task_number = int(input("Enter task number to delete: "))
                todo_list.delete_task(task_number)

            elif choice == '4':
                task_number = int(input("Enter task number to add/update a due date: "))
                due_date = input("Enter a due date for the task (e.g., YYYY-MM-DD): ")
                todo_list.add_task_date(task_number, due_date)
                
        #   Add/Update a tag
            elif choice == '5':
                task_number = int(input("Enter task number to update: "))
                tag = input("Enter a tag for the task: ")
                todo_list.add_tag(task_number, tag)

            elif choice == '6':
                todo_list.delete_all_tasks()

            elif choice == '7':
                try:
                    task_number = int(input("Enter task number to update: "))
                    desc = input("Enter new task description: ")
                    todo_list.update_task(task_number, desc)
                except ValueError:
                    print("Invalid input! Please enter a number.")    

            elif choice == '8':
                print("Exiting To-Do List CLI App. Goodbye!")
                break

            else:
              print("Invalid choice! Please choose a valid option.")

        except ValueError:
            print("Invalid input! Please enter a number.")


if __name__ == '__main__':
    main()