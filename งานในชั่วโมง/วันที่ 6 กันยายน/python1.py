key = 55
try:
    value = int(input("กรุณาใส่ตัวเลข: "))
except ValueError:
    print("คุณต้องใส่ตัวเลขเท่านั้น")
while value != key:
    if value > key:
        print("ค่าที่คุณใส่มามากกว่าค่าที่ต้องการ")
    else:
        print("ค่าที่คุณใส่มาน้อยกว่าค่าที่ต้องการ")
    value = int(input("กรุณาใส่ตัวเลข: "))
print(f"คุณใส่ค่าถูกต้องแล้ว, ตัวเลขคือ {value}")