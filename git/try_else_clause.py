from fileinput import filename

try:
    f = open(filename, 'r')
except OSError:
    print("File could not be open for read")
else:
    print("Number of lines", sum(1 for line in f))
    f.close()