import json


motors = [
    {
        "name": "Motor_01",
        "voltage": 120,
        "current": 3
    },
    {
        "name": "Motor_02",
        "voltage": 220,
        "current": 5
    },
    {
        "name": "Motor_03",
        "voltage": 110,
        "current": 2
    }
]

def classify_power(power):
    if power > 500:
       return "HIGH"     
    else:
        return "NORMAL"

for motor in motors:
    power = motor["voltage"] * motor["current"]
    status = classify_power(power)

    motor["power"] = power
    motor["status"] = status


with open("week-01/day-03/motors.json", "w") as file:
    json.dump(motors, file, indent=4)
print("JSON file saved")

with open("week-01/day-03/motors.json", "r") as file:
 loaded_motors = json.load(file)      

for motor in loaded_motors:
 if motor["status"] == "HIGH":  
  print(f"{motor['name']} -> {motor['power']} W")