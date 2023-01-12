# -*- coding: utf-8 -*-
from datetime import datetime  # import datetime to get current date and time
from influxdb_client import (
    InfluxDBClient,
    Point,
    WritePrecision,
)  # import InfluxDBClient and Point from influxdb_client library, to use InfluxDBClient and Point classes
from influxdb_client.client.write_api import (
    SYNCHRONOUS,
)  # import SYNCHRONOUS to write data with synchronization.
import time  # import time to use sleep function

import configparser  # import configparser to read the configuration file

config_obj = configparser.ConfigParser()  # create a configparser object
config_obj.read("./configfile.ini")  # read the configuration file
DDBB_config = config_obj[
    "InfluxDB"
]  # gets the section InfluxDB of the configuration file

token = DDBB_config["token"]  # gets the token from configuration file
org = DDBB_config["org"]  # gets the org from configuration file
bucket = DDBB_config["bucket"]  # gets the bucket from configuration file
url = DDBB_config["url"]  # gets the url from configuration file

client = InfluxDBClient(
    url=url, token=token, org=org
)  # create a InfluxDBClient object with the url, token and org
write_api = client.write_api(
    write_options=SYNCHRONOUS
)  # create a write_api object with the write options of SYNCHRONOUS


def write_point(data):
    """
    Writes data to InfluxDB
    Parameters:
    data (dict): dictionary containing data to be written to InfluxDB, with the keys "nombre", "tipodesensor" and "measure"
    """
    point = (
        Point(data["nombre"])
        .tag("Tipo", data["tipodesensor"])
        .field("Valor", float(data["measure"]))
        .time(datetime.utcnow(), WritePrecision.S)
    )
    # creates a Point object with the Point class, with the name of the point, a tag "Tipo" with the type of sensor, a field "Valor" with the measure, and the time in UTC format and with second precision
    write_api.write(bucket, org, point)  # writes the point in the bucket with the org
    print("Enviant point rebut")  # Prints this message when the point is written
    time.sleep(1)  # Sleeps for 1 second
