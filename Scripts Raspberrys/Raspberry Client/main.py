import time
import json
import configparser

import MQTT_library as MQTT
#import INFLUXDB_library as INFLUXDB
#import MODBUS_library as MODBUS
import Control_library as Control

interval= 5

#message = '[{"nombre":"Sensor 1","tipodesensor":"Temperatura","intervalodetiempo":"Cada minuto","funciónmodbuslectura":"Function 01 (Read Coil Status)","dirección":"00","nºregistros":"1","comentarios":""},{"nombre":"Sensor 2","tipodesensor":"Presión","intervalodetiempo":"Cada hora","funciónmodbuslectura":"Function 02 (Read Input Status)","dirección":"02","nºregistros":"1","comentarios":""},{"nombre":"Sensor 3","tipodesensor":"Conductancia","intervalodetiempo":"Una vez al día","funciónmodbuslectura":"Function 03 (Read Holding Registers)","dirección":"04","nºregistros":"1","comentarios":""},{"nombre":"Sensor 4","tipodesensor":"pH","intervalodetiempo":"Una vez a la semana","funciónmodbuslectura":"Function 04 (Read Input Registers)","dirección":"06","nºregistros":"2","comentarios":""},{"nombre":"Sensor 5","tipodesensor":"Otro","intervalodetiempo":"Una vez a la semana","funciónmodbuslectura":"Function 04 (Read Input Registers)","dirección":"14","nºregistros":"2","comentarios":""}]'
#q = Queue()

def setup():
    #MODBUS_client = MODBUS.setup() #Modbus Setup
    MQTT_client = MQTT.setup() #MQTT Setup
    
    return MQTT_client


def main():
    current_sensor_config = ' '
    MQTT_client = setup()
    while True:
        MQTT_client.on_message = MQTT.on_message
        while not MQTT.q.empty():
           new_sensors_config = MQTT.q.get()
           if new_sensors_config is not None:
               #print("received from queue",new_sensors_config)
               if new_sensors_config != current_sensor_config :
                   llista_sensors = Control.load_sensors(new_sensors_config)
                   current_sensor_config = new_sensors_config
                   print("New Config of the System: ",new_sensors_config)
        #message = MQTT.prepare_data()
        #MQTT.publish(MQTT_client,MQTT.publish_topic,message)
        time.sleep(interval)
    
if __name__ == '__main__':
    main()