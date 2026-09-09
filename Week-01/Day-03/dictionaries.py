sensor = {
    "name": "temperature_sensor",
    "temperature": 32.5,
    "status": "SAFE"
}

print(sensor)
print(sensor["name"])
print(sensor["temperature"])
print(sensor["status"])

sensor["temperature"] = 45.0
sensor["status"] = "DANGER"
sensor["unit"] = "C"

print(sensor)

for key, value in sensor.items():
    print(f"{key}: {value}")