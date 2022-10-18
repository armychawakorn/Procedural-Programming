import pandas as pd
DataFailes = pd.read_excel('Procedural Programming/งานในชั่วโมง/11 ตุลาคม/products.xlsx', sheet_name='Sheet2')

FirstDataFiles = DataFailes[DataFailes['พื้นที่'] == 'Central']
NewDataframe = pd.DataFrame(
    {"ชื่อสินค้า" : FirstDataFiles['สินค้า'], 'ราคา': FirstDataFiles['ราคา/หน่วย']})
NewDataframe.to_excel('Procedural Programming/งานในชั่วโมง/11 ตุลาคม/Central.xlsx', index=False)