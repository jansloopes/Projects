import errno
import hashlib
import json
import requests

global_path_laptop = "C:\\Surfdrive\\MyWork\\Leiden\\2018-2019\\iscrip\\"
global_path_desktop = "D:\\Users\\jan\\Surfdrive\\MyWork\\Leiden\\2018-2019\\iscrip\\"
global_file_name = "20190103_api_virus_total.txt"
global_file_virus = "virus_total_output.txt"


# print (globals())

def read_virus_total_file(virus_total_file):
    try:
        with (open(virus_total_file, 'r')) as f:
            jason_virus_str = f.read()
            jason_virus_dict = json.loads(jason_virus_str)
    except IOError as ex:
        print("File not found!")
        exit()
    f.close()
    return (jason_virus_dict)


def main():
    virus_total_file = ('{0}{1}'.format(global_path_laptop, global_file_virus))
    jason_virus_dict = read_virus_total_file(virus_total_file)
    print(type(jason_virus_dict))
    for key1 in jason_virus_dict:
        print("key1 is {} and virus is {}".format(key1, jason_virus_dict[key1]))
        for key2 in jason_virus_dict["results"]:
            print("key2 is {} and results is {}".format(jason_virus_dict.keys(),jason_virus_dict["results"][key2]))
            for key3 in jason_virus_dict["results"]["scans"]:
                print ("key 3 is {} and scans is {}".format(key3,jason_virus_dict["results"]["scans"][key3]))

# ------------------------------
# Call Main
# ------------------------------
if __name__ == "__main__":
    main()
