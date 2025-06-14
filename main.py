import csv
import pokebase as pb
import requests
from PIL import Image




def get_names(filename):
    result = []
    with open(filename,'r') as file:
        reader = csv.reader(file)
        for row in reader:
            result.append(row[1])
            
    return result

def get_info(name):
    pokemon = pb.pokemon(name)
    details = {
        'name': pokemon.name,
        'id': pokemon.id,
        'height': pokemon.height,
        'weight': pokemon.weight,
        'types': [t.type.name for t in pokemon.types],
        'abilities': [a.ability.name for a in pokemon.abilities]
    }

    stats = {
        'hp': pokemon.stats[0].base_stat,
        'attack': pokemon.stats[1].base_stat,
        'defense': pokemon.stats[2].base_stat,
        'sp_attack': pokemon.stats[3].base_stat,
        'sp_defense': pokemon.stats[4].base_stat,
        'speed': pokemon.stats[5].base_stat
    }
    return details, stats

details = get_info('pikachu')[0]
stat = get_info('pikachu')[1]

def format_stats(stats):
    formatted = []
    for stat, value in stats.items():
        formatted.append(f"{stat.replace('_', ' ').title():10}  {value:3}")
    return "\n".join(formatted)

def format_details(details):
    formatted = []
    formatted.append(f"{'Name:':15} {details['name'].title()}")
    formatted.append(f"{'Dex Number:':15} {details['id']}")
    formatted.append(f"{'Height:':15} {details['height']}")
    formatted.append(f"{'Weight:':15} {details['weight']}")
    formatted.append(f"{'Types:':15} " + ", ".join(details['types']).title())
    formatted.append(f"{'Abilities:':15} " + ", ".join(details['abilities']).title())
    return "\n".join(formatted)

sprite_url = pb.pokemon('pikachu').sprites.front_default
print(f"Sprite URL: {sprite_url}")

def get_sprite(url):
    response = requests.get(url)
    if response.status_code == 200:
        with open('sprite.png', 'wb') as file:
            file.write(response.content)
        return Image.open('sprite.png')
    else:
        print(f"Failed to retrieve sprite: {response.status_code}")
        return None
    
sprite_image = get_sprite(sprite_url)
