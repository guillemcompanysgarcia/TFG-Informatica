# -*- coding: utf-8 -*-
import time  # Import the time module
import json  # Import the json module
import configparser  # Import the configparser module
import sys  # Import the sys module

import MQTT_library as MQTT  # Import the MQTT_library module and give it the alias MQTT
import INFLUXDB_library as INFLUXDB  # Import the INFLUXDB_library module and give it the alias INFLUXDB


def setup():
    """
    Set up the MQTT client and publish topic

    Returns:
        MQTT_client: MQTT client object
        publish_topic: MQTT publish topic string
    """
    MQTT_client, publish_topic = MQTT.setup()  # MQTT Setup
    return MQTT_client, publish_topic


def main():
    interval = 5  # Initialize the interval variable to 5
    current_sensor_config = (
        " "  # Initialize the current_sensor_config variable to a single space
    )
    # Print a message indicating that the script is waiting for the next task
    print("Awaiting for messages")
    try:
        MQTT_client, publish_topic = setup()  # Set up the MQTT client and publish topic
    except Exception as e:  # If an exception is raised
        print("Error in DDBB/MQTT setup", e)  # Print an error message
        sys.exit(1)  # Exit the program with a status code of 1

    while True:  # Run indefinitely
        try:
            new_sensors_config = (
                MQTT.prepare_data()
            )  # Prepare the data for the MQTT client
        except Exception as e:  # If an exception is raised
            print("Error recovering sensors' config", e)  # Print an error message
            sys.exit(1)  # Exit the program with a status code of 1

        if new_sensors_config != "[]" and new_sensors_config != current_sensor_config:
            # If the new_sensors_config variable is not an empty list and not equal to the current_sensor_config variable
            MQTT.publish(
                MQTT_client, publish_topic, new_sensors_config
            )  # Publish the new_sensors_config variable to the MQTT client
        current_sensor_config = (
            new_sensors_config  # Update the value of the current_sensor_config variable
        )

        # Receive data
        MQTT_client.on_message = (
            MQTT.on_message
        )  # Set the on_message attribute of the MQTT_client object to the on_message function from the MQTT_library module
        while (
            not MQTT.q.empty()
        ):  # While the q queue from the MQTT_library module is not empty
            new_measure = MQTT.q.get()  # Get the next value from the q queue
            if new_measure is not None:  # If the value is not None
                INFLUXDB.write_point(
                    new_measure
                )  # Write the value to the database using the write_point function from the INFLUXDB_library module

        time.sleep(interval)


if __name__ == "__main__":
    main()
