from flask import Flask, render_template
import paho.mqtt.client as mqtt

app = Flask(__name__)

# MQTT Configuration
mqtt_broker= "broker.mqttdashboard.com"
mqtt_topic = "SmartChessdip"
mqtt_client = mqtt.Client()

# Flag to indicate whether to continue displaying the image
continue_display = True

# Callback when MQTT message is received
def on_message(client, userdata, msg):
    global continue_display
    if msg.payload.decode() == "continue":
        continue_display = not continue_display

# Configure MQTT client
mqtt_client.on_message = on_message
mqtt_client.connect(mqtt_broker, 1883, 60)
mqtt_client.subscribe(mqtt_topic)
mqtt_client.loop_start()

# Route to render the HTML page
@app.route('/')
def index():
    return render_template('index.html', continue_display=continue_display)

if __name__ == '__main__':
    app.run(debug=True)
