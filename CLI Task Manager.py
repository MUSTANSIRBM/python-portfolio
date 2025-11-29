class Task:
    def __init__(self,title):
        self.title = title
        self.is_completed = False
    def mark_done(self):
        self.is_completed = True
    def __str__(self):
        # RIGHT: Give the string back to the program
        status = "x" if self.is_completed else " "
        return f"[{status}] {self.title}"
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()
    def add_task(self,title):
        new_task = Task(title)
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"Task added: {title}")
    def complete_task(self,index):
        if 0 <= index < len(self.tasks):
            target_task = self.tasks[index]
            target_task.mark_done()
            self.save_tasks()
            print(f"Marked '{target_task.title}' as done.")
        else:
            print("Invalid task number.")
    def show_task(self):
        for index,task in enumerate(self.tasks):
            print(f"{index}. {task}")
            # self.save_tasks()
    def save_tasks(self):
        with open('tasks.txt','w') as f:
           for task in self.tasks:
               line = f"{task.title},{task.is_completed}\n"
               f.write(line)
    def load_tasks(self):
        with open('tasks.txt','r') as f:
            f.read()
            try:
                with open('tasks.txt', 'r') as f:
                    for line in f:
                        # Step A: Clean up
                        line = line.strip()
                        if not line: continue  # Skip empty lines

                        # Step B: Split (Unpack)
                        # "Learn Git,False" -> title="Learn Git", status="False"
                        title, status_str = line.split(',')

                        # Step C: Create Object
                        loaded_task = Task(title)

                        # Step D: Restore Status (Convert string "True" to Boolean)
                        if status_str == "True":
                            loaded_task.is_completed = True
                        else:
                            loaded_task.is_completed = False

                        # Step E: Add to list
                        self.tasks.append(loaded_task)

            except FileNotFoundError:
                print("No saved tasks found. Starting fresh!")

# 1. Initialize
manager = TaskManager()

# 2. Add Tasks
manager.add_task("Learn Git")
manager.add_task("Master Python")

# 3. View
manager.show_task()

# 4. Complete First Task
manager.complete_task(0) # Index 0

# 5. View again (Should show [x] Learn Git)
manager.show_task()

# 6. CHECK FILE 'tasks.txt'
