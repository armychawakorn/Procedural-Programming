x = 30
y = 6
for i in range(0, 6):
    y -= 1
    x -= 5
    for i in range(y):
        print(x, " ", end="")
    print()