# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 15:42:28 2023

@author: jivbl
"""
import pandas as pd
import os
import urllib.request
import datetime

#this function is to ensure the datetime format is consistently in yyy-MM-dd format

def convert_date_format(df):
    for col in df.columns:
        try:
            #try to convert the column header to a date
            date = pd.to_datetime(col, errors='raise')
            #if successful, convert the date to the standard format of yyyy-MM-dd
            df = df.rename(columns={col: date.strftime('%Y-%m-%d')})
        except ValueError:
            #if the conversion fails, leave the column header unchanged
            continue
    return df

#This funcion validates the schema between the two dataframe in the form of a boolean if statement

def compare_dfs(dfOriginal, dfToCompare):
    if set(dfOriginal.columns) == set(dfToCompare.columns):
        if dfOriginal.dtypes.equals(dfToCompare.dtypes):
            if dfOriginal.equals(dfToCompare):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

#url for the page from which to scrape the data from

url = "https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1126335/ET_3.1_DEC_22.xlsx"

# Get the filename from the url

filename = url.split('/')[-1]
namefile = filename.split('.')[0]
namefile = namefile + ".csv"

# Check if the file exists

if os.path.exists(filename):
  
    
    m_time = os.path.getmtime(filename)
    # convert timestamp into DateTime object
    modified_date = datetime.datetime.fromtimestamp(m_time)
    
    # Get the last modified date of the file link
    response = urllib.request.urlopen(url)
    request_date = response.headers['Last-Modified']
    
    datetimeToCompare = datetime.datetime.strptime(request_date, "%a, %d %b %Y %H:%M:%S %Z")
    # Compare the two dates
    if modified_date > datetimeToCompare:
        # Download the file if the file link is more recent than the file on the computer
        urllib.request.urlretrieve(url, filename)

# Download the file if the file does not exist on the computer
else:
   urllib.request.urlretrieve(url, filename)

#Clean data
#Load excel file into pandas dataframe

df = pd.read_excel(filename, sheet_name = "Quarter", index_col=(False))

#replace missing values with empty string (This is wrong as it only replacing the first gap and not gap after data)

#TODO Also DELETE DATA UNDER Excel file
df.fillna("", inplace=True)

#Remove unnecessary information (This is wrong as it only replacing the first gap and not gap after data)
#TODO Also DELETE DATA UNDER Excel file

df = df.drop(df.index[:3])

#make Date row into header columns

df.columns = df.iloc[0]

df = df[1:]

#reset the index

df = df.reset_index(drop=True)

#replacer dict to replace YYYY ___ quarter into YYYY-MM-dd

quarters_mapping = {
    '1st quarter': '-03-31',
    '2nd quarter': '-06-30',
    '3rd quarter': '-09-30',
    '3nd quarter': '-09-30',
    '4th quarter': '-12-31',
    '[provisional]' :'',
    ' ' : ''
}
#replacer dict to replace newline marker

newline_remover = {'\n' : ''}

#replacer dict to replace first column title

first_column_name = {'Cum1' : 'Energy Categories'}

print(df.iloc[0])

df.columns = df.columns.to_series().replace(quarters_mapping, regex=True)
df.columns = df.columns.to_series().replace(newline_remover, regex=True)
df.columns = df.columns.to_series().replace(first_column_name, regex=True)
print (df)

print(df.iloc[0])

#Ensure that any dates and timestamps are converted into a standard dateformat

#convert header row into YYY-MM-dd format

df = convert_date_format(df)
print(df)

#check if old dataframe exists, if not, then convert df to csv, if exists, check current and existing schema are the same
if (os.path.isfile(namefile)):
    dfToCompare = pd.read_csv(namefile)
    if (compare_dfs(df,dfToCompare)):
        df.to_csv(namefile)
else: df.to_csv(namefile, encoding = "utf-8-sig", index = False)


