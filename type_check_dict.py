person = {
"name" : "ganga",
"age" : 30,
"Location" : "Dublin"
}

print(type(person))
print(type(person['name']))
print(type(person["age"]))

# get values in dictionary by key
print("name" in person)

# change value in dictionary
person["age"] = 31
print(person["age"])

# use update method to add 
person.update({"age": 25})
print(person["age"])