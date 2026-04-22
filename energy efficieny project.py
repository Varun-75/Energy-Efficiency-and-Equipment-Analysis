import pandas as pd
import numpy as np

np.random.seed(42)

time_range = pd.date_range(start="2025-01-01", periods=24*30, freq="h")

equipment = ["Motor-101", "Pump-202", "Compressor-303"]

data = []

for eq in equipment:
    base_efficiency = np.random.uniform(0.85, 0.95)
    
    for t in time_range:
        hour = t.hour
        
    
        load = 60 + 30 * np.sin((hour / 24) * 2 * np.pi)  
        load += np.random.normal(0, 5)
        load = np.clip(load, 40, 100)
        
        days_passed = (t - time_range[0]).days
        efficiency = base_efficiency - (days_passed * 0.0005)
    
        voltage = np.random.uniform(380, 440)
        

        current = load * np.random.uniform(0.8, 1.2)
        
        power = voltage * current * efficiency / 1000  
        
        temperature = 30 + 0.6 * load + np.random.normal(0, 2)
        
        downtime = 0
        if temperature > 85 and load > 90:
            if np.random.rand() > 0.7:  
                downtime = np.random.randint(5, 60)
        
        data.append([
            t, eq, round(load, 2), round(power, 2),
            round(voltage, 2), round(current, 2),
            round(temperature, 2), downtime
        ])
df = pd.DataFrame(data, columns=[
    "Timestamp", "Equipment", "Load (%)", "Power (kW)",
    "Voltage (V)", "Current (A)", "Temperature (C)", "Downtime (min)"
])

df.to_csv(r"C:\Users\prasa\OneDrive\Desktop\energy_equipment_data.csv", index=False)

print("Dataset generated successfully!")

energy_by_eq = df.groupby("Equipment")["Power (kW)"].sum().sort_values(ascending=False)
print(energy_by_eq)

df["Hour"] = pd.to_datetime(df["Timestamp"]).dt.hour

peak_load = df.groupby("Hour")["Load (%)"].mean()
print(peak_load)


correlation = df[["Load (%)", "Temperature (C)"]].corr()
print(correlation)

downtime_eq = df.groupby("Equipment")["Downtime (min)"].sum()
print(downtime_eq)


import matplotlib.pyplot as plt

energy_by_eq.plot(kind='bar')
plt.title("Energy Consumption by Equipment")
plt.show()


import matplotlib.pyplot as plt

energy_by_eq.plot(kind='bar')
plt.title("Energy Consumption by Equipment")
plt.show()

import pandas as pd

df = pd.read_csv("energy_equipment_data.csv")

df["Timestamp"] = pd.to_datetime(df["Timestamp"])

df["Hour"] = df["Timestamp"].dt.hour
df["Day"] = df["Timestamp"].dt.day

energy_by_eq = df.groupby("Equipment")["Power (kW)"].sum().sort_values(ascending=False)
print(energy_by_eq)

load_by_hour = df.groupby("Hour")["Load (%)"].mean()
print(load_by_hour)

downtime_by_eq = df.groupby("Equipment")["Downtime (min)"].sum().sort_values(ascending=False)
print(downtime_by_eq)

correlation = df[["Load (%)", "Temperature (C)", "Power (kW)"]].corr()
print(correlation)


high_risk = df[(df["Temperature (C)"] > 80) & (df["Load (%)"] > 85)]
print("High-risk instances:", len(high_risk))

import matplotlib.pyplot as plt

energy_by_eq.plot(kind='bar')
plt.title("Total Energy Consumption by Equipment")
plt.ylabel("Energy (kW)")
plt.show()

load_by_hour.plot()
plt.title("Average Load by Hour")
plt.xlabel("Hour")
plt.ylabel("Load (%)")
plt.show()

downtime_by_eq.plot(kind='bar')
plt.title("Downtime by Equipment")
plt.ylabel("Minutes")
plt.show()

cost_per_kwh = 8  
df["Cost"] = df["Power (kW)"] * cost_per_kwh

total_cost = df.groupby("Equipment")["Cost"].sum()
print(total_cost)
