import time
import json
import configparser

import MQTT_library as MQTT
#import INFLUXDB_library as INFLUXDB

interval= 10

def main():
    MQTT.setup()
    MQTT_client = MQTT.connect()
    MQTT_client.subscribe(MQTT.subscribe_topic)
    MQTT_client.loop_start()
    message = MQTT.prepare_data()
    while True:
        if message != "[]":
            MQTT.publish(MQTT_client,MQTT.publish_topic,message)
            time.sleep(interval)
    '''while True:
        MQTT.publish(MQTT_client,MQTT.publish_topic,message)
        MQTT_client.on_message=MQTT.on_message
        time.sleep(interval)
    '''
    
if __name__ == '__main__':
    main()