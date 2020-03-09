def scoresToevoegen(scorebord: dict, scores_land: dict) -> dict:
    # function to add scores. Returns dict scorebord
    # if country in scorebord then add new score.
    for key1 in scorebord:
        for key2 in scores_land:
            if key1 == key2:
                scorebord[key1] += scores_land[key2]
    # if county not in scorebord dict then add.
    for key3 in scores_land:
        if key3 not in scorebord:
            scorebord[key3] = scores_land[key3]

    print("scorebord in function is {}".format(scorebord))
    return (scorebord)


def convertDicttoList(scorebord: dict) -> list:
    # zet dict om in list en sorteerd eerst alfabetisch en dan score
    list_landen = []
    for key in scorebord:
        list_landen.append((key, scorebord[key]))
    list_landen.sort()
    list_landen.sort(key=lambda x: x[1])
    return (list_landen)


def scoresTonen(*arg):
    # function to show scores.
    # has flexibel amount of call elements.
    # aantal getoonde landen is het aantal landen dat wordt getoond bij printen.
    if len(arg) == 1:
        list_landen = arg[0]
        print("scorebord is {} ".format(list_landen))
    if len(arg) == 2:
        list_landen = arg[0]
        aantalgetoondelanden = arg[1]
        print("scorebord is [", end="")
        for i in range(aantalgetoondelanden):
            print("{}, ".format(list_landen[i]), end="")
        print("]")
    return ()


def main():
    scorebord = {}
    list_landen = []
    scores_land = {'Lithuania': 7, 'Russia': 3, 'Estonia': 4, 'Azerbaijan': 2, 'Sweden': 12, 'Turkey': 1,
                   'Spain': 8, 'Germany': 6,
                   'Malta': 5, 'Ireland': 10}
    scorebord = scoresToevoegen(scorebord, scores_land)
    #  for key1 in scorebord:
    #      print("scorebord 1 van {} is {}".format(key1, scorebord[key1]))
    scores_land = {'Albania': 8, 'Russia': 7, 'Iceland': 6, 'Italy': 5, 'Sweden': 12, 'Turkey': 3, 'Spain': 1,
                   'Germany': 10, 'Serbia': 4, 'Moldova': 2}
    scorebord = scoresToevoegen(scorebord, scores_land)
    #  for key1 in scorebord:
    #      print("scorebord  2 van {} is {}".format(key1, scorebord[key1]))

    list_landen = convertDicttoList(scorebord)
    scoresTonen(list_landen)
    scoresTonen(list_landen, 2)
    scoresTonen(list_landen, 3)


# ------------------------------
# Call Main
# ------------------------------
if __name__ == "__main__":
    main()
