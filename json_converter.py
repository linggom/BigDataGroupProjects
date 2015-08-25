#convert to json

import csv
import json

csvfile = open('word_jkw_score.csv', 'r')
jsonfile = open('word_jkw_score.json', 'w')

#fieldnames = ("word","count","avg_score")
reader = csv.DictReader( csvfile)
for row in reader:
    if int(row['size']) > 0:
        json.dump(row, jsonfile)
        jsonfile.write(',\n')
