import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Warning", "You must select a task to delete.")

def update_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        new_task = task_entry.get()
        if new_task != "":
            tasks_listbox.delete(selected_task_index)
            tasks_listbox.insert(selected_task_index, new_task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")
    except:
        messagebox.showwarning("Warning", "You must select a task to update.")

def mark_completed():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        task = tasks_listbox.get(selected_task_index)
        tasks_listbox.delete(selected_task_index)
        tasks_listbox.insert(tk.END, task + " - Completed")
    except:
        messagebox.showwarning("Warning", "You must select a task to mark as completed.")

# Create the main window
root = tk.Tk()
root.title("Advanced To-Do List")

# Create a frame for the task entry and buttons
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

# Task entry widget
task_entry = tk.Entry(input_frame, width=35, font=("Arial", 14))
task_entry.pack(side=tk.LEFT, padx=10)

# Add task button
add_task_button = tk.Button(input_frame, text="Add Task", width=10, command=add_task)
add_task_button.pack(side=tk.LEFT)

# Update task button
update_task_button = tk.Button(input_frame, text="Update Task", width=10, command=update_task)
update_task_button.pack(side=tk.LEFT, padx=10)

# Listbox to display tasks
tasks_listbox = tk.Listbox(root, width=50, height=10, font=("Arial", 14), selectmode=tk.SINGLE)
tasks_listbox.pack(pady=20)

# Mark completed button
mark_completed_button = tk.Button(root, text="Mark Completed", width=15, command=mark_completed)
mark_completed_button.pack(side=tk.LEFT, padx=10)

# Delete task button
delete_task_button = tk.Button(root, text="Delete Task", width=10, command=delete_task)
delete_task_button.pack(side=tk.LEFT, padx=10)

# Run the main loop
root.mainloop()
class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.description}"

class User:
    def __init__(self, username):
        self.username = username
        self.tasks = []

    def add_task(self, task_description):
        self.tasks.append(Task(task_description))
        print(f"Task '{task_description}' added for user '{self.username}'.")

    def view_tasks(self):
        if not self.tasks:
            print(f"No tasks for user '{self.username}'.")
        else:
            print(f"Tasks for user '{self.username}':")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].completed = True
            print(f"Task {task_index + 1} marked as completed for user '{self.username}'.")
        else:
            print("Invalid task number.")

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f"Task '{removed_task.description}' removed for user '{self.username}'.")
        else:
            print("Invalid task number.")

class ToDoApp:
    def __init__(self):
        self.users = {}

    def add_user(self, username):
        if username not in self.users:
            self.users[username] = User(username)
            print(f"User '{username}' added.")
        else:
            print(f"User '{username}' already exists.")

    def get_user(self, username):
        return self.users.get(username)

    def display_menu(self):
        print("\nOptions:")
        print("1. Add User")
        print("2. Add Task")
        print("3. View Tasks")
        print("4. Mark Task as Completed")
        print("5. Remove Task")
        print("6. Exit")

    def main(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            
            if choice == "1":
                username = input("Enter username: ")
                self.add_user(username)
            elif choice == "2":
                username = input("Enter username: ")
                user = self.get_user(username)
                if user:
                    task_description = input("Enter the task: ")
                    user.add_task(task_description)
                else:
                    print(f"User '{username}' not found.")
            elif choice == "3":
                username = input("Enter username: ")
                user = self.get_user(username)
                if user:
                    user.view_tasks()
                else:
                    print(f"User '{username}' not found.")
            elif choice == "4":
                username = input("Enter username: ")
                user = self.get_user(username)
                if user:
                    task_index = int(input("Enter the task number to mark as completed: ")) - 1
                    user.mark_task_completed(task_index)
                else:
                    print(f"User '{username}' not found.")
            elif choice == "5":
                username = input("Enter username: ")
                user = self.get_user(username)
                if user:
                    task_index = int(input("Enter the task number to remove: ")) - 1
                    user.remove_task(task_index)
                else:
                    print(f"User '{username}' not found.")
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = ToDoApp()
    app.main()
