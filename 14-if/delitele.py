#while True:
#    číslo = int(input("Zadaj číselko (Pre ukončenie zadaj 0):"))
#    if číslo == 0:
#        print("Číselko je nula.   Dovidenia!!!!")
#        break
#    elif číslo % 2 == 0:
#        print("Číselko je párne.")
#    else:
#        print("Číselko je nepárne.")



while True:
    číslo = int(input("Zadaj číselko (Pre ukončenie zadaj 0):"))
    počet = 0
    print("Delitele sú:", end=" ")
    for delitel in range(1,číslo + 1):
        if číslo % delitel == 0:
            print(delitel, end=" ")
            počet += 1        #počet = počet + 1
    print()
    print("Počet delitelov je",počet,".")
    if počet == 2:
        print("Je to prvočíslo")
    else:
        print("Nie je to prvočíslo.")
    if číslo ==0:
        break
