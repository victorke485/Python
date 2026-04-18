# with open("13_pandas/weather_data.csv") as file:
#     contents = file.readlines()
#     print(contents)

# import csv
# with open("13_pandas/weather_data.csv") as file:
#     data = csv.reader(file)
#     # for row in data:
#     #     print(row)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
        
#     print(f"Temperatures: {temperatures}")

# Pandas
import pandas as pd

# data = pd.read_csv("13_pandas/weather_data.csv")
# print(type(data))
# print(data)
# print(type(data["temp"]))



# Get data in Columns
# print(data["temp"])
# print(data.temp)

# Get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# print(monday.temp[0] * 1.8 + 32)



# Methods
# temp_list = data["temp"].to_list() # Converting to list
# print(temp_list)
# print(data["temp"].mean()) # Getting average
# print(data["temp"].max()) # Getting maximum value
# print(data.to_dict()) # Converting to dictionary


# Creating a dataframe from scratch
data_dict = {
    "students": ["Alex", "John", "Kim"],
    "scores": [56, 76, 86]
}
data = pd.DataFrame(data_dict)
print(data)

data.to_csv("13_pandas/new_data.csv")