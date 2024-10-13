import os
import json

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def load_tasks(filename):
    """Load tasks from the given filename or return an empty list."""
    if not os.path.exists(filename):
        return []  # If file doesn't exist, return an empty list

    with open(filename, 'r') as file:
        content = file.read().strip()

        if not content:  # If the file is empty
            return []

        return json.loads(content).get("tasks", [])  # Load tasks

def save_tasks(filename, tasks):
    """Save tasks to the given filename."""
    with open(filename, 'w') as file:
        json.dump({"tasks": tasks}, file)

def add_task(tasks):
    """Add a new task to the list."""
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    save_tasks('data.json', tasks)

def remove_task(tasks):
    """Remove a task or delete all tasks if '*' is entered."""
    view_tasks(tasks)
    task_input = input("Enter task number to remove or '*' to remove all tasks: ").strip()

    if task_input == '*':
        confirm = input("Are you sure you want to delete all tasks? (y/n): ").strip().lower()
        if confirm == 'y':
            tasks.clear()  # Remove all tasks
            print("All tasks have been deleted.")
        else:
            print("Cancelled deleting all tasks.")
    else:
        try:
            index = int(task_input) - 1
            if 0 <= index < len(tasks):
                tasks.pop(index)
                print(f"Task {index + 1} has been removed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid task number or '*'.")
    
    save_tasks('data.json', tasks)



from prompt_toolkit import prompt

def edit_task(tasks):
    """Edit an existing task with live editing."""
    view_tasks(tasks)
    index = int(input("Enter task number to edit: ")) - 1
    if 0 <= index < len(tasks):
        current_task = tasks[index]["task"]
        
        # Prompt user to edit the task with the current task pre-filled
        new_task = prompt(f"Edit task (leave blank to keep it): ", default=current_task)

        if new_task:
            tasks[index]["task"] = new_task  # Update task if user provides new input
            print("Task updated successfully.")
        else:
            print("No changes made.")
        
        save_tasks('data.json', tasks)
    else:
        print("Invalid task number.")




def replace_task_position(tasks):
    """Swap two tasks by their positions."""
    view_tasks(tasks)
    index1 = int(input("Enter task number to move: ")) - 1
    index2 = int(input("Enter new position: ")) - 1
    if 0 <= index1 < len(tasks) and 0 <= index2 < len(tasks):
        tasks[index1], tasks[index2] = tasks[index2], tasks[index1]
        save_tasks('data.json', tasks)
    else:
        print("Invalid task number.")

def mark_task_complete(tasks):
    """Toggle task completion or mark/unmark all tasks."""
    view_tasks(tasks)
    task_input = input("Enter task number or '*' to mark/unmark all: ").strip()

    if task_input == '*':
        # If all tasks are marked complete, unmark them, otherwise mark them complete
        all_completed = all(task['completed'] for task in tasks)
        for task in tasks:
            task['completed'] = not all_completed
        status = "unmarked as incomplete" if all_completed else "marked as complete"
        print(f"All tasks have been {status}.")
    else:
        try:
            index = int(task_input) - 1
            if 0 <= index < len(tasks):
                tasks[index]["completed"] = not tasks[index]["completed"]
                status = "complete" if tasks[index]["completed"] else "incomplete"
                print(f"Task {index + 1} marked as {status}.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid task number or '*'.")

    save_tasks('data.json', tasks)

def view_tasks(tasks):
    """Display all tasks with their completion status."""
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, 1):
            task_text = f"{i}. {task['task']}"
            if task["completed"]:
                task_text = f"\033[9m\033[3m{task_text}\033[0m"  # Strikethrough & italicize completed tasks
            print(task_text)


def display_help():
    """Display the help menu."""
    print("\nHelp Menu:")
    commands = {
        'v': "View tasks",
        'a': "Add task",
        'd': "Remove task",
        'e': "Edit task",
        'r': "Replace task position",
        'm': "Mark task complete/incomplete",
        'c': "Clear screen",
        'h': "Show this help menu",
        'credits': "Show credits",
        'z': "Exit the app"
    }
    for cmd, desc in commands.items():
        print(f"{cmd} - {desc}")

def credits():
    os.system('figlet -f digital -c "CREDITS"')
    print("CREATED BY GROUP 1\n")
    print("Aadhil Negim(@mitnichiter)\nAbin Manuvel\nJewel K Sunish\nShifana Latheef\nSumi R S\n")
    input("Press Enter to continue...")
    clear_screen()

def main():
    filename = 'data.json'
    tasks = load_tasks(filename)

    while True:
        try:
            command = input("Enter a command (type 'h' for help): ").strip().lower()

            if command == 'v':
                clear_screen()
                view_tasks(tasks)
            elif command == 'a':
                clear_screen()
                add_task(tasks)
            elif command == 'd':
                clear_screen()
                remove_task(tasks)
            elif command == 'e':
                clear_screen()
                edit_task(tasks)
            elif command == 'r':
                clear_screen()
                replace_task_position(tasks)
            elif command == 'm':
                clear_screen()
                mark_task_complete(tasks)
            elif command == 'c':
                clear_screen()
            elif command == 'h':
                clear_screen()
                display_help()
            elif command == 'credits':
                clear_screen()
                credits()
            elif command == 'z':
                save_tasks(filename, tasks)  # Save before exiting
                print("")
                os.system('figlet "ADIOS!"')
                input("Press Enter to exit...")
                break
            else:
                print("Invalid command. Type 'h' to show help.")

        except KeyboardInterrupt:
            clear_screen()
            print("\nHasty huh? Saving tasks before u exit...")
            save_tasks(filename, tasks) 
            os.system("figlet -f slant ADIOUS!")
            input("Press Enter to exit...")
            break



if __name__ == "__main__":
    clear_screen()
    os.system('figlet -f term -c "Welcome to the"')
    os.system('figlet -f standard "To-Do List App"')
    os.system('figlet -f term -c "by Group 1"')
    print("")
    main()
