import glob

mf = glob.glob("../files/*.txt")

print(mf)

for path in mf:
    with open(path, "r") as f:
        print(f.read())
