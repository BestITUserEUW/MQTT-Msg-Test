import threading 
import datetime
import time
import paho.mqtt.client as mqtt



Topic = "#"


def mqtt_msg(msg):
    print("[MQTT] : '{}' | {}".format(msg,datetime.datetime.now()))
    

def connect_to_broker(client,userdata,flags,rc):
    client.subscribe(Topic)
    print(" Connected to Topic: '{}' with result Code: {}\n".format(Topic, rc))
    print("<\f>--------------------------------------------------< LIVE FEED >---------------------------------------------------<\f>")
    
def mqtt_on_message(client,userdata,msg):
    msg_str = str(msg.payload.decode("utf-8"))
    topic = msg.topic
    mqtt_msg("Received Msg: '{}' || Topic: {}".format(msg_str, topic))
    

def connect_mqtt():
    print("Connecting to broker: {}\n".format(mqtt_IP))
    client = mqtt.Client()
    client.connect(mqtt_IP,1883,60)
    client.on_connect = connect_to_broker
    client.on_message = mqtt_on_message
    client.loop_forever()
    return client

if __name__ == "__main__":
    mqtt_IP = input("IP:")
    print("------------------------------------------------< MQTT SERVER SERVICE >-------------------------------------------------")
    mqtt_client = connect_mqtt()
    print("---------------------------------------------------< EXITING SKRIPT >---------------------------------------------------")
    print("shutting down...")

