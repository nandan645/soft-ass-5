# todo.py
tasks = []

def add_task(task):
    tasks.append(task)
    print(f'Task "{task}" added.')

def delete_task(index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f'Task "{removed}" removed.')
    else:
        print("Invalid task number.")
        
def list_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for idx, task in enumerate(tasks, start=1):
            print(f'{idx}. {task}')

if __name__ == "__main__":
    add_task("Finish Assignment")
    list_tasks()