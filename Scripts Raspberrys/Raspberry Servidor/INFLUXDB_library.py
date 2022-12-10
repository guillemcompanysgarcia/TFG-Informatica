# -*- coding: utf-8 -*- 
from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import time

import configparser

config_obj = configparser.ConfigParser()
config_obj.read("./configfile.ini")
DDBB_config = config_obj["InfluxDB"]

token =  DDBB_config["token"]
org = DDBB_config["org"]
bucket = DDBB_config["bucket"]
url = DDBB_config["url"]
    
client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)
    
def write_point(data):
	point = Point(data["nombre"]).tag("Tipo", data["tipodesensor"]).field("Valor", float(data["measure"])).time(datetime.utcnow(), WritePrecision.S)
	write_api.write(bucket, org, point)
	time.sleep(1)
