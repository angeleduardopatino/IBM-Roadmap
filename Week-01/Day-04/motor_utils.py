def calculate_power(voltage, current):
    power = voltage * current
    return power


def classify_power(power):
    if power > 500:
        return "HIGH"
    else:
        return "NORMAL"

def is_high_power(status):
     if status == "HIGH":
         return True
     else:
         return False
            