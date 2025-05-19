import requests
from bs4 import BeautifulSoup

def main():
    URL = "https://pokemondb.net/pokedex/game/red-blue-yellow"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')

    pokemon_links = []

    for a in soup.find_all('a', class_='ent-name'):
        pokemon_links.append(a['href'])

    with open('pokemon.txt', 'w', encoding='utf-8') as file:
        counter = 1
        for link in pokemon_links:
            data = extract(link)
            file.write(f"{counter},{','.join(data)}\n")
            counter+=1


def extract(url):

    URL = "https://pokemondb.net" + url
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    data = []
    type = []

    pokemon = soup.find('main').find('p').find('em').text.strip()
    data.append(pokemon)

    TYPE = soup.find('main').find('p')
    for t in TYPE:
        soup_item = BeautifulSoup(str(t), 'html.parser')
        if soup_item.a:
            type.append(soup_item.a.text)
    data.append('/'.join(type))

    dex = soup.find(class_="cell-med-text").text.strip()
    data.append(dex)

    return data


main()

















