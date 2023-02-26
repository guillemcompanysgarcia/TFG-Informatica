import paho.mqtt.client as mqtt  # import the paho mqtt library
import json  # import the json library
import configparser  # import the configparser library

from queue import Queue  # import the queue class from the queue library

q = Queue()  # Create an empty queue instance


def setup():
    """
    Setup and Config MQTT connection
    """

    global device, broker_address, publish_topic, subscribe_topic
    # Declare the global variables
    device = "Prova"  # device name
    broker_address = "192.168.1.161"  # broker address
    publish_topic = "A"  # topic for publishing
    subscribe_topic = "Client Configuration"  # topic for subscribing

    MQTT_client = connect()  # Connect to MQTT broker
    MQTT_client.subscribe(subscribe_topic)  # subscribe to a topic
    MQTT_client.loop_start()  # Start the loop for the MQTT client

    return MQTT_client, publish_topic


def connect():
    """
    Connects to the MQTT broker
    """
    client = mqtt.Client(device)  # create a client object with the device name
    rc = client.connect(broker_address)  # try to connect to the broker
    if rc == 0:  # connection successful
        print("Connexió Iniciada amb Mosquitto localment")
    else:
        print("Error al connectar-se, codi error %d\n", rc)
    return client


def publish(client, topic, message):
    """
    Publish a message to a topic
    Args:
        client: mqtt client instance
        topic: the topic to publish to
        message: the message to publish
    """
    status = client.publish(topic, message, 2, retain=True)
    if status[0] == 0:
        print(f"Enviant `{message}` al topic `{topic}`")
    else:
        print(f"Error enviant missatge a {topic}")
        print(status[0])


def convert_to_JSON(diccionari):
    """
    Converts a dictionary to a JSON string

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
    Converts a JSON string to a dictionary
    Args:
        JSON: JSON string
    Returns:
        dic: dictionary object
    """
    dic = json.loads(JSON)
    return dic


def prepare_data(sensor, read_data):
    """
    Prepare the data for publishing
    Args:
        sensor: the sensor object
        read_data: the data read from the sensor
    Returns:
        JSON_a_enviar: JSON string ready to be published
    """
    diccionari = dict()
    diccionari = generate_data_from_sensors(sensor, read_data)
    JSON_a_enviar = convert_to_JSON(diccionari)
    return str(JSON_a_enviar)


def generate_data_from_sensors(sensor, read_data):
    """
    Generate data dictionary from sensor information
    Args:
        sensor: the sensor object
        read_data: the data read from the sensor
    Returns:
        diccionari: dictionary object containing sensor information
    """
    diccionari = {
        "nombre": str(sensor.check_Name()),
        "tipodesensor": str(sensor.check_Type()),
        "measure": str(read_data),
    }

    return diccionari


def on_message(client, userdata, message):
    """
    Callback function when a message is received on the subscribed topic
    Args:
        client: mqtt client instance
        userdata:  additional data passed to the callback
        message: the message received
    """
    JSON_rebut = str(
        message.payload.decode("utf-8")
    )  # Decode the message payload from bytes to string
    sensors = convert_to_dict(
        JSON_rebut
    )  # convert the received JSON string to dictionary
    q.put(sensors)  # put the sensor data in the queue


def main():
    client,topic =setup()


if __name__ == "__main__":
    main()


