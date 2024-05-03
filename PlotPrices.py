import numpy as np
import matplotlib.pylab as plt

#This first section was just copied from DataOil file because I couldnt figure out how to import a specific list into this file
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
    price[i] = float(price[i])    #converting the price data into floats

n = 12
yearly_price = [sum(price[i:i+n])/n for i in range(0, len(price), n)]

#This next part is what is actually doing the plotting
plt.figure(figsize=(20,10))
years = list(range(1973,2023))
plt.plot(years, yearly_price)    #adds the years list and yearly price list to the plot


plt.xlabel('Year (From 1974-2023)', fontsize = 20)
plt.ylabel('Price (in U.S Dollars)', fontsize = 20)
plt.title('Average Yearly price of Crude Oil Barrel from 1974-2023', fontsize = 30)
plt.grid(True)    #just adds the grid to the background which makes it easier to see

plt.savefig("OilPrice1.png")

