import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import folium
from folium.plugins import HeatMap

dataframe = pd.read_csv('C:\\Users\\apoor\\Desktop\\Code\\IT ACADEMIC CODE\\Design Project - 5th Semester\\US_Accidents.csv')
numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']

# print(dataframe.head())
# print(dataframe.columns)
# print(dataframe.info())
# print(dataframe.describe())

# numeric_dataframe = dataframe.select_dtypes(include = numerics)
# print(len(numeric_dataframe.columns))

# missing_percent = dataframe.isna().sum().sort_values(ascending = False) / len(dataframe)
# missing_percent_plot = missing_percent[missing_percent != 0].plot(kind = 'barh')
# plt.tight_layout()
# plt.show()

# cities = dataframe['City'].unique()
# print(len(cities))

# city_accident = dataframe['City'].value_counts()
# print(city_accident)
# city_accident[:10].plot(kind = 'barh')
# plt.title('Accidents V/S City')
# plt.tight_layout()
# plt.show()

# sns.set_style('darkgrid')
# sns.histplot(city_accident, log_scale = True)
# plt.title('Histogram: Accidents V/S City')
# plt.tight_layout()
# plt.show()

# very_high_accident_city = city_accident[city_accident >= 25000]
# sns.set_style('darkgrid')
# sns.distplot(very_high_accident_city)
# plt.title('Very High Accident City Density Curve')
# plt.tight_layout()
# plt.show()

# high_accident_city = city_accident[(city_accident >= 10000) & (city_accident < 25000)]
# sns.set_style('darkgrid')
# sns.distplot(high_accident_city)
# plt.title('High Accident City Density Curve')
# plt.tight_layout()
# plt.show()

# low_accident_city = city_accident[city_accident < 10000]
# sns.set_style('darkgrid')
# sns.distplot(low_accident_city)
# plt.title('Low Accident City Density Curve')
# plt.tight_layout()
# plt.show()

# dataframe['Start_Time'] = pd.to_datetime(dataframe['Start_Time'])

# sns.set_style('darkgrid')
# sns.distplot(dataframe['Start_Time'].dt.hour, bins = 24, kde = False, norm_hist = True)
# plt.tight_layout()
# plt.show()

# sns.set_style('darkgrid')
# sns.distplot(dataframe['Start_Time'].dt.day_of_week, bins = 7, kde = False, norm_hist = True)
# plt.tight_layout()
# plt.show()

# sunday_start_time = dataframe['Start_Time'][dataframe['Start_Time'].dt.day_of_week == 0]
# sns.set_style('darkgrid')
# sns.distplot(sunday_start_time.dt.hour, bins = 24, kde = False, norm_hist = True)
# plt.tight_layout()
# plt.show()

# monday_start_time = dataframe['Start_Time'][dataframe['Start_Time'].dt.day_of_week == 6]
# sns.set_style('darkgrid')
# sns.distplot(monday_start_time.dt.hour, bins = 24, kde = False, norm_hist = True)
# plt.tight_layout()
# plt.show()

# dataframe_2016 = dataframe['Start_Time'][dataframe['Start_Time'].dt.year == 2016]
# sns.set_style('darkgrid')
# sns.distplot(dataframe_2016.dt.month, bins = 12, kde = False, norm_hist = True)
# plt.tight_layout()
# plt.show()

# dataframe_2018 = dataframe['Start_Time'][dataframe['Start_Time'].dt.year == 2018]
# sns.set_style('darkgrid')
# sns.distplot(dataframe_2018.dt.month, bins = 12, kde = False, norm_hist = True)
# plt.tight_layout()
# plt.show()

# dataframe_2020 = dataframe['Start_Time'][dataframe['Start_Time'].dt.year == 2020]
# sns.set_style('darkgrid')
# sns.distplot(dataframe_2020.dt.month, bins = 12, kde = False, norm_hist = True)
# plt.tight_layout()
# plt.show()

# sns.scatterplot(x = dataframe['Start_Lng'], y = dataframe['Start_Lat'], size = 0.001)
# plt.tight_layout()
# plt.show()

# latitude, longitude = dataframe['Start_Lat'][0], dataframe['Start_Lng'][0]
# latitude_longitude_pair = list(zip(list(dataframe['Start_Lat']), list(dataframe['Start_Lng'])))

# map = folium.Map()
# HeatMap(latitude_longitude_pair).add_to(map)
# map.save('map.html')

sample_dataframe = dataframe.sample(int(0.05 * len(dataframe)))

sample_latitude, sample_longitude = sample_dataframe['Start_Lat'], sample_dataframe['Start_Lng']
sample_latitude_longitude_pair = list(zip(list(sample_dataframe['Start_Lat']), list(sample_dataframe['Start_Lng'])))

sample_map = folium.Map()
HeatMap(sample_latitude_longitude_pair[0:10000]).add_to(sample_map)
sample_map.save('sample_map.html')