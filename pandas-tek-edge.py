########################
# pandas
#######################

import pandas as pd

####### Series - onedimentional array
ser = pd.Series([1,2,3,4,5,6],['a','b','c','d'])


######### indexing / selection - Series
ser['']
ser.loc[indexes]
ser.iloc[integres]

######### Data Frame - two dimensioanl
df = pd.Dataframe({'ones':pd.Series([1,2,3],['a','b','c']),
                    'two':pd.Series([4,5,6],['a','b','c'])})
df['column']['row']

pd.DataFrame(data, columns, index)

# Insert
df.pop(column_name)
df.insert(position, column_name, data)

########## Data Ingestion
import os
import os.chdir(path_copied)
df = pd.read_csv()

df.head()
df.tail()
df.info()
df.describe() # numerical stats of the dataframe

df['column_name']
df['column_name'].min()

################3
# matplotlib
################
