save = []

def functions():
    print("1: Add Task")
    print("2: View Task")
    print("3: Complete Task")
    print("4: Delete Task")
    print("5: Quit")

while True:

    choose = int(input("Choose the function (1-5): "))

    if choose == 1:
        task = input("Enter task: ")
        save.appent(task)
        print(f"Task {task}, Added")

    elif choose == 2:
        print("View added Task")

    elif choose == 3:
        print("Mark completed Task")

    elif choose == 4:
        print("Delete Task")

    elif choose == 5:
        print("Quit")
        break
    
    else:
        print("Invalid input! Try Again")
        continue


    