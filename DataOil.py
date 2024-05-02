file = open("OilPlainTextData.txt", "r")
read = file.readlines()
year = []
price = []

for line in read:
    if line[0] == " ":
        year.append(line[1:-1])    #the 1 is to avoid appending the \t and the -1 is to avoid appending the\n
    if line[0] == "\t":
        price.append(line[1:-1])

print(year)
print(price)

"""        Jan = month[0]
        print(month)
        Feb = month[1]
        Mar = month[2]
        Apr = month[3]
        May = month[4]
        Jun = month[5]
        Jul = month[6]
        Aug = month[7]
        Sep = month[8]
        Oct = month[9]
        Nov = month[10]
        Dec = month[11]
"""
