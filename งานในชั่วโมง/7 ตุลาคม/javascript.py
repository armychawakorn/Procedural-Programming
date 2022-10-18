import pandas as pd
df = pd.read_excel('Procedural Programming/งานในชั่วโมง/7 ตุลาคม/products.xlsx', sheet_name='Sheet2')

def GetProductPrice(Datafile):
    Product_name = Datafile['สินค้า'].tolist()
    Product_Price = Datafile['ราคา/หน่วย'].tolist()
    with open('C:/Users/Admin/Desktop/Class Programing/Procedural Programming/งานในชั่วโมง/7 ตุลาคม/ProductPrice.txt', 'w') as f:
        for i in range(len(Product_name)):
            print(f'{Product_name[i]}({Product_Price[i]} บาท)')
            f.write(f'{Product_name[i]}({Product_Price[i]} บาท)\n')
    print(f'บันทึกไฟล์เรียบร้อยแล้ว จำนวน {len(Product_name)} รายการ')
def GetLocation(Datafile):
    Location = Datafile['พื้นที่'].tolist()
    Agent = Datafile['ตัวแทน'].tolist()
    with open('C:/Users/Admin/Desktop/Class Programing/Procedural Programming/งานในชั่วโมง/7 ตุลาคม/GetLocation.txt', 'w') as f:
        for i in range(len(Location)):
            print(f'{Location[i]}({Agent[i]})')
            f.write(f'{Location[i]}({Agent[i]})\n')
    print(f'บันทึกไฟล์เรียบร้อยแล้ว จำนวน {len(Location)} รายการ')
def WhoSell(Datafile):
    Product_name = Datafile['สินค้า'].tolist()
    Agent = Datafile['ตัวแทน'].tolist()
    with open('C:/Users/Admin/Desktop/Class Programing/Procedural Programming/งานในชั่วโมง/7 ตุลาคม/WhoSell.txt', 'w') as f:
        for i in range(len(Product_name)):
            print(f'{Product_name[i]}({Agent[i]})')
            f.write(f'{Product_name[i]}({Agent[i]})\n')
    print(f'บันทึกไฟล์เรียบร้อยแล้ว จำนวน {len(Product_name)} รายการ')
    
def start():
    print('1. ราคาสินค้า')
    print('2. สถานที่ขายสินค้า')
    print('3. ตัวแทนขายสินค้า')
    print('4. ออกจากโปรแกรม')
    select = int(input('เลือกทำรายการ : '))
    if select == 1:
        GetProductPrice(df)
        start()
    elif select == 2:
        GetLocation(df)
        start()
    elif select == 3:
        WhoSell(df)
        start()
    elif select == 4:
        print('ออกจากโปรแกรม')
    else:
        print('กรุณากรอกเลขให้ถูกต้อง')
        start()
start()