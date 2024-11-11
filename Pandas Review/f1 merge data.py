import pandas as pd
df1 = pd.read_csv("F:/3.5 Years/First Year/Python/Web Scarping/f1_fastest_lap.csv")
print (df1.to_string(index=False))

df2 = pd.read_csv("F:/3.5 Years/First Year/Python/Web Scarping/f1_ranking.csv")
print (df2.to_string(index=False))


df2 = df2.drop(columns=['Pts','Pos'])

print ("------------------------------------------------------------------")
merged_df = pd.merge(df1, df2, on=['Driver', 'Car'], how='inner')
print(merged_df.to_string(index=False))

print ("------------------------------------------------------------------")
# hiện số lần win lap record của từng tay đua
result = merged_df.groupby("Driver").agg(
        count_record_lap = pd.NamedAgg (column = "Time" , aggfunc = 'count'))
print (result)

# hiện số lần win record lap dưới 1:20
query = merged_df[merged_df['Time'] <= "1:20"].groupby("Driver").agg(
        count = pd.NamedAgg(column = "Time" , aggfunc = "count")
        )
print (query)

# đếm số tay đua đạt record lap của từng quốc tịch
query_2 = merged_df.groupby("Nationality").agg(
    number_of_driver = pd.NamedAgg (column="Time", aggfunc = "count")
        )
print(query_2)


# đếm số lần đạt record lap của từng car
query_3 = merged_df.groupby("Car").agg(
    number_of_lap = pd.NamedAgg(column = "Time" , aggfunc = "count")
        )
print (query_3)
