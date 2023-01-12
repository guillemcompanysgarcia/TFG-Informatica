# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt  # Import the mqtt module from the paho package and give it the alias mqtt

import json  # Import the json module

import configparser  # Import the configparser module

from queue import Queue  # Import the Queue class from the queue module


q = Queue()  # Create a new Queue object and assign it to the q variable


def setup():
    """
    Set up the MQTT client, publish and subscribe topics, and start the MQTT loop

    Returns:
        MQTT_client: MQTT client object
        publish_topic: MQTT publish topic string
    """
    config_obj = (
        configparser.ConfigParser()
    )  # Create a new ConfigParser object and assign it to the config_obj variable
    config_obj.read(
        "./configfile.ini"
    )  # Read the configfile.ini file and parse it with the ConfigParser object
    MQTT_config = config_obj[
        "MQTT"
    ]  # Get the "MQTT" section from the ConfigParser object

    global device, broker_address, publish_topic, subscribe_topic  # Declare the device, broker_address, publish_topic, and subscribe_topic variables as global

    device = MQTT_config[
        "device"
    ]  # Get the "device" value from the "MQTT" section of the ConfigParser object and assign it to the device variable
    broker_address = MQTT_config[
        "broker_address"
    ]  # Get the "broker_address" value from the "MQTT" section of the ConfigParser object and assign it to the broker_address variable
    publish_topic = MQTT_config[
        "publish_topic"
    ]  # Get the "publish_topic" value from the "MQTT" section of the ConfigParser object and assign it to the publish_topic variable
    subscribe_topic = MQTT_config[
        "subscribe_topic"
    ]  # Get the "subscribe_topic" value from the "MQTT" section of the ConfigParser object and assign it to the subscribe_topic variable

    MQTT_client = (
        connect()
    )  # Create a new MQTT client object and assign it to the MQTT_client variable
    MQTT_client.subscribe(
        subscribe_topic
    )  # Subscribe the MQTT client to the subscribe_topic
    MQTT_client.loop_start()  # Start the MQTT loop

    return (
        MQTT_client,
        publish_topic,
    )  # Return the MQTT_client and publish_topic variables


def connect():
    """
    Connect the MQTT client to the broker

    Returns:
        client: MQTT client object
    """
    client = mqtt.Client(device)  # Create a new MQTT client object with the device name
    rc = client.connect(
        broker_address
    )  # Connect the MQTT client to the broker at the specified address
    if rc == 0:  # If the connection is successful
        print(
            "Connexió Iniciada amb Mosquitto localment"
        )  # Print a message indicating the connection was successful
    else:  # If the connection is not successful
        print("Error al connectar-se, codi error %d\n", rc)
    return client  # Return the MQTT_client


def publish(client, topic, message):
    """
    Publish a message to the specified topic using the MQTT client

    Args:
        client: MQTT client object
        topic: MQTT topic string
        message: message string to be published
    """
    status = client.publish(
        topic, message, 2, retain=True
    )  # Publish the message to the specified topic using the MQTT client
    if status[0] == 0:  # If the publication is successful
        print(
            f"Enviant `{message}` al topic `{topic}`"
        )  # Print a message indicating the message was sent to the specified topic
    else:  # If the publication is not successful
        print(f"Error enviant missatge a {topic}")  # Print an error message
        print(status[0])  # Print the status code of the publication


def convert_to_JSON(diccionari):
    """
    Convert a dictionary to a JSON string

    Args:
        diccionari: dictionary object

    Returns:
        JSON: JSON string
    """
    JSON = json.dumps(
        diccionari
    )  # Convert the dictionary to a JSON string and assign it to the JSON variable
    return JSON  # Return the JSON string


def convert_to_dict(JSON):
    """
    Convert a JSON string to a dictionary

    Args:
        JSON: JSON string

    Returns:
        dic: dictionary object
    """
    dic = json.loads(
        JSON
    )  # Convert the JSON string to a dictionary and assign it to the dic variable
    return dic  # Return the dictionary


def prepare_data():
    """
    Prepare data for publishing to the MQTT client

    Returns:
        str(JSON_a_enviar): JSON string of the data
    """
    diccionari = (
        dict()
    )  # Create a new empty dictionary and assign it to the diccionari variable
    diccionari = get_data_from_file(
        diccionari
    )  # Get data from a file and update the diccionari dictionary
    JSON_a_enviar = convert_to_JSON(
        diccionari
    )  # Convert the diccionari dictionary to a JSON string and assign it to the JSON_a_enviar variable
    return str(JSON_a_enviar)  # Return the JSON_a_enviar string as a string object


def get_data_from_file(diccionari):
    """
    Get data from a file and update a dictionary with the data

    Args:
        diccionari: dictionary object

    Returns:
        diccionari: updated dictionary object
    """
    f = open(
        "/home/servidor/Desktop/TFG/Docker_Servidor/config/RaspConfig.json", "r"
    )  # Open the RaspConfig.json file in read mode and assign the file object to the f variable
    diccionari = json.load(f)  # Load the JSON data from the file to the dictionary
    return diccionari  # Return the diccionari dictionary


def on_message(client, userdata, message):
    """
    Callback function for when a message is received by the MQTT client

    Args:
        client: MQTT client object
        userdata: user data object
        message: message object
    """
    JSON_rebut = str(
        message.payload.decode("utf-8")
    )  # Convert the message payload to a string and assign it to the JSON_rebut variable
    sensor_measure = convert_to_dict(
        JSON_rebut
    )  # Convert the JSON_rebut string to a dictionary and assign it to the mesura_sensors variable
    q.put(sensor_measure)  # Add the sensor_measure dictionary to the q queue
