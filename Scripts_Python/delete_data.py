import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS
import time

bucket = "Sensors"
org = "Chemplate"
token = "ZkMULTFUywOA9DmFHHU7QrFICdETc8v5t_KlxeiBkYkl-qYs6rbOrqSocWbx1k7Qj5ngSRfKi2BDm919vClIkQ=="
# Store the URL of your InfluxDB instance
url="http://83.48.111.92:8086"

client = influxdb_client.InfluxDBClient(
    url=url,
    token=token,
    org=org
)


start = "1970-01-01T00:00:00Z"
stop = "2023-02-16T00:00:00Z"
delete_api = client.delete_api()
delete_api.delete(start, stop, '_measurement="Temperatura Sensor Probe 1"', bucket=bucket, org=org)

# Query script
query_api = client.query_api()
query = """
from(bucket: "Sensors")
  |> range(start: -1d)
  |> filter(fn: (r) => r["_measurement"] == "Temperatura Sensor Probe 1")
  |> filter(fn: (r) => r["_field"] == "Valor")
  |> filter(fn: (r) => r["Tipo"] == "Temperatura")
  |> yield(name: "mean")
"""

result = query_api.query(org=org, query=query)
results = []
for table in result:
    for record in table.records:
        results.append((record.get_field(), record.get_value()))

print(results)
time.sleep(10)