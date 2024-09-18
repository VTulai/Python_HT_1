import modules.file_utils
import time


while True:
    user_action = input("Enter add, show, edit, complete or exit: ")

    if user_action.startswith("add"):

        todo_items = modules.file_utils.get_todos()

        new_todo = user_action[4:] + '\n'
        todo_items.append(new_todo)

        modules.file_utils.write_todos(todo_items)

    elif user_action.startswith("show"):

        todo_items = modules.file_utils.get_todos()

        if len(todo_items) == 0:
            print("Empty TO DO, nothing to show!")
        else:
            for index, item in enumerate(todo_items):
                item = item.strip('\n')
                row = f"{index + 1}. {item}"
                print(row)

    elif user_action.startswith("edit"):
        try:
            todo_items = modules.file_utils.get_todos()

            num = int(user_action[5:])
            edited_todo = input("Enter new TO DO: ")
            todo_items[num - 1] = edited_todo + '\n'

            modules.file_utils.write_todos(todo_items)
        except ValueError:
            print("The command is not valid!")
            continue
        except IndexError:
            print("No such index!")
            continue

    elif user_action.startswith("complete"):
        try:
            todo_items = modules.file_utils.get_todos()

            num = int(user_action[9:])
            completed_item = todo_items.pop(num - 1).strip('\n')
            print(f"Item '{completed_item}' is completed!")

            modules.file_utils.write_todos(todo_items)
        except IndexError:
            print("No such index!")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Invalid operation! Try again!")

print("Bye!")
