import pandas as pd
import json

# Load Recon config
f = open('.\\config\\Recon1.json')
fdata = f.read()
conf = json.loads(fdata)

print(conf)
print(conf['ReconciliationName'])

# Load Input files
CSVdf = pd.DataFrame(pd.read_csv(conf['AInputFilePath'], header=0))
print("-----------------------CSVdf--------------------------")
print(CSVdf)

XLSXdf = pd.DataFrame(pd.read_excel(conf['BInputFilePath'], header=0))
print("-----------------------XLSXdf--------------------------")
print(XLSXdf)

# Load compare columns and output columns
compare1_cols = conf['AInputFileCompareColumns'].split(',')
compare2_cols = conf['BInputFileCompareColumns'].split(',')
result_cols = conf['OutputFileColumns'].split(',')

res_df = pd.merge(CSVdf, XLSXdf, left_on=compare1_cols, right_on=compare2_cols, how='outer', suffixes=['_B1', '_B2'], indicator='match_result')
print("-----------------------res_df--------------------------")
print(res_df)

# res_df.loc[res_df['matched_result']!='both', 'matched_result'] = 'Unmatched'
# res_df.loc[res_df['matched_result']=='both', 'matched_result'] = 'Matched'

res_df['match_result'] = res_df['match_result'].replace(['both', 'left_only', 'right_only'], ['Matched', 'Unmatched', 'Unmatched'])

res_df = res_df[result_cols]

# Export csv or xlsx
if conf['OutputFilePath'].endswith('csv'):
    res_df.to_csv(conf['OutputFilePath'])
elif conf['OutputFilePath'].endswith('xlsx'):
    res_df.to_excel(conf['OutputFilePath'], sheet_name='sheet1')
else:
    print("The output file extension is Unexpected!!")


print("-----------------------res_df--------------------------")
print(res_df)

