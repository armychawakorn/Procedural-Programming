try:
    value = int(input("กรุณาใส่ตัวเลข: "))
except ValueError:
    print("คุณต้องใส่ตัวเลขเท่านั้น")
while (value % 7) != 0:
    print("ค่าที่คุณใส่มาไม่หารด้วย 7 ลงตัว")
    value = int(input("กรุณาใส่ตัวเลข: "))
print(f"คุณใส่ค่าถูกต้องแล้ว, ตัวเลขคือ {value}")