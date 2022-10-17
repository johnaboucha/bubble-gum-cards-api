from urllib.request import urlopen
import csv
import codecs

SHEET_ID = '1g1E_k1V1VuHXCwT0sZUEMjg-4pUmUzaOkSkCOO5PkFc'
SHEET_NAME = 'cards'
url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'

cards = []
categories_all = []

res = urlopen(url)

csvfile = csv.reader(codecs.iterdecode(res, "utf-8"))

for index, row in enumerate(csvfile):
	if index == 0:
		continue
	cards.append({
			"id": index,
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
	categories_all.append(row[6])
categories = list(set(categories_all))
categories.sort()