import pandas as pd

column_names = [
    "sepal_length_cm",
    "sepal_width_cm",
    "petal_length_cm",
    "petal_width_cm",
    "species"
]

iris = pd.read_csv(
    "Week-05/iris.csv",
    header=None,
    names=column_names
)

print(iris.head())
print("Dataset shape:", iris.shape)
print("Records per species:")
print(iris["species"].value_counts())
print("Average petal measurements by species:")
print(
    iris.groupby("species")[["petal_length_cm", "petal_width_cm"]]
    .mean()
)
print("Plants with petal length above 5 cm:")
print(iris[iris["petal_length_cm"] > 5.0].head())
print("Five longest petals:")
print(iris.sort_values(by="petal_length_cm", ascending=False).head())
print("Summary of measurements:")
print(iris.describe())

print("Missing values per column:")
print(iris.isnull().sum())