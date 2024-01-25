import csv
import re

def strip(png):
    pattern1 = re.compile("[1234567890][.]")
    pattern2 = re.compile("[1234567890][1234567890][.]")
    png = re.sub(pattern2,'',png)
    png = re.sub(pattern1,'',png)
    print(png)
    return png


with open("chess_games.csv", "r") as org, open("chess_games_edit.csv", "w", newline='') as new:
    writer = csv.writer(new)
    count = 0
    for row in csv.reader(org):
        if count > 0:
            if "bullet" not in row[0] and (int(row[6]) + int(row[7]))/2 > 1900 and '{' not in row[14] and "20." in row[14]:
                writer.writerow((row[3],row[10],row[12],row[13], strip(row[14])))
        if count == 0:
            writer.writerow((row[3],row[10],row[12],row[13],strip(row[14])))
        count+=1
