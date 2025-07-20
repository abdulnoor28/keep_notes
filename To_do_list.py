
while True:
    choices=["1.Add a Task","2.View Tasks","3.Delete a Task","4.Exit"]
    for choice in choices:
        print(choice)
    user_choice=int(input("enter your choice (1-4): "))
    print("\n")
    if(user_choice==1):
        with open("notes.txt","a") as file:
            task=input("enter your task:")
            file.write(task+"\n")
            print("task added successfully")
    elif(user_choice==2):
        try:
            with open("notes.txt","r") as file:
                content=file.readlines()
                if not content:
                    print("No tasks found. Please add a task first.")
                    continue
                else:
                    print("tasks:")
                    for index, line in enumerate(content, start=1):
                        print(f"{index}. {line.strip()}")
                    print("\n")
        except FileNotFoundError:
            print("No tasks found. Please add a task first.")
            continue
    elif(user_choice==3):
        try:
            with open("notes.txt","r") as file:
                content=file.readlines()
                if(len(content)==0):
                    print("No tasks found. Please add a task first.")
                else:
                    index=int(input("enter the index of task to delete (1-"+str(len(content))+" ): "))-1
                    if 0<=index<len(content):
                        content.pop(index)
                    else:
                        print("Invalid index. Please enter a valid index.")
                        continue
                    with open("notes.txt","w") as file:
                        file.writelines(content)
                    print("task deleted successfully")
        except FileNotFoundError:
            print("No tasks found. Please add a task first.")
            continue
    elif(user_choice==4):
        print("Exiting the program. Goodbye!")
        exit()

    else:
        print("incorrect choice. Please try again.")
        continue

        
