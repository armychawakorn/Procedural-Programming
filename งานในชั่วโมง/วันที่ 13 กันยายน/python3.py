def printa(i,j, text):
    A = i*j
    count = 0
    for i in range(A):
        count += 1
        print(f"{text} ", end="")
        if(count == 4):
            print()
            count = 0
    return A

#------------------Main------------------

i = int(input("Enter number i: "))
j = int(input("Enter number j: "))
text = input("Enter text: ")
x = printa(i,j, text)
print(f"มีการจัดพิมพ์ซ้ำทั้งหมด {x} ครั้ง")