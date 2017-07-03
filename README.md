# GoogleSheetClient
Automatic Downloading from and Uploading to Google Sheet from local settings

2017-05-24
Created. <br>
2017-07-03
Created Python Package.

### Before using the package:
follow [this link](https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html) as a step-by-step guide to enable Google Drive API, get credentials and share Workbooks.
<br><br>
Notes: The particular workbook to work with has to be **SHARED** with the email specified in json file.


### installation
Make sure you installed **pip & git** already. In the command line, type in
```python
pip install git+https://github.com/yang0339/TextPreViz.git
```

### Step-by-Step Guide
1. import modules
```python
from GoogleSheetClient.main_program import *
```
2. Use absolute path to refer to the path json_file is stored
```python
json_file = 'PATH2JsonFile/xxx.json'
```
3. Create an instance
```python
ins = GoogleSheetDownloader(json_file=json_file)
```
4. Test the connection
```python
ins.connection()
```

### Functionalities:

- ***get_one_worksheet(workbook, sheet_name)***: get a particular sheet from a workbook
- ***get_all_worksheet(workbook)***: get all sheets from a workbook
- ***to_dataframe(records)***: get_XXX_worksheet returns in json, use to_dataframe to convert to pandas DataFrame
- ***upload_dataframe(df, workbook, sheet_name)***: upload dataframe to a Google Drive. The workbook have to be created at first place.

### Use Case:
```python
# extract all data as in json records
workbook = 'example_workbook'
records = ins.get_all_worksheet(workbook=workbook) # all sheets have to be in the same format.
records_from_one_sheet = ins.get_one_worksheet(workbook=workbook, sheet_name="test")
# convert to dataframe
import pandas as pd
df = ins.to_dataframe(records=records)
df2 = ins.to_dataframe(records=records_from_one_sheet)
# upload dataframe: workbook and sheet have to be created before hand.
ins.upload_dataframe(df=df, workbook='example_workbook2', sheet_name='test2')
```
