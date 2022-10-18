def printa():
    A = 3*10
    count = 0
    for i in range(A):
        count += 1
        print("A ", end="")
        if(count == 10):
            print()
            count = 0
printa()