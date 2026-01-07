'''📝 Exercise 1
Create TodoApp class with:
__init__
load_tasks
save_tasks'''
'''📝 Exercise 2
Add methods:
add_task(task_name)
show_tasks()
mark_done(index)'''
import json
class TodoApp:
    def __init__(self,filename="Python_/Python_Exercise/tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()
    
    def load_tasks(self):
        try:
            with open(self.filename,"r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []
        
    def save_tasks(self):
        with open(self.filename,"w") as file:
            json.dump(self.tasks,file,indent=4)
    
    def add_task(self,task_name):
        self.tasks.append({"task":task_name,"done":False})
        self.save_tasks()
        print("Task added!")
    
    def show_task(self):
        if not self.tasks:
            print("No Task found")
            return 
        
        for i , task in enumerate(self.tasks,1):
            status = "✅" if task["done"] else "❌"
            print(f"{i}.{task['task']} {status}")
    
    def mark_done(self,index):
        if 1<=index <= len(self.tasks):
            self.tasks[index-1]['done']=True
            self.save_tasks()
            print("task mark as done")
        else:
            print("Invaild index")

    def delete_task(self,index):
        if 1<=index <=len(self.tasks):
            del self.tasks[index-1]
            self.save_tasks()


    


app=TodoApp()

is_running = True
while is_running:
        print("1.Add task")
        print("2.Show task")
        print("3.Mark task as done")
        print("4.Remove task")
        print("5.Exit")

        try:
            choice = int(input("Enter the choice: "))
        
        except ValueError:
            print("Input should be num")
        
        if choice ==1:
            tasks = input("Enter the task: ")
            app.add_task(tasks)
        
        elif choice ==2:
            app.show_task()
        
        elif choice ==3:
            app.show_task()
            index = int(input("Enter task number: "))
            app.mark_done(index)
        
        elif choice ==4:
            app.show_task()
            index = int(input("Enter the task number: "))
            app.delete_task(index)
            print("Task Removed")
        elif choice==5:
            is_running=False
            print("Goodbye")
        else:
            print("Invaid index")


        
        

'''🔥 Mini Challenge (Optional)
Add method:

def delete_task(index):'''