# -*- coding: utf-8 -*-
import pandas as pd
import json


def info():
    read_excel_file = pd.read_excel('booking_Odessa.xlsx', sheet_name='Sheet1')
    df_excel = pd.DataFrame(read_excel_file)
    col = "Цена"
    price = df_excel[col].str[3:]
    currency = df_excel[col].str[:3]
    name = read_excel_file['Название']
    df_excel.insert(0, "Hotel_Name", name)
    df_excel.insert(1, "Price", price)
    df_excel.insert(2, "Currency", currency)

    def convert_to_int(val):
        new_val = ''.join([n for n in val if n.isdigit()])
        return int(new_val)

    df_excel['Price'] = df_excel['Price'].apply(convert_to_int)
    del df_excel['Цена']
    del df_excel['Название']
    min_price = df_excel[df_excel['Price'] == df_excel['Price'].min()]
    print(min_price)


info()
