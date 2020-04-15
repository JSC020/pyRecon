import pandas as pd
import numpy as np

'''
Ldf = pd.DataFrame({'key1':['K0', 'K0', 'K1', 'K2'],
                    'key2':['K0', 'K1', 'K0', 'K1'],
                    'A':['A0', 'A1', 'A2', 'A3'],
                    'B':['B0', 'B1', 'B2', 'B3']})

Rdf = pd.DataFrame({'key1':['K0', 'K1', 'K1', 'K2'],
                    'key2':['K0', 'K0', 'K0', 'K0'],
                    'C':['C0', 'C1', 'C2', 'C3'],
                    'D':['D0', 'D1', 'D2', 'D3']})

matched_result = pd.merge(Ldf, Rdf, on=['key1', 'key2'])

left_result = pd.merge(Ldf, Rdf, how='left', on=['key1', 'key2'])

right_result = pd.merge(Ldf, Rdf, how='right', on=['key1', 'key2'])

outer_result = pd.merge(Ldf, Rdf, how='outer', on=['key1', 'key2'])

outer_indicator_result = pd.merge(Ldf, Rdf, how='outer', on=['key1', 'key2'], indicator='matched_indicator')
# validate: many_to_many, one_to_one, one_to_many, many_to_one
outer_validate_result = pd.merge(Ldf, Rdf, how='outer', on=['key1', 'key2'], validate='one_to_many')

print("-----------------------Ldf--------------------------")
print(Ldf)
print("-----------------------Rdf--------------------------")
print(Rdf)

print("-----------------------matched_result--------------------------")
print(matched_result)
print("-----------------------left_result--------------------------")
print(left_result)
print("-----------------------right_result--------------------------")
print(right_result)
print("-----------------------outer_result--------------------------")
print(outer_result)
print("-----------------------outer_indicator_result--------------------------")
print(outer_indicator_result)
print("-----------------------outer_validate_result--------------------------")
print(outer_validate_result)

'''

CSVdf = pd.DataFrame(pd.read_csv('.\\report\\Broker_P1.csv', header=0))
print("-----------------------CSVdf--------------------------")
print(CSVdf)

XLSXdf = pd.DataFrame(pd.read_excel('.\\report\\Broker_P2.xlsx', header=0))
print("-----------------------XLSXdf--------------------------")
print(XLSXdf)


compare_cols = ['Account', 'Current', 'Amount', 'Qty']
result_cols = ['Trader_P1', 'Account', 'Current', 'Amount', 'Qty', 'Trader_P2', 'result']

res_df = pd.merge(CSVdf, XLSXdf, on=compare_cols, how='outer', suffixes=['_P1', '_P2'], indicator='result')

res_df['result'] = res_df['result'].replace(['both', 'left_only', 'right_only'], ['Matched', 'Unmatched', 'Unmatched'])

print("-----------------------res_df--------------------------")
print(res_df)

# res_df = res_df[result_cols]

# export csv
# res_df.to_csv('.\\report\\result.csv')

# export xlsx
# writer = pd.ExcelWriter('.\\report\\result111.xlsx', date_format='YYYY-MM-DD')
# res_df.to_excel(writer, sheet_name='sheet1')
res_df.to_excel('.\\report\\result111.xlsx', sheet_name='sheet1')

