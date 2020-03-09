import yara
import os


def process_directory(yrules, folder_path):
    match_info = []
    for root, _, files in yara.walk(folder_path):
        for entry in files:
            file_entry = yara.path.join(root, entry)
            match_info += process_file(yrules, file_entry)
    return match_info


def process_file(yrules, file_path):
    match = yrules.match(file_path)
    match_info = []
    for rule_set in match:
        for hit in rule_set.strings:
            match_info.append({
                'file_name': file_path,
                'rule_name': rule_set.rule,
                'rule_tag': ",".join(rule_set.tags),
                'hit_offset': hit[0],
                'rule_string': hit[1],
                'hit_value': hit[2]
            })
    return match_info




def main():
    try:
        fh = open('./test-rules.yara')
    except IOError:
        print("Could not open {}".format(fh))
    yrules = yara.compile(file=fh)
    yrules.save('./test_rules_compiled')
    match_info = process_directory(yrules, './')
    columns = ['rule_name', 'hit_value', 'hit_offset', 'file_name',
               'rule_string', 'rule_tag']
    for entry in match_info:
        for col in columns:
            print("{}: {}".format(col, entry[col]))


# ------------------------------
# Call Main
# ------------------------------
if __name__ == "__main__":
    main()

"""
try:
    fh = open('./test-rules.yara')
except IOError:
    print ("Could not open {}". format(fh))  
rules = yara.compile(file=fh)
rules.save('./test_rules_compiled')
matches = rules.match('./*.py')
if len(matches) > 0:
    print('matches: {}'.format(matches))
    for x in range(len(matches)):
        print(matches[x].rule)
        print(matches[x].tags)
        print(matches[x].strings)

matches = process_directory(yrule, './')
"""
