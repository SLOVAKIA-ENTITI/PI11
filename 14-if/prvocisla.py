while True:
    n = int(input("Zadaj číselko (Pre ukončenie zadaj 0):"))
    for číslo in range(2,(n // 2)+1):
        počet = 0
        for delitel in range(1,číslo + 1):
            if číslo % delitel == 0:
                počet += 1        #počet = počet + 1
        if počet == 2:
            print(číslo, end=" ")
    print()
    if n == 0:
        break
