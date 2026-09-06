voltage = float(input("Enter the voltage (in volts): "))
current = float(input("Enter the current (in amperes): "))
power = voltage * current
resistance = voltage / current
print("Voltage:", voltage, "V")
print("Type of voltage variable:", type(voltage))
print("Current:", current, "A")
print("Type of current variable: ", type(current))
print("Power:", power, "W")
print("Type of power variable: ", type(power))
print("Resistance:", resistance, "Ω")
print("Type of resistance variable: ", type(resistance))
