import json
import os
from datetime import datetime

DATA_FILE = "todos.json"


def load_todos():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


def save_todos(todos):
    with open(DATA_FILE, "w") as f:
        json.dump(todos, f, indent=2)


def show_todos(todos):
    if not todos:
        print("\n  No tasks yet!\n")
        return
    print("\n  Your Tasks:")
    print("  " + "-" * 40)
    for i, todo in enumerate(todos, 1):
        status = "✓" if todo["done"] else "○"
        print(f"  {i}. [{status}] {todo['task']}  ({todo['date']})")
    print()


def add_todo(todos):
    task = input("  Enter task: ").strip()
    if task:
        todos.append({
            "task": task,
            "done": False,
            "date": datetime.now().strftime("%d %b %Y")
        })
        save_todos(todos)
        print("  Task added!\n")
    else:
        print("  Empty task, skipped.\n")


def complete_todo(todos):
    show_todos(todos)
    if not todos:
        return
    try:
        num = int(input("  Enter task number to mark complete: "))
        if 1 <= num <= len(todos):
            todos[num - 1]["done"] = True
            save_todos(todos)
            print("  Task marked as done!\n")
        else:
            print("  Invalid number.\n")
    except ValueError:
        print("  Please enter a valid number.\n")


def delete_todo(todos):
    show_todos(todos)
    if not todos:
        return
    try:
        num = int(input("  Enter task number to delete: "))
        if 1 <= num <= len(todos):
            removed = todos.pop(num - 1)
            save_todos(todos)
            print(f"  Deleted: {removed['task']}\n")
        else:
            print("  Invalid number.\n")
    except ValueError:
        print("  Please enter a valid number.\n")


def main():
    print("=" * 44)
    print("         Simple To-Do App")
    print("=" * 44)

    todos = load_todos()

    while True:
        print("  1. View tasks")
        print("  2. Add task")
        print("  3. Mark task complete")
        print("  4. Delete task")
        print("  5. Exit")
        print()

        choice = input("  Choose an option (1-5): ").strip()
        print()

        if choice == "1":
            show_todos(todos)
        elif choice == "2":
            add_todo(todos)
        elif choice == "3":
            complete_todo(todos)
        elif choice == "4":
            delete_todo(todos)
        elif choice == "5":
            print("  Bye!\n")
            break
        else:
            print("  Invalid option, try again.\n")


if __name__ == "__main__":
    main()
