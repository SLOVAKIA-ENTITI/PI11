retazec = input(str("Zadaj: "))
print(retazec)

i = 0
for i in range(len(retazec)):
    print(i, retazec[i])
for i in range(1,len(retazec)+1):
    print(-i, retazec[-i])


#for i in range(-1, -len(retazec)-1,-1):
#    print(i,retazec[i])