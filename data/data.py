import csv

card_file = "data/cards.csv"
manufacturer_file = "data/manufacturers.csv"
players_file = "data/players.csv"
teams_file = "teams.csv"

fields = []
cards = []
manufacturers = []
players = []
teams = []



with open(card_file, 'r') as csvfile:
	csvreader = csv.reader(csvfile)

	fields = next(csvreader)

	counter = 0

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

with open(manufacturer_file, 'r') as csvfile:
	csvreader = csv.reader(csvfile)

	fields = next(csvreader)

	counter = 0
	
	for row in csvreader:
		counter += 1
		manufacturers.append({
			"id": counter,
			"name": row[0],
			"year_founded": row[1],
			"year_defuct": row[2],
			"fate": row[3],
			"headquarters": row[4]
		})