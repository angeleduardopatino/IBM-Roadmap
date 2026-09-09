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

    if motor["status"] == "HIGH":
               print(f"{motor['name']} -> {power} W")

    #print(f"{motor['name']} -> Power: {power} W -> {status}")}



#print(motors)