#กำหนดค่า
sum1, sum2, sum3, k = 0, 0, 0, 1

#รับค่าN
N = int(input("Enter your N: "))

#while loop
while k <= N:
    sum1 = sum1 + k
    if(k % 2 == 0):
        sum2 = sum2 + k
    else:
        sum3 = sum3 + k
    k = k + 1

#แสดงผล
print(f"Sum1 = {sum1}")
print(f"Sum2 = {sum2}")
print(f"Sum3 = {sum3}")