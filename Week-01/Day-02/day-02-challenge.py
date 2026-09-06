temperatures = []
safe_count = 0
danger_count = 0

def classify_temperature(temperature):
    if temperature > 40:
       return "DANGER"     
    else:
        return "SAFE"
        
while len(temperatures) < 5:
  try:
    temp = float(input(f"Enter temperature {len(temperatures) + 1}: "))
   
    temperatures.append(temp)
    
  except ValueError:
    print("Invalid temperature")
    continue
 
average_temp = sum(temperatures) / len(temperatures)

for temp in temperatures:
  status = classify_temperature(temp)
  print(f"Temperature: {temp} C -> {status}")

  if status == "SAFE":
     safe_count += 1
  else:
     danger_count += 1
     

print(f"Minimum temperature: {min(temperatures)} C")
print(f"Maximum temperature: {max(temperatures)} C")
print(f"Average temperature: {average_temp:.2f} C")
print(f"Safe measurements: {safe_count}")
print(f"Danger measurements: {danger_count}")
