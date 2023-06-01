import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import requests
import json

temp_list = []



# print(int(dt.datetime.now().strftime('%d')))
# print(int((dt.datetime.now() + dt.timedelta(days=7)).strftime('%d')))
days_list = []
for i in range(7):
    days_list.append((dt.datetime.now() + dt.timedelta(days=i)).strftime('%d'))
print(days_list)
days_list = []
for i in range(15):
    days_list.append(((dt.datetime.now() - dt.timedelta(days=7)) + dt.timedelta(days=i)).strftime('%d'))
print(days_list)


# def get_data(city):
#     url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/' \
#           f'{city}?unitGroup=metric&key=F9DYHJZYHS4KHS2YPKGQSJUXY&contentType=json'
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = json.loads(response.content)
#         data = data['days']
#         for j in range(9):
#             temp_list.append(data[j]['temp'])
#
#
# get_data('Grudziadz')
# print(temp_list)
#
# plt.title("Graph")
# plt.xticks(np.arange(len(days_list)), days_list)
# plt.xlabel('Days')
# plt.ylabel('avg temp °C')
# plt.plot(days_list, temp_list)
# plt.show()
