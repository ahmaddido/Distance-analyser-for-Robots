from func import total_measurments, minimum_measurment, maximum_measurment, average_measurment, decision

measurments = []
#classifer = {}
#danger_readings = []
#warning_readings = []
#safe_readings = []

d = 0
w = 0
s = 0
classifcation = {
    "DANGER": d,
    "WARNING": w,
    "SAFE": s,
}

def print_results():
    if len(measurments) > 0:
        #print(classifer)
        print(classifcation)
        print("Total number of measurements is:", total_number)
        print(f"Minimum is {minimum} cm and Maximum is {maximum} cm")
        print(f"Average is {average} cm")
        #print(f"Total danger readings: {total_danger} \n Total warning readings: {total_warning} \n Total safe readings: {total_safe}")
        print(info)
        
    else:
        print("NO DATA AVALIABLE")

while True:
    read = input("Enter your measurements in cm or type done to finsih:")
    if read == "done":
        break
    else:
        if read.isdigit() and float(read) >= 0:
            measurments.append(float(read))
        else:
            print("please enter a valid number")

# for i in measurments:
#     if i <= 20:
#         classifer[i] = "DANGER"
#         danger_readings.append(i)
#     elif i > 20 and i <= 50:
#         classifer[i] = "WARNING"
#         warning_readings.append(i)
#     else:
#         classifer[i] = "SAFE"
#         safe_readings.append(i)

for i in measurments:
    if i <= 20:
        d = d+1 
        classifcation.update({"DANGER": d})

    elif i > 20 and i <= 50:
        w = w+1 
        classifcation.update({"WARNING": w})
    else:
        s = s+1 
        classifcation.update({"SAFE": s})


total_number = total_measurments(measurments)
minimum = minimum_measurment(measurments)
maximum = maximum_measurment(measurments)
average = average_measurment(measurments)

#total_danger = len(danger_readings)
#total_warning = len(warning_readings)
#total_safe = len(safe_readings)
info = decision(classifcation)
print_results()