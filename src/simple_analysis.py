import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create sample data
data = {
    "day": [1, 2, 3, 4, 5],
    "sales": [100, 120, 90, 150, 130],
    "customers": [10, 12, 9, 15, 13]
}

df = pd.DataFrame(data)

# Compute summary statistic
mean_sales = df["sales"].mean()
print("Mean sales:", mean_sales)

# Create a simple plot
plt.plot(df["day"], df["sales"])
plt.xlabel("Day")
plt.ylabel("Sales")
plt.title("Sales Over Time")
plt.show()
