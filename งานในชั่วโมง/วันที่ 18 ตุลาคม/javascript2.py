#รับค่าN
N = int(input("Enter your N: "))
I = 1
SUM = 0

#while loop
while I <= N:
    SUM = SUM + I
    I = I + 2

#แสดงผล
print("Sum = ", SUM)