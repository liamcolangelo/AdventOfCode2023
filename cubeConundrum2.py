games = None
sum = 0

with open("cubeConundrum.txt", 'r') as f:
    games = f.read().split("\n")
    f.close()

for i in range(len(games)):
    red = 0
    blue = 0
    green = 0
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
                    blue = int(value.replace(" blue", ""))
            elif "green" in value:
                if int(value.replace(" green", "")) > green:
                    green = int(value.replace(" green", ""))
            else:
                if int(value.replace(" red", "")) > red:
                    red = int(value.replace(" red", ""))
    sum += red * blue * green
print(sum)