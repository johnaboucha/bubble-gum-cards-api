import csv

card_file = "data/cards.csv"
manufacturer_file = "data/manufacturers.csv"
players_file = "data/players.csv"
teams_file = "data/teams.csv"

fields = []
cards = []
manufacturers = []
players = []
teams = []


#
#  CARDS
#
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

#
#  MANUFACTURERS
#
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
			"headquarters": row[4],
			"website": row[5],
			"revenue": row[6],
			"employees": row[7],
			"address": row[8]
		})

#
#  PLAYERS
#
with open(players_file, 'r') as csvfile:
	csvreader = csv.reader(csvfile)

	fields = next(csvreader)

	counter = 0
	
	for row in csvreader:
		counter += 1
		players.append({
			"id": counter,
			"first_name": row[0],
			"last_name": row[1],
			"position": row[2],
			"birth_date": row[3],
			"death_date": row[4],
			"throws": row[5],
			"bats": row[6],
			"height": row[7],
			"weight": row[8]
		})

#
#  TEAMS
#
with open(teams_file, 'r') as csvfile:
	csvreader = csv.reader(csvfile)

	fields = next(csvreader)

	counter = 0
	
	for row in csvreader:
		counter += 1
		teams.append({
			"id": counter,
			"location": row[0],
			"name": row[1],
			"league": row[2],
			"league_level": row[3],
			"year_established": row[4],
			"year_defunct": row[5],
		})