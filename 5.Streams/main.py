"""""""""
2. Откройте и прочитайте данные с файла lorum.txt, способом,
который рассматривается в видео из пункта 1.
"""
file = open('lorum.txt', 'r')
print(file.readlines())
file.close()
"""
5. Посмотрите видео про контекстный менеджер 
и повторите все действия из видео с файлом из пункта 2
"""
import os
import threading
import aiohttp

with open('lorum.txt', 'r') as file:
    print(file.readlines())

with os.scandir(".") as entryes:
    for entry in entryes:
        print(entry.name, "->", entry.stat().st_size, "bytes")

balance_lock = threading.Lock()
with balance_lock:
    pass

async with aiohttp.ClientSession() as session:
    async with session.get('google.com') as response:
        print(response.status)
"""
6. Прочитайте статью и выполните действия, которые там указаны с файлом bikes.csv
"""
import pandas as pd
import pathlib

work_path = pathlib.Path.cwd()
data_path = pathlib.Path(work_path, '5.Streams', 'bikes.csv')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
data = pd.read_csv(data_path)
print(data.head(100))
"""
7. Посчитайте сумму столбца Rachel1 из файла bikes.csv
"""
import pandas as pd
import pathlib

work_path = pathlib.Path.cwd()
data_path = pathlib.Path(work_path, '5.Streams', 'bikes.csv')
data = pd.read_csv(data_path)
col_sum = 0
print([col_sum := data['Rachel1'][i] + col_sum for i in range(len(data))])
print(col_sum)
print(data['Rachel1'].sum())
"""
8. Прочитайте семь первых статей по работе с pandas и выполните из них все действия
"""
"""Часть 1: Чтение данных из csv файла"""
import pandas as pd
import matplotlib.pyplot as plt
import pathlib

plt.style.use('ggplot')  # Красивые графики
plt.rcParams['figure.figsize'] = (15, 5)  # Размер картинок

work_path = pathlib.Path.cwd()
data_path = pathlib.Path(work_path, '5.Streams', 'bikes_2.csv')
fixed_df = pd.read_csv(filepath_or_buffer=data_path,  # Это то, куда вы скачали файл
                       sep=';',
                       encoding='latin1',
                       parse_dates=['Date'],
                       dayfirst=True,
                       index_col='Date')
fixed_df['Berri 1'].plot()
fixed_df.plot(figsize=(15, 10))
"""Часть 2: Выбор данных и нахождение наиболее частых жалоб"""
import pandas as pd
import matplotlib.pyplot as plt
import pathlib

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (10, 5)

work_path = pathlib.Path.cwd()
data_path = pathlib.Path(work_path, '5.Streams', '311-service-requests.csv')
complaints = pd.read_csv(data_path)
# Первые 5 строк
print(complaints[:5])
# Первый столбец у первых 5 строк
print(complaints['Complaint Type'][:5])
# Два столбца
print(complaints[['Complaint Type', 'Borough']])
# Первые 10 строк двух столбцов
print(complaints[['Complaint Type', 'Borough']][:10])
# Количество одинаковых значений
print(complaint_counts := complaints['Complaint Type'].value_counts())
# Первые 10 из одинаковых
print(complaint_counts[:10])
# График
complaint_counts[:10].plot(kind='bar')
"""Часть 3: объединение и группировка данных"""
import pandas as pd
import matplotlib.pyplot as plt
import pathlib

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (10, 5)

work_path = pathlib.Path.cwd()
data_path = pathlib.Path(work_path, '5.Streams', 'bikes_2.csv')
bikes = pd.read_csv(filepath_or_buffer=data_path,
                    sep=';',
                    encoding='latin1',
                    parse_dates=['Date'],
                    dayfirst=True,
                    index_col='Date')

bikes['Berri 1'].plot()
berri_bikes = bikes[['Berri 1']].copy()
# print(berri_bikes[:5])
berri_bikes.loc[:, 'weekday'] = berri_bikes.index.weekday
# print(berri_bikes[:5])
weekday_counts = berri_bikes.groupby('weekday').aggregate(sum).sum()
# print(weekday_counts)
weekday_counts.index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# print(weekday_counts)
weekday_counts.plot(kind='bar')
"""Часть 4: объединение нескольких dataframe"""
import pandas as pd
import matplotlib.pyplot as plt
import pathlib


