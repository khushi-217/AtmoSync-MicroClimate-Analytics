import csv
import time

print("=" * 40)
print("      ATMOSYNC CONSUMER")
print("=" * 40)

with open("sensor_data.csv", "r") as file:

    reader = csv.DictReader(file)

    count = 1

    for row in reader:


        print("\nReceiving data from Producer...")
        print(f"\nReceived Record {count}")
        print("-" * 30)

        print("Container_ID :", row["Container ID"])
        print("Commodity    :", row["Commodity"])
        print("Temperature  :", row["Temperature"])
        print("Humidity     :", row["Humidity"])
        print("Vibration    :", row["Vibration"])
        print("Battery      :", row["Battery"])
        print("Timestamp    :", row["Timestamp"])

        # Alerts
        if float(row["Temperature"]) > 6:
            print("⚠ ALERT: High Temperature")

        if int(row["Battery"]) < 85:
            print("⚠ ALERT: Low Battery")

        count += 1

        time.sleep(1)

print("\n========================================")
print("Consumer successfully processed all sensor records.")
print("========================================")