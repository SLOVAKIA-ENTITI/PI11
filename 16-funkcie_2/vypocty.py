def sucet(x, y):
    return x + y
def parne(cislo):
    if cislo % 2 == 0:
        return "číslo je párne."
    else:
        return "číslo je nepárne."
def prvocislo(cislo):
    prvocis = True
    for i in range(2, cislo):
        if cislo % i == 0:
            prvocis = False
    return prvocis


a = int(input("Zadaj prvé číslo:"))
b= int(input("Zadaj druhé číslo:"))
sucet = sucet(a, b)
print(f"Súčet čísel {a} + {b} = {sucet}.")
print(f"Prvé číslo {a} je {parne(a)}")
print(f"Prvé číslo {b} je {parne(b)}")
if prvocislo(a):
    print(f"Číslo {a} je prvočíslo. ")
else:
    print(f"Číslo {a} nie je prvočíslo.")
if prvocislo(a):
    print(f"Číslo {b} je prvočíslo. ")
else:
    print(f"Číslo {b} nie je prvočíslo.")
