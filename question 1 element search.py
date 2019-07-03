def binarySearch (arr, l, r, x): 

	# Check base case 
	if r >= l: 

		mid =int( l + (r - l)/2)

		# If element is present at the middle itself 
		if arr[mid] == x: 
			return mid 
		
		# If element is smaller than mid, then it can only 
		# be present in left subarray 
		elif arr[mid] > x: 
			return binarySearch(arr, l, mid-1, x) 

		# Else the element can only be present in right subarray 
		else: 
			return binarySearch(arr, mid+1, r, x) 

	else: 
		# Element is not present in the array 
		return -1



# creating an empty list 
lst = [] 

# number of elemetns as input 
n = int(input("Enter number of elements : ")) 
print("enter the elements")
# iterating till the range 
for i in range(0, n): 
	ele = int(input()) 

	lst.append(ele) # adding the element
	
x=int(input("Enter the element you want to seach for : ")) 

# Function call 
result = binarySearch(lst, 0, len(lst)-1, x) 

if result != -1: 
	print("Element is present at index %d" % result)
else: 
	raise Exception("Element is not present in array")

