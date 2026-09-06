try:
    number = float(input("Enter a number: "))
    result = 10 / number
    print(result)

except ZeroDivisionError:
    print("Error: You cannot divide by zero.")

except ValueError:
    print("Error: You must enter a number")