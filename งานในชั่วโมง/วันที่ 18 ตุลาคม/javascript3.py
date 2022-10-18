#รับค่าN
N = int(input("Enter your N: "))
Fact = 1
Ctrl = 1

#while loop
while Ctrl <= N:
    Fact = Fact * Ctrl
    Ctrl = Ctrl + 1

#แสดงผล
print(f"Factorial = {Fact}")