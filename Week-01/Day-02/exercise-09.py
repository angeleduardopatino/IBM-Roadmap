def calculate_resistance(voltage, current):
    resistance = voltage / current
    return resistance


try:
    voltage = float(input("Enter voltage: "))
    current = float(input("Enter current: "))

    resistance = calculate_resistance(voltage, current)

    print(f"The resistance is: {resistance} Ohms")

except ZeroDivisionError:
    print("Current cannot be zero")

except ValueError:
    print("Invalid number")