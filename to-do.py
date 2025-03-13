list = []
    

while True:

    print("\n=== To-Do List App ===")
    print("1: Add Task")
    print("2: View Task")
    print("3: Complete Task")
    print("4: Delete Task")
    print("5: Quit")

    choose = input("Choose the function (1-5): ")

#Adding task in list 

    if choose == "1":
        task = input("Enter task: ")
        list.append(task)                       
        print(f"Task {task}, Added")

#Showing the list of saved task
    elif choose == "2":
        if not list:
            print(" No Task Yet!")
        else:
            print(f"\nYour Tasks:")
            for i in range (len(list)):         #Provide list, a numbers
                print(f"{i + 1}. {list[i]}")     #Increase number with 1 as list goes on

#To mark the list of Task as completed
    elif choose == "3":
        if  not list:
            print(" NO Task Yet")
        else:
            print(f"\nYour Tasks:")
            for i in range (len(list)):
                print(f"{i + 1}. {list[i]}")

            try:
                task_no = int(input("Enter the task no. you want to mark: "))
                if 1 <= task_no <= len(list):                       #Check Input either valid with in range or not 
                    if "[DONE]" not in list [task_no - 1]:          #Check whether selected task is already marked or not
                        list [task_no - 1] += "[DONE]"              #Modify selected task as [DONE] 
                        print(f"Task {task_no} marked")
                    else:
                        print(f"Task {task_no} is already marked")
                else:
                    print(f"Enter between(1-{len(list)})")
            except ValueError:
                print("Invalid input! Enter number")


    elif choose == "4":
        if not list:
            print("\n No Task Yet")
        else:
            print(f"\nYour Tasks:")
            for i in range (len(list)):
                print (f"{i + 1} {list[i]}")
        
            try:
                task_no = int(input("Enter a task number to delete: "))
                if 1 <= task_no <= len(list):
                    delete = list.pop(task_no - 1)         #Remove element from Task List
                    print(f"Task '{delete}' deleted")
                else:
                    print(f"Enter between 1-{len(list)}")
            except ValueError:
                print(f"Invalid Input! Enter number")

    elif choose == "5":
        print("Quit")
        break
    
    else:
        print("Invalid input! Try Again")



    