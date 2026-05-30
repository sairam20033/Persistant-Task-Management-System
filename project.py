import json


def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

tasks = load_tasks()

while True:
    print("\n===== TASK MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")

        print("0. Yet to start\n1. Completed\n2. Not completed")
        status_choice = input("Enter status: ")

        if status_choice == "0":
            status = "Yet to start"
        elif status_choice == "1":
            status = "Completed"
        elif status_choice == "2":
            status = "Not Completed"
        else:
            status = "Unknown"

        tasks.append({"task": task, "status": status})
        save_tasks(tasks)
        print("Task added!")

    elif choice == "2":
        if not tasks:
            print("No tasks found.")
        else:
            print("\n--- Your Tasks ---")
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t['task']} --> {t['status']}")

    #Delete Tasks
    elif choice == "3":
        if not tasks:
            print("No tasks to delete.")
        else:
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t['task']} --> {t['status']}")

            try:
                delete_index = int(input("Enter task number to delete: ")) - 1
                if 0 <= delete_index < len(tasks):
                    removed = tasks.pop(delete_index)
                    save_tasks(tasks)
                    print(f"🗑 Deleted: {removed['task']}")
                else:
                    print("Invalid number.")
            except:
                print("Invalid input.")

    # Exit
    elif choice == "4":
        print("Goodbye.")
        break

    else:
        print("Invalid choice. Try again.")