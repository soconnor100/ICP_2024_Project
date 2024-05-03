file = open("OilPlainTextData.txt", "r")
read = file.readlines()
year = []
price = []

for line in read:
    if line[0] == " ":
        year.append(line[1:-1])    #the 1 is to avoid appending the \t and the -1 is to avoid appending the\n
    if line[0] == "\t":
        price.append(line[1:-1])

for i in range(len(price)):
    price[i] = float(price[i])

print(year)
print(price)


