# This program gives example about various list operation..
#Syntax : list[start: end: step]

myList = [8, 9, 3, 4, 5, 6, 7, 1, 2]
#index    0, 1, 2, 3, 4, 5, 6, 7, 8

#List Slicing
print('Original List:',myList)
print('First Element :',myList[0])	# prints 0th element of list
print('Element at 2nd Index position:',myList[2])
print('Element from 0th to 4th index',myList[0 : 5])
print('Element at index -7',myList[-7])

# Append an element to a list
myList.append(10)
print('Appended List:',myList)

# to find index of particular element
print('Index of element\'6\':',myList.index(6))

# To sort the list
myList.sort()

# To pop last element
print('Popped element :',myList.pop())

#To remove particular element
myList.remove(6)
print('After removing \'6\':',myList)

# insert an element at specified Index
myList.insert(5, 6)
print('Inserting \'6\'at 5th index:',myList)

myList.append(1)

# To count number of occurences of element in list
print('No of occurences of \'1\':',myList.count(1))

# to extend a list that is insert multiple elements at once at the end of the list
myList.extend([11,0])
print('Extending list :',myList)

# To reverse a list
myList.reverse()
print('Reversed list :',myList)