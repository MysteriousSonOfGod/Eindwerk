import asyncio
import json
import KV
import functies as f
import paho.mqtt.client as mqtt
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp

class EindwerkApp(MDApp):
    label_totaleverbruik = StringProperty("Totale verbruik: No data")

    def build(self):
        # thema instellen
        self.theme_cls.primary_palette = "Yellow"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Dark"

        # de string 'KV' laden
        return Builder.load_string(KV.KV)

    # schakelaar 1
    def S1AL(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(f.S1A())

    def S1UL(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(f.S1U())

    # schakelaar 2
    def S2AL(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(f.S2A())

    def S2UL(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(f.S2U())

    # schakelaar 3
    def S3AL(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(f.S3A())

    def S3UL(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(f.S3U())

    # schakelaar 4
    def S4AL(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(f.S4A())

    def S4UL(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(f.S4U())

    def on_start(self):
        topic = "servicelocation/91d9dff3-dee8-4316-af61-dafd26172dd9/realtime"

        def onConnect(client, userdata, flags, rc):
            mqttc.subscribe(topic, 0)

        def onMessage(client, userdata, msg):
            msg.payload = msg.payload.decode("utf-8")
            data = msg.payload
            data = json.loads(data)
            global totalPower
            totalPower = data["totalPower"]

            if msg.topic == 'servicelocation/91d9dff3-dee8-4316-af61-dafd26172dd9/realtime':
                # App
                self.label_totaleverbruik = f"Totale vebruik: {totalPower} Watt"

        mqttc = mqtt.Client(client_id="kivy-client", clean_session=True)
        mqttc.on_connect = onConnect
        mqttc.on_message = onMessage
        mqttc.connect("broker.mqttdashboard.com", 1883, keepalive=60, bind_address="")
        mqttc.loop_start()  # start loop to process callbacks! (new thread!)

class LoginScreen(Screen):
    def verify_credentials(self):
        # controleren op gebruikersnaam en wachtwoord.
        if self.ids["gebruikersnaam"].text == "admin" and self.ids["wachtwoord"].text == "admin":
            self.manager.current = "Menu"  # naar menu-scherm

        # Wachtwoord en gebruikernaams veld leeg maken als wachtwoord fout is. 
        self.ids["gebruikersnaam"].text = ""
        self.ids["wachtwoord"].text = ""


class MenuScreen(Screen):
    pass


class Verbruiker1Screen(Screen):
    pass


class Verbruiker2Screen(Screen):
    pass


class Verbruiker3Screen(Screen):
    pass


class Verbruiker4Screen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(LoginScreen(name='Login'))
sm.add_widget(MenuScreen(name='Menu'))
sm.add_widget(Verbruiker1Screen(name='Verbruiker1'))
sm.add_widget(Verbruiker2Screen(name='Verbruiker2'))
sm.add_widget(Verbruiker3Screen(name='Verbruiker3'))
sm.add_widget(Verbruiker4Screen(name='Verbruiker4'))

EindwerkApp().run()
