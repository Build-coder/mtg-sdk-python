index_file = open("index.txt", "r")
index = []

for line in index_file:
    # x is easier to work with
    x = line

    index_card = x[:x.find(',')].strip()

    index.append(index_card)


# Python3 code to implement iterative Binary
# Search.

# It returns location of x in given array arr/index
# if present, else returns -1
def binarySearch(arr, l, r, x):

	while l <= r:

		mid = l + (r - l) // 2
		
		# Check if x is present at mid
		if arr[mid] == x:
			return mid

		# If x is greater, ignore left half
		elif arr[mid] < x:
			l = mid + 1

		# If x is smaller, ignore right half
		else:
			r = mid - 1
	
	# If we reach here, then the element
	# was not present
	return -1

# Driver Code
arr = [ 2, 3, 4, 10, 40 ]
x = 'Afterlife'

# Function call
result = binarySearch(index, 0, len(index)-1, x)

if result != -1:
	print ("Element is present at index % d" % result)
else:
	print ("Element is not present in array")
