red = 12
green = 13
blue = 14

games = None
sum = 0

with open("cubeConundrum.txt", 'r') as f:
    games = f.read().split("\n")
    f.close()

for i in range(len(games)):
    works = True
    id = int(games[i].split(":")[0].replace("Game ", ""))
    rounds = games[i].split(":")[1].split(";")
    """
    values = []
    for r in rounds:
        for v in r.split(","):
            values.append(v)
    """
    for round in rounds:
        values = round.split(",")
        for value in values:
            if "blue" in value:
                if int(value.replace(" blue", "")) > blue:
                    works = False
                    break
            elif "green" in value:
                if int(value.replace(" green", "")) > green:
                    works = False
                    break
            else:
                if int(value.replace(" red", "")) > red:
                    works = False
                    break
        if works == False:
            break
    if works == True:
        sum += id
print(sum)