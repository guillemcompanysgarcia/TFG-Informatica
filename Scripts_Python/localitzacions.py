from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import time
import random as r


def task0():
	token = "gnhMEKetH_YvFIJsxZVlTfDL-eHB7EDebUCWPWan6FH8zdvzwQLGgFi64ZjPSBoYXPE439xHpx6OkdqUJB1y7A=="
	org = "Chemplate"
	bucket = "Localitzacions"
	client = InfluxDBClient(url="http://83.48.111.92:8086", token=token, org=org)
	write_api = client.write_api(write_options=SYNCHRONOUS)			
	point = Point("GDE") \
	.tag("Coordenades", "GDE") \
	.field("ValorLatitud", 41.53886808206179) \
	.field("ValorLongitud", 2.030495964258169) \
	.time(datetime.utcnow(), WritePrecision.S)
	write_api.write(bucket, org, point)
	print("Fi")



def main():
	task0()
	
if __name__ == '__main__':
   main()
