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
