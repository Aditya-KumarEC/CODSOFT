def main():#define  list to store tasks
    tasks =[]
    #Display menu for user actions
    while True:
        print("\n=====To-Do list menu=====")
        print("1. Add a task")
        print("2. View all task")
        print("3. Update a task")
        print("4. Exit")
        #ADD A TASKS
        choice =input("enter your choice: ")
        if choice =='1':
            print()
            tasks_no =int(input("How many tasks you want do- "))

            for i in range(tasks_no):
                task=input("Enter the task: ")
                tasks.append({"task" : task,"done" :False})
                print("Task added!")
        #VIEW THE TASKS
        elif choice =='2':
            print("\nTasks:")
            for index, task in enumerate(tasks):
                status ="Done" if task["done"] else "Not Done"
                print(f"{index+1}. {task['task']} -{status}")
        #UPDATE THE TASKS
        elif choice =='3':
            task_index=int(input("Enter the task no to mark as done: "))-1
            if 0<=task_index <len(tasks):
                tasks[task_index]["done"] = True
                print("Task marked as done!")
            else:
                print("invalid task number.")
        #EXIT
        elif choice =='4':
            print("\nThank you")
            break
        else :
            print("Invalid . please try again.")

if __name__=="__main__":
    main()