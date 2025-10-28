import pandas as pd

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data"
columns = ["buying", "maint", "doors", "persons", "lug_boot", "safety", "class"]
df = pd.read_csv(url, names=columns)

df.to_csv("car_evaluation.csv", index=False)
print("✅ Dataset descargado y guardado como car_evaluation.csv")
