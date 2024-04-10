ret = input("Zadj retazec: ")
posun = int(input("Zadaj posun pre kódovanie: "))

for i in range(len(ret)):
    #print(ret[i],':', ord(ret[i]))
    print(f'{ret[i]}:{ord(ret[i])}')

ret_kod = ""
for i in range(len(ret)):
    #print(ret[i],':', ord(ret[i]))
    print(f'{ret[i]}:{chr(ord(ret[i])+1)}')
    ret_kod += chr(ord(ret[i])+ posun)                   #alebo ret_kod = ret_kod + chr.....



print(f'Zakódovaný reťazec:{ret_kod}')



