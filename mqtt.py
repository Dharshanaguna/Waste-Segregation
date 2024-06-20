from paho.mqtt import client as mqtt_client
import time

broker = 'rabbitmq.selfmade.ninja'
port = 1883
topic = "Smart_Door_Bell"
client_id = "ESP_SERVER_Sender"
username = "SuriyaBharathwaj_ESP_SERVER:Sender"
password = "stegil&9"

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code {}".format(rc))

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = f"Message #{msg_count}"
        result = client.publish(topic, msg)
        status = result[0]
        if status == 0:
            print(f"Sent {msg} to topic {topic}")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1


mqtt_client = connect_mqtt()
mqtt_client.loop_start()
publish(mqtt_client)