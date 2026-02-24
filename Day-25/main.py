import csv
import pandas as pd 
with open("Day-25/weather_data.csv") as data_file:
    data = data_file.readlines()
    data = [line.strip() for line in data]
    print(data)

with open("Day-25/weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperature = []
    for row in data:
        print(row)
        if row[1]!='temp':
            temperature.append(int(row[1]))
    print(temperature)

data = pd.read_csv("Day-25/weather_data.csv")
print(data)
print(data["temp"])

dict_data = data.to_dict()
print(dict_data)
list_data = data["temp"].to_list()
print(list_data)

print(type(data))
print(type(data["temp"]))
print(data["temp"].mean())
print(data["temp"].max())
print(data["temp"].min())

print(data["condition"])
print(data.condition)

print(data[data.day=="Monday"])
print(data[data.temp==data.temp.max()])

monday = data[data.day=="Monday"]
print(monday)
print(type(monday))
print(monday.condition)
monday_temp = monday.temp[0]
monday_temp_f = monday_temp * 9/5 + 32
print(monday_temp_f)







