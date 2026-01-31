import os
import pandas as pd
import matplotlib.pyplot as plt
from fredapi import Fred

# Get API Key
FRED_API_KEY = os.getenv("FRED_API_KEY")

if not FRED_API_KEY:
    raise ValueError("Missing FRED_API_KEY. Set it in Terminal first.")

fred = Fred(api_key=FRED_API_KEY)

# Get CPI data
cpi = fred.get_series("CPIAUCSL")

# Format data
cpi = cpi.to_frame("CPI").reset_index()
cpi.columns = ["date", "CPI"]
cpi["date"] = pd.to_datetime(cpi["date"])
cpi = cpi.sort_values("date")

# Inflation
cpi["YoY"] = cpi["CPI"].pct_change(12) * 100
cpi["MoM"] = cpi["CPI"].pct_change() * 100

recent = cpi[cpi["date"] >= "2015-01-01"]

# Plot YoY
plt.figure()
plt.plot(recent["date"], recent["YoY"])
plt.title("US Inflation (YoY %)")
plt.xlabel("Year")
plt.ylabel("Percent")
plt.tight_layout()
plt.savefig("inflation_yoy.png")

# Plot CPI
plt.figure()
plt.plot(recent["date"], recent["CPI"])
plt.title("Consumer Price Index")
plt.xlabel("Year")
plt.ylabel("Index")
plt.tight_layout()
plt.savefig("cpi_level.png")

# Latest
latest = recent.dropna().iloc[-1]

print("Latest Data")
print("Date:", latest["date"].date())
print(f"YoY Inflation: {latest['YoY']:.2f}%")
print(f"MoM Inflation: {latest['MoM']:.2f}%")

# Save
recent.to_csv("inflation_data.csv", index=False)

print("Files created.")
