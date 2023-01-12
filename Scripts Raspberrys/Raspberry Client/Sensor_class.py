from datetime import (
    datetime,
    timedelta,
)  # import the datetime and timedelta modules to work with dates and times


class Sensor:
    def __init__(self, sensor_info):
        """
        Initializes the sensor with provided information

        Args:
            sensor_info: dictionary containing sensor information.
        """
        self.name = sensor_info["nombre"]  # Sensor name
        self.type = sensor_info["tipodesensor"]  # Sensor type
        self.time_interval = sensor_info["intervalodetiempo"]  # Sensor read interval
        self.modbus_function = self.calculate_ModbusFunc(
            sensor_info["funciónmodbuslectura"]
        )  # Modbus function to use with the sensor
        self.address = int(sensor_info["dirección"])  # Sensor address
        self.register_count = int(
            sensor_info["nºregistros"]
        )  # Number of registers to read
        self.comments = sensor_info["comentarios"]  # Additional sensor comments
        self.next_timer = self.calculate_timer(
            datetime.now()
        )  # Sets the next reading time

    def add_Timer(self, timer):
        """
        Adds a timer to the sensor

        Args:
            timer: the time to set the next timer
        """
        self.next_timer = timer

    def check_Timer(self):
        """
        Check the next timer for the sensor

        Returns:
            the next timer for the sensor
        """
        return self.next_timer

    def check_Name(self):
        """
        Check the name of the sensor

        Returns:
            name of the sensor
        """
        return self.name

    def check_timeinterval(self):
        """
        Check the time interval of the sensor

        Returns:
            the time interval of the sensor
        """
        return self.time_interval

    def check_Modbusfunction(self):
        """
        Check the Modbus function of the sensor

        Returns:
            the Modbus function of the sensor
        """
        return self.modbus_function

    def check_Address(self):
        """
        Check the address of the sensor

        Returns:
            the address of the sensor
        """
        return self.address

    def check_Registercount(self):
        """
        Check the register count of the sensor

        Returns:
            the register count of the sensor
        """
        return self.register_count

    def check_Type(self):
        """
        Check the type of the sensor

        Returns:
            the type of the sensor
        """
        return self.type

    def calculate_ModbusFunc(self, func):
        """
        Given a Modbus function name, returns the corresponding function code

        Args:
            func: the string name of the Modbus function

        Returns:
            the function code of the Modbus function
        """
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
        """
        Calculates the next reading time for the sensor based on the time interval.

        Args:
            timer: the current time

        Returns:
            timer: the next reading time for the sensor
        """
        if self.time_interval == "Cada 10 segundos":
            timer = timer + timedelta(seconds=10)
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
        """
        Refreshes the timer for the sensor.
        """
        self.add_Timer(self.calculate_timer(self.next_timer))