def download_weather_month(year, month, name_columns, url):
    download_url = url.format(year=year, month=month)
    weather_data = pd.read_csv(filepath_or_buffer=download_url,
                               index_col='Date/Time (LST)',
                               encoding='latin1')
    weather_data.columns = name_columns
    weather_data = weather_data.dropna(axis=1)
    weather_data = weather_data.drop(labels=['Longitude', 'Latitude',
                                             'Year', 'Month',
                                             'Day', 'Time'],
                                     axis=1)
    return weather_data


pd.options.display.max_rows = 7
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 3)
plt.rcParams['font.family'] = 'sans-serif'
url_template = ("http://climate.weather.gc.ca/climate_data/bulk_data_e.html?"
                + "format=csv&"
                + "stationID=5415&"
                + "Year={year}&"
                + "Month={month}&"
                + "timeframe=1&"
                + "submit=Download+Data")

# url = url_template.format(month=3, year=2012)
# weather_mar2012 = pd.read_csv(filepath_or_buffer=url,
#                              index_col='Date/Time (LST)',
#                              parse_dates=True,
#                              encoding='latin1')
# print(weather_mar2012)
# weather_mar2012['Temp (Â°C)'].plot(figsize=(15, 5))
data_columns = [
    u'Longitude', u'Latitude', u'Station Name',
    u'Climate ID', u'Year', u'Month',
    u'Day', u'Time', u'Temp (C)',
    u'Temp Flag', u'Dew Point Temp', u'Dew Point Temp Flag',
    u'Rel Hum', u'Rel Hum Flag', u'Precip. Amount',
    u'Precip. Amount Flag', u'Wind Dir (10s deg)', u'Wind Dir Flag',
    u'Wind Spd (km/h)', u'Wind Spd Flag', u'Visibility (km)',
    u'Visibility Flag', u'Stn Press (kPa)', u'Stn Press Flag',
    u'Hmdx', u'Hmdx Flag", u', u'Wind Chill',
    u'Wind Chill Flag', u'Weather']
# weather_mar2012.columns = data_columns
# weather_mar2012 = weather_mar2012.dropna(axis=1, how='any')
# weather_mar2012 = weather_mar2012.drop(labels=['Longitude', 'Latitude',
#                                                'Year', 'Month',
#                                                'Day', 'Time'],
#                                        axis=1)
# print(weather_mar2012[:5])

# temperatures = weather_mar2012[[u'Temp (C)']].copy()
# temperatures.loc[:, 'Hour'] = weather_mar2012.index.hour
# temperatures.groupby('Hour').median().plot()

# print(download_weather_month(2012, 1)[:5])

data_by_month = [download_weather_month(2012, i, data_columns, url_template) for i in range(1, 13)]
weather_2012 = pd.concat(data_by_month)

work_path = pathlib.Path.cwd()
data_path = pathlib.Path(work_path, '5.Streams', 'weather_2012.csv')
weather_2012.to_csv(data_path, encoding='latin1')

weather_2012_final = pd.read_csv(filepath_or_buffer=data_path,
                                 encoding='latin1',
                                 index_col='Date/Time (LST)')
weather_2012_final[u'Temp (C)'].plot()
plt.show(block=True)
"""Часть 5: ищем самый снежный месяц"""
import pandas as pd
import matplotlib.pyplot as plt
import pathlib

pd.options.display.max_rows = 7
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 3)
plt.rcParams['font.family'] = 'sans-serif'

work_path = pathlib.Path.cwd()
data_path = pathlib.Path(work_path, '5.Streams', 'weather_2012.csv')
weather_2012 = pd.read_csv(filepath_or_buffer=data_path,
                           parse_dates=True,
                           index_col='Date/Time (LST)')
