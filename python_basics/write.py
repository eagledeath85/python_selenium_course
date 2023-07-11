
# read the file and store all the lines in list
# reverse the list
# write the list back to the file

with open('test_file.txt', 'r', encoding='utf-8', newline='') as reader:
    content = reader.readlines()    # hold all the content of test_file.txt in a list named content
    reversed_content = reversed(content)
    with open('test_file.txt', 'w', encoding='utf-8', newline='') as writer:
        for element in reversed_content:
            writer.write(element)