import datetime
import json
def log_activity(func):
    def wrapper(*args,**kwargs):
        timestamp = datetime.datetime.now()
        with open('audit.log','a') as f:
            f.write(f'{timestamp} Executing Function: {func.__name__}\n')
        return func(*args,**kwargs)
    return wrapper
class User:
    def __init__(self,username,role='Dev'):
        self.username = username
        self.role = role
    def __str__(self):
        return f'{self.role} User: {self.username}'
class Manager(User):
    def __init__(self,username):
        super().__init__(username,role='Manager')
class Task:
    def __init__(self,title,assignee,status='pending'):
        self.title = title
        self.status = status
        self.assignee = assignee
    def __str__(self):
        return f"[Status: {self.status}] Task: '{self.title}' (Assigned to: {self.assignee.username})"
class Project:
    def __init__(self,title):
        self.title = title
        self.tasks =[]
    @log_activity
    def add_task(self, task_obj):
        self.tasks.append(task_obj)
    def save_to_json(self):
        data = []
        for t in self.tasks:
            task_dict = {"title": t.title,
                "status": t.status,
                "assignee": t.assignee.username}
            data.append(task_dict)
        with open('project_db.json','w') as f:
            json.dump(data,f)
    def load_data(self):
        try:
           with open('project_db.json','r') as f:
               raw = json.load(f)
           self.tasks = []
           for item in raw:
               user_obj = User(item['assignee'])
               new = Task(item['title'], user_obj, item['status'])
               self.tasks.append(new)
           print('Data loaded successfully!')

        except FileNotFoundError:
            print("No saved data found. Starting fresh.")

    def get_pending_count(self):
        pending_list = [t for t in self.tasks if t.status == 'pending']
        return len(pending_list)


    def mark_task_done(self, title_to_complete):
        found = False
        for t in self.tasks:
            if t.title ==title_to_complete:
                t.status = 'DONE'
                print(f"Task '{title_to_complete}' marked as DONE.")
                self.save_to_json()
                return
        print('task not found')
    def remove_task(self, title_to_remove):
        for t in self.tasks:
            if t.title == title_to_remove:
                self.tasks.remove(t)
                print(f"Task '{title_to_remove}' deleted.")
                self.save_to_json()
                return
        print('Task not Found')

print("--- 1. INITIALIZING SYSTEM ---")
boss = Manager("Alice")
dev = User("Bob")

my_project = Project("Website Redesign")
my_project.load_data()

print("\n--- 2. ADDING TASKS ---")
t1 = Task("Fix Login Bug", dev)
t2 = Task("Design Homepage", boss)

my_project.add_task(t1)
my_project.add_task(t2)

print("\n--- 3. VIEWING LIST ---")
for task in my_project.tasks:
    print(task)

print(f"\nPending Count: {my_project.get_pending_count()}")

print("\n--- 4. COMPLETING A TASK ---")
my_project.mark_task_done("Fix Login Bug")

print("\n--- 5. FINAL STATUS ---")
for task in my_project.tasks:
    print(task)

print(f"Pending Count: {my_project.get_pending_count()}")

print("\nCheck 'audit.log' for timestamps and 'project_db.json' for data!")


