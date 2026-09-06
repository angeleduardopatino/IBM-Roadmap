while True:
    temperature = float(input("Enter temperature: "))

    if temperature > 40:
        print("DANGER")
        break

    print("Temperature is OK")

print("System stopped")