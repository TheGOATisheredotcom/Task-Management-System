# 📝 Python CLI Task Manager

A feature-rich Command Line Interface (CLI) application built with Python to help you organize tasks, set priorities, and track deadlines. This project demonstrates Object-Oriented Programming (OOP), JSON data persistence, and CSV data exporting.

---

## 🚀 Features

* **Task Management:** Create, view, and complete tasks with ease.
* **Organization:** Group tasks by categories: *Work, Personal, Urgent, Others*.
* **Prioritization:** Assign *Low, Medium, or High* priority to stay focused.
* **Deadlines:** Track due dates and automatically identify **Overdue** tasks.
* **Data Persistence:** Tasks are saved to `tasks.json` so you never lose your progress.
* **Export to CSV:** Generate a `tasks.csv` file to view your data in Excel or Google Sheets.
* **Clean Interface:** Automatic screen clearing for a modern, distraction-free CLI experience.

---

## 🛠️ Installation & Setup

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/yourusername/task-manager.git](https://github.com/yourusername/task-manager.git)
    cd task-manager
    ```

2.  **Ensure Python is Installed:**
    This app requires Python 3.x. Check your version with:
    ```bash
    python --version
    ```

3.  **Run the Application:**
    ```bash
    python main.py
    ```

---

## 📂 File Structure

* `main.py`: The entry point containing the main menu loop and user input logic.
* `task.py`: The `Task` class (handles individual task data and dictionary conversion).
* `task_manager.py`: The "Brain" of the app (manages the list of tasks, filtering, and sorting).
* `storage.py`: Handles reading/writing to `tasks.json` and exporting to `tasks.csv`.
* `menu.py`: Handles the visual display of the user interface menu.

---

## 💡 Usage Tips

* **Date Format:** Always enter dates as `YYYY-MM-DD` (e.g., 2026-01-17).
* **Completing Tasks:** Use the "Mark Task Complete" option to move tasks to 'Done' status.
* **Exporting:** Run the CSV export option before closing to create a spreadsheet-ready file.

---

## 🛡️ License

This project is open-source and available under the [MIT License](LICENSE).