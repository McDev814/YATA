from Task import Task


def choices():
    print('Enter a choice from the list of options below.')
    print('1 - Enter a new task')
    print('2 - View current tasks')
    print('x - exit the progrom')
    print('h - help (display this menu again)\n')


current_id = 1
tasks = {}
running = True
choices()
while (running):
    choice = input('--> ')
    if choice == '1':
        title = input('Enter a name for the task: ')
        description = input('Enter a longer description for the task: ')
        tasks[current_id] = Task(title, description)
        current_id += 1
    elif choice == '2':
        for k, v in tasks.items():
            print(f'{k} : {v.title} | {v.description}')
    elif choice == 'x':
        running = False
    elif choice == 'h':
        choices()
    else:
        print('Sorry, that is not one of the valid options.\n\n')
