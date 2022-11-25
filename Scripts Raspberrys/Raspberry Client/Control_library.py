from datetime import datetime, timedelta


from Sensor_class import Sensor
import MODBUS_library as MODBUS

def load_sensors(config_sensors):
    llista_sensors = list()
    for sensor in config_sensors:
        llista_sensors.append(Sensor(sensor))
        
    llista_timers = configure_timers(llista_sensors)
    
    for sensor, timer in zip(llista_sensors,llista_timers):
        sensor.add_Timer(timer)
        
    return llista_sensors


def calculate_timer(time_interval):
    timer = datetime.now()
    

    if time_interval == "Cada minuto":
        timer = timer + timedelta(minutes=1)
    if time_interval == "Cada hora":
        timer = timer + timedelta(hours=1)
    if time_interval == "Una vez al día":
        timer = timer + timedelta(days=1)
    if time_interval == "Una vez a la semana":
        timer = timer + timedelta(weeks=1)
    return timer
        
    
def configure_timers(llista_sensors):
    llista_timers = list()
    for sensor in llista_sensors:
        time_interval = sensor.time_interval
        llista_timers.append(calculate_timer(time_interval))
    
    return llista_timers

def calculate_ModbusFunc(func):   
    func_num = 0
    if func == "Function 01 (Read Coil Status)":
        func_num = 1
    if func == "Function 02 (Read Input Status)":
        func_num = 2
    if func == "Function 03 (Read Holding Registers)":
        func_num = 3
    if func == "Function 04 (Read Input Registers)":
        func_num = 4
    if func == "Function 05 (Force Single Coil)":
        func_num = 5
    if func == "Function 16 (Preset Multiple Registers)":
        func_num = 16
    
    return func_num


def read_sensor(Modbus_Client, sensor):
    func = calculate_ModbusFunc(sensor.check_Modbusfunction())
    result = 0
    try:
        if func == "1":
            result = MODBUS.Function01(Modbus_Client, sensor.check_Address, sensor.check_Registercount)
        if func == "2":
            result = MODBUS.Function02(Modbus_Client, sensor.check_Address, sensor.check_Registercount)
        if func == "3":
            result = MODBUS.Function03(Modbus_Client, sensor.check_Address, sensor.check_Registercount)
        if func == "4":
            result = MODBUS.Function04(Modbus_Client, sensor.check_Address, sensor.check_Registercount)
        if func == "5":
            result = MODBUS.Function05(Modbus_Client, sensor.check_Address, sensor.check_Registercount)
        if func == "16":
            result = MODBUS.Function16(Modbus_Client, sensor.check_Address, sensor.check_Registercount)

    except Exception as e:
        print("Error reading sensor ", sensor.check_Name(), e )
    
    #New timers
    sensor = configure_timers(sensor)
    return sensor, result