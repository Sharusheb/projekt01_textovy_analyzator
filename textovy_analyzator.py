"""projekt_1.py: první projekt do Engeto Online Python Akademie

author: Šárka Böhmová
email: sarka.bohmova@seznam.cz
discord: ShareenBoom#6281
"""
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley.''',
'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

text_1 = tuple(TEXTS[0].split(" "))
text_2 = tuple(TEXTS[1].split(" "))
text_3 = tuple(TEXTS[2].split(" "))

registrovani = {
    "bob":"123", 
    "ann":"pass123", 
    "mike":"password123", 
    "liz":"pass123"
    }

oddelovac = "-"*40

jmeno = input("Zadej prihlasovaci jmeno: ")
heslo = input("Zadej heslo: ")

if registrovani.get(jmeno) == heslo:
    print(oddelovac)
    print("Vitej v aplikaci, ", jmeno)
    print("K dispozici jsou 3 texty k analyze.")
    print(oddelovac)
else:
    print(oddelovac)
    print("Neregistrovany uzivatel, ukoncuji program..")
    quit()

vyber_textu = input("Vyber si cislo textu od 1 do 3: ")

if int(vyber_textu) not in range(1, 4) or not vyber_textu.isnumeric():
    print("Text s vybranym cislem neexistuje! Ukoncuji program...")
    quit()
elif vyber_textu == "1":
    vyber_textu = text_1
elif vyber_textu == "2":
    vyber_textu = text_2
else:
    vyber_textu = text_3

pocet_slov = []

for slovo in vyber_textu:
    pocet_slov.append(slovo.replace("\n", "").strip(",.!?:"))
delka_textu = len(pocet_slov)
print(oddelovac)
print(f"Ve vybranem textu je {delka_textu} slov.")

velke_pismeno = []

for slovo in vyber_textu:
    if slovo.istitle():
        velke_pismeno.append(slovo)
velke_pismeno_pocet = len(velke_pismeno)
print(f"Ve vybranem textu je {velke_pismeno_pocet} slov zacinajici velkym pismenem.")

velka_pismena = []

for slovo in vyber_textu:
    if slovo.isupper() and slovo.isalpha():
        velka_pismena.append(slovo)
velka_pismena_pocet = len(velka_pismena)
print(f"Ve vybranem textu je {velka_pismena_pocet} slov velkym pismenem.")

mala_pismena = []

for slovo in vyber_textu:
    if slovo.islower():
        mala_pismena.append(slovo)
mala_pismena_pocet = len(mala_pismena)
print(f"Ve vybranem textu je {mala_pismena_pocet} slov malym pismenem.")

cisla = []

for slovo in vyber_textu:
    if slovo.isnumeric():
        cisla.append(slovo)
pocet_cisel = len(cisla)
print(f"Ve vybranem textu je {pocet_cisel} cisel.")

for cislo in range(len(cisla)):
    cisla[cislo] = int(cisla[cislo])
suma_cisel = sum(cisla)
print(f"Suma vsech cisel je {suma_cisel}.")

print(oddelovac)

print("len".upper(), "|", "\t", "occurences".upper(), "\t", "|", "nr.".upper())

print(oddelovac)

graf=dict()

for slovo in pocet_slov:
    delka_slova = len(slovo)
    if delka_slova in graf:
        graf[delka_slova]+=1
    else:
        graf[delka_slova]=1

for delka_slova in sorted(graf):
    print(f"{delka_slova} | {graf[delka_slova]*'*'} | {graf[delka_slova]}")

