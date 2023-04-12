import csv

with open('yoda-corpus.csv', newline='') as csvfile, open('yoda.txt', 'w') as txtfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['character'] == 'YODA':
            txtfile.write(row['text'] + '\n')