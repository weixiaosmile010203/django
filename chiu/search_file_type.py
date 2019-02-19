import os, re


def search_file_type(path,file_type):
    file_list = []
    for name in os.listdir(path):
        if name.endswith(file_type):
            file_list.append(name)
    return file_list


def find_date_on_file(time_regix,files):
    file_regex = re.compile(time_regix)
    for file in files:
        with open(file,'r') as fb:
            file_on = fb.readlines()
            times = file_regex.search(file_on)
            print(times)


file_path = input("please input file path:")
file_type = input("please input file type:")
files = search_file_type(file_path,file_type)
find_date_on_file()


