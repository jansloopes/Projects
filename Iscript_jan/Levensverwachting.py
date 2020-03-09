from typing import Dict, Any


def levensverwachting(persoon_dict):
    print(type(persoon_dict))
    print("persoon in functie is {} ".format(persoon_dict['geslacht']))
    levensduur = 70
    if persoon_dict['geslacht'] == "vrouw":
        levensduur += 4
    if persoon_dict['roker'] == True:
        levensduur -= 5
    else:
        levensduur += 5
    if persoon_dict['sport'] == 0:
        levensduur -= 3
    else:
        levensduur = levensduur + (1 * int(persoon_dict['sport']))
    if int(persoon_dict['alcohol']) == 0:
        levensduur += 2
    elif int(persoon_dict['alcohol']) > 7:
        levensduur = levensduur + ( int(persoon_dict['alcohol']) - 7) * 0, 5
    if persoon_dict['fastfood'] == False:
        levensduur += 3
    return (levensduur)


def convert_str_dict(persoon):
    type(persoon)
    persoon_nospace = persoon.replace(" ", "")
    # Splitting the string based on , we get key value pairs
    list = persoon_nospace.split(",")
    persoon_dict: Dict[Any, Any] = {}
    for i in list:
        # Get Key Value pairs separately to store in dictionary
        keyvalue = i.split('=')

        # Replacing the single quotes in the leading.
        m = keyvalue[0].strip('\'')
        #  m = m.replace("\"", "")
        persoon_dict[m] = keyvalue[1].strip('"\'')
    print("persoon in functie is {} ".format(persoon_dict['geslacht']))
    return (persoon_dict)


def main():
    persoon: str = input("geef dictionary: ")
    print("persoon is {}".format(persoon))
    persoon_dict = convert_str_dict(persoon)

    for key in persoon_dict:
        print("{} : {}".format(key, persoon_dict[key]))
    print("persoon_dict is: ".format(persoon_dict))
    print("levensverwachting is {}".format(levensverwachting(persoon_dict)))


# ------------------------------
# Call Main
# ------------------------------
if __name__ == "__main__":
    main()
