temperature = float(input("Enter the temperature in Celsius: "))
if temperature < 0 or temperature > 40:
    print("DANGER: Temperature is out of safe range!")
else:
    print("SAFE: Temperature is within the safe range.")

