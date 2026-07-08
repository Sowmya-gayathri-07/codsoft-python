import json
import os

FILE_NAME = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save tasks
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Add task
def add_task(tasks):
    task = input("Enter task: ")
    tasks.append({
        "task": task,
        "completed": False
    })
    save_tasks(tasks)
    print("Task Added Successfully!")

# View tasks
def view_tasks(tasks):
    if len(tasks) == 0:
        print("\nNo tasks available.\n")
        return

    print("\nYour Tasks:\n")

    for i, task in enumerate(tasks, start=1):
        status = "✔" if task["completed"] else "✘"
        print(f"{i}. {task['task']} [{status}]")

# Complete task
def complete_task(tasks):
    view_tasks(tasks)

    if len(tasks) == 0:
        return

    try:
        num = int(input("\nEnter task number to complete: "))
        tasks[num - 1]["completed"] = True
        save_tasks(tasks)
        print("Task Completed!")
    except:
        print("Invalid Choice")

# Delete task
def delete_task(tasks):
    view_tasks(tasks)

    if len(tasks) == 0:
        return

    try:
        num = int(input("\nEnter task number to delete: "))
        removed = tasks.pop(num - 1)
        save_tasks(tasks)
        print(f"Deleted: {removed['task']}")
    except:
        print("Invalid Choice")

# Main Menu
def main():

    tasks = load_tasks()

    while True:

        print("\n====== TO-DO LIST ======")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            print("Thank You!")
            break

        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()