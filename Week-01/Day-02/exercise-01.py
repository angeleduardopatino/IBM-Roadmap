resistance = 10

for voltage in range(1, 6, 1):
    current = voltage / resistance
    print(f"Voltage: {voltage} V, Current: {current} A")