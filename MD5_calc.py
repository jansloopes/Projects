# Import hashlib library (md5 method is part of it)
import hashlib


def calculate_md5(file_name):
    # Open,close, read file and calculate MD5 on its contents
    try:
        file_to_check = open(file_name,"r")
    except FileNotFoundError:
        print ("Cannot open file {}".format(file_name))
        exit(-1)
    # read contents of the file
    data = file_to_check.read()
    data_bytes = data.encode('utf-8')
    # pipe contents of the file through
    return hashlib.md5(data_bytes).hexdigest()

# Finally compare original MD5 with freshly calculated


def main():
    file_name = input ("geef file naam: ")
    print("MD5 van file {} is {}".format(file_name,calculate_md5(file_name)))


# ------------------------------
# Call Main
# ------------------------------
if __name__ == "__main__":
    main()

