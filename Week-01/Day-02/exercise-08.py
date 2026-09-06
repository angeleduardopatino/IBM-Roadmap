def calculate_power(voltage,current):
    power = voltage * current
    return power

def clasify_power(power):

   if power > 50:
    return "High power"
   else:
    return "Normal power"

result = calculate_power(float(input("Enter voltage: ")), float(input("Enter current: ")))
print(f"The power is: {result} Watts")
print(f"The power status is: {clasify_power(result)}")



