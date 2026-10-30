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
    if "DANGER" in valuss:
        return "decision: STOP"
    elif "WARNING" in valuss and "SAFE" in valuss:
        return "decision: SLOW"
    else:
        return "decision: MOVE"
    


