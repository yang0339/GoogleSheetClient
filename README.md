# GoogleSheetClient
Automatic Downloading from and Uploading to Google Sheet from local settings

2017-05-24
Created.

Serveral functions:

- get_one_worksheet: get a particular sheet from a workbook
- get_all_worksheet: get all sheets from a workbook
- to_dataframe: get_XXX_worksheet returns in json, use to_dataframe to convert to pandas DataFrame
- upload_dataframe: upload dataframe to a Google Drive, but the workbook have to be created at first place.
