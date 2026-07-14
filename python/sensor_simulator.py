import random
import time
import csv
from datetime import datetime
container_id = "ATM001"
container_id = "ATM001"
commodity = "Avocado"
temperature = round(random.uniform(2.0, 8.0), 2)

humidity = round(random.uniform(40.0, 70.0), 2)

timestamp = datetime.now()
vibration = random.randint(1, 15)
battery = random.randint(80, 100)

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








