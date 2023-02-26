# Import the datetime and timedelta modules from the built-in Python datetime library
# and the Sensor class from the Sensor_class module
from datetime import datetime, timedelta
from Sensor_class import Sensor

# Import the MODBUS_library and MQTT_library modules
import MODBUS_library as MODBUS
import MQTT_library as MQTT

# Define the load_sensors function that takes in a list of sensor configurations
def load_sensors(config_sensors):
    # Initialize an empty list to store the sensor objects
    llista_sensors = list()

    # Iterate through the list of sensor configurations
    for sensor in config_sensors:
        # Create a sensor object for each configuration and add it to the list
        llista_sensors.append(Sensor(sensor))

    # Return the list of sensor objects
    return llista_sensors


# Define the read_sensor function that takes in a sensor object, an event scheduler object,
# Modbus client object, MQTT client object, and a MQTT topic string
def read_sensor(sensor, s, Modbus_Client, MQTT_Client, topic):
    # Initialize a result variable to store the data read from the sensor
    result = 0

    # Get the appropriate Modbus function for the sensor based on its configuration
    func = sensor.check_Modbusfunction()

    # Try to read data from the sensor using the specified Modbus function
    try:
        # Use the appropriate Modbus function based on the sensor's configuration
        if func == 1:
            result = MODBUS.Function01(
                Modbus_Client, sensor.check_Address(), sensor.check_Registercount()
            )
        if func == 2:
            result = MODBUS.Function02(
                Modbus_Client, sensor.check_Address(), sensor.check_Registercount()
            )
        if func == 3:
            result = MODBUS.Function03(
                Modbus_Client, sensor.check_Address(), sensor.check_Registercount()
            )
        if func == 4:
            result = MODBUS.Function04(
                Modbus_Client, sensor.check_Address(), sensor.check_Registercount()
            )
        if func == 5:
            result = MODBUS.Function05(
                Modbus_Client, sensor.check_Address(), sensor.check_Registercount()
            )
        if func == 16:
            result = MODBUS.Function16(
                Modbus_Client, sensor.check_Address(), sensor.check_Registercount()
            )

        # Print a message indicating that the sensor data was successfully read using the specified Modbus function
        print(
            "Measure of sensor "
            + sensor.check_Name()
            + " done using Modbus function "
            + str(func)
        )

    # Catch any exceptions that may occur during the reading process
    except Exception as e:
        # Print an error message and the exception if an error occurs
        print("Error reading sensor ", sensor.check_Name(), e)

    # Refresh the timer for the sensor
    sensor.refresh_timer()

    # Schedule task to read sensor and publish data over MQTT when timer expires
    s.enter(
        (sensor.check_Timer() - datetime.now()).seconds,
        1,
        read_sensor,
        argument=(sensor, s, Modbus_Client, MQTT_Client, topic),
    )

    # Prepare data for publishing
    message = MQTT.prepare_data(sensor, result)

    # Publish data over MQTT
    MQTT.publish(MQTT_Client, topic, message)
