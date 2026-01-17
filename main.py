import os

from task import Task
from task_manager import TaskManager
from storage import load_file, save_file, export_to_csv
from menu import display_menu

# Initialize the global manager object to handle business logic
manager = TaskManager()


# ---------------- Helper Functions ----------------
def export_data():
    return {
        "tasks": [task.to_dict() for task in manager.tasks],
    }

def refresh_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def pause():
    """Pauses the program until the user presses Enter."""
    input("Press Enter to continue...")
    refresh_screen()

# ---------------- Main Program Loop ----------------

def main():

    data = load_file()
    if isinstance(data, dict):
        raw_tasks = data.get("tasks", [])
        for item in raw_tasks:
            manager.tasks.append(Task.from_dict(item))

    while True:
        display_menu()
        choice = input("Select an option (1-7): ")

        if choice == '1':
            refresh_screen()
            manager.add_task()
            save_file(export_data())
            pause()

        elif choice == '2':
            refresh_screen()
            manager.list_tasks()
            pause()

        elif choice == '3':
            refresh_screen()
            manager.mark_task_complete()
            save_file(export_data())
            pause()

        elif choice == '4':
            refresh_screen()
            manager.check_overdue_tasks()
            pause()
            
        elif choice == '5':
            refresh_screen()
            manager.view_by_category()
            pause()

        elif choice == '6':
            refresh_screen()
            manager.view_by_due_date()
            pause()
        
        elif choice == '7':
            refresh_screen()
            manager.view_by_priority()
            pause()

        elif choice == '8':
            refresh_screen()
            manager.delete_completed_tasks()
            save_file(export_data())
            pause()

        elif choice == '9':
            refresh_screen()
            task_dicts = [t.to_dict() for t in manager.tasks]
            export_to_csv(task_dicts)
            pause()

        elif choice == '10':
            refresh_screen()
            print("Exiting the program. Goodbye!")
            save_file(export_data())
            break
        else:
            print("Invalid choice. Please try again.")
            pause()

if __name__ == "__main__":
    main()