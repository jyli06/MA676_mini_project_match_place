import pandas as pd
import re

def read_data(file_name):
    # read the file from txt
    return open(file_name, "r").read().splitlines()

def match_area_code(num):
    pattern = re.compile(r'\d{3}')
    num3 = [pattern.findall(i)[0] for i in num]
    return num3

def main_get_state():
    # get friends' infomation
    lst1 = read_data("friends.txt")
    # get the data
    lst2 = read_data("area_code.txt")

    # create "df1" to record area_code dictionary as a dataframe
    '''
    df1:
      col: area_code, state
      structure:
      area_code              state
0         201         New Jersey
1         202    Washington D.C.
2         203        Connecticut
3         204  Canada - Manitoba
4         205            Alabama
..        ...                ...
386       979              Texas
387       980     North Carolina
388       984     North Carolina
389       985          Louisiana
390       989           Michigan
      
    '''
    df1 = pd.DataFrame({'area_code': lst2[0::2], 'state': lst2[1::2]})

    ## now we need to get the dataframe of the info of friends
    name = lst1[0::2]
    num = lst1[1::2]
    num3 = match_area_code(num)

    # create "df2" to record the information of friends as a dataframe
    '''
    df2:
      col: name, phone_num, area_code
      structure:
    name       phone_num   area_code
0    Ana     801-456-789       801
1    Ben     609 4567890       609
2   Cory  (206)-345-2619       206
3  Danny      6095648765       609
    '''
    df2 = pd.DataFrame({"name": name, "phone_num": num, "area_code": num3})

    # now we need to join the 2 dataframe to get the state where our friends are.
    df_join = df2.merge(df1, on="area_code", how='left')

    return df_join

# get_state()

if __name__ == '__main__':
    df1 = main_get_state()
    print(df1)

