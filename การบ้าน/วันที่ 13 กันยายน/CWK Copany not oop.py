def คำนวนภาษี(SelectArrayProduct):
    for i in SelectArrayProduct:
        Vat = i[2] * (i[3] / 100)
        VatandPrice = Vat + i[2]
        i.append('%.2f' % Vat)
        i.append(VatandPrice)
    return SelectArrayProduct

def สูงสุด(SelectArrayProduct):
    Data = SelectArrayProduct
    MaxVatData = []
    for i in Data:
        MaxVatData.append(i[3])
    for i in Data:
        if i[3] == sorted(MaxVatData)[-1]:
            print("สินค้าที่จ่ายภาษีมากที่สุดคือ", i[1], "ภาษีที่ต้องจ่ายคือ", i[3], "%." "รวมเป็นเงิน", (i[2] * (i[3] / 100)) + i[2], "บาท")

def MinVat(SelectArrayProduct):
    Data = SelectArrayProduct
    MinVatData = []
    for i in Data:
        MinVatData.append(i[3])
    for i in Data:
        if i[3] == sorted(MinVatData)[0]:
            print(
                f"สินค้าที่จ่ายภาษีน้อยที่สุดคือ {i[1]} ภาษีที่ต้องจ่ายคือ {i[3]} %. รวมเป็นเงิน { (i[2] * (i[3] / 100)) + i[2]} บาท")

def GetAvgVat(SelectArrayProduct):
    Data = SelectArrayProduct
    SumVat = 0
    for i in Data:
        SumVat += i[3]
    print('ค่าเฉลี่ยเงินภาษี ของสินค้าทุกชิ้นคือ %0.2f' %
        (SumVat / len(Data)))

def MaxPrice(SelectArrayProduct):
    Data = SelectArrayProduct
    MaxPriceData = []
    for i in Data:
        MaxPriceData.append(i[2])
    for i in Data:
        if i[2] == sorted(MaxPriceData)[-1]:
            print(f"สินค้าที่มีราคาสูงสุดคือ {i[1]} ราคา {i[2]} บาท")

def MinPrice(SelectArrayProduct):
    Data = SelectArrayProduct
    MinPriceData = []
    for i in Data:
        MinPriceData.append(i[2])
    for i in Data:
        if i[2] == sorted(MinPriceData)[0]:
            print(f"สินค้าที่มีราคาต่ำสุดคือ {i[1]} ราคา {i[2]} บาท")
            break

def Display(SelectArrayProduct):
    Data = SelectArrayProduct
    print("รหัสสินค้า\t\tชื่อสินค้า\t\tราคา\t\tภาษี\t\tราคาสุทธิ")
    for i in Data:
        print(f"{i[0]}\t\t{i[1]}\t\t{i[2]}\t\t{i[4]}\t\t{i[5]}")

ข้อมูล = [
    ['801', 'Coconut', 5.00, 3],
    ['810', 'Kiwi', 3.00, 2],
    ['807', 'Watermelon', 7.00, 5],
    ['808', 'Apple', 4.00, 4],
    ['809', 'Apricot', 3.00, 5],
    ['811', 'Jackfruit', 9.00, 5],
    ['815', 'Orange', 8.00, 6],
    ['814', 'Guava', 4.00, 7],
    ['813', 'Lemon', 7.00, 5]
]

ข้อมูลใหม่ = คํานวนภาษี(ข้อมูล)

สูงสุด(ข้อมูลใหม่)