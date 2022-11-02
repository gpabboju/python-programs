simpleList = ["red", "green", "blue", 4, 5, 6]
print(simpleList)
print(type(simpleList))

#simpleList[1] = green type is str
print("simpleList[1] = ", simpleList[1])

print(type(simpleList[1]))

#simpleList[4] = 5 type is int
print("simpleList[4] = ", simpleList[4])

print(type(simpleList[4]))

# simpleList[0:3] = ['red', 'green', 'blue']
print("simpleList[0:3] = ", simpleList[0:3])

# simpleList[3:] = [4,5,6]
print("simpleList[3:] =", simpleList[3:])

# changing values in the list
simpleList[2] = 10
print("value is changed in the list: ", simpleList)

# last value of the list
print(simpleList[-1])

# we can add value to the list
simpleList.insert(6, "new value")
print(simpleList)

# remove a value from the list by item value
simpleList.remove("new value")
print("one item removed from list by value ", simpleList)

# remove a value from the list by index
simpleList.pop(2)
print("one item removed from list by value ", simpleList)
