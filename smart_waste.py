import random
import time
from datetime import datetime
import csv

# Bin simulation class
class SmartBin:
    def __init__(self, bin_id, location, max_height_cm=50):
        self.bin_id = bin_id
        self.location = location
        self.max_height = max_height_cm  # Height from sensor to bin base
        self.fill_level = 0  # cm of trash
        self.last_update = None

    def measure_fill_level(self):
        # Simulate ultrasonic sensor reading (trash height increases randomly)
        self.fill_level = random.randint(0, self.max_height)
        self.last_update = datetime.now()
        return self.fill_level

    def is_full(self, threshold=80):
        # Threshold in percentage (default: 80% full)
        fill_percent = (self.fill_level / self.max_height) * 100
        return fill_percent >= threshold

    def get_status(self):
        return {
            "id": self.bin_id,
            "location": self.location,
            "level_cm": self.fill_level,
            "full": self.is_full(),
            "timestamp": self.last_update
        }

# Simulate IoT transmission
def transmit_data(bin_status):
    print(f"📡 Transmitting Data from {bin_status['id']} at {bin_status['timestamp']}")
    # Here, you can replace with MQTT/HTTP POST logic
    with open("bin_data.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            bin_status['timestamp'],
            bin_status['id'],
            bin_status['location'],
            bin_status['level_cm'],
            "FULL" if bin_status['full'] else "OK"
        ])

# Actuator simulation
def alert_collection_vehicle(bin_info):
    if bin_info['full']:
        print(f"🚛 ALERT: Bin {bin_info['id']} is FULL at {bin_info['location']}! Schedule collection.")
    else:
        print(f"✅ Bin {bin_info['id']} is OK.")

# Main simulation loop
def main():
    bins = [
        SmartBin("BIN_01", "Sahid Nagar"),
        SmartBin("BIN_02", "Patia"),
        SmartBin("BIN_03", "Old Town"),
    ]

    print("🗑️ Smart Waste Monitoring System Started...\n")

    # Create CSV log file
    with open("bin_data.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Bin ID", "Location", "Level (cm)", "Status"])

    while True:
        for bin_unit in bins:
            bin_unit.measure_fill_level()
            status = bin_unit.get_status()
            transmit_data(status)
            alert_collection_vehicle(status)
            print("—" * 40)
        time.sleep(10)  # Run every 10 sec (can be changed)

if __name__ == "__main__":
    main()
