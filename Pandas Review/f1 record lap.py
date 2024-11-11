import pandas as pd


dt_frame = pd.read_csv("F:/3.5 Years/First Year/Python/Web Scarping/f1_fastest_lap.csv")
print (dt_frame.columns)
print ("------------------------------------------------------------------")



# tìm các lap nhanh hơn 1:25
less_than_125 = dt_frame[dt_frame['Time'] < '1:25']
print (less_than_125)
print ("------------------------------------------------------------------")

# tìm các lap trong khoảng 1:25 đến 1:35
lap_range = dt_frame[ (dt_frame['Time'] >= '1:25') & (dt_frame['Time'] <= '1:35') ]
print (lap_range)
print ("------------------------------------------------------------------")



# tìm các record lap lớn hơn 1:35
lap_range_2 = dt_frame[dt_frame['Time'] >= '1:35']
print(lap_range_2)
print ("------------------------------------------------------------------")


# tìm các record lap của Ferrari
ferrari_record_lap = dt_frame[dt_frame['Car'] == 'Ferrari']
print (ferrari_record_lap)
print ("------------------------------------------------------------------")

# tìm các lap record dưới 1:17
less_than_117 = dt_frame[dt_frame['Time'] <= '1:17']
print (less_than_117)
print ("------------------------------------------------------------------")


print (dt_frame[['Time','Car']])
print ("------------------------------------------------------------------")


# tìm các lap record dưới 1:30 và team là Ferrari

result = dt_frame[(dt_frame['Time'] <= '1:30') & ((dt_frame['Car'] == "Mercedes") | (dt_frame['Car'] == 'Ferrari'))]
print (result)


