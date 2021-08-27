from mtgsdk import Card, Set
from create_dict import _dict

'''
Create list of card names from deck
'''

deck = []

deck_file = open("deck.txt", "r")

for line in deck_file:
    # x is easier to work with
    x = line

    deck_card = x[x.find(' '):x.find(' (')].strip()

    deck.append(deck_card)


'''
For each card in deck, find it's
counterpart in index
'''

# Python3 code to implement iterative Binary
# Search.

# It returns location of x in given array arr/index
# if present, else returns -1
def binarySearch(arr, l, r, x):

	while l <= r:

		mid = l + (r - l) // 2
		
		# Check if x is present at mid
		if arr[mid]['name'] == x:
			return mid

		# If x is greater, ignore left half
		elif arr[mid]['name'] < x:
			l = mid + 1

		# If x is smaller, ignore right half
		else:
			r = mid - 1
	
	# If we reach here, then the element
	# was not present
	return -1


# Driver Code

_index = _dict()

for _card in deck:
	x = _card

	# Function call
	result = binarySearch(_index, 0, len(_index)-1, x)

	if result != -1:
		print (x + " is present at index % d" % result + ' its img_url: ' + _index[result]['image_url'])
	else:
		print (x + " is not present in array")
