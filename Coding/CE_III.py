from search import linearSearch

array = [5, 7, 8, 4, 3, 19, 34]
print("\nGiven array: {} \n".format(array))
print("Test Case 1")
target = 8
print("Target = {}".format(target))
print("Target Index = {} \n".format(linearSearch(array, target)))
	
print("Test Case 2")
target = 3
print("Target = {}".format(target))
print("Target Index = {} \n".format(linearSearch(array, target)))

print("Test Case 3")
target = 5
print("Target = {}".format(target))
print("Target Index = {} \n".format(linearSearch(array, target)))

print("Test Case 4")
target = 34
print("Target = {}".format(target))
print("Target Index = {} \n".format(linearSearch(array, target)))