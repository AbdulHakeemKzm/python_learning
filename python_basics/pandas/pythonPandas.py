import pandas

df=pandas.DataFrame([[2,4,6],[10,20,30]])
print(df, '\n')

df1=pandas.DataFrame([[2,4,6],[10,20,30,]],columns=["Price","Age","Value"])
print(df1, '\n')

df2=pandas.DataFrame([[2,4,6],[10,20,30,]],columns=["Price","Age","Value"],index=["First","Second"])
print(df2, '\n')

df3=pandas.DataFrame([{"Name":"jhon"},{"Name":"jack"}])
print(df3, '\n')

print(df.mean(), '\n')
print(df1.Price, '\n')
print(df1.Price.mean(),)
