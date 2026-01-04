'''from greeting import hello,goodbye,add,sub

print(hello("Milan"))
print(goodbye("Milan"))
print(add(2,1))
print(sub(3,1))

import random

for _ in range(5):
    print(random.randint(1,50))'''


#===========Files and Json=========================

'''with open("text.txt", "w") as file:
    file.write("Line1\n")
    file.write("Line2\n")
    file.write("Line3\n")'''

'''with open("text.txt","r") as file:
    content = file.read()
    print(content)'''

'''import json
data = {"name":"Milan", "age":24, "skills":["Python","Git"]}

with open("profile.json", 'w') as file:
    json.dump(data,file,indent=4)

with open("profile.json","r") as file:
    content = json.load(file)
    print(content["skills"])
   
data["language"]="English"

with open("profile.json","w") as file:
    json.dump(data,file,indent=4)'''
import json
file_name = "profile.json"

def read_task():
    with open(file_name,"r") as file:
        return json.load(file)
    

def save_task(tasks):
    with open(file_name,"w") as file:
        json.dump(tasks,file,indent=4)


def add_task(task_name):
    tasks = read_task()
    tasks.append({"task":task_name,"done":False})
    save_task(tasks)
    print("Task Added")

def show_task():
    tasks = read_task()
    for i , task in enumerate(tasks,1):
        status = "✅" if task["done"] else "❌"
        print(f"{i}. {task['task']} {status}")
       

def mark_done(index):
    tasks = read_task()
    tasks[index-1]["done"] = True
    save_task(tasks)
    print("Task marked as done.")

        


    # ----------- Simple Menu -----------
while True:
    print("\n1. Add task")
    print("2. Show tasks")
    print("3. Mark task as done")
    print("4. Exit")

    choice = input("Choose: ")

    if choice =="1":
        task = input("Enter the task: ")
        add_task(task)
    
    elif choice =="2":
        show_task()
    
    elif choice =="3":
        show_task()
        num = int(input("Enter task number: "))
        mark_done(num)
    elif choice=="4":
        break
    else:
        print("Invalid choice ")





