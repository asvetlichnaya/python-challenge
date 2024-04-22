import pandas as pd
import openpyxl
from openpyxl.utils.dataframe import dataframe_to_rows


def get_points(df):
    df['points'] = df['chocolate'] * 3 + df['regular']
    return df


def get_winner(df):
    filtered_df = df[df['points'] == max(df['points'])]
    return filtered_df['name'].values


def get_count_of_eggs(chocolate):
    return sum(chocolate)


def get_family_points(df):
    return df.groupby('family')['points'].sum()


df = pd.read_csv('egghunt.csv')

df_with_points = get_points(df)

winners = get_winner(df_with_points)
print('Winners are ', winners)

print('There are ', get_count_of_eggs(df['chocolate']), ' chocolate eggs')

print('Individual result: \n', df[['name', 'points']])

print('Team result: \n', get_family_points(df_with_points))

wb = openpyxl.Workbook()
sheet = wb.active

for r in dataframe_to_rows(df[['name', 'points']], index=False, header=True):
    sheet.append(r)

wb.save("result.xlsx")

print('Show the content of excel file: \n', pd.read_excel('result.xlsx'))

