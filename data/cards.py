import csv

file = "data/cards.csv"

fields = []
cards = []

counter = 0

with open(file, 'r') as csvfile:
	csvreader = csv.reader(csvfile)

	fields = next(csvreader)

	for row in csvreader:
		counter += 1
		cards.append({
			"id": counter,
			"year": int(row[0]),
			"manufacturer": row[1],
			"player": row[2],
			"series": row[3],
			"number": row[4],
			"description": row[5],
			"category": row[6],
			"parallel": row[7],
			"image": row[8]
		})
	print(len(cards))
