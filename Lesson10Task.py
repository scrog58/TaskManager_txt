def listTask():
    with open('test.txt', 'r') as file:
        x = input('To print list press "l" for list: ')
        for count, line in enumerate(file, 1):
            if x == 'l' or x == 'L':
                print(count, str(line), end='')
            else:
                print("Incorrect entry")
    entry = input(
        '\nTo go back to the menu press "m" for list otherwise click "q" to quit: '
    )
    if entry == 'm':
        theTask()
    elif entry == 'q':
        print('You quit the application')
    else:
        print('Error: your entry wasn\'t regnozed')


def addTask():
    add = input('Add your task: ')
    if add == '':
        print('You didn\'t add anything')
    else:
        with open('test.txt', 'a') as file:
            file.write('\n' + str(add))
    entry = input(
        '\nTo go back to the menu press "m" for list otherwise click "q" to quit: '
    )
    if entry == 'm':
        theTask()
    elif entry == 'q':
        print('You quit the application')
    else:
        print('Error: your entry wasn\'t regnozed')


def deleteTask():
    print(
        '\nTo delete you must enter all the characters you want removed or you will get and ERROR'
    )
    delete = int(input('What do you want deleted: '))
    if delete == '':
        print('Error you didn\'t write anything')
    else:
        with open('test.txt', 'r') as file:
            lists = file.readlines()
            if delete > len(lists):
                print("Error wrong input")
            else:
                lists.pop(delete - 1)
                print('Delete!')
                file_write = open('test.txt', 'w')
                for list in lists:
                    file_write.write(list)
            file.close()


def theTask():
    print(
        "\n1. SEE lists select 1\n2. To ADD onto you're lists select 2\n3. To REMOVE from your lists select 3"
    )
    entry = input('What\'s your selection? ')
    if entry == '1':
        listTask()
    elif entry == '2':
        addTask()
    elif entry == '3':
        deleteTask()
    elif entry == '4':
        markComplete()
    else:
        print('Incorrect input')


def markComplete():
    with open('test.txt', 'a') as file:
        complete = int(input("What do you want to complete"))
        lists = file.readlines
        for list in lists:
            if not list[0]:
                if complete > 1:
                    complete = complete - 1
                else:
                    lists[0] = (list[0], True)
                    print(list + " Complete")
                    return


theTask()
