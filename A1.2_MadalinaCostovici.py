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

# Filtering highway-mpg values
lowMPG = highwayMPG < 20
midLowMPG = (highwayMPG >= 20) & (highwayMPG < 30)
midHighMPG = (highwayMPG >= 30) & (highwayMPG < 40)
highMPG = highwayMPG >= 40

# Scatter plot of horsepower vs price, with highway-mpg segments encoded by colour
plt.scatter(horsepower[lowMPG], price[lowMPG], c="red", alpha=0.5, label="<20")
plt.scatter(horsepower[midLowMPG], price[midLowMPG], c="gold", alpha=0.5, label="20-30")
plt.scatter(horsepower[midHighMPG], price[midHighMPG], c="dodgerblue", alpha=0.5, label="30-40")
plt.scatter(horsepower[highMPG], price[highMPG], c="green", alpha=0.5, label=">40") 
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

