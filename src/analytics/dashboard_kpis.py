import pandas as pd
from pathlib import Path

project_root = Path(__file__).resolve().parents[2]

readings = pd.read_csv(
    project_root / "data" / "cleaned_sensor_readings.csv"
)

risk = pd.read_csv(
    project_root / "data" / "shipment_risk_report.csv"
)

kpis = {
    "total_shipments": risk["shipment_id"].nunique(),
    "total_sensor_readings": len(readings),
    "high_risk_shipments": (risk["risk_level"] == "High").sum(),
    "average_temperature": round(readings["temperature_c"].mean(), 2)
}

kpi_df = pd.DataFrame(
    list(kpis.items()),
    columns=["metric", "value"]
)

output_file = project_root / "data" / "dashboard_kpis.csv"
kpi_df.to_csv(output_file, index=False)

print(kpi_df)
print("\nDashboard KPIs saved:", output_file)