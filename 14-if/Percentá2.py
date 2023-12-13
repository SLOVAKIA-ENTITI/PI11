max_bodov = 30
pocet_bodov = int(input("Zadaj svoj počet bodov za test."))
percenta = (pocet_bodov / max_bodov) * 100
print(f"Získal si {percenta}%")
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