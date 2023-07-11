
# try/except block will not fail the code. Instead, if the try code is not successful, then we execute whatever is in the except block

# This syntax is used when we want to print a customized message when the except block is executed
try:
    with open('test_file.txt', 'r', encoding='utf-8', newline='') as reader:
        reader.read()
except FileNotFoundError: # FileNotFoundError is the error that would raised if we wouldn't have put the code in a try/except block
    print("File not found") # Print our customized message



# This syntax is used when we want to know what exception Python has thrown
try:
    with open('filelog.txt', 'r', encoding='utf-8', newline='') as reader:
        reader.read()
except Exception as e:
    print(e)


# finally keyword allows to run a block of code no matter hte result of the try/except block
try:
    with open('test_file.txt', 'r', encoding='utf-8', newline='') as reader:
        reader.read()
except Exception as e:
    print(e)
finally:
    print("Cleaning resources at the end")