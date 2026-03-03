import sys

TASKS_FILE = "tasks.txt"


def load_tasks():
    """Read tasks from the file and return them as a list."""
    try:
        with open(TASKS_FILE, "r") as f:
            tasks = [line.strip() for line in f if line.strip()]
        return tasks
    except FileNotFoundError:
        return []  # No file yet — that's fine, we'll create it when adding


def save_tasks(tasks):
    """Write the list of tasks to the file."""
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")


def add_task(task_text):
    """Add a new task to the list."""
    if not task_text:
        print("Error: Please provide a task description.")
        print('Example: python todo.py add "Buy groceries"')
        sys.exit(1)

    tasks = load_tasks()
    tasks.append(task_text)
    save_tasks(tasks)
    print(f'Task added: "{task_text}"')
    print(f"You now have {len(tasks)} task(s) in your list.")


def view_tasks():
    """Display all current tasks."""
    tasks = load_tasks()

    if not tasks:
        print("Your to-do list is empty. Add a task with:")
        print('  python todo.py add "Your task here"')
        return

    print(f"Your To-Do List ({len(tasks)} task(s)):")
    print("-" * 30)
    for i, task in enumerate(tasks, start=1):
        print(f"  {i}. {task}")
    print("-" * 30)


def print_usage():
    """Show the user how to use the script."""
    print("Usage:")
    print('  python todo.py add "Your task"  — Add a new task')
    print("  python todo.py view             — View all tasks")


# --- Main entry point ---

if len(sys.argv) < 2:
    print("Error: No command provided.")
    print_usage()
    sys.exit(1)

command = sys.argv[1].lower()

if command == "add":
    task_text = " ".join(sys.argv[2:]).strip()
    add_task(task_text)
elif command == "view":
    view_tasks()
else:
    print(f'Error: Unknown command "{command}".')
    print_usage()
    sys.exit(1)
