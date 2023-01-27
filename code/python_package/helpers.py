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
# -------------------------------------------------------------------------------------------------------/

# 2. function definition --------------------------------------------------------------------------------/

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