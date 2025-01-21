import pandas as pd
import os
path="C:/Users/ipappau/Downloads"
directory=os.listdir(path)
# for file in directory:
#     if "TESTCODE" in file: 
#         excel=pd.read_excel(path + '/' + file)
        
excel = [pd.read_excel(path + '/' + file) for file in directory if 'TESTCODE' in file][0]

# print(excel)

# print(excel['XREF'])

firstColumn = excel['XREF']

# print(firstColumn)


newExcel = excel.drop(axis =0, columns=['XREF'])

# print(excel)
# print(newExcel)

newExcel['XREF'] = firstColumn

newExcel = newExcel.reset_index(drop=True)
newExcel.to_excel(path+'/newTestCode.xlsx', sheet_name='Instil', index=False)

print(newExcel)

print('Done')


