'''
Arvauspeli
'''
sana = "koira"
import random
arvaukset = 0
häpeä = 0 
arvauspötkö = ["_"] * len(sana)

while True:
    
    arvaus = input("Arvaa sana tai pyydä 'vihje': ")
    if arvaus.lower() == "vihje":
            vihje = random.randint(0, len(sana) - 1)
            print(f"sanassa on kirjain {sana[vihje]}")
            print("Häpeäää Häpeääääääääää!")
            häpeä += 1
            
    if arvaus.lower() == "lopeta":
        print("Peli lopetettu.")
        break
    else:
        arvaukset += 1


    
    if arvaus == sana:
        print("Oikein!")
        print(f"Arvauksia yhteensä: {arvaukset} ja häpeää {häpeä}")

        break
    else:
        if arvaus != "vihje":
            print("Väärin, yritä uudestaan.")
            print(f"Arvauksia yhteensä: {arvaukset} ja häpeää {häpeä}")
        if arvaukset > 4:
            print(f"Häpeäsi jatkaa vain kasvua")

