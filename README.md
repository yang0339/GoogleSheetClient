# GoogleSheetClient
Automatic Downloading from and Uploading to Google Sheet from local settings

2017-05-24
Created.

Set-ups:
follow [this link](https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html) as a step-by-step guide to enable Google Drive API, get credentials and share Workbooks.

Use absolute path to refer to system path as well as json_file path
```python
import sys
sys.path.append('/home/fredyang/GitHub/GoogleSheetClient/google-sheet-downloader')
from main_program import *
scope = ['https://spreadsheets.google.com/feeds']
json_file = '/home/fredyang/GitHub/GoogleSheetClient/MSO-projects-87dd9cc7a873.json'
#  create a instance
ins = GoogleSheetDownloader(scope=scope, json_file=json_file)
```


Serveral functions:

- ***get_one_worksheet***: get a particular sheet from a workbook
- ***get_all_worksheet***: get all sheets from a workbook
- ***to_dataframe***: get_XXX_worksheet returns in json, use to_dataframe to convert to pandas DataFrame
- ***upload_dataframe***: upload dataframe to a Google Drive, but the workbook have to be created at first place.

An example:
```python
# extract all data as in json records
workbook = 'sg_blogs_retrieved_data'
records = ins.get_all_worksheet(workbook=workbook)
records_from_one_sheet = ins.get_one_worksheet(workbook=workbook, sheet_name="test")
# convert to dataframe
import pandas as pd
df = ins.to_dataframe(records=records)
# upload dataframe
ins.upload_dataframe(df=df, workbook='sg_blogs_retrieved_data', sheet_name='test')
```
