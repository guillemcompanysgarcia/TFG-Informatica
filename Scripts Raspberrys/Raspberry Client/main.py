# -*- coding: utf-8 -*-
import sched  # import the sched module to schedule tasks
import time  # import the time module to keep track of time
import json  # import the json module to parse JSON data
import configparser  # import the configparser module to parse configuration files
import sys  # import the sys module to interact with the Python interpreter
from datetime import (
    datetime,
    timedelta,
)  # import the datetime and timedelta modules to work with dates and times

import MQTT_library as MQTT  # import the MQTT_library module and give it the alias MQTT
import MODBUS_library as MODBUS  # import the MODBUS_library module and give it the alias MODBUS
import Control_library as Control  # import the Control_library module and give it the alias Control

# Define the setup function
def setup():
    MODBUS_client = MODBUS.setup()  # Set up the Modbus client
    (
        MQTT_client,
        publish_topic,
    ) = MQTT.setup()  # Set up the MQTT client and get the topic to publish messages to

    # Return the Modbus and MQTT clients, along with the MQTT publish topic
    return MODBUS_client, MQTT_client, publish_topic


# Define the main function
def main():
    # Set the interval between iterations of the main loop to 5 seconds
    interval = 5

    # Initialize the current sensor configuration as an empty string
    current_sensor_config = " "

    # Initialize the scheduler
    s = sched.scheduler(time.time, time.sleep)

    # Try to set up the Modbus and MQTT clients
    try:
        MODBUS_client, MQTT_client, publish_topic = setup()
    except Exception as e:  # If there is an error, print the error message and exit the script
        print("Error in MODBUS/MQTT setup", e)
        sys.exit(1)

    # Start an infinite loop
    while True:
        # Run the scheduler in non-blocking mode
        s.run(blocking=False)

        # Print a message indicating that the script is waiting for the next task
        print("Awaiting next task")

        # Set the MQTT client's on_message callback to the on_message function defined in the MQTT_library module
        MQTT_client.on_message = MQTT.on_message

        # Check if there are any new sensor configuration messages in the queue
        while not MQTT.q.empty():
            # If there are, get the new sensor configuration from the queue
            new_sensors_config = MQTT.q.get()

            # If the new configuration is not None
            if new_sensors_config is not None:
                # Print the new message
                print("New message: ", new_sensors_config)

                # If the new configuration is different from the current configuration
                if new_sensors_config != current_sensor_config:
                    # Load the new list of sensors from the new configuration
                    llista_sensors = Control.load_sensors(new_sensors_config)
                    # Update the current sensor configuration
                    current_sensor_config = new_sensors_config

                    # Print the new configuration
                    print("New Config of the System: ", new_sensors_config)

                    # If there are any tasks in the scheduler queue
                    if s.empty() is False:
                        # Cancel all the tasks
                        list(map(s.cancel, s.queue))

                        # Initialize a new scheduler
                        s = sched.scheduler(time.time, time.sleep)

                    # For each sensor in the list of sensors
                    for sensor in llista_sensors:
                        # Add a task to the scheduler to read the sensor value at the specified interval
                        s.enter(
                            (sensor.check_Timer() - datetime.now()).seconds,
                            1,
                            Control.read_sensor,
                            argument=(
                                sensor,
                                s,
                                MODBUS_client,
                                MQTT_client,
                                publish_topic,
                            ),
                        )

        # Sleep for the specified interval before continuing the loop
        time.sleep(interval)


if __name__ == "__main__":
    main()
