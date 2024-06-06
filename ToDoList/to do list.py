tasks=[]

def addtask():
    task=input('Please Enter a Task:')
    tasks.append(task)
    print(f'Task: {task} added to the list.')

def listtasks():
    if not tasks:
        print('There are No tasks Currently in the list')
    else:
        print('Current Tasks:')
        for index , task in enumerate(tasks):
            print(f'Task #{index}.{task}')



def deletetask():
    task=input('Please Enter a Task to Delete:')
    listtasks()
    try:
        tasktodelete=int(input('Choose the # of task you want to delete:'))
        if tasktodelete<len(tasks):
            tasks.pop(tasktodelete)
        else:
            print(f'Task # {tasktodelete} was not found')

    except:
        print('Invalid Input!')


if __name__ == '__main__':

    print('Welcome to the to do list app:)')
    while True:
        print('\n')
        print('Please select one of the following options:')
        print('___________________________________________')
        print('1. Add a New Task')
        print('2. Delete a Task')
        print('3. List Tasks')
        print('4. Quit!')

        choice= input('Enter your choice:')

        if(choice=='1'):
            addtask()
        elif(choice=='2'):
            deletetask()
        elif(choice=='3'):
            listtasks()
        elif(choice=='4'):
            break
        else:
            print('Invalid choice! Please Try again')

print('GoodBye👋🏻👋🏻')



    