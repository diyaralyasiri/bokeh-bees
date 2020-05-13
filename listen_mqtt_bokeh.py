# Script for MQTT client that listens for new broadcasts and stores messages in Database

import paho.mqtt.client as mqtt
import json
from SQL_helper_functions import Store_Telemetry_Data

# MQTT Settings 
MQTT_Broker = "mqtt.eclipse.org"
MQTT_Port = 1883
Keep_Alive_Interval = 45
MQTT_Topic = "Connectedbees/Telemetry"

#Subscribe to all Sensors at Base Topic
def on_connect(mosq, obj, flag,rc):
	mqttc.subscribe(MQTT_Topic, 0)
	print("Subscribed to MQTT topic.")

#Save Data into DB Table
def on_message(mosq, obj, msg):
	# This is the Master Call for saving MQTT Data into DB
	# For details of "sensor_Data_Handler" function please refer "sensor_data_to_db.py"
	print ("MQTT Data Received...")
	print ("MQTT Topic: " + msg.topic)
	msg_decoded = msg.payload.decode()
	data_dict = json.loads(msg_decoded)
	print ("Data: " + str(data_dict))

	Store_Telemetry_Data(data_dict)


	#sensor_Data_Handler(msg.topic, data_dict)


def on_subscribe(mosq, obj, mid, granted_qos):
    pass


mqttc = mqtt.Client()

# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

# Connect
mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))

# Continue the network loop
mqttc.loop_forever()
