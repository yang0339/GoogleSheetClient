from GoogleSheetClient.main_program import *
workbook = 'sg_blogs_retrieved_data'
json_file = ''
#  create a instance
ins = GoogleSheetDownloader(json_file=json_file)
# extract all data as in json records
records = ins.get_all_worksheet(workbook=workbook)
df = ins.to_dataframe(records=records)
ins.upload_dataframe(df=df, workbook='sg_blogs_retrieved_data', sheet_name='test')