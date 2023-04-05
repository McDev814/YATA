#!/usr/bin/python

from Task import Task
import csv
import sys

current_id = 1
tasks = {}
running = True


def choices():
    print('Enter a choice from the list of options below.')
    print('1 - Enter a new task')
    print('2 - View current tasks')
    print('x - exit the progrom')
    print('h - help (display this menu again)\n')


def save(task_dict):
    with open('data.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for k, v in task_dict.items():
            writer.writerow([k, v.title, v.description, v.created])
        csv_file.close()


def open_csv(file_name):
    try:
        with open(file_name) as csv_file:
            reader = csv.reader(csv_file)
            global current_id
            for row in reader:
                tasks[row[0]] = Task(row[1], row[2], created=row[3])
                current_id += 1
            csv_file.close()
    except (FileNotFoundError):
        print(f'It appears that {sys.argv[1]} does not exist')
        print('Perhaps it was a mispelling?')
        file_choice = input('Enter the name of the csv file, 0 to exit, or leave blank to start a new Todo list: ')
        if file_choice == '0':
            exit()
        elif file_choice != '':
            open_csv(file_choice)
    except Exception as e:
        print('An unforseen error has occured:')
        print(e)


if len(sys.argv) > 1:
    open_csv(sys.argv[1])
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
            print(f'{k} : {v.title} | {v.description} | {v.created}')
    elif choice == 'x':
        save(tasks)
        running = False
    elif choice == 'h':
        choices()
    else:
        print('Sorry, that is not one of the valid options.\n\n')