print(weather_2012[:5])
weather_description = weather_2012['Weather']
is_snowing = weather_description.str.contains('Snow')
print(is_snowing[:5])
is_snowing = is_snowing.astype(int)
is_snowing.plot()

weather_2012['Temp (C)'].resample('ME').median().plot(kind='bar')
plt.show(block=True)

is_snowing.astype(int).resample('ME').mean()

print(is_snowing.astype(int)[:10])

is_snowing.astype(int).resample('ME').mean().plot(kind='bar')
plt.show(block=True)

temperature = weather_2012['Temp (C)'].resample('ME').median()
is_snowing = weather_2012['Weather'].str.contains('Snow')
snowiness = is_snowing.astype(int).resample('ME').mean()

temperature.name = "Temperature"
snowiness.name = "Snowiness"

stats = pd.concat([temperature, snowiness], axis=1)
print(stats)

stats.plot(kind='bar')
plt.show(block=True)

stats.plot(kind='bar', subplots=True, figsize=(15, 10))
plt.show(block=True)
"""Часть 6: работа с загрязненными данными"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pathlib

pd.options.display.max_rows = 7
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 3)
plt.rcParams['font.family'] = 'sans-serif'

requests = pd.read_csv('data/311-service-requests.csv')

requests['Incident Zip'].unique()

na_values = ['NO CLUE', 'N/A', '0', ]

work_path = pathlib.Path.cwd()
data_path = pathlib.Path(work_path, '5.Streams', '311-service-requests.csv')
requests = pd.read_csv(filepath_or_buffer=data_path,
                       na_values=na_values,
                       dtype={'Incident Zip': str, })

requests['Incident Zip'].unique()

rows_with_dashes = requests['Incident Zip'].str.contains('-').fillna(False)
len(requests[rows_with_dashes])

print(requests[rows_with_dashes]['Incident Zip'])

long_zip_codes = requests['Incident Zip'].str.len() > 5
requests['Incident Zip'][long_zip_codes].unique()

requests['Incident Zip'] = requests['Incident Zip'].str.slice(0, 5)
print(requests[requests['Incident Zip'] == '00000'])

zero_zips = requests['Incident Zip'] == '00000'
requests.loc[zero_zips, 'Incident Zip'] = np.nan

unique_zips = requests['Incident Zip'].unique()
print(unique_zips)

zips = requests['Incident Zip']
# Let's say the zips starting with '0' and '1' are okay, for now. (this isn't actually true -- 13221 is in Syracuse,
# and why?)
is_close = zips.str.startswith('0') | zips.str.startswith('1')
# There are a bunch of NaNs, but we're not interested in them right now, so we'll say they're False
is_far = ~is_close & zips.notnull()

print(zips[is_far])

requests[is_far][['Incident Zip', 'Descriptor', 'City']].sort_values('Incident Zip')

requests['City'].str.upper().value_counts()
"""Часть 7: работа с датами и временем"""
import pandas as pd
import matplotlib.pyplot as plt
import pathlib
import numpy as np

plt.style.use('ggplot')  # Красивые графики
plt.rcParams['figure.figsize'] = (15, 5)  # Размер картинок

# Read it, and remove the last row
work_path = pathlib.Path.cwd()
data_path = pathlib.Path(work_path, '5.Streams', 'popularity-contest.csv')
popcon = pd.read_csv(filepath_or_buffer=work_path, sep=' ')[:-1]
popcon.columns = ['atime', 'ctime', 'package-name', 'mru-program', 'tag']

print(popcon[:5])

popcon['atime'] = popcon['atime'].astype(int)
popcon['ctime'] = popcon['ctime'].astype(int)

popcon['atime'] = pd.to_datetime(popcon['atime'], unit='s')
popcon['ctime'] = pd.to_datetime(popcon['ctime'], unit='s')

print(popcon['atime'].dtype)
print(popcon[:5])

popcon = popcon[popcon['atime'] > '1970-01-01']

nonlibraries = popcon[~popcon['package-name'].str.contains('lib')]

print(nonlibraries.sort_values('ctime', ascending=False)[:10])
