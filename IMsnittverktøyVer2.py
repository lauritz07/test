import statistics

def les_karakter(fag):
    while True:
        try:
            karakter = float(input(f"Hva er din karakter i {fag}? (Mellom 1 og 6): "))
            if 1 <= karakter <= 6:
                return karakter
            else:
                print("De fleste har karakterer mellom 1 og 6, vet ikke hvordan lærer du har som setter sånne karakterer😂")
        except ValueError:
            print("Slutt og tull da, din lille plopp. Skriv inn et tall😂")

print ("Velkommen til snittkalulatoren for fagene på 1IM!")
navn = input("Hva heter du? ")

fag = ["Engelsk", "Matematikk1-PY IM", "Naturfag", "Kroppsøving", "Yrkesfaglig fordypning", "Teknologiforståelse", "Konseptutvikling og programmering", "produksjon og historiefortelling"]

karakterer = []

for fag_navn in fag:
    karakterer.append(les_karakter(fag_navn))

skriftlig_eksamen = input("Har du hatt skriftlig eksamen? [ja eller nei (små bokstaver) ] ")
if skriftlig_eksamen == "ja": 
    im10 = float(input("Hva er din karakter i skriftlig eksamen? "))
    if 1 <= im10 <= 6:
        karakterer.append(im10)
    else:
        print("De fleste har karakterer mellom 1 og 6, vet ikke hvordan lærer du har som setter sånne karakterer😂")
elif skriftlig_eksamen != "nei":
    print("Ugyldig")

muntlig_eksamen = input("Har du hatt muntlig eksamen? [ja eller nei (små bokstaver) ] ")
if muntlig_eksamen == "ja": 
    im11 = float(input("Hva er din karakter i muntlig eksamen? "))
    if 1 <= im11 <= 6:
        karakterer.append(im11)
    else:
        print("De fleste har karakterer mellom 1 og 6, vet ikke hvordan lærer du har som setter sånne karakterer😂")

gjennomsnitt = statistics.mean(karakterer)
if gjennomsnitt < 2.0:
    print("Å nei, du gjorde det ikke så veldig bra med et snitt på", gjennomsnitt, ". Bedre lykke neste år")
else:
    print("Gratulerer,", navn + ",", "snittet ditt er", gjennomsnitt, "!")
