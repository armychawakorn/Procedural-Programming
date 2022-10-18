def printa(text):
    A = 3*10
    for i in range(A):
        print(f"{text} ", end="")
        if((A % 10) != 0):
            print()
            count = 0
text = input("Enter text: ")
printa(text=text)