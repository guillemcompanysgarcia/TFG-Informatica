# -*- coding: utf-8 -*-
import time
import json
import configparser
import sys

import MQTT_library as MQTT
import INFLUXDB_library as INFLUXDB




def setup():
    MQTT_client = MQTT.setup() #MQTT Setup
    return  MQTT_client

def main():
    interval= 5
    current_sensor_config = ' '
    try:
        MQTT_client = setup()
    except Exception as e:
        print("Error in DDBB/MQTT setup", e )
        #sys.exit(1)
        
    nova_mesura={
    'nombre': "Sensor1", 
    'tipodesensor': "pH", 
    'measure': 7.2
    }
    INFLUXDB.write_point(nova_mesura)
''''while True:
        try:
            new_sensors_config = MQTT.prepare_data()
        except Exception as e:
            print("Error recovering sensors' config", e )
            sys.exit(1)
            
        if new_sensors_config != "[]" and new_sensors_config != current_sensor_config:
            MQTT.publish(MQTT_client,MQTT.publish_topic,new_sensors_config)
            current_sensor_config = new_sensors_config
        
        #Receive data
        MQTT_client.on_message = MQTT.on_message
        while not MQTT.q.empty(): #Nova Configuració
           nova_mesura = MQTT.q.get()
           if nova_mesura is not None:
               INFLUXDB.write_point(nova_mesura)
        time.sleep(interval)'''

    
if __name__ == '__main__':
    main()