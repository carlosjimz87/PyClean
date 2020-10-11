def BAD_FILE_HANDLING():
    f = open('input.txt', 'r')

    file_contents = f.read()

    f.close()

    words = file_contents.split(' ')

    return len(words)


# using context manager
# use this every time you're manipulating resources
# that should be leaved in the same state their where found
# (files, databases, threads...)
def GOOD_FILE_HANDLING():
    with open('input.txt', 'r') as f:
        file_contents = f.read()

    words = file_contents.split(' ')

    return len(words)


# print(BAD_FILE_HANDLING())
print(GOOD_FILE_HANDLING())
