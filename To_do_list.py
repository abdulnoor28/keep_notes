
while True:
    choices=["1.Add a Task.","2.View Tasks.","3.Delete a Task.","4.mark a task as completed.","5.show me the pending task only","6.show me the completed tasks only.","7.exit"]
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
    elif(user_choice==7):
        print("Exiting the program. Goodbye!")
        exit()
    elif(user_choice==4):
        with open("notes.txt","r") as file:
            content=file.readlines()
        print("tasks:")
        for index, line in enumerate(content, start=1):
            print(f"{index}. {line.strip()}")
        print("\n")
        user=int(input("enter the index which you want to mark as completed:"))
        if 1<=user<=len(content):
            old_line=content[user-1].strip()
            updated_line=old_line+" ( completed )\n"
            content[user-1]=updated_line
            
            with open("notes.txt","w") as file:
                file.writelines(content)
                
            print(f"\nLine {user} marked as updated!")
        
        else:
            print("invalid line number.try again")
            continue
    elif(user_choice==5):
        with open("notes.txt","r") as file:
            lines=file.readlines()
        print("pending tasks:")
        for line in lines:
            if "completed" not in line:
                print(line.strip())
        print("\n")
    elif(user_choice==6):
        with open("notes.txt","r") as file:
            lines=file.readlines()
        print("completed tasks:")
        for line in lines:
            if "completed" in line:
                print(line.strip())
        print("\n")
        
    else:
        print("incorrect choice. Please try again.")
        continue

        