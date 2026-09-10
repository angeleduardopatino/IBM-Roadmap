import json
from motor_utils import calculate_power, classify_power, is_high_power
from data import motors


def main():
    for motor in motors:
        power = calculate_power(
            motor["voltage"],
            motor["current"]
        )

        status = classify_power(power)

        motor["power"] = power
        motor["status"] = status

        print(
            f"{motor['name']} -> "
            f"{power} W -> "
            f"{status}"
        )

    print("\nHIGH POWER MOTORS")
    for motor in motors:
     if is_high_power(motor["status"]):
        print(f"{motor['name']} -> {motor['power']} W")
    
    with open("week-01/day-04/motors_output.json", "w") as file:
     json.dump(motors, file, indent=4)

     print("\nData saved to motors_output.json")   

    



if __name__ == "__main__":
    main()

  