#convert to json

import csv
import json

csvfile = open('word_prab_score2.csv', 'r')
jsonfile = open('word_prab_score2.json', 'w')

#fieldnames = ("word","count","avg_score")
reader = csv.DictReader( csvfile)
json.dump('{\"name\": \"flare\",\"children\": [', jsonfile)
for row in reader:
    if int(row['size']) > 0 :
        json.dump(row, jsonfile)
        jsonfile.write(',\n')
json.dump(']}', jsonfile)
