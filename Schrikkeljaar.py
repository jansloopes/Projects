def schrikkeljaar(jaartal) -> None:
    try:
        jaar: int = int(jaartal)
    except ValueError:
        print("Error converting jaartal {}".format(jaar))
        exit(-1)
    if (jaar % 400 == 0):
        print("jaar {} is schrikkeljaar".format(jaar))
    elif (jaar % 4 == 0) and (jaar % 100 != 0):
        print("jaar {} is schrikkeljaar".format(jaar))
    else:
        print("jaar {} is geen schrikkeljaar".format(jaar))
    return ()


def main():
    jaartal:int = input("geef jaartal")
    schrikkeljaar(jaartal)


# ------------------------------
# Call Main
# ------------------------------
if __name__ == "__main__":
    main()
