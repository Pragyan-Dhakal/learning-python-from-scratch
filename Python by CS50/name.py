import sys

try:
    print("Hello,",sys.argv[1])

except IndexError:
    print("After a file name type your name and the first name will be display.")