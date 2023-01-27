# --------------------------------------------------------------------------------------------------------
# ---------------------------------------------- Constants------------------------------------------------
# --------------------------------------------------------------------------------------------------------

# 1. folders and files name -----------------------------------------------------------------------------/
BROWSER              = "chrome"
PROCESSING_TOOL      = "html.parser"
# -------------------------------------------------------------------------------------------------------/

# 2. defining directories -------------------------------------------------------------------------------/
MARS_NEWS_URL        = "https://static.bc-edx.com/data/web/mars_news/index.html"
MARS_TEMP_URL        = "https://static.bc-edx.com/data/web/mars_facts/temperature.html"
OUTPUT_PATH          = "../output/"

CROWDFUNDING_PATH    = "../resource/crowdfunding.xlsx"
CONTACTS_PATH        = "../resource/contacts.xlsx"
RESULTS_PATH          = "../resource/results/"
# -------------------------------------------------------------------------------------------------------/

HORIZONTAL_LINE      = f"""⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n"""
ENTER_LINE           = f"""\n"""
TEXT_SEPARATOR       = "e"
LIST_COUNTER         = "Number of Distinct values: "
C_ID                 = "_id"


# --regex function constatnts
REGEX_COLUMNS        = ["contact_id","first_name","last_name","email"]
REGEX_SEARCHER       = ['contact_id":(.*), "n',r'name": "(.*)\s\w+", "',r'name": "\w+\s(.*)", "',r'email": "(.*)"']