import json as js
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_n = os.path.join(BASE_DIR, "tasks.json")

def load_file():
    try:
        with open(file_n, 'r') as file:
            return js.load(file)
    except (FileNotFoundError, js.JSONDecodeError):
        return []
    
def save_file(tasks):
    try:
        with open(file_n, 'w') as file:
            js.dump(tasks, file, indent=4)
    except Exception as e:
        print(f"Error saving data: {e}")

def export_to_csv(tasks, filename="tasks.csv"):
    import csv
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Description", "Category", "Due Date", "Priority", "Status"])
            for task in tasks:
                writer.writerow([task.description, task.category, task.due_date, task.priority, task.status])
    except Exception as e:
        print(f"Error exporting to CSV: {e}")