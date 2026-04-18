import pandas as pd
data = pd.read_csv("13_pandas/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260418.csv")

gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
}

new_data = pd.DataFrame(data_dict)
print(new_data)
new_data.to_csv("13_pandas/squirrel_count.csv")