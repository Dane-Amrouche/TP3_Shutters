import shutter


def main():
    MQTT_SERVER = "192.168.0.206"
    MQTT_PORT = 1883
    MQTT_PUB_TOPIC = "1r1/014/shutter"
    MQTT_SUB_TOPIC = "1r1/014/shutter/command"

    # declare the 3 shutters in our class
    unitID = "center"
    con = shutter.Shutter(unitID,MQTT_PUB_TOPIC,MQTT_SUB_TOPIC,MQTT_SERVER,MQTT_PORT)
    return 0


# Execution or import
if __name__ == "__main__":
    main()