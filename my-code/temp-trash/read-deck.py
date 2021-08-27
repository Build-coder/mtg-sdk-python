import _Card

deck_file = open("deck.txt", "r")
index_file = open("index.txt", "r")

deck = []
index = []

for line in deck_file:
    # x is easier to work with
    x = line

    deck_card = x[x.find(' '):x.find(' (')].strip()

    deck.append(deck_card)


for line in index_file:
    # x is easier to work with
    x = line

    index_card = x[:x.find(',')].strip()

    index.append(index_card)

print(deck)
print(index)

for x in deck:
    print(x)
    for y in index:
        print(y)


deck_file.close()
index_file.close()


# num_list = [1, 2, 3]
# alpha_list = ['a', 'b', 'c']

# for number in num_list:
#     print(number)
#     for letter in alpha_list:
#         print(letter)