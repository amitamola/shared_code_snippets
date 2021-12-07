'''If you want to use a list of values to select rows from a Pandas dataframe.

Credit for the answer- https://stackoverflow.com/a/12098586/2126357 and https://stackoverflow.com/a/19960116/2126357
'''
import pandas as pd
df = pd.DataFrame({'A': [5,6,3,4], 'B': [1,2,3,5]})

print(df[df['A'].isin([3, 6])])

#And to get the opposite use ~:

print(df[~df['A'].isin([3, 6])])
