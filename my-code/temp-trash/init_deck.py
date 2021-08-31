from mtgsdk import Card, Set
import time

f = open("deck.txt", "r")
player_deck = []

for line in f:

    # 'x' is easier to work with
    x = line

    _list = x.split(' ')

    _number = _list[-1].strip('\n')
    _name = x[x.find(' '):x.find(' (')].strip()
    _set = str(x[x.find('('):x.find(')')].strip('('))

    # print(query.__dict__)

    query = Card.where(name=_name, code=_set, number=_number)

    for card in query:
        try:
            print(card.name + ', img_url: ' + card.image_url)
            player_deck.append(card)

        except:
            print(card.name + ' has no image url')

print()