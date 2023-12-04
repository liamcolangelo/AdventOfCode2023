cards = ""
with open("scratchcards.txt", 'r') as f:
    cards = f.read()
    f.close()

cards = cards.split("\n")
winnings = []
numbers = []
for i in range(len(cards)):
    winnings.append(cards[i].split("|")[0])
    print(cards[i])
    numbers.append(cards[i].split("|")[1].split(" "))

for i in range(len(numbers)):
    try:
        while True:
            numbers[i].remove("")
    except:
        pass

for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        numbers[i][j] = int(numbers[i][j])


for i in range(len(winnings)):
    winnings[i] = winnings[i].split(":")
    winnings[i] = winnings[i].remove(winnings[i][0])
    winnings[i] = winnings[i].split(" ")
    try:
        while True:
            winnings[i] = winnings[i].remove("")
    except:
        pass
    
for i in range(len(winnings)):
    for j in range(len(winnings[i])):
        winnings[i][j] = int(winnings[i][j])

print(winnings)