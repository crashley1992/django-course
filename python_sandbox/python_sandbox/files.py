# Python has functions for creating, reading, updating, and deleting files.

# open a file
myFile = open('myfile.txt', 'w')

# get some info
print('Name: ', myFile.name)
print('Is Closed', myFile.closed)
print('Opening Mode ', myFile.mode)

# write to file
myFile.write('I love Python')
myFile.write(' and JavaScript')
myFile.close()

# a appends to already existing file, w will overwrite
myFile = open('myfile.txt', 'a')
myFile.write(' I also like PHP')
myFile.close()

# read from file
myFile = open('myfile.txt', 'r+')
# gives back first 10 characters. can adjust the numbers to get more letters
text = myFile.read(10)
print(text)



