ratios = None
numbers = "1234567890"

with open("gearRatios.txt" , 'r') as f:
    ratios = f.read()
    f.close()

ratios = ratios.split("\n")
for line in range(len(ratios)):
    ratios[line] = list(ratios[line])
    ratios[line].append(".")

total = 0
number = "0"
ids = []

# Returns True if there is a special symbol
def check(line, start, end):
    top = line
    bottom = line
    if line != 0:
        top = line - 1
    if line != len(ratios) - 1:
        bottom = line + 1
    if start != 0:
        start -= 1
    if end != len(ratios[line]) - 1:
        end += 1
    for l in range(top, bottom + 1):
        for c in range(start, end + 1):
            if ratios[l][c] not in numbers and ratios[l][c] != ".":
                return True
    return False


for line in range(len(ratios)):
    for value in range(len(ratios[line])):
        if ratios[line][value] in numbers:
            number += ratios[line][value]
            ids.append(value)
        elif number != "0" and check(line, ids[0], ids[-1]):
            total += int(number)
            number = "0"
            ids = []
        elif number != 0:
            number = "0"
            ids = []

print(total)