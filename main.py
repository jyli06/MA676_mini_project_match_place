import pandas as pd
import re

def read_data(file_name):
    # read the file from txt
    return open(file_name, "r").read().splitlines()

def match_area_code(num):
    pattern = re.compile(r'\d{3}')
    num3 = [pattern.findall(i)[0] for i in num]
    return num3

def get_state():
    # get friends' infomation
    lst1 = read_data("friends.txt")
    # get the data
    lst2 = read_data("area_code.txt")

    '''
    df1:
      col: area_code, state
    '''
    df1 = pd.DataFrame({'area_code': lst2[0::2], 'state': lst2[1::2]})

    ## now we need to get the dataframe of the info of friends
    name = lst1[0::2]
    num = lst1[1::2]
    num3 = match_area_code(num)
    '''
    df2:
      col: name, phone_num, area_code
    '''
    df2 = pd.DataFrame({"name": name, "phone_num": num, "area_code": num3})

    df_join = df2.merge(df1, on="area_code", how='left')

    return print(df_join)

# get_state()

if __name__ == '__main__':
    get_state()

