#รับค่าอุณหภูมิของน้ำ
Temp = float(input("Enter the temperature of water: "))

#สถานะของน้ำ
stringoftemp = None

#เงื่อนไข
while(True):
    if Temp <= 0:
        stringoftemp = "Frozen"
    elif Temp <= 12:
        stringoftemp = "Cold"
    elif Temp <= 25:
        stringoftemp = "Warm"
    elif Temp <= 75:
        stringoftemp = "Hot"
    elif Temp <= 100:
        stringoftemp = "Very Hot"
    else:
        stringoftemp = "Burning"
    break

#แสดงผล
print("Temperature of water is", stringoftemp)