from func import total_measurments, minimum_measurment, maximum_measurment, average_measurment

measurments = []
classifer = {}

while True:
    read = input("Enter your measurements in cm or type done to finsih:")
    if read == "done":
        break
    else:
        if read.isdigit() and int(read) >= 0:
            measurments.append(int(read))
        else:
            print("please enter a valid number")

for i in measurments:
    if i < 20:
        classifer[i] = "DANGER"
    elif i >= 20 and i < 50:
        classifer[i] = "WARNING"
    else:
        classifer[i] = "SAFE"

total_number = total_measurments(measurments)
minimum = minimum_measurment(measurments)
maximum = maximum_measurment(measurments)
average = average_measurment(measurments)



print(classifer)
print("Total number of measurements is:", total_number)
print(f"Minimum is {minimum} cm")
print(f"Maximum is {maximum} cm")
print(f"Average is {average} cm")
