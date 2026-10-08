from matplotlib.lines import Line2D
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

colours = [
    'blue', 'orange', 'green', 'red', 'purple', 'brown', 'magenta', 
    'black', 'darkgray', 'yellow', 'lime', 'cyan', 'gold', 'navy', 
    'maroon', 'olive', 'saddlebrown', 'darkviolet', 'salmon', 
    'turquoise', 'khaki', 'aquamarine'
]

# Mapping makes to sizes for the scatter plot
makeColourMap = dict(zip(makeUnique, colours))

# Assigning sizes to each make in the data
makeColoursLow = [makeColourMap.get(m, "grey") for m in make[lowMPG]]
makeColoursMidLow = [makeColourMap.get(m, "grey") for m in make[midLowMPG]]
makeColoursMidHigh = [makeColourMap.get(m, "grey") for m in make[midHighMPG]]
makeColoursHigh = [makeColourMap.get(m, "grey") for m in make[highMPG]]

# Scatter plot of horsepower vs price, with highway-mpg segments encoded by size and make encoded by colour
fig, ax = plt.subplots()

plot1 = ax.scatter(horsepower[lowMPG], price[lowMPG], c = makeColoursLow, s=10, alpha=0.5, label = makeUnique)
plot2 = ax.scatter(horsepower[midLowMPG], price[midLowMPG], c = makeColoursMidLow, s=30, alpha=0.5, label = makeUnique)
plot3 = ax.scatter(horsepower[midHighMPG], price[midHighMPG], c = makeColoursMidHigh, s=60, alpha=0.5, label = makeUnique)
plot4 = ax.scatter(horsepower[highMPG], price[highMPG], c = makeColoursHigh, s=80, alpha=0.5, label = makeUnique)

# Legend for highway-mpg segments
legend1 = ax.legend(handles = [plot1, plot2, plot3, plot4], loc = "upper right", bbox_to_anchor=(1.1, 1.1), title="Highway-MPG Segments", labels=["<20", "20-30", "30-40", ">40"])
ax.add_artist(legend1)

# Legend for car makes
makeHandles = [Line2D([0], [0], marker = "o", color = "w", markerfacecolor = colour, markersize = 10, label = make) for make, colour in makeColourMap.items()]
legend2 = ax.legend(handles = makeHandles, loc = "upper center", bbox_to_anchor=(0.5, -0.15), title="Car Makes", ncol = 5)

plt.xlabel("Horsepower")
plt.ylabel("Price")
plt.title("Horsepower vs Price with Highway-MPG encoded in size and Make encoded in colour")
plt.tight_layout()
plt.show()

# PART C: Encode as much of the dataset as possible
