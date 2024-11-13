import pandas as pd

df_1 = pd.read_csv("F:/3.5 Years/First Year/Python/Web Scarping/f1_ranking.csv")
print (df_1)

df_2 = pd.read_csv("F:/3.5 Years/First Year/Python/Web Scarping/f1_drivers_details.csv")
print (df_2)

df_1["Driver"] = df_1["Driver"].str[:-4]
print (df_1)


merged_df = pd.merge(df_1,df_2, on = 'Driver', how = 'inner')
print (merged_df)



print ("------------------------------------------------------------")
# tìm các tay đua có Grands Prix entered >= 300
query = merged_df[merged_df["Grands Prix entered"] >= 300]
print (query["Driver"])


print ("------------------------------------------------------------")
# tìm các tay đua có highest grid position = 1 và Grands Prix entered >= 200
query_2 = merged_df[(merged_df["Highest grid position"]) == 1 & (merged_df["Grands Prix entered"] >= 200)]
print (query_2["Driver"])


print ("------------------------------------------------------------")
# tìm tổng podium, số championships của từng team
query_3 = merged_df.groupby("Team").agg(
        total_podiums = pd.NamedAgg(column = "Podiums", aggfunc = 'sum'),
        total_world_championships = pd.NamedAgg(column = "World Championships", aggfunc = "sum")
        )

print (query_3)


print ("------------------------------------------------------------")
# hiện ra các nhà vô địch mà total world champion != 0
query_4 = merged_df[merged_df["World Championships"] != 0].groupby("Team")["World Championships"].sum()
print (query_4)


print ("------------------------------------------------------------")
# 2nd way
query_4_2nd = merged_df.groupby("Team").agg(
        total_championships = pd.NamedAgg(column = "World Championships", aggfunc = "sum")
    )

query_4_2nd = query_4_2nd[query_4_2nd["total_championships"] > 0]
print(query_4_2nd)

print ("------------------------------------------------------------")

# mean podium
mean_podium = merged_df["Podiums"].mean()
print (mean_podium)
print ("------------------------------------------------------------")

# meam points 
mean_points = merged_df["Points"].mean()
print (mean_points)
print ("------------------------------------------------------------")

# các team có tông điểm lớn hơn mean, cả số lần win podium
query_5 = merged_df.groupby("Team").agg(
        above_mean = pd.NamedAgg(column ="Points", aggfunc = lambda x : (x.sum() > mean_points)),
        Podiums_win  = pd.NamedAgg(column = "Podiums", aggfunc = "sum")
        )

print (query_5)
print ("------------------------------------------------------------")

# tìm các tay đua có top 1 trên 20 lần
# Split 'Highest race finish' to get the top position and the count
merged_df[['Top_Position', 'Times']] = merged_df['Highest race finish'].str.extract(r'(\d) \(x(\d+)\)')
# Convert the 'Times' column to integer for comparison
merged_df['Times'] = merged_df['Times'].astype(int)

# Filter for drivers who finished at position 1 more than 20 times
query_6 = merged_df[(merged_df['Top_Position'] == '1') & (merged_df['Times'] > 20)]
print(query_6[['Driver', 'Highest race finish']])

print ("------------------------------------------------------------")

# in các tay đua chưa có top 1 
query_7 = merged_df[merged_df["Top_Position"] > '1']
print(query_7[["Driver", "Highest race finish"]])
print ("------------------------------------------------------------")

# kiểm tra xem các tay đua của từng team có đạt top 1 hay chưa
query_8 = merged_df.groupby(["Team", "Driver"]).agg(
    top1_or_not = pd.NamedAgg(column = "Top_Position" , aggfunc = lambda x:(x == '1'))
        )
print (query_8)
