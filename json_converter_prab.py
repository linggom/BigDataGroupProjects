#convert to json

import csv
import json

csvfile = open('word_prab_score2.csv', 'r')
jsonfile = open('word_prab_score2.json', 'w')

#fieldnames = ("word","count","avg_score")
reader = csv.DictReader( csvfile)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')