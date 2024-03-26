from kivy.uix.screenmanager import SScreen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

import Global
import sys

class encounterWindow(BoxLayout, Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.options[1]
        
        self.toolBar         = BoxLayout(orientation='horizontal')
        self.horizontalBox   = BoxLayout(orientation='horizontal')

        #Create Toolbar for info
        self.healthBox = Label(text=f"Health: {Global.player.health}", markup = True)
        self.toolBar.add_widget(self.healthBox)
        self.ammoBox = Label(text=f"Ammo: {Global.player.ammunition}", markup = True)
        self.toolBar.add_widget(self.ammoBox)


        for i in Global.player.attackList:
            self.button = Button(text=i)
            self.button.bind(on_press=self.shoot_out)
            self.horizontalBox.add_widget(self.button)


        self.exitButton = Button(text="Exit")
        self.exitButton.bind(on_press=self.exitGame)

        #Add widgets to the screen
        self.add_widget(self.horizontalBox)
        self.add_widget(self.exitButton)


    #Closes the application
    def exitGame(self, event):
        sys.exit()