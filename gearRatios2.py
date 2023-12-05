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

# Returns True if there is a number
def find(line: int, value: int) -> list:
    moreThanOne = False
    lines = []
    cols = []
    top = line
    bottom = line
    start = value
    end = value
    if line != 0:
        top = line - 1
    if line != len(ratios) - 1:
        bottom = line + 1
    if start != 0:
        start = value - 1
    if end != len(ratios[line]) - 1:
        end = value + 1
    for l in range(top, bottom + 1):
        for c in range(start, end + 1):
            if ratios[l][c] in numbers:
                if l in lines:
                    if abs(cols[lines.index(l)] - c) != 1:
                        moreThanOne = True
                else:
                    lines.append(l)
                    cols.append(c)

    
    nums = []
    for l in range(top, bottom + 1):
        for c in range(start, end + 1):
            number = ""
            pointer = c
            while ratios[l][pointer] in numbers:
                number = number + ratios[l][pointer]
                pointer += 1
            pointer = c
            while ratios[l][pointer] in numbers:
                if pointer != c:
                    number = ratios[l][pointer] + number
                pointer -= 1
            nums.append(number)

    nums = list(set(nums))
    nums.remove('')
    if len(nums) < 2:
        moreThanOne = False
    else:
        moreThanOne = True
    return [moreThanOne, nums]



for line in range(len(ratios)):
    for value in range(len(ratios[line])):
        if ratios[line][value] == "*" and find(line, value)[0]:
            nums = find(line, value)[1]
            total += int(nums[0]) * int(nums[1])

print(total)