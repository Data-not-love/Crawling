import pandas as pd 


df_1 = pd.read_csv("F:/3.5 Years/First Year/Python/Web Scarping/f1_fastest_lap.csv")
print (df_1["Driver"])

print ("------------------------------------------------------------------")
df_2 = pd.read_csv("F:/3.5 Years/First Year/Python/Web Scarping/f1_drivers_details.csv")
print (df_2)

print ("------------------------------------------------------------------")

df_1["Driver"] = df_1["Driver"].str[:-4]
print (df_1)

print ("------------------------------------------------------------------")
# in data frame sau merge
merged_df = pd.merge(df_1,df_2, on = 'Driver', how = 'inner')
print (merged_df)

print ("------------------------------------------------------------------")
#
query_1 = merged_df[(merged_df["Time"] <= "1:25")]
print (query_1[["Grand Prix","Driver","Time"]])

print ("------------------------------------------------------------------")

# tìm lap record <= 1:24 và team  Mercesdes
query_2 = merged_df[(merged_df["Time"] <= "1:25") & (merged_df["Car"] == "Mercedes")]
print (query_2[["Grand Prix","Driver","Time"]])

# mean time
def time_to_seconds(time_str):
    minutes, seconds = time_str.split(':')
    return float(minutes) * 60 + float(seconds)


merged_df['Time in seconds'] = merged_df['Time'].apply(time_to_seconds)

print ("------------------------------------------------------------------")
# mean time
mean = merged_df["Time in seconds"].mean()
print ("Mean time in seconds : " + str(mean))

def seconds_to_minute (seconds):
    minutes = int(seconds // 60)
    remaining_seconds = round(seconds % 60, 3)
    return f"{minutes}:{remaining_seconds:05.3f}"


mean_to_minute = seconds_to_minute(mean)
print ("Reformated : " + str(mean_to_minute))

print ("------------------------------------------------------------------")
# tìm các tay đua có time < mean

query_3 = merged_df[merged_df["Time"] <= mean_to_minute ]
print (query_3[["Grand Prix","Driver","Time"]])




