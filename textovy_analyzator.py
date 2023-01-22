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
which traverse the valley. ''',
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
else:
    print("bla")