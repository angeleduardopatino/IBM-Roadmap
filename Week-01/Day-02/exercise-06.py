temperatures = [20, 45, 32, 51, 18]
print("If you wanna win, you have to delete all temperatures in 10 attempts")
for i in range(10):
    temp = float(input(f"Enter temperature to delete {i + 1}: "))
    if temp in temperatures:
        temperatures.remove(temp)
        print(f"Temperature {temp} deleted successfully, you have {len(temperatures)} for delete")
    else:
        print(f"Temperature {temp} not found in the list.")

    if len(temperatures) == 0:
        print("Congratulations! You have deleted all temperatures.")
        break

if len(temperatures) > 0:
        print(f"You lose! You have {len(temperatures)}")