with open("high_score.txt") as file:
    hscore = file.read()

hscore = int(hscore)
print(hscore)