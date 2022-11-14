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
    current_sensor_config = ' '
    new_sensors_config = MQTT.prepare_data()
    while True:
        if new_sensors_config != "[]" and new_sensors_config != current_sensor_config:
            MQTT.publish(MQTT_client,MQTT.publish_topic,new_sensors_config)
            current_sensor_config = new_sensors_config
            time.sleep(interval)
    '''while True:
        MQTT.publish(MQTT_client,MQTT.publish_topic,message)
        MQTT_client.on_message=MQTT.on_message
        time.sleep(interval)
    '''
    
if __name__ == '__main__':
    main()