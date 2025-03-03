import pathlib
import zipfile


def compress(files, destination_folder):
    dest_path = pathlib.Path(destination_folder, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as zip_arch:
        for file in files:
            file = pathlib.Path(file)
            zip_arch.write(file, arcname=file.name)


if __name__ == 'main':
    compress(files=['../files/file1.txt', '../files/file2.txt'], destination_folder='dest')
