todo_item = []
while True:
    user_action = input("Enter add, show, edit, complete or exit: ")
    match user_action.strip():
        case "add":
            new_todo = input("Enter a TO DO: ")
            todo_item.append(new_todo)
        case "show":
            if len(todo_item) == 0:
                print("Empty TO DO, nothing to show!")
            else:
                for index, item in enumerate(todo_item):
                    row = f"{index + 1}. {item}"
                    print(row)
        case "edit":
            num = int(input("Enter number of TO DO item you want to edit: "))
            edited_todo = input("Enter new TO DO: ")
            todo_item[num - 1] = edited_todo
        case "complete":
            num = int(input("Enter number of TO DO item you want to complete: "))
            print(f"Item '{todo_item.pop(num - 1)}' is completed!")
        case "exit":
            break

print("Bye!")
