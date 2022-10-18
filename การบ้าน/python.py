number = 1
for i in range(1,10):
    for z in range(1, i+1):
      if(number%10 == 5 or number%5 == 0):
        number += 1
        print(number , end="\t")
      else:
        print(number, end="\t")
      number += 1
    print()