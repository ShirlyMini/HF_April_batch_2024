#### fetch data from excel and fortmat it is list of tuple
# [(u,p,e)]
from Utilities.xlutility import *

def load_td_from_xl(xl_path, sheet):
    row = GetRow(xl_path, sheet)#5
    col = GetCol(xl_path, sheet)#3

    l2=[]
    for r in range(2, row+1):# 2 to 5
        l1=[]
        for c in range(1,col+1):
            l1.append(ReadData(xl_path, sheet, r, c))
        #print(tuple(l1))
        l2.append(tuple(l1))
    #print(l2)# list of tuple
    return l2

# load_td_from_xl(r".\LoginData.xlsx", "Sheet1")
#[('Admin', 'admin123', 'Pass'), ('Admin', 'admin', 'Fail'), ('admin123', 'admin123', 'Fail'), ('admin123', 'admin456', 'Fail')]
