
class Sensor():
    
    def __init__(self, sensor_info):
       
        self.name = sensor_info['nombre']
        self.type = sensor_info['tipodesensor']
        self.time_interval = sensor_info['intervalodetiempo']
        self.modbus_function = sensor_info['funciónmodbuslectura']
        self.address = sensor_info['dirección']
        self.register_count = sensor_info['nºregistros']
        self.comments= sensor_info['comentarios']
        
    
    def add_Timer(self, timer):
        self.next_timer = timer