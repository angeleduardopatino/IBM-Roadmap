voltage = float(input("Input the voltage in V and press Enter: "))

if voltage < 3.0:
    print("LOW")
elif voltage <= 5.0:
    print("NORMAL")
else:
    print("HIGH")