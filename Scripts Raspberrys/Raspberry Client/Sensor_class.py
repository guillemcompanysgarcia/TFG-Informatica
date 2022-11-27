from datetime import datetime, timedelta

class Sensor():
    
    def __init__(self, sensor_info):
       
        self.name = sensor_info['nombre']
        self.type = sensor_info['tipodesensor']
        self.time_interval = sensor_info['intervalodetiempo']
        self.modbus_function = self.calculate_ModbusFunc(sensor_info['funciónmodbuslectura'])
        self.address = int(sensor_info['dirección'])
        self.register_count = int(sensor_info['nºregistros'])
        self.comments= sensor_info['comentarios']
        self.next_timer = self.calculate_timer(datetime.now())
        
    
    def add_Timer(self, timer):
        self.next_timer = timer

    def check_Timer(self):
        return self.next_timer
    
    def check_Name(self):
        return self.name

    def check_timeinterval(self):
        return self.time_interval
    
    def check_Modbusfunction(self):
        return self.modbus_function

    def check_Address(self):
        return self.address

    def check_Registercount(self):
        return self.register_count
    
    def check_Type(self):
        return self.type
    
    def calculate_ModbusFunc(self,func):   
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
     
    def calculate_timer(self, timer):
        if self.time_interval == "Cada minuto":
            timer = timer + timedelta(minutes=1)
        if self.time_interval == "Cada 15 minutos":
            timer = timer + timedelta(minutes=15)
        if self.time_interval == "Cada 30 minutos":
            timer = timer + timedelta(minutes=30)
        if self.time_interval == "Cada hora":
            timer = timer + timedelta(minutes=60)
        return timer
    
    def refresh_timer(self):
        self.add_Timer(self.calculate_timer(self.next_timer))
        
