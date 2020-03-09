def scoresToevoegen(scorebord, scores_land):
    for key1 in scorebord:
        for key2 in scores_land:
            if key1 == key2:
                scorebord[key1] += scores_land[key2]
    for key3 in scores_land:
        if key3 not in scorebord:
            scorebord[key3] = scores_land[key3]

    print("scorebord in function is {}".format(scorebord))
    return (scorebord)


def scoresTonen(*arg):
    if len(arg) == 1:
        scorebord = arg[0]
    if len(arg) == 2:
        scorebord = arg[0]
        n = arg[1]
    print("scorebord is {} ".format(scorebord))

    return ()


def main():
    scorebord = {}
    scores_land = {'Lithuania': 7, 'Russia': 3, 'Estonia': 4, 'Azerbaijan': 2, 'Sweden': 12, 'Turkey': 1,
                   'Spain': 8, 'Germany': 6,
                   'Malta': 5, 'Ireland': 10}
    scorebord = scoresToevoegen(scorebord, scores_land)
    for key1 in scorebord:
        print("scorebord 1 van {} is {}".format(key1, scorebord[key1]))
    scores_land = {'Albania': 8, 'Russia': 7, 'Iceland': 6, 'Italy': 5, 'Sweden': 12, 'Turkey': 3, 'Spain': 1,
                   'Germany': 10, 'Serbia': 4, 'Moldova': 2}
    scorebord = scoresToevoegen(scorebord, scores_land)
    for key1 in scorebord:
        print("scorebord  2 van {} is {}".format(key1, scorebord[key1]))
    scoresTonen(scorebord)


# ------------------------------
# Call Main
# ------------------------------
if __name__ == "__main__":
    main()
