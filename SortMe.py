lines = []
with open('Sort Me.txt') as f:
    lines = f.readlines()

for x in lines:
    x.replace(" ", "")

def sort(fileStrings):
    lines.sort(key= len)
    for x in fileStrings:
        print(x)

sort(lines)