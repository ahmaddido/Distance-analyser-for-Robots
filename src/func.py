def total_measurments(list):
    total_number = len(list)
    return total_number
    
def minimum_measurment(list):
    minimum = min(list)
    return minimum

def maximum_measurment(list):
    maximum = max(list)
    return maximum

def average_measurment(list):
    average = sum(list) / len(list)
    return average

def decision(dict):
    valuss = dict.values()
    for value in valuss:
        if value == "DANGER":
            print("Recommended: STOPPING")
        elif value == "WARNING":
            print("Recommended: SLOWING")
        else:
            print("Recommended: CONTINUE MOVING")
    return value