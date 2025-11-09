# import pandas as pd
# df = pd.DataFrame()
# print(df)

# import pandas as pd
# data=[1,2,3,4,5]
# df = pd.DataFrame(data)
# print(df)

# import pandas as pd
# data = [['Alex',10], ['Bob',11], ['Cacto',12]]
# df = pd.DataFrame(data,columns=['Name','Age'])
# print(df)

# import pandas as pd
# data=[['Alex',10],['Bob',11],['Cacty',12]]
# df = pd.DataFrame(data,columns=['Name','Age'],dtype=float)
# print(df)

# import pandas as pd
# data={'Name':['Alex','Ricky','Steve','Mike'], 'Age':[10,11,12,14]}
# df = pd.DataFrame(data)
# print(df)

# import pandas as pd
# data={'Name':['Alex','Bob','Cacty','Ricky'],'Age':[10,11,12,14]}
# df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
# print(df)

# import pandas as pd
# data=[{'a':1,'b':2}, {'a':10,'b':20,'c':30}]
# df = pd.DataFrame(data)
# print(df)

# import pandas as pd
# data=[{'a':1,'b':2},{'a':10,'b':20,'c':30}]
# df = pd.DataFrame(data,index=['first','second'])
# print(df)

# import pandas as pd
# data=[{'a':1,'b':2}, {'a':10,'b':20,'c':30}]
# df1=pd.DataFrame(data,index=['first','second'],columns=['a','b'])
# df2=pd.DataFrame(data,index=['first','second'],columns=['a','b1'])
# print(df1)
# print(df2)

# import pandas as pd
#
# d = {'one': pd.Series([1,2,3],index=['a','b','c']),
#      'two': pd.Series([1,2,3,4], index=['a','b','c','d'])}
#
# df = pd.DataFrame(d)
# print(df)

# import pandas as pd
#
# d = {'one': pd.Series([1,2,3], index=['a','b','c']),
#      'two': pd.Series([1,2,3,4], index=['a','b','c','d'])}
#
# df = pd.Series(d)
# print(df['one'])

# import pandas as pd
#
# d = {'one':pd.Series([1,2,3], index=['a','b','c']),
#      'two':pd.Series([1,2,3,4], index=['a','b','c','d'])}
#
# df = pd.DataFrame(d)
# print(df)
#
# print("\nAdding a new column  by passing as series")
# df['three'] = pd.Series([1,2,3,4], index=['a','b','c','d'])
# print(df)
#
# print("\nAdding a new column using existing columns in dataframe")
# df['four'] = df['one'] + df['three']
# print(df)

# import pandas as pd
# d = {'one': pd.Series([1,2,3], index=['a','b','c']),
#      'two': pd.Series([1,2,3,4], index=['a','b','c','d']),
#      'three': pd.Series([1,2,3], index=['a','b','c'])}
# df = pd.DataFrame(d)
# print("Our DataFrame is:")
# print(df)
#
# print("\ndel function")
# del df['one']
# print(df)
#
# print("\npop function")
# df.pop('three')
# print(df)

# import pandas as pd
#
# d = {'one':pd.Series([1,2,3], index=['a','b','c']),
#      'two':pd.Series([1,2,3,4], index=['a','b','c','d'])}
# df = pd.DataFrame(d)
# print(df.loc['b'])
#
# import pandas as pd
#
# d = {'one':pd.Series([1,2,3], index=['a','b','c']),
#      'two':pd.Series([1,2,3,4], index=['a','b','c','d'])}
# df = pd.DataFrame(d)
# print(df.iloc[3])

# import pandas as pd
# d = {'one':pd.Series([1,2,3], index=['a','b','c']),
#       'two':pd.Series([1,2,3,4],index=['a','b','c','d'])}
# df = pd.DataFrame(d)
# print(df[2:4])

# import pandas as pd
#
# df1 = pd.DataFrame([[1,2],[3,4]], columns=['a','b'])
# df2 = pd.DataFrame([[5,6],[7,8]], columns=['a','b'])
#
# df1 = df1._append(df2)
# print(df1)

import pandas as pd

df1 = pd.DataFrame([[1,2],[3,4]],columns=['a','b'])
df2 = pd.DataFrame([[5,6],[7,8]], columns=['a','b'])

df1 = df1._append((df2))
print(df1)

df1 = df1.drop(0)
print(df1)