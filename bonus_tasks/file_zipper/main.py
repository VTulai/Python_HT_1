import FreeSimpleGUI as fsg

label_1 = fsg.Text("Select files to compress")
file_to_compress = fsg.InputText()
choose_btn1 = fsg.FilesBrowse("Choose")

label_2 = fsg.Text("Select destination folder")
destination_folder = fsg.InputText()
choose_btn2 = fsg.FolderBrowse("Choose")

compress_btn = fsg.Button("Compress")

window = fsg.Window("File Zipper",
                    layout=[[label_1, file_to_compress, choose_btn1],
                            [label_2, destination_folder, choose_btn2],
                            [compress_btn]])

window.read()
window.close()
