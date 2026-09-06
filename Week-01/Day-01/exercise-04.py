battery_voltage = float(input("Inserte nivel de batería: "))

if battery_voltage < 10.5:
    print("CRITICAL")
elif battery_voltage < 12.0:
    print("LOW")
elif battery_voltage <= 14.4:
    print("NORMAL")
else:
    print("OVERVOLTAGE")

    