treb = ""
numbers = "1234567890"
textnumbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0"
}

with open("trebuchet.txt", 'r') as f:
    treb = f.read()

treb = treb.split("\n")

firsts = []
lasts = []

for i in range(len(treb)):
    first = treb[i]
    for j in range(len(treb[i])):
        string = first[:j]
        for key in textnumbers:
            string = string.replace(key, textnumbers[key])
        first = string + first[j:]

    for j in range(len(first)):
        if first[j] in numbers:
            firsts.append(first[j])
            break

for i in range(len(treb)):
    last = treb[i]
    for j in range(len(last) - 1, -1, -1):
        string = last[j:]
        for key in textnumbers:
            string = string.replace(key, textnumbers[key])
        last = last[:j] + string
    for j in range(len(last) - 1, -1, -1):
        if last[j] in numbers:
            lasts.append(last[j])
            break

all = []
for i in range(len(firsts)):
    all.append(int(firsts[i] + lasts[i]))
    print(str(i) + ": " + firsts[i] + lasts[i])

print(sum(all))

