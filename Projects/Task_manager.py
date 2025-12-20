def load_task(filename="tasks.txt"):
    tasks = []
    try:
     with open(filename,"r") as file:
        for line in file:
            name,complete = line.strip().split(" | ")
            tasks.append({ "task":name, "complete":complete=="True"})
    except FileNotFoundError:
       pass
    return tasks

def save_task(tasks,filename="tasks.txt"):
   with open(filename,"w") as file:
      for task in tasks:
         file.write(f"{task['task']} | {task['complete']}\n")

def add_task(tasks,name):
   tasks.append({"task":name, "complete":False})
   print(f"Task '{name} added!")

def view_task(tasks):
   for i, task in enumerate(tasks,1):
      status = "✅" if task['complete'] else "❌"
      print(f"{i}. {task['task']} - {status}")


def complete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]["complete"] = True
        print(f"Task '{tasks[index]['task']}' marked as completed!")
    else:
        print("Invalid task number.")
tasks=load_task()
while True:
   
   print("\n===Task Manager===")
   print("1. Add Task")
   print("2.View Task")
   print("3.Complete Task")
   print("4.Exit")
   print("=====================")

   choice = input("Enter Choice: ")

   if choice=="1":
      name = input("Enter the task name:")

      add_task(tasks,name)
      
   elif choice=="2":
    view_task(tasks)
    
    
   elif choice =="3":
      view_task(tasks)

      try:
         index = int(input("Enter the task to complete: ")) -1
         complete_task(tasks,index)

      except ValueError:
         print("Enter the valid number")

   elif choice =="4":
      save_task(tasks)
      print("saved tasked. Goodbye")
      break
   else:
      print("Invalid choice")
      
