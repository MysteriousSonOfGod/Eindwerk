KV = """
#: import FadeTransition kivy.uix.screenmanager.FadeTransition
ScreenManager:
    LoginScreen:    
    MenuScreen:
    Verbruiker1Screen:
    Verbruiker2Screen:
    Verbruiker3Screen:
    Verbruiker4Screen:

<LoginScreen>:
    name: 'Login'
    FloatLayout:

        MDToolbar:
            pos_hint: {'center_x':0.5, 'top':1}
            title: "KNX DEMO APP"

        Label:
            text: "LOGIN"
            font_size: 50
            halign: 'center'
            pos_hint: {'center_x':0.5,'center_y':0.74}

        MDTextFieldRect:
            id: gebruikersnaam
            hint_text: 'Gebruikersnaam'
            pos_hint: {'center_x':0.5,'center_y':0.64}
            size_hint: 0.5, 0.05
            write_tab: False
            multiline: False

        MDTextFieldRect:
            id: wachtwoord
            hint_text: 'Wachtwoord'
            password: True
            pos_hint: {'center_x':0.5,'center_y':0.58}
            size_hint: 0.5, 0.05
            write_tab: False
            multiline: False

        MDRectangleFlatButton:
            text: 'Aanmelden'
            pos_hint: {'center_x':0.5,'center_y':0.51}
            size_hint: 0.3, 0.05
            on_release: 
                root.verify_credentials()

<MenuScreen>:
    name: 'Menu'

    FloatLayout:

        MDToolbar:
            title: 'menu'
            pos_hint: {'center_x':0.5, 'top':1}
            left_action_items: [['menu', lambda x: nav_drawer.set_state()]]
            elevation: 10

        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'

                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'Menu'
                            on_press:
                                nav_drawer.set_state("close")
                                root.manager.transition = FadeTransition(duration=0.01)
                                root.manager.current = 'Menu'
                            IconLeftWidget:
                                icon: 'home'

                        OneLineIconListItem:
                            text: 'Verbruiker 1'
                            on_press:
                                nav_drawer.set_state("close")
                                root.manager.transition = FadeTransition(duration=0.01)
                                root.manager.current = 'Verbruiker1'
                            IconLeftWidget:
                                icon: 'lightbulb'

                        OneLineIconListItem:
                            text: 'Verbruiker 2'
                            on_press:
                                nav_drawer.set_state("close")
                                root.manager.transition = FadeTransition(duration=0.01)
                                root.manager.current = 'Verbruiker2'
                            IconLeftWidget:
                                icon: 'lightbulb'

                        OneLineIconListItem:
                            text: 'Verbruiker 3'
                            on_press:
                                nav_drawer.set_state("close")
                                root.manager.transition = FadeTransition(duration=0.01)
                                root.manager.current = 'Verbruiker3'
                            IconLeftWidget:
                                icon: 'lightbulb'

                        OneLineIconListItem:
                            text: 'Verbruiker 4'
                            on_press:
                                nav_drawer.set_state("close")
                                root.manager.transition = FadeTransition(duration=0.01)
                                root.manager.current = 'Verbruiker4'
                            IconLeftWidget:
                                icon: 'lightbulb'

                        OneLineIconListItem:
                            text: 'Logout'
                            on_press:
                                nav_drawer.set_state("close")
                                root.manager.transition = FadeTransition(duration=0.01)
                                root.manager.current = 'Login'
                            IconLeftWidget:
                                icon: 'logout'

<Verbruiker1Screen>:
    name: 'Verbruiker1'

    Label:
        id: label_boven
        text: app.label_boven
        font_size: 25
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.75}

    FloatLayout:
        MDToolbar:
            title: 'Verbruiker'
            pos_hint: {'center_x':0.5, 'top':1}
            left_action_items: [['menu', lambda x: nav_drawer.set_state()]]
            elevation: 10

        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'

                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'Menu'
                            on_press:
                                nav_drawer.set_state("close")
                                root.manager.transition = FadeTransition(duration=0.01)
                                root.manager.current = 'Menu'
                            IconLeftWidget:
                                icon: 'home'

                        OneLineIconListItem:
                            text: 'Verbruiker 1'
                            on_press:
                                nav_drawer.set_state("close")
                                root.manager.transition = FadeTransition(duration=0.01)
                                root.manager.current = 'Verbruiker1'
                            IconLeftWidget:
                                icon: 'lightbulb'

                        OneLineIconListItem:
                            text: 'Verbruiker 2'
                            on_press:
                                nav_drawer.set_state("close")
                                root.manager.transition = FadeTransition(duration=0.01)
                                root.manager.current = 'Verbruiker2'
                            IconLeftWidget:
                                icon: 'lightbulb'

                        OneLineIconListItem:
                            text: 'Verbruiker 3'
                            on_press:
                                nav_drawer.set_state("close")
                                root.manager.transition = FadeTransition(duration=0.01)
                                root.manager.current = 'Verbruiker3'
                            IconLeftWidget:
                                icon: 'lightbulb'

                        OneLineIconListItem:
                            text: 'Verbruiker 4'
                            on_press:
                                nav_drawer.set_state("close")
                                root.manager.transition = FadeTransition(duration=0.01)
                                root.manager.current = 'Verbruiker4'
                            IconLeftWidget:
                                icon: 'lightbulb'

                        OneLineIconListItem:
                            text: 'Logout'
                            on_press:
                                nav_drawer.set_state("close")
                                root.manager.transition = FadeTransition(duration=0.01)
                                root.manager.current = 'Login'
                            IconLeftWidget:
                                icon: 'logout'

<Verbruiker2Screen>:
    name: 'Verbruiker2'

    Label:
        id: label_beneden
        text: app.label_beneden
        font_size: 25
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.75}

    FloatLayout:
        MDToolbar:
            title: 'Beneden'
            pos_hint: {'center_x':0.5, 'top':1}
            left_action_items: [['menu', lambda x: nav_drawer.set_state()]]
            elevation: 10

        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'

                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'Menu'
                            on_press:
                                nav_drawer.set_state("close")
                                root.manager.transition = FadeTransition(duration=0.01)
                                root.manager.current = 'Menu'
                            IconLeftWidget:
                                icon: 'home'

                        OneLineIconListItem:
                            text: 'Verbruiker 1'
                            on_press:
                                nav_drawer.set_state("close")
                                root.manager.transition = FadeTransition(duration=0.01)
                                root.manager.current = 'Verbruiker1'
                            IconLeftWidget:
                                icon: 'lightbulb'

                        OneLineIconListItem:
                            text: 'Verbruiker 2'
                            on_press:
                                nav_drawer.set_state("close")
                                root.manager.transition = FadeTransition(duration=0.01)
                                root.manager.current = 'Verbruiker2'
                            IconLeftWidget:
                                icon: 'lightbulb'

                        OneLineIconListItem:
                            text: 'Verbruiker 3'
                            on_press:
                                nav_drawer.set_state("close")
                                root.manager.transition = FadeTransition(duration=0.01)
                                root.manager.current = 'Verbruiker3'
                            IconLeftWidget:
                                icon: 'lightbulb'

                        OneLineIconListItem:
                            text: 'Verbruiker 4'
                            on_press:
                                nav_drawer.set_state("close")
                                root.manager.transition = FadeTransition(duration=0.01)
                                root.manager.current = 'Verbruiker4'
                            IconLeftWidget:
                                icon: 'lightbulb'

                        OneLineIconListItem:
                            text: 'Logout'
                            on_press:
                                nav_drawer.set_state("close")
                                root.manager.transition = FadeTransition(duration=0.01)
                                root.manager.current = 'Login'
                            IconLeftWidget:
                                icon: 'logout'

<Verbruiker3Screen>:
    name: 'Verbruiker3'

    Label:
        id: label_buiten
        text: app.label_buiten
        font_size: 25
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.75}

    FloatLayout:
        MDToolbar:
            title: 'Buiten'
            pos_hint: {'center_x':0.5, 'top':1}
            left_action_items: [['menu', lambda x: nav_drawer.set_state()]]
            elevation: 10

        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'

                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'Menu'
                            on_press:
                                nav_drawer.set_state("close")
                                root.manager.transition = FadeTransition(duration=0.01)
                                root.manager.current = 'Menu'
                            IconLeftWidget:
                                icon: 'home'

                        OneLineIconListItem:
                            text: 'Verbruiker 1'
                            on_press:
                                nav_drawer.set_state("close")
                                root.manager.transition = FadeTransition(duration=0.01)
                                root.manager.current = 'Verbuiker1'
                            IconLeftWidget:
                                icon: 'lightbulb'

                        OneLineIconListItem:
                            text: 'Verbruiker 2'
                            on_press:
                                nav_drawer.set_state("close")
                                root.manager.transition = FadeTransition(duration=0.01)
                                root.manager.current = 'Verbruiker2'
                            IconLeftWidget:
                                icon: 'lightbulb'

                        OneLineIconListItem:
                            text: 'Verbruiker 3'
                            on_press:
                                nav_drawer.set_state("close")
                                root.manager.transition = FadeTransition(duration=0.01)
                                root.manager.current = 'Verbruiker3'
                            IconLeftWidget:
                                icon: 'lightbulb'

                        OneLineIconListItem:
                            text: 'Verbruiker 4'
                            on_press:
                                nav_drawer.set_state("close")
                                root.manager.transition = FadeTransition(duration=0.01)
                                root.manager.current = 'Verbruiker4'
                            IconLeftWidget:
                                icon: 'lightbulb'

                        OneLineIconListItem:
                            text: 'Logout'
                            on_press:
                                nav_drawer.set_state("close")
                                root.manager.transition = FadeTransition(duration=0.01)
                                root.manager.current = 'Login'
                            IconLeftWidget:
                                icon: 'logout'

<Verbruiker4Screen>:
    name: 'Verbruiker4'

    Label:
        id: label_boven
        text: app.label_boven
        font_size: 25
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.75}

    FloatLayout:
        MDToolbar:
            title: 'Verbruiker'
            pos_hint: {'center_x':0.5, 'top':1}
            left_action_items: [['menu', lambda x: nav_drawer.set_state()]]
            elevation: 10

        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'

                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'Menu'
                            on_press:
                                nav_drawer.set_state("close")
                                root.manager.transition = FadeTransition(duration=0.01)
                                root.manager.current = 'Menu'
                            IconLeftWidget:
                                icon: 'home'

                        OneLineIconListItem:
                            text: 'Verbruiker 1'
                            on_press:
                                nav_drawer.set_state("close")
                                root.manager.transition = FadeTransition(duration=0.01)
                                root.manager.current = 'Verbruiker1'
                            IconLeftWidget:
                                icon: 'lightbulb'

                        OneLineIconListItem:
                            text: 'Verbruiker 2'
                            on_press:
                                nav_drawer.set_state("close")
                                root.manager.transition = FadeTransition(duration=0.01)
                                root.manager.current = 'Verbruiker2'
                            IconLeftWidget:
                                icon: 'lightbulb'

                        OneLineIconListItem:
                            text: 'Verbruiker 3'
                            on_press:
                                nav_drawer.set_state("close")
                                root.manager.transition = FadeTransition(duration=0.01)
                                root.manager.current = 'Verbruiker3'
                            IconLeftWidget:
                                icon: 'lightbulb'

                        OneLineIconListItem:
                            text: 'Verbruiker 4'
                            on_press:
                                nav_drawer.set_state("close")
                                root.manager.transition = FadeTransition(duration=0.01)
                                root.manager.current = 'Verbruiker4'
                            IconLeftWidget:
                                icon: 'lightbulb'

                        OneLineIconListItem:
                            text: 'Logout'
                            on_press:
                                nav_drawer.set_state("close")
                                root.manager.transition = FadeTransition(duration=0.01)
                                root.manager.current = 'Login'
                            IconLeftWidget:
                                icon: 'logout'
"""