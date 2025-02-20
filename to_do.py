tasks = []
def main():
    global tasks
    flag = True
    print("\n---LIST MADE: (add a task)---\nWhat would you like to do?\n   1: Add\n   2: Remove\n   3: View\n   4: Quit\n")
    while flag:
        request = input("Please Respond: ")

        if(request.lower() == "add" or request.lower() == "1" or request.lower() == "-a"):
            task = input("Task to add: ")
            addTask(task)
        elif(request.lower() == "remove" or request.lower() == "2" or request.lower() == "-r"):
            task = input("Task to delete: ")
            deleteTask(task)
        elif(request.lower() == "view" or request.lower() == "3" or request.lower() == "-v"):
            seeTasks()
        elif(request.lower() == "quit" or request.lower() == "4" or request.lower() == "-q"):
            print("\nDone..")
            flag = False
        elif(request.lower() == "help" or request.lower() == "9" or request.lower() == "-h"):
            print("\n-------------COMMAND LIST--------------\nYou can either type [Action] or [list #] or [-a|-r|-v|-q|-h]\n   1: Add\n   2: Remove\n   3: View\n   4: Quit\n   9: Help\n")
        else:
            print("\n-------------NO SUCH COMMAND-----------\nNeed help just type 'help'\n")
        
    print("Exiting...")

def addTask(addition):
    global tasks
    tasks.append(addition)
    print("\nTASK APPENDED\n")

def deleteTask(deletion):
    global tasks

    try:
        isinstance(int(deletion), int)
        if len(tasks) < int(deletion):
            print("\nTask not on list!!!\n")
            return ''
        tasks.pop(int(deletion)-1)
        print("\nTASK REMOVED!\n")
        return ''
    except:
        for index in range(len(tasks)):
            if  deletion.lower() in tasks[index].lower():
                tasks.pop(index)
                print("\nTASK REMOVED!\n")
                return ''

    print("\nTask not on list!!!\n")
    return ''

def seeTasks():
    global tasks
    if len(tasks) == 0:
        print("\n------ LIST EMPTY!!! -----\n")
        return ''
    print("\n----------------- TASK LIST --------------")
    for index in range(len(tasks)):
        print(f"{index+1}: {tasks[index]}")
    print("------------------------------------------\n")

main()