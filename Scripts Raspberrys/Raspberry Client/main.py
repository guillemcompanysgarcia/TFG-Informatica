# -*- coding: utf-8 -*-
import sched
import time
import json
import configparser
import sys
from datetime import datetime, timedelta

import MQTT_library as MQTT
import MODBUS_library as MODBUS
import Control_library as Control

#q = Queue()

def setup():
    MODBUS_client = MODBUS.setup() #Modbus Setup
    MQTT_client, publish_topic = MQTT.setup() #MQTT Setup
    
    
    return  MODBUS_client, MQTT_client, publish_topic


def main():

    interval= 5
    current_sensor_config = ' '
    s = sched.scheduler(time.time, time.sleep)

    try:    #print("Mockup") 
            MODBUS_client, MQTT_client, publish_topic = setup()

    except Exception as e:
        print("Error in MODBUS/MQTT setup", e )
        sys.exit(1)
    '''    
    new_sensors_config = [{"nombre":"Sensor 3","tipodesensor":"pH","intervalodetiempo":"Cada minuto","funciónmodbuslectura":"Function 03 (Read Holding Registers)","dirección":"0","nºregistros":"2","comentarios":""},{"nombre":"Sensor 4","tipodesensor":"Temperatura","intervalodetiempo":"Cada minuto","funciónmodbuslectura":"Function 04 (Read Input Registers)","dirección":"12","nºregistros":"1","comentarios":""},{"nombre":"Sensor 5","tipodesensor":"Otro","intervalodetiempo":"Cada minuto","funciónmodbuslectura":"Function 05 (Force Single Coil)","dirección":"14","nºregistros":"2","comentarios":""},{"nombre":"Sensor 6","tipodesensor":"Otro","intervalodetiempo":"Cada minuto","funciónmodbuslectura":"Function 16 (Preset Multiple Registers)","dirección":"34","nºregistros":"2","comentarios":""}]
        
        
    #provisional
    
    llista_sensors = Control.load_sensors(new_sensors_config)
    for sensor in llista_sensors:
     s.enter((sensor.check_Timer()-datetime.now()).seconds, 1, Control.read_sensor, argument = (sensor, s))
    while True:    
      s.run(blocking = False)
      print("Temps lliure")
      time.sleep(interval)
     ''' 

    while True:    
        s.run(blocking = False)
        print("temps lliure")
        MQTT_client.on_message = MQTT.on_message
        while not MQTT.q.empty(): #Nova Configuració
           new_sensors_config = MQTT.q.get()
           if new_sensors_config is not None:
               print("New message: ",new_sensors_config)
               if new_sensors_config != current_sensor_config :
                   llista_sensors = Control.load_sensors(new_sensors_config)
                   current_sensor_config = new_sensors_config
                   print("New Config of the System: ",new_sensors_config)   
                   if s.empty() is False: #Mirar scheduler i borrar configuració
                    list(map(s.cancel, s.queue))
                    s = sched.scheduler(time.time, time.sleep)
                   for sensor in llista_sensors: #Escriure noves tasques (sensor.check_Timer()-datetime.now()).seconds)
                    s.enter((sensor.check_Timer()-datetime.now()).seconds, 1, Control.read_sensor, argument = (sensor, s, MODBUS_client, MQTT_client, publish_topic))
        
        time.sleep(interval)
    
    

    
if __name__ == '__main__':
    main()
