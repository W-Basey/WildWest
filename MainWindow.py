from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

import sys

import Global

class MainWindow(BoxLayout, Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.button1 = Button(text="ShootOut!")
        self.button1.bind(on_press=self.handle_button1_clicked)

        self.button2 = Button(text="Exit")
        self.button2.bind(on_press=self.handle_button2_clicked)

        #Add widgets to the screen
        self.add_widget(self.button1)
        self.add_widget(self.button2)

    #Moves current screen to shootout
    def handle_button1_clicked(self, event):
        #Temporary: Reset player and enemy stats for the fight
        Global.player.statistics = {
            "max_health": 3,
            "dexterity": 2,
            "accuracy": 4,
            "speed": 3,
            "damage": 1,
            "strength": 1
        }

        Global.player.health = Global.player.statistics.get('max_health')
        Global.enemy.health = Global.enemy.statistics.get('max_health')

        Global.player.currentDamage = Global.player.statistics.get('damage')
        Global.enemy.currentDamage = Global.enemy.statistics.get('damage')

        Global.player.ammunition = 6
        Global.enemy.ammunition = 6

        self.manager.current = "shootout_screen"

    #Closes the application
    def handle_button2_clicked(self, event):
        sys.exit()