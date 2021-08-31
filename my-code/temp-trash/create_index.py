"""
This program creates a txt file of all the cards in magic by name
and in order of their multiverse ID
"""

from mtgsdk import Card, Set
import time

index = []

def create_index_by_multi_id():

    f = open("index.txt", "w")

    count = 417574

    f.write('Name' + ', ' + 'Image Url' + ', ' + 'Multiverse-ID' + '\n')

    for x in range(1000):
        card = Card.find(count)
        print(card.name)
        f.write(card.name + ', ' + card.image_url + ', ' + card.multiverse_id + '\n')
        count = count + 1
        time.sleep(3)

    f.close()

def create_index_by_set():

    sets = ['kld','xln','rix','dom','m19','grn','rna','war','m20','eld','thb','iko','m21','znc']
    # sets = ['kld']

    f = open("index.txt", "w")

    for _set in sets:

        query = Card.where(code=_set)
        for card in query:

            try: 
                f.write(card.name + ',  ' + card.image_url + '\n')

            except:
                print(card.name + ' does not have an image url stored')

if __name__ == '__main__':
    create_index_by_set()