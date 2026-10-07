import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load the data from the CSV file
data = pd.read_csv('cars.csv')

# Extracting relevant columns, converting to numeric and handling missing values
data["price"] = pd.to_numeric(data["price"], errors='coerce').fillna(0)
data["horsepower"] = pd.to_numeric(data["horsepower"], errors='coerce').fillna(0)
data["highway-mpg"] = pd.to_numeric(data["highway-mpg"], errors='coerce').fillna(0)

# Extracting data for manipulation
price = data["price"]
horsepower = data["horsepower"]
highwayMPG = data["highway-mpg"]
make = data["make"]

# PART A: Visualising the correlation between price, horsepower and fuel efficiency

# Filtering highway-mpg values
lowMPG = highwayMPG < 20
midLowMPG = (highwayMPG >= 20) & (highwayMPG < 30)
midHighMPG = (highwayMPG >= 30) & (highwayMPG < 40)
highMPG = highwayMPG >= 40

# Scatter plot of horsepower vs price, with highway-mpg segments encoded by colour
plt.scatter(horsepower[lowMPG], price[lowMPG], c="red", alpha=0.5, label="<20")
plt.scatter(horsepower[midLowMPG], price[midLowMPG], c="gold", alpha=0.5, label="20-30")
plt.scatter(horsepower[midHighMPG], price[midHighMPG], c="green", alpha=0.5, label="30-40")
plt.scatter(horsepower[highMPG], price[highMPG], c="dodgerblue", alpha=0.5, label=">40") 
plt.title("Horsepower vs Price with Highway-MPG encoded in colour")
plt.xlabel("Horsepower")
plt.ylabel("Price")
plt.legend(loc = "upper right", bbox_to_anchor=(1.1, 1.1), title="Highway-MPG Segments", labels=["<20", "20-30", "30-40", ">40"])
plt.show()

# Scatter plot of horsepower vs price, with highway-mpg segments encoded by brightness
plt.scatter(horsepower, price, c=highwayMPG, cmap='Blues', alpha=0.5)
plt.title("Horsepower vs Price with Highway-MPG encoded in brightness")
plt.xlabel("Horsepower")
plt.ylabel("Price")
plt.colorbar(label='Highway-MPG')
plt.show()

# Scatter plot of horsepower vs price, with highway-mpg segments encoded by size
plt.scatter(horsepower[lowMPG], price[lowMPG], color = "black", s=10, alpha=0.5)
plt.scatter(horsepower[midLowMPG], price[midLowMPG], color = "black", s=30, alpha=0.5)
plt.scatter(horsepower[midHighMPG], price[midHighMPG], color = "black", s=60, alpha=0.5)
plt.scatter(horsepower[highMPG], price[highMPG], color = "black", s=80, alpha=0.5)
plt.title("Horsepower vs Price with Highway-MPG encoded in size")
plt.xlabel("Horsepower")
plt.ylabel("Price")
plt.legend(loc = "upper right", bbox_to_anchor=(1.1, 1.1), title="Highway-MPG Segments", labels=["<20", "20-30", "30-40", ">40"])
plt.show()

# PART B: How primary stats vary across car makes

# Getting unique list of makes & sorting alphabetically
makeUnique = list(set(data["make"]))
makeUnique.sort()

sizes = [
    10, 20, 30, 40, 50, 
    60, 70, 80, 90, 100, 
    110, 120, 130, 140, 150, 
    160, 170, 180, 190, 200, 
    210, 220
]

# Mapping makes to sizes for the scatter plot
makeSizeMap = dict(zip(makeUnique, sizes))

# Assigning sizes to each make in the data
makeSizes = data["make"].map(makeSizeMap)

makeLabels = list(makeSizeMap.keys())

# Scatter plot of horsepower vs price, with highway-mpg segments encoded by colour and make encoded by size
plt.scatter(horsepower[lowMPG], price[lowMPG], c="red", s = makeSizes[lowMPG], alpha=0.5, label="<20")
plt.scatter(horsepower[midLowMPG], price[midLowMPG], c="gold", s = makeSizes[midLowMPG], alpha=0.5, label="20-30")
plt.scatter(horsepower[midHighMPG], price[midHighMPG], c="green", s = makeSizes[midHighMPG], alpha=0.5, label="30-40")
plt.scatter(horsepower[highMPG], price[highMPG], c="dodgerblue", s = makeSizes[highMPG], alpha=0.5, label=">40") 
plt.title("Horsepower vs Price with Highway-MPG encoded in colour and Make encoded in size")
plt.xlabel("Horsepower")
plt.ylabel("Price")
plt.legend(loc = "upper right", bbox_to_anchor=(1.1, 1.1), title="Highway-MPG Segments", labels=["<20", "20-30", "30-40", ">40", makeLabels])
plt.show()

# ^ Fix labels to show make labels too
