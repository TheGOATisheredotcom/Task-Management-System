import datetime as dt
from task import Task

CATEGORIES = ['Work', 'Personal', 'Urgent', 'Others']
PRIORITIES = ['Low', 'Medium', 'High']

class TaskManager:
    def __init__(self):
        self.tasks = []

    def select_category(self):
        print("Select a category:")
        for idx, category in enumerate(CATEGORIES, 1):
            print(f"{idx}. {category}")
        choice = int(input("Enter the number corresponding to the category: "))
        return CATEGORIES[choice - 1]
    
    def select_due_date(self):
        while True:
            date_str = input("Enter due date (YYYY-MM-DD): ")
            try:
                due_date = dt.datetime.strptime(date_str, "%Y-%m-%d").date()
                return due_date
            except ValueError:
                print("Invalid date format. Please try again.")
                continue

    def select_priority(self):
        print("Select a priority:")
        for idx, priority in enumerate(PRIORITIES, 1):
            print(f"{idx}. {priority}")
        choice = int(input("Enter the number corresponding to the priority: "))
        return PRIORITIES[choice - 1]

    def add_task(self):

        description = input("Enter task description: ")
        category = self.select_category()
        due_date = self.select_due_date()
        priority = self.select_priority()
        status = "Incomplete"

        new_task = Task(description, category, due_date, priority, status)
        self.tasks.append(new_task)

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for idx, task in enumerate(self.tasks, 1):
            print(f"{idx}. {task.description} | Category: {task.category} | Due: {task.due_date} | Priority: {task.priority} | Status: {task.status}")
    
    def mark_task_complete(self):
        self.list_tasks()
        choice = int(input("Enter the number of the task to mark as complete: "))
        while True:
            if 1 <= choice <= len(self.tasks):
                self.tasks[choice - 1].status = 'Done'
                print("Task marked as complete.")
                break
            else:
                print("Invalid choice. Please try again.")
    
    def check_overdue_tasks(self):
        today = dt.date.today()
        overdue_tasks = [task for task in self.tasks if task.due_date < today and task.status != 'Done']
        if not overdue_tasks:
            print("No overdue tasks.")
            return
        print("Overdue Tasks:")
        for task in overdue_tasks:
            print(f"- {task.description} | Due: {task.due_date} | Status: {task.status}")
    
    def view_by_category(self):
        category = self.select_category()
        filtered_tasks = [task for task in self.tasks if task.category == category]
        if not filtered_tasks:
            print(f"No tasks found in category: {category}")
            return
        print(f"Tasks in category: {category}")
        for task in filtered_tasks:
            print(f"- {task.description} | Due: {task.due_date} | Status: {task.status}")

    def view_by_due_date(self):
        due_date = self.select_due_date()
        filtered_tasks = [task for task in self.tasks if task.due_date == due_date]
        if not filtered_tasks:
            print(f"No tasks found with due date: {due_date}")
            return
        print(f"Tasks with due date: {due_date}")
        for task in filtered_tasks:
            print(f"- {task.description} | Category: {task.category} | Status: {task.status}")

    def view_by_priority(self, priority):
        filtered_tasks = [task for task in self.tasks if task.priority == priority]
        if not filtered_tasks:
            print(f"No tasks found with priority: {priority}")
            return
        print(f"Tasks with priority: {priority}")
        for task in filtered_tasks:
            print(f"- {task.description} | Category: {task.category} | Due: {task.due_date} | Status: {task.status}")

    def delete_completed_tasks(self):
        before_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if task.status != 'Done']
        after_count = len(self.tasks)
        print(f"Deleted {before_count - after_count} completed tasks.")