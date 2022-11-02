# get current working directory
import os
currentWorkingDirectory = os.getcwd()
print("Current Working Directory", currentWorkingDirectory)


#change directory to any path such as /var/logs 
import os
os.chdir('/var/logs')
print("Changed to Directory: ",os.getcwd())
os.chdir(currentWorkingDirectory)
print("Current Working Directory: ",os.getcwd())

# check directories and file list
import os
print(os.listdir())
print("List of Directories and files", os.listdir())


# create a new directory
if os.path.exists("my_new_sample_directory"):
    print("The folder already exists")
else:
    os.mkdir("my_new_sample_directory")
    print("The folder is created")

