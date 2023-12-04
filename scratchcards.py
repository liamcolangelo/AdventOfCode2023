cards = ""
with open("scratchcards.txt", 'r') as f:
    cards = f.read()
    f.close()

cards = cards.split("\n")
total = 0
winnings = []
numbers = []

# Formats the winnings and numbers into separate lists
for i in range(len(cards)):
    winnings.append(cards[i].split("|")[0])
    numbers.append(cards[i].split("|")[1].split(" "))


for i in range(len(numbers)):
    while "" in numbers[i]:
        numbers[i].remove("")

    for j in range(len(numbers[i])):
        numbers[i][j] = int(numbers[i][j])


for i in range(len(winnings)):
    winnings[i] = winnings[i].split(":")
    winnings[i] = winnings[i][1]
    winnings[i] = winnings[i].split(" ")
    while "" in winnings[i]:
        winnings[i].remove("")
    
for i in range(len(winnings)):
    for j in range(len(winnings[i])):
        winnings[i][j] = int(winnings[i][j])

for game in range(len(winnings)):
    matches = 0
    for num in range(len(winnings[game])):
        if winnings[game][num] in numbers[game]:
            matches += 1
    if matches != 0:
        total += 2 ** (matches - 1)
    matches = 0

print(total)