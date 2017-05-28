# this script test the main program

import sys
sys.path.append('C:/Users/fredyang/Documents/GitHub/GoogleSheetClient/GoogleSheetClient')
from main_program import *
scope = ['https://spreadsheets.google.com/feeds']
workbook = 'sg_blogs_retrieved_data'
json_file = 'C:/Users/fredyang/Documents/GitHub/GoogleSheetClient/MSO-projects-87dd9cc7a873.json'
#  create a instance
ins = GoogleSheetDownloader(scope=scope, json_file=json_file)
# extract all data as in json records
records = ins.get_all_worksheet(workbook=workbook)
df = ins.to_dataframe(records=records)
ins.upload_dataframe(df=df, workbook='sg_blogs_retrieved_data', sheet_name='test')


# this is the script-style process
import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds']
workbook = 'sg_blogs_retrieved_data'
json_file = '/home/fredyang/GitHub/GoogleSheetClient/MSO-projects-87dd9cc7a873.json'
creds = ServiceAccountCredentials.from_json_keyfile_name(json_file, scope)
gc = gspread.authorize(creds)
sh = gc.open(workbook)
col_num = len(df.columns)
sheet = sh.add_worksheet(title='test', rows=1, cols=col_num)
# update headers
for num in range(0, col_num):
    sheet.update_cell(1, num+1, df.columns[num])
for num in range(0, len(df)):
    sheet.append_row(df.iloc[num])