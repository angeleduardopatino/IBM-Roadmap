temperatures = [20, 22, 25, 28, 31]

print(temperatures)
print(type(temperatures))

print(temperatures[0])
print(temperatures[2])
print(temperatures[-1])

for temp in temperatures: 
    print(temp)

print(len(temperatures))  

temperatures[2] = 100

print(len(temperatures))

temperatures.append(35)
print(temperatures)