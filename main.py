from database import *


create_table()


while True:
    print("\n1. Add Task")
    print("\n2. View Task")
    print("\n3. Complete Task")
    print("\n4. Delect Task")
    print("\n5. Exit")
    choice = input("choose:")

    if chioce =="1":
        title = input("Enter tasks:")
        add_task(title)

    elif choice == "2":
        task = get_tasks ()
        for task in tasks:
             print (task) 

    elif choice == "3":
        task_id =int(input("task ID:"))
        complete_task(tasks_id)

    elif choice == 4:
        task_id = int( input("task ID:"))
        Delect_task(task_id)   

    elif choice =="5":
          break                 