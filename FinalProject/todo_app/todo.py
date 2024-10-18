import json
from tkinter import *

class Task:
    def __init__(self, title, description, category,completed = False):
        self.title = title
        self.description = description
        self.category = category
        self.completed = completed
    def mark_completed(self):
        self.completed = True
        
    def __repr__(self) -> str:
        status = "Completed" if self.completed else "Not completed"
        return f"{self.title} ({self.category}) - {status}"


def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump([task.__dict__ for task in tasks], f)

def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            return [Task(**data) for data in json.load(f)]
    except FileNotFoundError:
        return []
    
    
    
def add_task(tasks):
    title = input("Enter title for your task: ")
    description = input("Enter descripton for the category: ")
    
    categories = ["Personal", "Work","Learn and Grow", "Entertainment","Misc"]
    while True:
        print("Select Category from below: ")
        for i,category_name in enumerate(categories):
            print(f"{i + 1}. {category_name}")
        index_range = f"[1 - {len(categories)}]"
        index = int(input(f"Enter category number {index_range}: "))
        
        
        if index in range(0,len(categories)+1):
            category = categories[index-1]
            task = Task(title,description,category)
            tasks.append(task)
            save_tasks(tasks)
            print("Task added successfully!")
            break
        else:
            print("Invalid category, try again")
            break

def view_task(tasks):
    print("Tasks ")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")

def mark_completed():
    pass

def delete_task():
    pass



def main():
    tasks = load_tasks()
    def __init__(self):
        self.root = Tk()
        self.root.title = "ToDo App"
        self.root.mainloop()
         
    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
         # Code to add a task
            add_task(tasks)
        elif choice == '2':
            view_task(tasks)
        # Code to display tasks
        elif choice == '3':
            mark_completed(tasks)
        # Code to mark a task as completed
        elif choice == '4':
        # Code to delete a task
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            break
        
if __name__ == "__main__":
    main()