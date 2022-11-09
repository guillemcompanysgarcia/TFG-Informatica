from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import time


#a canviar. passar .env per paràmetre i recuperar-ho
token = "78c0610d6f9c5a6276ee70550e3386c4"
org = "Chemplate"
bucket = "Localització Sensors"
client = InfluxDBClient(url="http://localhost:8086", token=token, org=org)
buckets_api = client.buckets_api()
query_api = client.query_api()

write_api = client.write_api(write_options=SYNCHRONOUS)

point = Point("Localització") \
  .field("Latitude", 41.556552462229796) \
  .field("Longitude", 2.1817401848744753)\
  .field("Place", "Chemplate") \
  .time(datetime.utcnow(), WritePrecision.S)
  
write_api.write(bucket, org, point)
time.sleep(1)
	
print("Fi")
