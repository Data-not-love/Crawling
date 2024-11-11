import pandas as pd


dt_frame = pd.read_csv("F:/3.5 Years/First Year/Python/Web Scarping/f1_ranking.csv")
print (dt_frame.to_string(index=False))


# tìm tổng điểm của 2 tay đua cùng loại xe và sắp xếp
result = dt_frame.groupby("Car").agg(
    sum_pts = pd.NamedAgg(column="Pts",aggfunc="sum")
)
print(result.sort_values(by="sum_pts", ascending=False))


# nhóm tay đua có Nationality GBR
result_2 = len(dt_frame[dt_frame["Nationality"] == 'GBR'])
print(result_2)

# cách 2
result_2_2nd = dt_frame[dt_frame["Nationality"] == 'GBR'].sum
print(result_2)

print ("-----------------------------------------------------------------------------------")
# kiểm tra quốc tịch của các tay đua
result_3 = dt_frame.groupby("Driver").agg(
        GBR_nationality = pd.NamedAgg(column="Nationality", aggfunc = lambda x :(x == 'GBR'))
        )
print ( result_3[result_3['GBR_nationality']] == True )




# kiểm tra các tay đua người GBR có điểm > 100
result_3_2nd = dt_frame[dt_frame["Nationality"] == 'GBR'].groupby("Driver").agg(
    Above_100_and_GBR = pd.NamedAgg(column='Pts', aggfunc=lambda x :(x>100))
)
print (result_3_2nd[result_3_2nd['Above_100_and_GBR']] == True)



# trung bình điểm
result_4 = dt_frame['Pts'].mean()
print ("Mean : "+str(result_4))

# mode 

result_5 = dt_frame['Pts'].mode()
print(result_5)

# median
result_6 = dt_frame['Pts'].median()
print(result_6)




# Step 1: Calculate total points for each team

# tìm các Car có trên tổng điểm trên mean
result_7 = dt_frame.groupby('Car').agg(
        Point_above_mean = pd.NamedAgg(column='Pts',aggfunc= lambda x:(x.sum()> result_4))
)
print (result_7[result_7['Point_above_mean']] == True)



# tìm cách driver có điểm lớn hớn median
result_8 = dt_frame.groupby('Driver').agg(
        Point_above_median = pd.NamedAgg(column='Pts', aggfunc = lambda x:(x > result_6))
        )
print (result_8[result_8['Point_above_median']] == True)


result_9 = dt_frame.groupby(['Car','Driver']).agg(
        Point = pd.NamedAgg(column='Pts',aggfunc = 'sum'),
        Above_mean = pd.NamedAgg(column='Pts', aggfunc = lambda x:(x.sum() > result_4))
        )
print (result_9)


# tìm driver có quốc tịch GBR và điểm trên 70
my_query = dt_frame[(dt_frame['Nationality'] == 'GBR') & (dt_frame['Pts'] > 70)]
print (my_query)


# đếm số lượng tay đua của mỗi Car và tổng điểm các tay đua cùng team
number_of_racers = dt_frame.groupby("Car").agg(
        number_of_racers_each_car = pd.NamedAgg(column = "Car", aggfunc = 'count'),
        total_point = pd.NamedAgg(column = 'Pts', aggfunc = 'sum')
        )

print (number_of_racers)

# đếm số lượng tay đua mỗi nước
number_of_racer_each_country = dt_frame.groupby("Nationality").agg(
    Number_of_racer = pd.NamedAgg(column = "Nationality", aggfunc = "count")
        )
print (number_of_racer_each_country)

# 2nd way
number_of_racer_each_country = dt_frame["Nationality"].value_counts()
print(number_of_racer_each_country)


