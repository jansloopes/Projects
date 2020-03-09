import string


def germaniseer():
    zin = input("geef een zin")
    zin = string.capwords(zin)
    lijst_zin = zin.split(' ')
    for i in lijst_zin:
        print("i is {}".format(i))
        hoofd = i.capitalize()
        hoofdzin = ''
        hoofdzin = hoofdzin + hoofd
    return hoofdzin


def main():
    print("zin {} ".format(germaniseer()))


# ------------------------------
# Call Main
# ------------------------------
if __name__ == "__main__":
    main()
