'''
This file creates a list comprised of dictionaries,
each dictionary containing the card name and image_url
'''

def _dict():    
    _file = open("index.txt", "r")
    index = []

    for line in _file:
        _list = line.split(',')
        card_dict = { 'name' :_list[0], 'image_url' : _list[1] }
        index.append(card_dict)

    return index

    _file.close()

if __name__ == '__main__':
    _dict()