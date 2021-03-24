import paho.mqtt.client as mqtt
import json


#this is the IP we will connect to
number = 0
#here we define a callback func for connect_mqtt were we are subscribing to the topic
def connect_to_broker(client,userdata,flags,rc):
    print("Connected on Topic: {} with result Code: {} ".format(mqtt_topic,rc))
    client.subscribe(mqtt_topic)
    
#here we define a callback func for coonect_mqtt were are all the msg will come in for the subscribed topic 
def mqtt_on_message(client,userdata,msg):
    msg_str = str(msg.payload.decode("utf-8"))
    topic = msg.topic
    global number
    number+=1
    print("Received Msg: {} || Topic: {} Times Received:{}".format(msg_str,topic,number))
    
    
   
# here we connect to the broker and waiting for messages forever with the client.loop_forever()
# you can change the loop_forever to a loop_start() if want to run something after subscribing 
# it will still listen for incoming messages    
def connect_mqtt():
    try:
        print("Connecting to broker: %s"% mqtt_ip)
        client = mqtt.Client()
        client.connect(mqtt_ip,1883,60)
        client.on_connect = connect_to_broker
        client.on_message = mqtt_on_message
        client.loop_forever()
    except Exception:
        print("couldnt find Server with IPV4: {}".format(mqtt_ip))
    
#main_function 
if __name__=="__main__":
    mqtt_topic = input("Topic:")
    while True:
        mqtt_ip = input("MQTT-IPV4:")
        connect_mqtt()
