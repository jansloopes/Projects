from datetime import date,datetime


class Klant:
    def __init__(self, naam, has_a_verhuurorganisatie, has_a_voucher):
        self.naam = naam
        self.has_a_verhuurorganisatie = has_a_verhuurorganisatie
        self.has_a_voucher = has_a_voucher

    def __repr__(self):
        return ("{} {} {} ".format(self.naam, self.has_a_voucher, self.has_a_verhuurorganisatie))


class Verhuur_organisatie:
    def __init__(self, naam: object) -> object:
        self.naam = naam

    def __repr__(self):
        return ("{}".format(self.naam))


class Voucher():
    def __init__(self, verhuurdatum, aantaldagen, totaalbedrag, tijdverhuur, has_a_auto):
        self.verhuurdatum = verhuurdatum
        self.aantaldagen = aantaldagen
        self.totaalbedrag = totaalbedrag
        self.tijdverhuur = tijdverhuur
        self.has_a_auto = has_a_auto

    def __repr__(self):
        return ("{} {} {} {} {}".format(self.verhuurdatum, self.aantaldagen, self.totaalbedrag, self.tijdverhuur,
                                        self.has_a_auto))


class Auto():
    def __init__(self, merk, verhuurplaats, dagprijs, verhuurorganisatie):
        self.merk = merk
        self.verhuurplaats = verhuurplaats
        self.dagprijs = dagprijs
        self.verhuurorganisatie = verhuurorganisatie

    def __repr__(self):
        return ("{} {} {} {} ".format(self.verhuurplaats, self.dagprijs, self.merk, self.verhuurorganisatie))


class Servicemedewerker():
    def __init__(self, naam, emailadres):
        self.naam = naam
        self.emailadres = emailadres

    def ___repr___(self):
        return ("{} {}".format(self.emailadres, self.naam))


class Autoverhuurcatalogus():
    def __index__(self, has_a_auto):
        self.o_auto = has_a_auto


class Invoerdatum:
    def get_date(self):
        date_entry = input('Enter a date in YYYY-MM-DD format')
        year, month, day = map(int, date_entry.split('-'))
        date1 = datetime(year, month, day)
        return (date1)


def main():
    verhuurorganisatie_hertz = Verhuur_organisatie('Hertz')
    verhuurorganisatie_sunCars = Verhuur_organisatie('Sun Cars')
    verhuurorganisatie_connectcar = Verhuur_organisatie('Connectcar')
    auto_objects = []
    auto_vw = Auto('vw', 'amsterdam', 250, verhuurorganisatie_hertz)
    auto_objects.append(auto_vw)
    auto_ford = Auto('Ford', 'Rotterdam', 100, verhuurorganisatie_sunCars)
    auto_objects.append(auto_ford)
    auto_opel = Auto('opel', 'Amsterdam ', 120, verhuurorganisatie_connectcar)
    auto_objects.append(auto_opel)
    voornaamklant = input("geef uw voornaam")
    mailadresklant = input('geef uw mailadres')

    i = 0
    for auto in auto_objects:
        print("{} {} ".format(i, auto))
        i += 1

    keuze_auto = int(input("welke auto wil u huren? [x]"))
    while (keuze_auto < 0 or keuze_auto > i):
        print("Uw keuze is niet correct {} moet >=0 of kleiner dan of gelijk aan {}".format(keuze_auto, i))
        keuze_auto = int(input("welke auto wil u huren? [x]"))
    print("auto keuze is {}".format(auto_objects[keuze_auto]))

    aantaldagen = int(input("Hoe lang wilt u de auto huren >0"))
    date_object = Invoerdatum()
    print("Geef de startdatum")
    verhuurdatumstart = date_object.get_date()
    print("verhuurstartdatum is {}", format(verhuurdatumstart))

    # servicemedewerker1 = Servicemedewerker('Jan', 'jan@self.nl')
    # klant1 = Klant(voornaamklant, verhuurorgranisatie1, voucher1)
    # voucher1 = Voucher('22022018', 4, 100, 4, auto1)
    # klant1 = Klant('jan', verhuurorgranisatie1, voucher1)
    # print("{} {}".format(klant1, klant1.has_a_voucher))


# ------------------------------
# Call Main
# ------------------------------
if __name__ == "__main__":
    main()
