temperatures = []

for i in range(5):
    temp = float(input(f"Enter temperature {i + 1}: "))
    temperatures.append(temp)

average_temp = sum(temperatures) / len(temperatures)

print(f"Measuremets: {temperatures}")
print(f"Minimum temperature: {min(temperatures)}")
print(f"Maximum temperature: {max(temperatures)}")
print(f"Average temperature: {average_temp:.2f}")