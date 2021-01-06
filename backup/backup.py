# Kivy/KivyMD
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from time import sleep
import paho.mqtt.client as mqtt
import KV
import json


class EindwerkApp(MDApp):
    label_boven = StringProperty("Verbuik boven: No data")
    label_beneden = StringProperty("Verbuik beneden: No data")
    label_buiten = StringProperty("Verbuik buiten: No data")

    def build(self):
        # thema instellen
        self.theme_cls.primary_palette = "Yellow"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Dark"

        # de string 'KV' laden
        return Builder.load_string(KV.KV)

    def on_start(self):
        topic = "servicelocation/91d9dff3-dee8-4316-af61-dafd26172dd9/realtime"

        def onConnect(client, userdata, flags, rc):
            mqttc.subscribe(topic, 0)

        def onMessage(client, userdata, msg):
            msg.payload = msg.payload.decode("utf-8")
            data = msg.payload
            data = json.loads(data)
            totalPower = data["totalPower"]
            print(totalPower)

            if msg.topic == 'servicelocation/91d9dff3-dee8-4316-af61-dafd26172dd9/realtime':
                self.label_boven = f"Verbruik: {totalPower} Watt"

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


class BovenScreen(Screen):
    pass


class BenedenScreen(Screen):
    pass


class BuitenScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(LoginScreen(name='Login'))
sm.add_widget(MenuScreen(name='Menu'))
sm.add_widget(BovenScreen(name='Boven'))
sm.add_widget(BenedenScreen(name='Beneden'))
sm.add_widget(BuitenScreen(name='Buiten'))

EindwerkApp().run()
