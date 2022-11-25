import sched
import time
import json
import configparser
import sys

import MQTT_library as MQTT
import MODBUS_library as MODBUS
import Control_library as Control


#message = '[{"nombre":"Sensor 1","tipodesensor":"Temperatura","intervalodetiempo":"Cada minuto","funciónmodbuslectura":"Function 01 (Read Coil Status)","dirección":"00","nºregistros":"1","comentarios":""},{"nombre":"Sensor 2","tipodesensor":"Presión","intervalodetiempo":"Cada hora","funciónmodbuslectura":"Function 02 (Read Input Status)","dirección":"02","nºregistros":"1","comentarios":""},{"nombre":"Sensor 3","tipodesensor":"Conductancia","intervalodetiempo":"Una vez al día","funciónmodbuslectura":"Function 03 (Read Holding Registers)","dirección":"04","nºregistros":"1","comentarios":""},{"nombre":"Sensor 4","tipodesensor":"pH","intervalodetiempo":"Una vez a la semana","funciónmodbuslectura":"Function 04 (Read Input Registers)","dirección":"06","nºregistros":"2","comentarios":""},{"nombre":"Sensor 5","tipodesensor":"Otro","intervalodetiempo":"Una vez a la semana","funciónmodbuslectura":"Function 04 (Read Input Registers)","dirección":"14","nºregistros":"2","comentarios":""}]'
#q = Queue()

def setup():
    MODBUS_client = MODBUS.setup() #Modbus Setup
    MQTT_client = MQTT.setup() #MQTT Setup
    
    return MQTT_client, MODBUS_client


def main():

    interval= 5
    current_sensor_config = ' '
    s = sched.scheduler(time.time, time.sleep)

    try: MQTT_client, MODBUS_client = setup()

    except Exception as e:
        print("Error in MODBUS/MQTT setup", e )
        sys.exit(1)
    
    new_sensors_config = [{"nombre":"Sensor 1","tipodesensor":"Temperatura","intervalodetiempo":"Cada minuto","funciónmodbuslectura":"Function 01 (Read Coil Status)","dirección":"00","nºregistros":"2","comentarios":""},{"nombre":"Sensor 2","tipodesensor":"pH","intervalodetiempo":"Cada hora","funciónmodbuslectura":"Function 02 (Read Input Status)","dirección":"04","nºregistros":"2","comentarios":""},{"nombre":"Sensor 3","tipodesensor":"pH","intervalodetiempo":"Cada hora","funciónmodbuslectura":"Function 03 (Read Holding Registers)","dirección":"24","nºregistros":"2","comentarios":""},{"nombre":"Sensor 4","tipodesensor":"Temperatura","intervalodetiempo":"Cada hora","funciónmodbuslectura":"Function 04 (Read Input Registers)","dirección":"12","nºregistros":"1","comentarios":""},{"nombre":"Sensor 5","tipodesensor":"Otro","intervalodetiempo":"Una vez al día","funciónmodbuslectura":"Function 05 (Force Single Coil)","dirección":"14","nºregistros":"2","comentarios":""},{"nombre":"Sensor 6","tipodesensor":"Otro","intervalodetiempo":"Una vez al día","funciónmodbuslectura":"Function 16 (Preset Multiple Registers)","dirección":"34","nºregistros":"2","comentarios":""}]
    while True:
        MQTT_client.on_message = MQTT.on_message
        while not MQTT.q.empty(): #Nova Configuraci�
           new_sensors_config = MQTT.q.get()
           if new_sensors_config is not None:
               print("New message: ",new_sensors_config)
               if new_sensors_config != current_sensor_config :
                   llista_sensors = Control.load_sensors(new_sensors_config)
                   current_sensor_config = new_sensors_config
                   print("New Config of the System: ",new_sensors_config)   
                   if s.empty() is False: #Mirar scheduler i borrar configuraci�
                    list(map(s.cancel, s.queue))
                    s = sched.scheduler(time.time, time.sleep)
                   for sensor in llista_sensors: #Escriure noves tasques
                    s.enter(sensor.check_Timer(), 1, Control.read_sensor(MODBUS_client, sensor))
                   s.run()
                
        #Tractament timers i lectura. Regeneraci� timers
        #mirar tasques i enviar
        #message = MQTT.prepare_data()
        #MQTT.publish(MQTT_client,MQTT.publish_topic,message)
        time.sleep(interval)
    
if __name__ == '__main__':
    main()