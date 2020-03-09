def dubbels(lijst):
    dubbel_lijst = []

    print("dubbel_lijst is {}".format(dubbel_lijst))
    for i in range(0, len(lijst) - 1):
        if lijst[i] in lijst[i + 1:(len(lijst))]:
            print(" dubbel_lijst is{}".format(dubbel_lijst))
            if lijst[i] not in dubbel_lijst:
                        dubbel_lijst.append(lijst[i])
    return(dubbel_lijst)


def main():
    lijst: list = input("geef lijst")

    print("double_lijst is {}".format(dubbels(lijst)))


# ------------------------------
# Call Main
# ------------------------------
if __name__ == "__main__":
    main()
