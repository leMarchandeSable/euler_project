

with open("22##name.txt", "r") as f:
    names = f.readline()
    names = names.replace('"', "")
    names = names.split(",")
    names = sorted(names)


abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

s = 0
for name in names:
    name_score = 0
    for letter in name:
        name_score += abc.index(letter) + 1
    s += name_score * (names.index(name) + 1)

print(s)