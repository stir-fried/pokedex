import sqlite3

def main():
    dbConnection = sqlite3.connect('pokedex.db')
    dbCursor = dbConnection.cursor()

    dbConnection.execute("CREATE TABLE IF NOT EXISTS Pokemon (DexNum INTEGER, Name TEXT, Type TEXT, DexEntry TEXT)")

    pokemondata(dbCursor)

    dbConnection.commit()
    dbConnection.close()

def pokemondata(cursor):
    with open('pokemon.txt', 'r') as file:
        for line in file:
            if line.strip():
                parts = line.split(',')
                dex_num = parts[0].strip()
                name = parts[1].strip()
                type = parts[2].strip()
                dex_entry = ','.join(
                    parts[3:]).strip()  # Join the remaining parts as dex_entry
                cursor.execute(
                    "INSERT INTO Pokemon (DexNum, Name, Type, DexEntry) VALUES (?, ?, ?, ?)",
                    (int(dex_num), name, type, dex_entry))

main()