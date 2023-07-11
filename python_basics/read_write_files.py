
file_to_read = 'test_file.txt'

# readline() method reads line by line and return a string
with open(file_to_read, 'r', encoding='utf-8', newline='') as testfile:
    line = testfile.readline()
    # while line is different from empty string, keep on reading
    while line != "":
        print(line)
        line = testfile.readline()

print("######################")

# readlines() method reads all the lines, and each line is stored in a list
with open(file_to_read, 'r', encoding='utf-8', newline='') as testfile:
    for line in testfile.readlines():
        print(line)
