import pandas as pd

data = pd.read_csv('weather_data.csv')
# print(data['temp'])

# print(data['temp'].max())

# print(data[data['day'] == "Monday"])

# print(f"Max tempature row is :\n{data[data['temp'] == data['temp'].max()]}")

monday = data[data.day == "Monday"]
temp_far = monday['temp'] * 1.8 + 32
print(temp_far)