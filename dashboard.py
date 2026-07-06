import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("urban_traffic.csv")

critical = df[df["congestion_score"] >= 80].sort_values(
    "congestion_score",
    ascending=False
)

print("EcoRoute Intelligence Dashboard Summary")
print("--------------------------------------")
print(f"Routes analyzed: {len(df)}")
print(f"Critical congestion routes: {len(critical)}")
print(f"Highest risk route: {critical.iloc[0]['route']} - {critical.iloc[0]['area']}")
print(
    f"Highest emissions route: "
    f"{df.sort_values('co2_emissions_kg_per_hour', ascending=False).iloc[0]['route']}"
)

print("\nCritical Routes:")
print(
    critical[
        ["route", "area", "congestion_score", "co2_emissions_kg_per_hour"]
    ]
)

plt.figure(figsize=(10, 6))
plt.bar(df["route"], df["congestion_score"])
plt.xticks(rotation=45, ha="right")
plt.title("EcoRoute Intelligence - Congestion Score by Route")
plt.xlabel("Route")
plt.ylabel("Congestion Score")
plt.tight_layout()
plt.savefig("dashboard_congestion.png")

plt.figure(figsize=(10, 6))
plt.bar(df["route"], df["co2_emissions_kg_per_hour"])
plt.xticks(rotation=45, ha="right")
plt.title("EcoRoute Intelligence - CO2 Emissions by Route")
plt.xlabel("Route")
plt.ylabel("CO2 kg/hour")
plt.tight_layout()
plt.savefig("dashboard_emissions.png")

print("\nDashboard images generated:")
print("- dashboard_congestion.png")
print("- dashboard_emissions.png")
