import FreeSimpleGUI as fsg
import zip_creator as zc

label_1 = fsg.Text("Select files to compress")
file_to_compress = fsg.InputText()
choose_btn1 = fsg.FilesBrowse("Choose", key='choose_file')

label_2 = fsg.Text("Select destination folder")
destination_folder = fsg.InputText()
choose_btn2 = fsg.FolderBrowse("Choose", key='choose_folder')

compress_btn = fsg.Button("Compress")
output_label = fsg.Text(key='output', text_color='green')

window = fsg.Window("File Zipper",
                    layout=[[label_1, file_to_compress, choose_btn1],
                            [label_2, destination_folder, choose_btn2],
                            [compress_btn, output_label]])

while True:
    event, values = window.read()
    filepaths = values['choose_file'].split(';')
    folder = values['choose_folder']
    zc.compress(filepaths, folder)
    window['output'].update('Compression completed!')

window.close()
