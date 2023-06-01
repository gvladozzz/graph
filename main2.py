from influxdb import InfluxDBClient

client = InfluxDBClient(host='192.168.1.218', port=8086, username="a5", password="5a")
client.switch_database('luftdaten')
q = client.query(
    '''SELECT mean("temperature") FROM "feinstaub" WHERE ("node" = 'esp8266-14503497') AND time >= now() - 
    6d and time <= now() GROUP BY time(10m)''')
d = {}
for i in q.raw['series'][0]['values']:
    d[i[0][:10]] = 0

print(d)

