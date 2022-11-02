#File read example
#Simple Read file example

from genericpath import samefile


f = open("sample_file.txt", "r")
print(f.read())
f.close()

# we can read file with specific encoding
f = open("sample_file.txt", mode='r', encoding='utf-8')
print(f.read())
f.close()

# read file if the file exists
import os
if os.path.exists("sample_file.txt"):
    print("Reading file when it is existing")
    f = open("sample_file.txt", "r")
    print(f.read())
    f.close()
else:
    print("The file does not exist")

# append file
f = open("sample_file2.txt", "a")
f.write("This the line added by python function \n")
f.close()

# file write mode example
f = open("sample_file2.txt", "w")
f.write("This is a line just overwritten the existing file")
f.close()
f = open("sample_file2.txt", "r")
print(f.read())
f.close()

# delete file if exisits
import os
if os.path.exists("sample_file2.txt"):
    os.remove("sample_file2.txt")
else:
    print("The file does not exist")

