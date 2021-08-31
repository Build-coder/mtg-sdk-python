from mtgsdk import Card, Set
import _Card
import time


_file = open("deck.txt", "r")

def scan_deck(_file):

    player_deck = []

    for line in _file:

        # 'x' is easier to work with
        x = line

        _list = x.split(' ')

        card_number = _list[-1].strip('\n')
        card_name = x[x.find(' '):x.find(' (')].strip()
        set_name = x[x.find('('):x.find(')')].strip('(')

        set_name = str(set_name)

        query = Card.where(set=set_name, number=card_number)

        # print(query.__dict__)

        for card in query:
            player_deck.append(card)

    for _card in player_deck:
        print(_card.name)
        
    


        # list of all the cards in the set
        # cards = Card.where(set=set_name)

        
    # for _card in cards:
    #     print(_card.name)


        # match = check_match(card_name, set_name)

        # if match:
        #     image_url = get_image_url(card_name, set_name)
        #     _card = _Card(card_name, image_url)
        #     player_deck.append(_card)
        
            

def check_match(card_name, set_name):

    # list of all the cards in the set
    cards = Card.where(set=set_name).all()

    for card in cards:
        if card.name == card.name:
            return True
    return False


def get_image_url(card_name, set_name):

    # list of all the cards in the set
    cards = Card.where(set=set_name).all()

    for card in cards:
        if card.name == card.name:
            print(card.image_url)
            return card.image_url
    return None

scan_deck(_file)

_file.close()

# x = 

# cards = Card.where(set=x).all()

# for x in cards:
#     print(x.name + ' ' + x.image_url)