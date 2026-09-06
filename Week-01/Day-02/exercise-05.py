temperatures = []
safe_count = 0
danger_count = 0

for i in range(5):
    temp = float(input(f"Enter temperature {i + 1}: "))
    temperatures.append(temp)

for temp in temperatures:
    if temp > 40:
        print(f"Temperature {temp} -> DANGER")
        danger_count += 1
    else:
        print(f"Temperature {temp} -> SAFE")
        safe_count += 1

print(f"Safe measurements: {safe_count}")
print(f"Danger measurements: {danger_count}")
