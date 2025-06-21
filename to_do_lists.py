tasks = []

def show_menu():
    print("""
TO DO LIST:
1. ADD A TASK
2. SHOW TASKS
3. MARK TASK AS DONE
4. EXIT
""")

def show_tasks():
    if not tasks:
        print("No tasks yet.")
        return
    for i, task in enumerate(tasks, 1):
        status = "✓ Done" if task['done'] else "✗ Not Done"
        print(f"{i}. {task['description']} - {status}")

while True:
    show_menu()
    try:
        choice = int(input("Enter Your Choice Number: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        task_text = input("Add a task: ")
        if not any(t['description'] == task_text for t in tasks):
            tasks.append({'description': task_text, 'done': False})
        else:
            print("Task already exists.")
    elif choice == 2:
        show_tasks()
    elif choice == 3:
        show_tasks()
        try:
            task_no = int(input("Enter task number to mark as done: "))
            if 1 <= task_no <= len(tasks):
                tasks[task_no - 1]['done'] = True
                print("Task marked as done.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a number.")
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again.")
