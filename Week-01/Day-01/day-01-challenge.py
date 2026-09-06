voltage = float(input("Input the voltage in V and press Enter: "))
current = float(input("Input the current in A and press Enter: "))

power = voltage * current
resistance = voltage / current

print(" -- ELECTRICAL SYSTEM REPORT -- ")

print(f"the voltage is {voltage:.2f} V.")
print(f"the current is {current:.2f} A.")
print(f"The power is {power:.2f} W.")
print(f"The resistance is {resistance:.2f} Ohm.")

if power < 100:
    print("LOW LOAD")
elif power <= 500:
    print("Status: NORMAL LOAD")
else: 
    print("Status: HIGH LOAD")