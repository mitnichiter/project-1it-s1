import os
import json
from lolpython import lol_py

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def load_tasks(filename):
    """Load tasks from the given filename."""
    if not os.path.exists(filename):
        return []  # Return empty tasks

    with open(filename, 'r') as file:
        content = file.read().strip()  # Read content and strip whitespace

        if not content:  # Check if the content is empty
            return []  # Return empty tasks

        data = json.loads(content)  # Load JSON data

    return data.get("tasks", [])  # Return tasks or empty list if not found

def save_tasks(filename, tasks):
    """Save tasks to the given filename."""
    data = {
        "tasks": tasks,
    }
    
    with open(filename, 'w') as file:
        json.dump(data, file)

def add_task(tasks):
    """Add a new task to the task list."""
    task = input("Enter the task you want to add: ")
    tasks.append({"task": task, "completed": False})  # Ensure task is added as a dictionary
    save_tasks('data.json', tasks)  # Save after adding

def remove_task(tasks):
    """Remove a task from the task list."""
    view_tasks(tasks)
    index = int(input("Enter the task number you want to remove: ")) - 1
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks('data.json', tasks)  # Save after removing
    else:
        print("Invalid task number.")

def edit_task(tasks):
    """Edit an existing task."""
    view_tasks(tasks)
    index = int(input("Enter the task number you want to edit: ")) - 1
    if 0 <= index < len(tasks):
        new_task = input("Enter the new task: ")
        tasks[index]["task"] = new_task
        save_tasks('data.json', tasks)  # Save after editing
    else:
        print("Invalid task number.")

def replace_task_position(tasks):
    """Replace a task's position in the list."""
    view_tasks(tasks)
    index1 = int(input("Enter the task number to replace: ")) - 1
    index2 = int(input("Enter the new position for this task: ")) - 1
    if 0 <= index1 < len(tasks) and 0 <= index2 < len(tasks):
        tasks[index1], tasks[index2] = tasks[index2], tasks[index1]
        save_tasks('data.json', tasks)  # Save after replacing
    else:
        print("Invalid task number.")

def mark_task_complete(tasks):
    """Mark a task as complete or unmark it if already completed."""
    view_tasks(tasks)
    task_input = input("Enter the task number you want to mark/unmark complete or type '*' to mark/unmark all: ").strip()

    if task_input == '*':
        # Check if all tasks are already marked complete
        if all(task['completed'] for task in tasks):
            # Unmark all tasks
            for task in tasks:
                task['completed'] = False
            print("All tasks have been unmarked as incomplete.")
        else:
            # Mark all tasks as complete
            for task in tasks:
                task['completed'] = True
            print("All tasks have been marked complete.")
    else:
        try:
            index = int(task_input) - 1
            if 0 <= index < len(tasks):
                # Toggle the task's completion status
                tasks[index]["completed"] = not tasks[index]["completed"]
                status = "complete" if tasks[index]["completed"] else "incomplete"
                print(f"Task {index + 1} marked as {status}.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid task number or '*'.")

    save_tasks('data.json', tasks)  # Save after marking complete or unmarking

def view_tasks(tasks):
    """Display the list of tasks."""
    if not tasks:
        print("No tasks available.")
    else:
        print("Tasks:")
        for i, task_info in enumerate(tasks, 1):
            task = task_info.get("task", "")  # Get task string
            completed = task_info.get("completed", False)  # Get completed status
            if completed:
                # Strikethrough and italicize completed tasks
                print(f"{i}. \033[9m\033[3m{task}\033[0m")  # 9m is for strikethrough, 3m is for italic
            else:
                print(f"{i}. {task}")
    input("Press Enter to continue...")  # Wait for user input

def display_help():
    """Display the help menu."""
    print("\nHelp Menu:")
    print("v - View tasks")
    print("a - Add task")
    print("d - Remove task")
    print("e - Edit task")
    print("r - Replace task position")
    print("m - Mark task as complete")
    print("c - Clear screen")
    print("h - Show this help menu")
    print("z - Exit the app")
    print("If you enter an invalid command, type 'h' to show this help menu.\n")
    input("Press Enter to continue...")  # Wait for user input

def main():
    filename = 'data.json'
    
    # Load tasks
    tasks = load_tasks(filename)

    try:
        while True:
            
            command = input("Enter a command (type 'h' for help): ").strip().lower()

            if command == 'v':
                clear_screen()
                view_tasks(tasks)
                clear_screen()
            elif command == 'a':
                clear_screen()
                add_task(tasks)
                clear_screen()
            elif command == 'd':
                clear_screen()
                remove_task(tasks)
                clear_screen()
            elif command == 'e':
                clear_screen()
                edit_task(tasks)
                clear_screen()
            elif command == 'r':
                clear_screen()
                replace_task_position(tasks)
                clear_screen()
            elif command == 'm':
                clear_screen()
                mark_task_complete(tasks)
                clear_screen()
            elif command == 'c':
                clear_screen()
            elif command == 'h':
                clear_screen()
                display_help()
            elif command == 'z':
                save_tasks(filename, tasks)  # Save before exiting
                print("")
                os.system('figlet "ADIOS!"')
                break
            else:
                print("Invalid command. Type 'h' to show help.")  # No screen clear here
    except KeyboardInterrupt:
        save_tasks(filename, tasks) 
        print("") # Save before exiting
        os.system('figlet  "ADIOS!"')

if __name__ == "__main__":
    clear_screen()
    print('echo Welcome to the ')
    os.system('figlet  "To-Do List App"')
    print("")
    main()
