def display_menu():
    print("\nTo-Do List Manager")
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Remove a Task")
    print("4. Clear All Tasks")
    print("5. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("\nEnter the task you want to add: ")
    tasks.append(task)
    print(f"Task '{task}' has been added.")

def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("\nEnter the task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task}' has been removed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def clear_tasks(tasks):
    tasks.clear()
    print("\nAll tasks have been cleared.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            clear_tasks(tasks)
        elif choice == '5':
            print("\nExiting To-Do List Manager. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()


