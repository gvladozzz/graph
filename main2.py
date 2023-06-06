from datetime import datetime
from influxdb import InfluxDBClient


def num(event):
    return datetime.now().strftime(event)


client = InfluxDBClient(host='192.168.1.218', port=8086, username="a5", password="5a")
client.switch_database('luftdaten')
q = client.query(
    '''SELECT mean("temperature") FROM "feinstaub" WHERE ("node" = 'esp8266-14503497') AND time >= now() - 
    7d and time <= now() GROUP BY time(10m)''')
d = {}
for i in q.raw['series'][0]['values']:
    d[i[0][:10]] = []
for i in q.raw['series'][0]['values']:
    if i[1]:
        d[i[0][:10]].append(i[1])
for i in d:
    d[i] = sum(d[i])/len(d[i])
if d[f"{num('%Y')}-{num('%m')}-{num('%d')}"]:
    d.pop(f"{num('%Y')}-{num('%m')}-{num('%d')}")
temp = []
for i in d:
    temp.append(round(d[i], 1))
print(temp)
