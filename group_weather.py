import numpy as np
import pandas as pd

df = pd.read_csv('Weather\\weather-raw.csv', header=None, names=['Timestamp', 'Temperature', 'Humidity', 'Dew Point', 'Pressure', 'Wind Speed', 'Wind Bearing', 'Sunshine', 'Rainfall', 'Max Wind Speed'])

df['Temperature'] /= 10
df['Dew Point'] /= 10
df['Wind Speed'] /= 10
df['Sunshine'] /= 100
df['Rainfall'] /= 1000

df.index = pd.to_datetime(df['Timestamp'])

# Part A
print("Fastest Speed: " + str(df['Wind Speed'].max()) + " knots") #questionable
print("Coldest Temperature: " + str(df['Temperature'].min()) + " degrees C") #impossible
print("Most Commond Wind Direction: " + str(df['Wind Bearing'].mode()))

# Part B
rain_daily = df['Rainfall'].resample('D').sum()
av_humid_yearly = df['Humidity'].resample('YE').mean()
av_temp_yearly = df['Temperature'].resample('YE').mean()
av_temp_month = df['Temperature'].resample('ME').mean()

print("Greatest Rainfall: " + str(rain_daily.max()) + " on", rain_daily.idxmax().day, rain_daily.idxmax().month, rain_daily.idxmax().year)

print("Least Average Humidity: " + str(av_humid_yearly.min()) + " in", av_humid_yearly.idxmin().year)

print("Greatest Average Temperature (Year): " + str(av_temp_yearly.max()) + " in",  av_temp_yearly.idxmax().year)

print("Greatest Average Temperature (Month): " + str(av_temp_month.max()) + " in", av_temp_month.idxmax().month, av_temp_month.idxmax().year)