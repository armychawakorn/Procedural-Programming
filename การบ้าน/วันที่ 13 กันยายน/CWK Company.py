class CWKCompany:
    def __init__(self, SelectArry):
        self.SelectArry = SelectArry
    def VatCalCulator(self):
        for i in self.SelectArry:
            Vat = i[2] * (i[3] / 100)
            VatandPrice = Vat + i[2]
            i.append('%.2f' % Vat)
            i.append(VatandPrice)
        return self.SelectArry
    def MaxVat(self):
        Data = self.VatCalCulator()
        MaxVatData = []
        for i in Data:
            MaxVatData.append(i[3])
        for i in Data:
            if i[3] == sorted(MaxVatData)[-1]:
                print(
                    f"สินค้าที่จ่ายภาษีมากที่สุดคือ {i[1]} ภาษีที่ต้องจ่ายคือ {i[3]} %. รวมเป็นเงิน { (i[2] * (i[3] / 100)) + i[2]} บาท")
    def MinVat(self):
        Data = self.VatCalCulator()
        MinVatData = []
        for i in Data:
            MinVatData.append(i[3])
        for i in Data:
            if i[3] == sorted(MinVatData)[0]:
                print(
                    f"สินค้าที่จ่ายภาษีน้อยที่สุดคือ {i[1]} ภาษีที่ต้องจ่ายคือ {i[3]} %. รวมเป็นเงิน { (i[2] * (i[3] / 100)) + i[2]} บาท")
    def GetAvgVat(self):
        Data = self.VatCalCulator()
        SumVat = 0
        for i in Data:
            SumVat += i[3]
        print('ค่าเฉลี่ยเงินภาษี ของสินค้าทุกชิ้นคือ %0.2f' %
            (SumVat / len(Data)))
    def MaxPrice(self):
        Data = self.VatCalCulator()
        MaxPriceData = []
        for i in Data:
            MaxPriceData.append(i[2])
        for i in Data:
            if i[2] == sorted(MaxPriceData)[-1]:
                print(f"สินค้าที่มีราคาสูงสุดคือ {i[1]} ราคา {i[2]} บาท")
    def MinPrice(self):
        Data = self.VatCalCulator()
        MinPriceData = []
        for i in Data:
            MinPriceData.append(i[2])
        for i in Data:
            if i[2] == sorted(MinPriceData)[0]:
                print(f"สินค้าที่มีราคาต่ำสุดคือ {i[1]} ราคา {i[2]} บาท")
                break
    def Display(self):
        Data = self.VatCalCulator()
        print("รหัสสินค้า\t\tชื่อสินค้า\t\tราคา\t\tภาษี\t\tราคาสุทธิ")
        for i in Data:
            print(f"{i[0]}\t\t{i[1]}\t\t{i[2]}\t\t{i[4]}\t\t{i[5]}")

InputProduct = [
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
Program = CWKCompany(InputProduct)
Program.Display()
Program.MaxVat()
Program.MinVat()
Program.GetAvgVat()
Program.MaxPrice()
Program.MinPrice()