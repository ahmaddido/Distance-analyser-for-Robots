measurments = []

while True:
    read = input("Enter your measurements in cm or type done to finsih:")
    if read == "done":
        break
    else:
        if read.isdigit() and int(read) > 0:
            measurments.append(int(read))
        else:
            print("please enter a valid number")

print(measurments)