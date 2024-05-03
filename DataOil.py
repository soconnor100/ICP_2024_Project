file = open("OilPlainTextData.txt", "r")
read = file.readlines()    #reads every line within the text file
year = []     #empy list for years
price = []    #empty list for prices

for line in read:
    if line[0] == " ":
        year.append(line[1:-1])    #the 1 is to avoid appending the \t and the -1 is to avoid appending the\n
    if line[0] == "\t":
        price.append(line[1:-1])

for i in range(len(price)):
    price[i] = float(price[i])    #converting the price data into floats

n = 12
yearly_price = [sum(price[i:i+n])/n for i in range(0, len(price), n)]  #finds yearly average price

#print(yearly_price)
#print(len(yearly_price))

print(year)
print(price)


