import pandas as pd
DataFailes = pd.read_excel('Procedural Programming/งานในชั่วโมง/11 ตุลาคม/products.xlsx', sheet_name='Sheet2')

DataFailes = DataFailes[DataFailes['ราคา/หน่วย'] >= 150]
DataFailes.to_excel('Procedural Programming/งานในชั่วโมง/11 ตุลาคม/VIP.xlsx', index=False)