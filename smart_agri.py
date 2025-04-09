import time
import random
import csv
from datetime import datetime

# Mock functions for sensors (Replace with actual GPIO read code in real setup)
def read_soil_moisture():
    return random.randint(200, 800)  # simulate soil moisture

def read_temperature():
    return round(random.uniform(20, 40), 2)

def read_humidity():
    return round(random.uniform(40, 90), 2)

def read_rainfall():
    return random.choice([True, False])  # Simulated rainfall sensor

# Actuator control (replace print with actual GPIO control code)
def control_irrigation(pump_on):
    if pump_on:
        print("💧 Irrigation ON - Pump Activated")
    else:
        print("🛑 Irrigation OFF - Pump Deactivated")

# Data logger
def log_data(temp, humidity, soil, rain, irrigation):
    with open("sensor_data.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), temp, humidity, soil, rain, irrigation])

# Main loop
def main():
    print("🚜 Smart Agriculture System Started")
    while True:
        temperature = read_temperature()
        humidity = read_humidity()
        soil_moisture = read_soil_moisture()
        rainfall = read_rainfall()

        # Decision logic for irrigation
        # Assuming threshold soil moisture < 400 means dry
        if soil_moisture < 400 and not rainfall:
            control_irrigation(True)
            irrigation_status = "ON"
        else:
            control_irrigation(False)
            irrigation_status = "OFF"

        # Log the data
        log_data(temperature, humidity, soil_moisture, rainfall, irrigation_status)

        # Display for monitoring
        print(f"Temp: {temperature}°C, Humidity: {humidity}%, Soil: {soil_moisture}, Rain: {rainfall}, Irrigation: {irrigation_status}")

        # Run every 10 seconds
        time.sleep(10)
if __name__ == "__main__":
    # Create CSV headers if not exists
    with open("sensor_data.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Temperature", "Humidity", "Soil Moisture", "Rainfall", "Irrigation Status"])
    
    main()