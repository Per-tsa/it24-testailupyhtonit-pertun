import random

print("Kivi / Paperi / Sakset")
print("Ensimmäinen kolmesta voittoon!")

voitot = 0
häviöt = 0

valinnat = ["KIVI", "PAPERI", "SAKSET"]

def määritä_voittaja(pelaaja, kone):
    if pelaaja == kone:
        return "Tasapeli"
    elif (pelaaja == "KIVI" and kone == "SAKSET") or \
         (pelaaja == "PAPERI" and kone == "KIVI") or \
         (pelaaja == "SAKSET" and kone == "PAPERI"):
        return "Voitto"
    else:
        return "Häviö"

while True:
    pelaajakäsi = input("Valitse kätesi (KIVI/PAPERI/SAKSET): ").upper()
    if pelaajakäsi not in valinnat:
        print("Virheellinen valinta! Valitse KIVI, PAPERI tai SAKSET.")
        continue

    konevalinta = random.choice(valinnat)
    print(f"Valitsit: {pelaajakäsi}")
    print(f"Tietokone valitsi: {konevalinta}")

    tulos = määritä_voittaja(pelaajakäsi, konevalinta)

    if tulos == "Voitto":
        voitot += 1
        print("Voitit kierroksen!")
    elif tulos == "Häviö":
        häviöt += 1
        print("Hävisit kierroksen!")
    else:
        print("Tasapeli!")

    print(f"Pistetilanne: {voitot} - {häviöt}")

    if voitot == 3:
        print("Voitit pelin!")
        break
    elif häviöt == 3:
        print("Hävisit pelin!")
        break

print("Kiitos pelaamisesta!")
print(f"Lopputulos: Voitot {voitot}, Häviöt {häviöt}")