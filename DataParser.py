import csv
id_name = {}
with open('pokemon.txt','r') as file:
    reader = csv.reader(file)
    for row in reader:
        id = row[0]
        name = row[1]
        id_name[id] = name

print(id_name)