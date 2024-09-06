while True:
    user_action = input("Enter add, show, edit, complete or exit: ")
    match user_action.strip():
        case "add":

            with open('todos.txt', 'r') as file_read:
                todo_item = file_read.readlines()

            new_todo = input("Enter a TO DO: ") + '\n'
            todo_item.append(new_todo)

            with open('todos.txt', 'w') as file_write:
                todo_item = file_write.writelines(todo_item)

        case "show":

            with open('todos.txt', 'r') as file_read:
                todo_item = file_read.readlines()

            if len(todo_item) == 0:
                print("Empty TO DO, nothing to show!")
            else:
                for index, item in enumerate(todo_item):
                    item = item.strip('\n')
                    row = f"{index + 1}. {item}"
                    print(row)
        case "edit":

            with open('todos.txt', 'r') as file_read:
                todo_item = file_read.readlines()

            num = int(input("Enter number of TO DO item you want to edit: "))
            edited_todo = input("Enter new TO DO: ")
            todo_item[num - 1] = edited_todo + '\n'

            with open('todos.txt', 'w') as file_write:
                todo_item = file_write.writelines(todo_item)

        case "complete":

            with open('todos.txt', 'r') as file_read:
                todo_item = file_read.readlines()

            num = int(input("Enter number of TO DO item you want to complete: "))
            completed_item = todo_item.pop(num - 1).strip('\n')
            print(f"Item '{completed_item}' is completed!")

            with open('todos.txt', 'w') as file_write:
                todo_item = file_write.writelines(todo_item)

        case "exit":
            break

print("Bye!")
