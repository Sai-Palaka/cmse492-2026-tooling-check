import polars as pl

# Create a simple Polars DataFrame
df = pl.DataFrame({
    "x": [1, 2, 3, 4, 5],
    "y": [10, 20, 30, 40, 50]
})

# Use one Polars function
print(df)
print("Mean of y:", df["y"].mean())
