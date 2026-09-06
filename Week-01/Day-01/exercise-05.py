voltage = float(input("Input the voltage in V and press Enter: "))
current = float(input("Input the current in A and press Enter: "))

power = voltage * current
resistance = voltage / current

print(f"the voltage is {voltage:.2f} V. ")
print(f"the current is {current:.2f} A.")
print(f"The power is {power:.2F} W.")
print(f"The resistance is {resistance:.2f} Ohm.")