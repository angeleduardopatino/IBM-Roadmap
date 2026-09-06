def calculate_resistance(voltage, current):
    resistance = voltage / current
    return resistance
    
resistance = calculate_resistance(float(input("Enter voltage: ")), float(input("Enter current: ")))
print(f"The resistance is: {resistance} Ohms")