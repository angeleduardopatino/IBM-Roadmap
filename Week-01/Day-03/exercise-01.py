motor = {
    "name": "KAWA",
    "voltage": 50,
    "current": 2,
    "status":"SAFE"
    }

print(motor)
print(f"Motor: {motor['name']}")
print(f"Voltage: {motor['voltage']} V")
print(f"Current: {motor['current']} A")
print(f"Status: {motor['status']}")

motor["power"] = motor["voltage"] * motor["current"]

print(f"Power: {motor['power']} W")