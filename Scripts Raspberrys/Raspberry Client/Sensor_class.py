
class Sensor():
    
    def __init__(self, sensor_info):
       
        self.name = sensor_info['nombre']
        self.type = sensor_info['tipodesensor']
        self.time_interval = sensor_info['intervalodetiempo']
        self.modbus_function = sensor_info['funciónmodbuslectura']
        self.address = sensor_info['dirección']
        self.register_count = sensor_info['nºregistros']
        self.comments= sensor_info['comentarios']
        self.next_timer = 0
        
    
    def add_Timer(self, timer):
        self.next_timer = timer

    def check_Name(self):
        return self.name

    def check_Timer(self):
        return self.next_timer
    
    def check_Modbusfunction(self):
        return self.modbus_function

    def check_Address(self):
        return self.address

    def check_Registercount(self):
        return self.register_count