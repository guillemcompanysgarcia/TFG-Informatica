import minimalmodbus

instrument = minimalmodbus.Instrument('/dev/ttyUSB1', 1)  # port name, slave address (in decimal)

temperature = instrument.read_register(289, 1)  # Registernumber, number of decimals
print(temperature)


NEW_TEMPERATURE = 95
instrument.write_register(24, NEW_TEMPERATURE, 1)  # Registernumber, value, number of decimals for storage


def setup_sensor(port_name, address):
    print("Configure Sensor")
    
def read_sensor(sensor, register_number, decimals_number):
    print("Read Sensor")

def  calibrate_sensor():
    print("Calibrate Sensor")