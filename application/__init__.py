from flask import Flask
import paho.mqtt.client as mqtt

app = Flask("__name__")

MQTT_BROKER = "192.168.69.1"
MQTT_PORT = 1883
MQTT_TOPIC = "tele/vindriktning04/SENSOR"

mqtt_client = mqtt.Client()


# Connect to the MQTT Broker
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # Subscribe to a topic after connecting
    client.subscribe(MQTT_TOPIC)


# Callback when a message is received
def on_message(client, userdata, msg):
    print(f"Message received on topic {msg.topic}: {msg.payload.decode()}")

    # Set up callbacks


mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

# Connect to MQTT Broker
mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
