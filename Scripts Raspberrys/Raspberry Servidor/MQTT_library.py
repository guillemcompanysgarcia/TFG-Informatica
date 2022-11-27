import paho.mqtt.client as mqtt 
import json
import configparser
from queue import Queue

q = Queue()

def setup():
    config_obj = configparser.ConfigParser()
    config_obj.read("./configfile.ini")
    MQTT_config = config_obj["MQTT"]
    
    global device, broker_address, publish_topic, subscribe_topic
    
    device = MQTT_config["device"]
    broker_address = MQTT_config["broker_address"]
    publish_topic = MQTT_config["publish_topic"]
    subscribe_topic = MQTT_config["subscribe_topic"]
    
    MQTT_client = connect()
    MQTT_client.subscribe(subscribe_topic)
    MQTT_client.loop_start()
        
    return MQTT_client, publish_topic
    
def connect():
    client = mqtt.Client(device)
    rc = client.connect(broker_address)
    if rc == 0:
        print("Connexió Iniciada amb Mosquitto localment")
    else:
        print("Error al connectar-se, codi error %d\n", rc)
    return client

def publish(client, topic, message):
    status = client.publish(topic, message,1)
    if status[0] == 0:
        print(f"Enviant `{message}` al topic `{topic}`")
    else:
        print(f"Error enviant missatge a {topic}")
        print(status[0])
    
def convert_to_JSON(diccionari):
    JSON = json.dumps(diccionari)
    return JSON

def convert_to_dict(JSON):
    dic = json.loads(JSON)
    return dic

def prepare_data():
    diccionari=dict()
    diccionari=get_data_from_web(diccionari)
    JSON_a_enviar = convert_to_JSON(diccionari)
    return str(JSON_a_enviar)

def get_data_from_web(diccionari):
    f = open("./config/RaspConfig.json","r")
    diccionari =json.load(f)
    return diccionari

def on_message(client, userdata, message):
   JSON_rebut = str(message.payload.decode("utf-8"))
   mesura_sensors = convert_to_dict(JSON_rebut)
   q.put(mesura_sensors)
   #print(f"Rebut `{diccionari}` del topic `{message.topic}`")
