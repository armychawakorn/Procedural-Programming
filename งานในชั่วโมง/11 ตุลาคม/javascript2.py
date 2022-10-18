import pandas as pd
DataFailes = pd.read_excel('Procedural Programming/งานในชั่วโมง/11 ตุลาคม/products.xlsx', sheet_name='Sheet2')

FirstDataFiles = DataFailes[DataFailes['หน่วย'] > 50]
NewDataframe = pd.DataFrame({"ชื่อสินค้า" : FirstDataFiles['สินค้า'], 'หน่วย': FirstDataFiles['หน่วย']})
NewDataframe.to_excel('Procedural Programming/งานในชั่วโมง/11 ตุลาคม/Popular.xlsx', index=False)