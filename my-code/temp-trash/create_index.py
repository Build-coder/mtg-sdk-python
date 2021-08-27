"""
This program creates a txt file of all the cards in magic by name
and in order of their multiverse ID
"""

from mtgsdk import Card, Set

index = []

f = open("index.txt", "w")

count = 382835

f.write('Name' + ', ' + 'Image Url' + ', ' + 'Multiverse-ID' + '\n')

for x in range(10):
    card = Card.find(count)
    print(card.name)
    f.write(card.name + ', ' + card.image_url + ', ' + card.multiverse_id + '\n')
    count = count + 1

f.close()