from motor_utils import calculate_power, classify_power

voltage = 220
current = 5

power = calculate_power(voltage, current)
status = classify_power(power)

print(f"Power: {power} W")
print(f"Status: {status}")