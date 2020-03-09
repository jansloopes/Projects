naam_grote_prijs = input ("geef naam grote prijs: ")
km_ronde = input("Geef afstand ronde: ")
min_ronde = input ("Geef tijd van een ronde: ")

try:
    km_ronde  = float(km_ronde)
except ValueError:
        print("Error converting km ronde")
        exit(-1)
try:
    min_ronde  = float(min_ronde)
except ValueError:
        print("Error converting min ronde")
        exit(-1)

afstand = 0
tijd =0
ronde = 0


while (afstand <= 305) and  (tijd < 120):
    afstand += km_ronde
    tijd += min_ronde
    ronde += 1
    print ("Afstand is {} tijd is {}".format(afstand,tijd))

print ("De grote prijs van {} wordt verreden over {} ronden ({})".format(naam_grote_prijs, ronde, afstand))

