import gspread


class GoogleSheetDownloader(object):
    def __init__(self, json_file):
        """
        credentials to access google sheet
        follow https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html
        for step-by-step guide
        """
        self.scope = ['https://spreadsheets.google.com/feeds']
        self.json_file = json_file


    def connection(self):
        from oauth2client.service_account import ServiceAccountCredentials
        try:
            creds = ServiceAccountCredentials.from_json_keyfile_name(self.json_file, self.scope)
            # client = gspread.authorize(creds)
            print("connection established.\n")
        except:
            print("Connection failed. Check json file, worksheet configurations.")
        return creds

    def get_one_worksheet(self, workbook, sheet_name):
        gc = gspread.authorize(self.connection())
        sh = gc.open(workbook).worksheet(sheet_name)
        records = sh.get_all_records()
        print("Worksheet \"%s\" has been downloaded."%sheet_name)
        return records

    def get_all_worksheet(self, workbook):
        gc = gspread.authorize(self.connection())
        sh = gc.open(workbook)
        worksheet_list = sh.worksheets()
        records = []
        for item in worksheet_list:
            current_sheet = sh.worksheet(item._title)
            print("Downloading: ", current_sheet._title)
            # Extract all records
            records += current_sheet.get_all_records()
            print("\n")
        return records


    def upload_dataframe(self, df, workbook, sheet_name):
        gc = gspread.authorize(self.connection())
        try:
            sh = gc.open(workbook)
        except:
            print("Unknown name. Please firstly create a blank spreadsheet.")
            return
        # number of columns to create
        col_num = len(df.columns)
        sheet = sh.add_worksheet(title=sheet_name, rows=1, cols=col_num)
        # update headers
        for num in range(0,col_num):
            sheet.update_cell(num+1, 1, df.columns[num])
        print("uploading dataframe, this process might take some time.\n")
        for num in range(0,len(df)):
            sheet.append_row(df.iloc[num])


def to_dataframe(records):
    import pandas as pd
    import json
    df = pd.read_json(json.dumps(records))
    try:
        df.drop(labels='', axis=1, inplace=True)  # drop unnamed columns/excessive index
    except ValueError:
        pass
    return df