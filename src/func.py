def total_measurments(list):
    total_number = len(list)
    return total_number
    
# def minimum_measurment(list):
#     minimum = min(list)
#     return minimum

# def maximum_measurment(list):
#     maximum = max(list)
#     return maximum

# def average_measurment(list):
#     average = sum(list) / len(list)
#     return average

def decision(dict):
    keyss = dict.keys()
    if "DANGER" in keyss:
        return "decision: STOP"
    elif "WARNING" in keyss:
        return "decision: SLOW"
    elif "SAFE" in keyss:
        return "decision: MOVE"
    else:
        pass
    
    
def minimum_measurment(list):
    if len(list) == 0:
        pass
    else:
        minimum = min(list)
        return minimum

def maximum_measurment(list):
    if len(list) == 0:
        pass
    else:
        maximum = max(list)
        return maximum

def average_measurment(list):
    if len(list) == 0:
        pass
    else:
        average = sum(list) / len(list)
        return average


