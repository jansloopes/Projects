import errno
import json
import request

from virus_total_apis import PublicApi as VirusTotalPublicApi

global_path_laptop = "C:\\Surfdrive\\MyWork\\Leiden\\2018-2019\\iscrip\\"
global_path_desktop =  "D:\\Users\\jan\\Surfdrive\\MyWork\\Leiden\\2018-2019\\iscrip\\"
global_file_name = "20190103_api_virus_total.txt"
global_file_virus = "virus_total_output.txt"
globals()


def online_scan(api_key, EICAR_MD5):
    vt = VirusTotalPublicApi(api_key)
    response = vt.get_file_report(EICAR_MD5)
    #response from virustotal
    print ("respons of virustotal is {} type is {}".format (response , type(response)))
    # print(json.dumps(response, sort_keys=False, indent=4))
    # convert json output data to  string
    str_data_json = json.dumps(response, sort_keys=True, indent=4)
    # write string data to file
    try:
        with open('{0}{1}'.format(global_path_laptop,global_file_virus), 'w') as f:
            f.write(str_data_json)
    except IOError as ex:
        print("File not found!")
        exit()
    f.close
    print ("raw_data_json is {} type is {}".format(str_data_json, type(str_data_json)))
    raw_json_dict = json.loads(str_data_json)
    return raw_json_dict


def get_api_key():
    try:
        fp = open('{0}{1}'.format(global_path_laptop, global_file_name), 'r')
        api_key = fp.read()
    except IOError as ex:
        if ex.args[0] == errno.ENOENT:
            print("File not found!")
            exit()
    finally:
        fp.close()
    print("api_key is {} ".format(api_key))
    return (api_key)


def main():
    # print(online_scan('your_api', 'www.google.com'))
    eicar = "X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"
    eicar_md5 = hashlib.md5(eicar.encode('utf-8')).hexdigest()
    api_key = get_api_key()
    raw_json_dict = online_scan(api_key, eicar_md5)
    print("raw_json_dict is {} type is {}". format(raw_json_dict, type(raw_json_dict)))


# ------------------------------
# Call Main
# ------------------------------
if __name__ == "__main__":
    main()
