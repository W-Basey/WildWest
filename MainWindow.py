from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

import sys

import Global

class MainWindow(BoxLayout, Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.shootOutButton = Button(text="ShootOut!")
        self.shootOutButton.bind(on_press=self.gotoShootOut)

        self.exitButton = Button(text="Exit")
        self.exitButton.bind(on_press=self.exitGame)

        self.characterCreate = Button(text="Create a Character")
        self.characterCreate.bind(on_press=self.gotoCharacterCreate)

        #Add widgets to the screen
        self.add_widget(self.shootOutButton)
        self.add_widget(self.characterCreate)
        self.add_widget(self.exitButton)

    def gotoCharacterCreate(self, event):
        self.manager.current = 'character_create_screen'

    #Moves current screen to shootout
    def gotoShootOut(self, event):
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
    def exitGame(self, event):
        sys.exit()