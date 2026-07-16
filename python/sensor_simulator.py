import random
import time
import csv
from datetime import datetime
def generate_sensor_data(container_id):
    commodity = "Avocado"
    temperature = round(random.uniform(2.0, 8.0), 2)
    humidity = round(random.uniform(40.0, 70.0), 2)
    timestamp = datetime.now()
    vibration = random.randint(1, 15)
    battery = random.randint(80, 100)

    return [
        container_id,
        commodity,
        temperature,
        humidity,
        timestamp,
        vibration,
        battery
    ]
container_id = "ATM001"

commodity = "Avocado"
temperature = round(random.uniform(2.0, 8.0), 2)

humidity = round(random.uniform(40.0, 70.0), 2)

timestamp = datetime.now()
vibration = random.randint(1, 15)
battery = random.randint(80, 100)
# Save sensor data into CSV
with open("sensor_data.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Container ID",
        "Commodity",
        "Temperature",
        "Humidity",
        "Timestamp",
        "Vibration",
        "Battery"
    ])

    for i in range(2000):
        container_id = f"ATM{i+1:04d}"
        sensor = generate_sensor_data(container_id)
        writer.writerow(sensor)
print("2000 sensor records generated successfully!")
# Data validation checks
import os

if os.path.exists("sensor_data.csv"):
    print("Sensor data CSV created successfully!")

with open("sensor_data.csv", "r") as file:
    total_records = sum(1 for line in file) - 1  # excluding header

print("Total records generated:", total_records)

if total_records == 2000:
    print("Data validation passed: 2000 records available")
else:
    print("Data validation failed")

print("=" * 40)
print("        ATMOSYNC SENSOR REPORT")
print("=" * 40)

print("Simulation Completed Successfully")
print("Generated Records : 2000")
print("Dataset Loaded Successfully")

print()
print("------ SAMPLE SENSOR DATA ------")

print("Container ID :", container_id)

print("Commodity :", commodity)

print("Temperature :", temperature, "°C")

print("Humidity :", humidity, "%")

print("Timestamp :", timestamp)

print("Vibration :", vibration)

print("Battery :", battery, "%")
if temperature > 6:
    print("⚠ ALERT: High Temperature Detected!")

if battery < 85:
    print("⚠ ALERT: Low Battery Level!")

print("\nReading Avocado Dataset...\n")

with open("dataset/avocado.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    count = 0

    for row in reader:
        print(row)
        count += 1
        if count == 5:
            break








