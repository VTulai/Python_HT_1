FILEPATH = "todos.txt"


def get_to_dos(filename=FILEPATH):
    with open(filename, 'r') as file:
        todo = file.readlines()
    return todo


def write_to_dos(todo, filename=FILEPATH):
    with open(filename, 'w') as file:
        file.writelines(todo)
