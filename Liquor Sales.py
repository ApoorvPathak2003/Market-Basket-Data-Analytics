import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

liquor_dataframe = pd.read_csv('C:\\Users\\apoor\\Desktop\\Code\\IT ACADEMIC CODE\\Design Project - 5th Semester\\Liquor Sales (Jan 2021-Jan 2022).csv')
# accident_dataframe = pd.read_csv('C:\\Users\\apoor\\Desktop\\Code\\IT ACADEMIC CODE\\Design Project - 5th Semester\\US_Accidents.csv')
modified_liquor_dataframe = liquor_dataframe[['store_name', 'city', 'address', 'category', 'item_description', 'sale_dollars', 'volume_sold_liters']].copy()
# modified_accident_dataframe = accident_dataframe[['City', 'State', 'Timezone', 'Street', 'Traffic_Signal', 'Sunrise_Sunset']].copy()

# print(modified_liquor_dataframe.describe())

# print(liquor_dataframe.head())
# print(liquor_dataframe.columns)
# print(modified_liquor_dataframe.head())
# print(modified_liquor_dataframe.columns)
# print(accident_dataframe.head())
# print(accident_dataframe.columns)

# accident_dataframe['Start_Time'] = pd.to_datetime(accident_dataframe['Start_Time'])

# dataframe_2020 = accident_dataframe['Start_Time'][accident_dataframe['Start_Time'].dt.year == 2020]
# sns.set_styl[e('darkgrid')
# sns.distplot(dataframe_2020.dt.month, bins = 12, kde = False, norm_hist = True)
# plt.title('Accidents in 2020')
# plt.tight_layout()
# plt.show()

# dataframe_2021 = accident_dataframe['Start_Time'][accident_dataframe['Start_Time'].dt.year == 2021]
# sns.set_style('darkgrid')
# sns.distplot(dataframe_2021.dt.month, bins = 12, kde = False, norm_hist = True)
# plt.title('Accidents in 2021')
# plt.tight_layout()
# plt.show()

stores_grouped_modified_liquor_dataframe = modified_liquor_dataframe.groupby(by = 'store_name').sum()
# print(stores_grouped_modified_liquor_dataframe.head())

# print(stores_grouped_modified_liquor_dataframe.sort_values(by = 'sale_dollars', ascending = False).head())

# bar_px = px.bar(x = 'city', y = 'sale_dollars', title = 'Top 100 countries with maximum alcohol sales', data_frame = modified_liquor_dataframe.head(100))
# bar_px.show()

# print(len(modified_liquor_dataframe['city'].unique()))

# fig, axis = plt.subplots(figsize = (10, 6))
# sns.heatmap(stores_grouped_modified_liquor_dataframe.corr(), annot = True, fmt = "0.3f", ax = axis)
# plt.show()

modified_liquor_dataframe['sale_dollars'] = modified_liquor_dataframe['sale_dollars'].head(15).astype(str)
modified_liquor_dataframe['volume_sold_liters'] = modified_liquor_dataframe['volume_sold_liters'].head(15).astype(str)
modified_liquor_dataframe['category'] = modified_liquor_dataframe['category'].head(15).astype(str)
modified_liquor_dataframe['city'] = modified_liquor_dataframe['city'].head(15).astype(str)

# plt.figure(figsize = (10, 7))
# plt.plot(modified_liquor_dataframe['city'].head(15), modified_liquor_dataframe['sale_dollars'].head(15))
# plt.plot(modified_liquor_dataframe['city'].head(15), modified_liquor_dataframe['volume_sold_liters'].head(15))
# plt.plot(modified_liquor_dataframe['city'].head(15), modified_liquor_dataframe['category'].head(15))
# plt.xticks(rotation = 90)
# plt.xlabel('City')
# plt.tight_layout()
# plt.legend(['sale_dollars', 'volume_sold_liters', 'category'])
# plt.show()

volumne_alcohol_sold_dataframe = modified_liquor_dataframe.groupby(by = 'city').sum()

# plt.figure(figsize = (10, 7))
# sns.histplot(volumne_alcohol_sold_dataframe['volume_sold_liters'])
# plt.title('Distribution of Total Litres of Alcohol')
# plt.tight_layout()
# plt.show()

# print(modified_liquor_dataframe['city'].loc[modified_liquor_dataframe['volume_sold_liters'].values == modified_liquor_dataframe['volume_sold_liters'].min()])
# print(modified_liquor_dataframe['city'].loc[modified_liquor_dataframe['volume_sold_liters']])
# print(modified_liquor_dataframe['volume_sold_liters'].min())
print(modified_liquor_dataframe['city'].loc[modified_liquor_dataframe['volume_sold_liters']])