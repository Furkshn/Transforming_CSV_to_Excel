
############################################################

#               Converting CSV to Excel

############################################################



import pandas as pd


def converting_func(file_name):               # Only file name, not adding file format type


    df_reading_file = pd.read_csv(file_name + ".csv",encoding= 'unicode_escape')     # Reading csv format

    excel_file = pd.ExcelWriter(file_name + ".xlsx")    # Generating excel format

    df_reading_file.to_excel(excel_file, index=False)   # Converting csv to excel(xlsx)

    excel_file.save()       # Save xlsx file


converting_func("Test")   # File name parameter



