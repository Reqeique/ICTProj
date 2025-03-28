import sys

def load_tasks():
    try:
        with open('tasks.txt', 'r') as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(f"{task}\n")

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added.")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks in the to-do list.")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def delete_task(task_number):
    tasks = load_tasks()
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"Task '{removed_task}' deleted.")
    else:
        print(f"Invalid task number: {task_number}")

def print_help():
    print("Usage:")
    print("  python todo.py add <task>      Add a new task")
    print("  python todo.py view            View all tasks")
    print("  python todo.py delete <number> Delete a task by its number")
    print("  python todo.py help            Show this help message")

def main():
    if len(sys.argv) < 2:
        print_help()
        return

    command = sys.argv[1].lower()
    if command == 'add':
        if len(sys.argv) < 3:
            print("Error: No task provided.")
            print_help()
        else:
            task = ' '.join(sys.argv[2:])
            add_task(task)
    elif command == 'view':
        view_tasks()
    elif command == 'delete':
        if len(sys.argv) < 3:
            print("Error: No task number provided.")
            print_help()
        else:
            try:
                task_number = int(sys.argv[2])
                delete_task(task_number)
            except ValueError:
                print("Error: Task number must be an integer.")
                print_help()
    elif command == 'help':
        print_help()
    else:
        print(f"Unknown command: {command}")
        print_help()

if __name__ == '__main__':
    main()
