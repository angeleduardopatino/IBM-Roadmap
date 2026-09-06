def greet(name):
    print(f"Hello {name}")

def calculate_power(voltage,current):
    power = voltage * current
    return power
    print("Finished")

result = calculate_power(float(input("Enter voltage: ")), float(input("Enter current: ")))
print(f"The power is: {result} Watts")

if result > 50:
    print("High power")
else:
    print("Normal power")
    