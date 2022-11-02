# Normal module usage example
print("Normal module usage")

import custom_module_example
custom_module_example.greet_person("ganga1")

print("Using alias and accessing variable")
import custom_module_example as cme
a = cme.personExample["age"]
print(a)

# use dir() function to get all the variables and functions
print("Using dir() function to get all the variables and functions of custom_module_example")
import custom_module_example
x = dir(custom_module_example)
print(x)