# Define a function
def my_hello_world_function():
    print("Hello my world")

# Calling a function
my_hello_world_function()


# Arbitrary Arguements, *args when we are not sure how many parameters will be there
def my_colors(*colors):
    print("The first color is " + colors[0])

my_colors("REd", "Green")
my_colors("1", "Green", "one")


# Use return statement to return a value from the function

def sum(a,b):
    return a + b
sumValue = sum(5,6)
print("The sum of the number is: ", sumValue)