from datetime import datetime, timedelta
from Sensor_class import Sensor

import MODBUS_library as MODBUS
import MQTT_library as MQTT

def load_sensors(config_sensors):
    llista_sensors = list()
    for sensor in config_sensors:
        llista_sensors.append(Sensor(sensor))
        
        
    return llista_sensors


#def read_sensor(sensor, s, Modbus_Client, MQTT_Client, topic):
def read_sensor(sensor, s):
    result = 0
    func = sensor.check_Modbusfunction()
    try:
        if func == 1:
            #result = MODBUS.Function01(Modbus_Client, sensor.check_Address(), sensor.check_Registercount())
            result = 1
        if func == 2:
            #result = MODBUS.Function02(Modbus_Client, sensor.check_Address(), sensor.check_Registercount())
            result = 2
        if func == 3:
            #result = MODBUS.Function03(Modbus_Client, sensor.check_Address(), sensor.check_Registercount())
            result = 3
        if func == 4:
            #result = MODBUS.Function04(Modbus_Client, sensor.check_Address(), sensor.check_Registercount())
            result = 4
        if func == 5:
            #result = MODBUS.Function05(Modbus_Client, sensor.check_Address(), sensor.check_Registercount())
            result = 5
        if func == 16:
            #result = MODBUS.Function16(Modbus_Client, sensor.check_Address(), sensor.check_Registercount())
            result = 16

    except Exception as e:
        print("Error reading sensor ", sensor.check_Name(), e )
    
    print("Mesura feta "+ sensor.check_Name())
    #Refresh timer
    sensor.refresh_timer()
   # s.enter((sensor.check_Timer()-datetime.now()).seconds, 1, read_sensor, argument = (sensor, s, Modbus_Client))
    s.enter((sensor.check_Timer()-datetime.now()).seconds, 1, read_sensor, argument = (sensor, s))
    
    #send message via mqqtt
    #message = MQTT.prepare_data(sensor, result)
    #MQTT.publish(MQTT_Client, topic, message)
