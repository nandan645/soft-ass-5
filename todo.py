# todo.py

tasks = []

def add_task(task):
    tasks.append(task)
    print(f'Task "{task}" added.')

def list_tasks():
    if not tasks:
        print("Task list is empty. Add some tasks!")
    else:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f'{idx}. {task}')

def delete_task(index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f'Task "{removed}" removed.')
    else:
        print("Invalid task number.")

if __name__ == "__main__":
    add_task("Finish Assignment")
    list_tasks()
    delete_task(0)