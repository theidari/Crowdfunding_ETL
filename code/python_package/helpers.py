# --------------------------------------------------------------------------------------------------------
# -------------------- All libraries, variables and functions are defined in this file -------------------
# --------------------------------------------------------------------------------------------------------

# 1. libraries ------------------------------------------------------------------------------------------/
from python_package.constants import * # constants

# a-1) import dependencies
import pandas as pd
import numpy as np
import json
from datetime import datetime as dt
import re

# -------------------------------------------------------------------------------------------------------/

# 2. function definition --------------------------------------------------------------------------------/
#a-2) df extractor
def New_df(df, column):
    df_list=[]
    for item in column:
        print(HORIZONTAL_LINE+item)
        #get the unique item (categories and subcategories) in separate lists.
        names=df[item].unique().tolist()
        print(HORIZONTAL_LINE+str(names))
        # get the number of distinct values in the (categories and subcategories) lists.
        print(ENTER_LINE+LIST_COUNTER+str(len(names)))
        # get the number of distinct values in the categories and subcategories lists.
        ids=[(item.split(TEXT_SEPARATOR))[0]+str(index+1)for index, element in enumerate (names)]
        print(ENTER_LINE+str(ids))
        df_out = pd.DataFrame({item+C_ID:ids, item: names})
        df_list.append(df_out)  
    return df_list

#b-2) regex searcher
def Regex_Text(df,column_tag):
    columns_length=len(REGEX_COLUMNS)
    searcher_length=len(REGEX_SEARCHER)
    if columns_length != searcher_length:
        print(f"""Please input a same number of elements in both list""")
    else:
        for i in range(len(REGEX_COLUMNS)):
            df[REGEX_COLUMNS[i]]=df[column_tag].str.extract(REGEX_SEARCHER[i])
        df=df.drop(columns=[column_tag])
        return df