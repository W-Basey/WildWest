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
        Global.player.refresh()
        Global.enemy.refresh

        shootOutscreen = self.manager.get_screen('shootout_screen')
        shootOutscreen.refreshText()
        self.manager.current = 'shootout_screen'

    #Closes the application
    def exitGame(self, event):
        sys.exit()