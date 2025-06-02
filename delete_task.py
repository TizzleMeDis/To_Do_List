from task_data import tasks

def delete_task(deletion):
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