contents = ["Grape", "Pineapple", "Pomaranc"]

files = ["file1.txt", "file2.txt", "file3.txt"]

for content, file in zip(contents, files):
    file = open(f"../files/{file}", 'w')
    file.write(content)
