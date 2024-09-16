import FreeSimpleGUI as fsg

label = fsg.Text("Type in your To-Do: ")
input_form = fsg.InputText(tooltip="Enter a to-do")
add_btn = fsg.Button("Add")
window = fsg.Window("My To-Do app", layout=[[label, input_form, add_btn]])

# Display window function
window.read()

window.close()

