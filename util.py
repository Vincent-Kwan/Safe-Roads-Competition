from math import trunc

def truncate(number, digits = 3) -> float:
    stepper = 10.0 ** digits
    return trunc(stepper * number) / stepper