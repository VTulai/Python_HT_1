FILEPATH = "todos.txt"


def get_todos(filename=FILEPATH):
    with open(filename, 'r') as file:
        todo = file.readlines()
    return todo


def write_todos(todo, filename=FILEPATH):
    with open(filename, 'w') as file:
        file.writelines(todo)
