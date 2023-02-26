import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS
import time

bucket = "Sensors"
org = "Chemplate"
token = "ZQMwUMRn8YHxCrgF_oXKwuB8GolonDYw3Ba1ig4Kh8s0hBgyz6zUgIO8LVUJfJ9J5HvuWYMBA1xljJoIjq5YEQ=="
# Store the URL of your InfluxDB instance
url="http://83.48.111.92:8086"

client = influxdb_client.InfluxDBClient(
    url=url,
    token=token,
    org=org
)

# Query script
query_api = client.query_api()
query = """
from(bucket: "Sensors")
  |> range(start: -1d)
  |> filter(fn: (r) => r["_measurement"] == "Sensor 1")
  |> filter(fn: (r) => r["_field"] == "Valor")
  |> filter(fn: (r) => r["Tipo"] == "pH")
  |> yield(name: "mean")
"""

result = query_api.query(org=org, query=query)
results = []
for table in result:
    for record in table.records:
        results.append((record.get_field(), record.get_value()))

print(results)
time.sleep(10)