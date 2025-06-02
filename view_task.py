from task_data import tasks

def view_task():

    if len(tasks) == 0:
        print("\n------ LIST EMPTY!!! -----\n")
    else:
        print("\n----------------- TASK LIST --------------")
        for index in range(len(tasks)):
            print(f"{index+1}: {tasks[index]}")
        print("------------------------------------------\n")