# model_train.py
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

def generate_data(n=2000, random_state=42):
    np.random.seed(random_state)

    land_area = np.random.uniform(500, 5000, n)
    no_of_labour = np.random.randint(3, 40, n)
    labour_cost_per_day = np.random.uniform(200, 2000, n)
    work_efficiency = np.random.uniform(50, 300, n)

    cement_qty = land_area * np.random.uniform(0.04, 0.12, n)
    bricks_qty = land_area * np.random.uniform(40, 80, n)
    steel_qty = land_area * np.random.uniform(0.01, 0.05, n)

    cement_rate = np.random.uniform(4000, 6000, n)
    bricks_rate = np.random.uniform(6, 14, n)
    steel_rate = np.random.uniform(60000, 90000, n)

    material_cost = cement_qty * cement_rate + bricks_qty * bricks_rate + steel_qty * steel_rate

    days = land_area / (work_efficiency * no_of_labour) + np.random.uniform(1, 3, n)
    days = np.clip(days, 5, None)

    labour_total = no_of_labour * labour_cost_per_day * days
    misc = land_area * np.random.uniform(20, 150, n)

    total_cost = material_cost + labour_total + misc

    df = pd.DataFrame({
        "land_area": land_area,
        "no_of_labour": no_of_labour,
        "labour_cost_per_day": labour_cost_per_day,
        "work_efficiency": work_efficiency,
        "cement_qty": cement_qty,
        "bricks_qty": bricks_qty,
        "steel_qty": steel_qty,
        "cement_rate": cement_rate,
        "bricks_rate": bricks_rate,
        "steel_rate": steel_rate,
        "days": days,
        "total_cost": total_cost
    })

    return df

df = generate_data()

features = [
    "land_area","no_of_labour","labour_cost_per_day","work_efficiency",
    "cement_qty","bricks_qty","steel_qty","cement_rate","bricks_rate","steel_rate"
]

X = df[features]
y_cost = df["total_cost"]
y_days = df["days"]

model_cost = LinearRegression().fit(X, y_cost)
model_days = LinearRegression().fit(X, y_days)

joblib.dump({
    "model_cost": model_cost,
    "model_days": model_days,
    "features": features
}, "model.pkl")

print("Model saved as model.pkl")
