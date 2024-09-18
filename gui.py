import FreeSimpleGUI as fsg
import modules.file_utils as fu
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", 'w') as file:
        pass

fsg.theme('DarkGrey12')

clock = fsg.Text('', key='clock')
label = fsg.Text("Type in your To-Do: ")
input_form = fsg.InputText(tooltip="Enter a to-do", key='new_todo')
add_btn = fsg.Button(key="Add", image_source='pictures/add.png',
                     tooltip='Add a todo', mouseover_colors='LightBlue2')

list_box = fsg.Listbox(values=fu.get_todos(), key='existing_todos',
                       enable_events=True, size=(45, 10))
edit_btn = fsg.Button('Edit')
complete_btn = fsg.Button(key='Complete', image_source='pictures/complete.png',
                          tooltip='Complete a todo', mouseover_colors='LightBlue2', size=10)

exit_button = fsg.Button('Exit')
info_label = fsg.Text(key='info')

window = fsg.Window("My To-Do app",
                    layout=[[clock], [label], [input_form, add_btn],
                            [list_box, fsg.Column([[edit_btn], [complete_btn]])],
                            [exit_button]],
                    font=('Helvetica', 20))


while True:
    # Display window function
    event, values = window.read(timeout=10)
    window['clock'].update(time.strftime('%b %d, %Y %H:%M:%S'))
    match event:
        case "Add":
            todo_items = fu.get_todos()

            new_todo = values['new_todo'] + '\n'
            if new_todo == '\n':
                continue
            todo_items.append(new_todo)

            fu.write_todos(todo_items)
            window['existing_todos'].update(values=todo_items)
            window['new_todo'].update('')
        case 'Edit':
            try:
                todo_to_edit = values['existing_todos'][0]
                new_todo = values['new_todo']

                todo_items = fu.get_todos()

                index = todo_items.index(todo_to_edit)
                todo_items[index] = new_todo + '\n'

                fu.write_todos(todo_items)

                window['existing_todos'].update(values=todo_items)
                window['new_todo'].update('')
            except IndexError:
                fsg.popup("Please select an item from the list!", font=('Helvetica', 20))
        case 'Complete':
            try:
                todo_to_edit = values['existing_todos'][0]
                todo_items = fu.get_todos()
                todo_items.remove(todo_to_edit)
                fu.write_todos(todo_items)

                window['existing_todos'].update(values=todo_items)
                window['new_todo'].update('')
            except IndexError:
                fsg.popup("Please select an item from the list!", font=('Helvetica', 20))
        case 'Exit':
            break
        case 'existing_todos':
            window['new_todo'].update(value=values['existing_todos'][0].strip('\n'))
        case fsg.WIN_CLOSED:
            break

window.close()
