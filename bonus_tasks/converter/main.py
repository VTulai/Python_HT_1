import FreeSimpleGUI as fsg
import converter_util as cu

fsg.theme('Black')

label_1 = fsg.Text("Enter feet: ", font=('Helvetica', 20))
feet = fsg.InputText(key='feet')

label_2 = fsg.Text("Enter inches: ", font=('Helvetica', 20))
inches = fsg.InputText(key='inches')

convert_btn = fsg.Button("Convert", font=('Helvetica', 20))
output_label = fsg.Text(key='output', text_color='green')

exit_btn = fsg.Button("Exit", font=('Helvetica', 20))

window = fsg.Window("File Zipper",
                    layout=[[label_1, feet],
                            [label_2, inches],
                            [convert_btn, exit_btn, output_label]])

while True:
    event, values = window.read()
    match event:
        case 'Convert':
            try:
                feet_value = float(values['feet'])
                inches_value = float(values['inches'])
                result = cu.convert(feet_value, inches_value)
                window['output'].update(f"{result}m")
            except ValueError:
                fsg.popup('Please provide 2 numbers!', font=('Helvetica', 20))
        case 'Exit':
            break

window.close()
