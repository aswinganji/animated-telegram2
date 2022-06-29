import time
from datetime import datetime
from paho.mqtt import client as mqtt_client

broker = 'broker.emqx.io'
port = 1883
topic = 'topicName/time'
client_id = 'iot'
username = 'test'
password = ''

def connect_mqtt():
	client = mqtt_client.Client(client_id)
	client.username_pw_set(username,password)
	client.connect(broker,port)
	return client

def publish(client):
	while True:
		time.sleep(1)
		now = datetime.now()
		current_time = now.strftime("%H:%M:%S")
		print("Current Time - ", current_time)
		client.publish(topic, current_time)

def subscribe(client:mqtt_client):
	def on_message(client,userdata,msg):
		print("Recieved Message: ", msg.payload.decode())

	client.subscribe(topic)
	print(topic)
	client.on_message = on_message

def run():
	client_run = connect_mqtt()
	subscribe(client_run)
	client_run.loop_forever()

if __name__ == '__main__':
    run() 
	
