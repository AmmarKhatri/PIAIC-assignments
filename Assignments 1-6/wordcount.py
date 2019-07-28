import os
import sys
d = {}
def print_words(fname):
    textfile = open(fname)
    listword = textfile.read()
    final = listword.lower()
    for c in final.split():
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    print(d)

def print_top(topfname):
    textfile = open(topfname)
    listword = textfile.read()
    final = listword.lower()
    for c in final.split():
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    Sortbyval=sorted(d.items(), key = lambda t : t[1], reverse=True)
    Top12 = Sortbyval[0:12]
    print(Top12)

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
    if len(sys.argv) != 3:
        print ('usage: ./wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]

    print(sys.argv[0])
    print(sys.argv[1])
    print(sys.argv[2])
    if option == '--count':
        print_words(filename)
        print(d)
    elif option == '--topcount':
        print_top(filename)
    else:
        print ('unknown option: ' + option)
        sys.exit(1)

if __name__ == '__main__':
    main()
