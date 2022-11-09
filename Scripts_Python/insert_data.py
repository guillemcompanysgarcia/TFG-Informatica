from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import time
import random as r

from threading import Thread

def task0():
	token = "78c0610d6f9c5a6276ee70550e3386c4"
	org = "Chemplate"
	bucket = "Sensors"
	client = InfluxDBClient(url="http://localhost:8086", token=token, org=org)
	write_api = client.write_api(write_options=SYNCHRONOUS)
	for l in range (10000):
		for j in range(3):#Cubell j
			for i in range(10):#Sensor i
				value= r.gauss(20000,5000)*1.0/1000
				point = Point("Cubell "+ str(j)) \
				.tag("Sensor", "Sensor XXXX") \
				.field("Temperatura(ºC)", value) \
				.time(datetime.utcnow(), WritePrecision.S)
				write_api.write(bucket, org, point)
				time.sleep(1)
	print("Fi thread 0")

def task1():
	token = "78c0610d6f9c5a6276ee70550e3386c4"
	org = "Chemplate"
	bucket = "Sensors"
	client = InfluxDBClient(url="http://localhost:8086", token=token, org=org)
	write_api = client.write_api(write_options=SYNCHRONOUS)
	for l in range (10000):
		for j in range(3):#Cubell j
			for i in range(10):#Sensor i
				value= r.gauss(70,20)*1.0/10
				point = Point("Cubell "+ str(j)) \
				.tag("Sensor", "Sensor YYYY") \
				.field("Acidesa(pH)", value) \
				.time(datetime.utcnow(), WritePrecision.S)
				write_api.write(bucket, org, point)
				time.sleep(1)
	print("Fi thread 1")
	
def task2():
	token = "78c0610d6f9c5a6276ee70550e3386c4"
	org = "Chemplate"
	bucket = "Sensors"
	client = InfluxDBClient(url="http://localhost:8086", token=token, org=org)
	write_api = client.write_api(write_options=SYNCHRONOUS)
	for l in range (10000):
		for j in range(3):#Cubell j
			for i in range(10):#Sensor i
				value= r.gauss(101300,20000)*1.0
				point = Point("Cubell "+ str(j)) \
				.tag("Sensor", "Sensor ZZZZ") \
				.field("Presió(Pa)", value) \
				.time(datetime.utcnow(), WritePrecision.S)
				write_api.write(bucket, org, point)
				time.sleep(1)
	print("Fi thread 2")
	
def main():
	thread0 = Thread(target=task0)
	thread1 = Thread(target=task1)
	thread2 = Thread(target=task2)
	thread0.start()
	thread1.start()
	thread2.start()
	
	thread0.join()
	thread1.join()
	thread2.join()
	
if __name__ == '__main__':
   main()
