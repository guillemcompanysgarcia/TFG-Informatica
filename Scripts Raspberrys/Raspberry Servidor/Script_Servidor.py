import time
import json
import configparser

import MQTT_library as MQTT
#import INFLUXDB_library as INFLUXDB

interval= 5

def main():
    MQTT.setup()
    client = MQTT.connect()
    client.subscribe(MQTT.subscribe_topic)
    client.loop_start()
    while True:
        message = MQTT.prepare_data()
        if message != "[]":
            MQTT.publish(client,MQTT.publish_topic,message)
        client.on_message=MQTT.on_message
        time.sleep(interval)
    
    
if __name__ == '__main__':
    main()
