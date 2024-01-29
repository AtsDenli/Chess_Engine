import csv

with open("chess_games_edit.csv", 'r') as file:
    reader = csv.reader(file)
    counter = 0
    for row in reader:
        counter += 1
    print(counter)