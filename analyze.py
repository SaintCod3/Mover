import json
import sys

listGames = sys.argv[2:]


found = []

with open('./DB/PSX.json', 'r') as file:
    data = json.load(file)

for listed in listGames:
	for obj in data:
		if 'Game' in obj and obj['Game'] == listed:
			print(f"Se encontró {obj['Game']} en PSX")
			found.append(listed)

