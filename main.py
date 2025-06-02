from add_task import add_task
from delete_task import delete_task
from view_task import view_task

def main():
    flag = True
    print("\n---LIST MADE: (add a task)---\nWhat would you like to do?\n   1: Add\n   2: Remove\n   3: View\n   4: Quit\n")
    while flag:
        request = input("Please Respond: ")

        if(request.lower() == "add" or request.lower() == "1" or request.lower() == "-a"):
            task = input("Task to add: ")
            if task == "":
                print("\nPlease Enter a task to Add!\n")
                continue
            add_task(task)
        elif(request.lower() == "remove" or request.lower() == "2" or request.lower() == "-r"):
            task = input("Task to delete: ")
            if task == "":
                print("\nPlease Enter a task to Delete!\n")
                continue
            delete_task(task)
        elif(request.lower() == "view" or request.lower() == "3" or request.lower() == "-v"):
            view_task()
        elif(request.lower() == "quit" or request.lower() == "4" or request.lower() == "-q"):
            print("\nDone..")
            flag = False
        elif(request.lower() == "help" or request.lower() == "9" or request.lower() == "-h"):
            print("\n-------------COMMAND LIST--------------\nYou can either type [Action] or [list #] or [-a|-r|-v|-q|-h]\n   1: Add\n   2: Remove\n   3: View\n   4: Quit\n   9: Help\n")
        else:
            print("\n-------------NO SUCH COMMAND-----------\nNeed help just type 'help'\n")
        
    print("Exiting...")

main()