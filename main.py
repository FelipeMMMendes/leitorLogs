
from pyparsing import line


path = r'C:\Users\felipe.mendes\Desktop\Programação\python\LeitorLogs\Brocade_5100_FC01'
with open(path,'r') as f:
    lines = f.readlines()
    for row in lines:
        word = 'CHASSIS/WWN'
        if row.find(word) == 0:
            print("String exists in file")
            print("Line Number: ",lines.index(row))
            print()
