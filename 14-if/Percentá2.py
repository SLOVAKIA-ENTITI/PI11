percenta = int(input("Zadaj percentá:"))

if percenta >= 90:
    print("Výborný.")
elif 75 <= percenta:
    print("Chválitebný.")
elif 50 <= percenta:
    print("Dobrý.")
elif 30 <= percenta:
    print("Dostatočný.")
else:
    print("Nedostatočný.")