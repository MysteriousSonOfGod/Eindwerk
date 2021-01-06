import asyncio
import json
import paho.mqtt.client as mqtt
from xknx import XKNX

xknx = XKNX(config='xknx.yaml')

topic = "servicelocation/91d9dff3-dee8-4316-af61-dafd26172dd9/realtime"

def onConnect(client, userdata, flags, rc):
    mqttc.subscribe(topic, 0)


def onMessage(client, userdata, msg):
    msg.payload = msg.payload.decode("utf-8")
    data = msg.payload
    data = json.loads(data)
    totalPower = data["totalPower"]
    print(f'\nTotale vermogen: {totalPower}')

    #status dimmer
    print(f'Status dimmer: {xknx.devices["dimmer.Light_1"].state}')

    # Asynchrone functie oproepen en waarde van totalPower meegeven
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send(totalPower))

    # Dimmer 33%, 66%, 100% laten branden, afhankelijk van totale vermogen.
    dimmer33 = 190
    dimmer66 = 80
    dimmer100 = 100

    if totalPower > dimmer33 and xknx.devices["dimmer.Light_1"].state:
        # dimmer op 33%
        print('dimmer op 33 procent')
        loop = asyncio.get_event_loop()
        loop.run_until_complete(functie_dimmer33())

    if dimmer66 < totalPower < dimmer33 and xknx.devices["dimmer.Light_1"].state:
        # dimmer op 66%
        print('dimmer op 66 procent')
        loop = asyncio.get_event_loop()
        loop.run_until_complete(functie_dimmer66())

    if totalPower < dimmer100 and xknx.devices["dimmer.Light_1"].state:
        print('dimmer op 100 procent')
        loop = asyncio.get_event_loop()
        loop.run_until_complete(functie_dimmer100())

async def send(totalPower):
    await xknx.start()
    await xknx.devices['vermogen_watt.Power'].set(totalPower)
    await xknx.devices["dimmer.Light_1"].sync()
    await xknx.stop()


async def functie_dimmer33():
    await xknx.start()
    await xknx.devices["dimmer.Light_1"].set_brightness(255/3)
    await xknx.stop()


async def functie_dimmer66():
    await xknx.start()
    await xknx.devices["dimmer.Light_1"].set_brightness((255/3) * 2)
    await xknx.stop()


async def functie_dimmer100():
    await xknx.start()
    await xknx.devices["dimmer.Light_1"].set_brightness(255)
    await xknx.stop()


mqttc = mqtt.Client(client_id="kivy-client", clean_session=True)
mqttc.on_connect = onConnect
mqttc.on_message = onMessage
mqttc.connect("broker.mqttdashboard.com", 1883, keepalive=60, bind_address="")
mqttc.loop_forever()

