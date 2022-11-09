import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

bucket = "BBDD"
org = "Chemplate"
token_portatil = "f-Cf0Cn5IsXOyCS2MM3nOxW34v0rIG8Sjh43GhRRck4II6hK-Oh5n3wUiEVGjq5N7vVRRfDisnE0CXab3xA_-w=="
token = "VL0TgMSf9Z2CNjckEa162LAbZBYKdJkGrsgUCV_ly3h1TFAVtiJTo_U772IsVkNB0xBvsWLQgsLtZMAfr6IRUQ=="
# Store the URL of your InfluxDB instance
url="http://localhost:8086"

client = influxdb_client.InfluxDBClient(
    url=url,
    token=token_portatil,
    org=org
)

#print(client.__dict__)

write_api = client.write_api(write_options=SYNCHRONOUS)

p = influxdb_client.Point("my_measurement").tag("location", "Prague").field("temperature", 25.3)
write_api.write(bucket=bucket, org=org, record=p)

query = 'from(bucket: "BBDD") |> range(start: -1h)'
tables = client.query_api().query(query, org=org)
for table in tables:
    for record in table.records:
        print(record)