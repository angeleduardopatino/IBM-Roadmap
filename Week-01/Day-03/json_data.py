import json

motor = {
    "name": "Motor_01",
    "voltage": 120,
    "current": 3,
    "power": 360,
    "status": "NORMAL"
}

with open("week-01/day-03/motor.json", "w") as file:
    json.dump(motor, file, indent=4)

print("JSON file saved")

with open("week-01/day-03/motor.json", "r") as file:
    loaded_motor = json.load(file)

print(loaded_motor)
print(loaded_motor["name"])
print(loaded_motor["power"])