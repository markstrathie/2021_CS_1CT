def dictionaryfx( file ):
    f = open( file )
    nextLine = f.readline()
    dictionary1 = {}
    while nextLine != "":
        bits = nextLine.split( sep="," )
        name = bits[0]
        address = bits[1]
        dictionary1[name] = address
    return dictionary1

dictionaryfx("names.txt")

print(dictionary1)
