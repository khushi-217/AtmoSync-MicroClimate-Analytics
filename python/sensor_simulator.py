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

print("------ ATMOSYNC SENSOR DATA ------")

print("Container ID :", container_id)

print("Commodity :", commodity)

print("Temperature :", temperature, "°C")

print("Humidity :", humidity, "%")

print("Timestamp :", timestamp)

print("Vibration :", vibration)

print("Battery :", battery, "%")

print("\nReading Avocado Dataset...\n")

with open("dataset/avocado.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    count = 0

    for row in reader:
        print(row)
        count += 1
        if count == 5:
            break








