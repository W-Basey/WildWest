
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import StringProperty
from kivy.core.window import Window

import sys

import Global
from ShootoutScreen import ShootoutScreen

#Define Globals

#Define overall app charicteristics
Window.size = (600, 400)

#Main menu screen creation
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
        
#Screen the enemy sees upon a game over
class DeathScreen(BoxLayout, Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation='vertical'

        self.textbox = Label(text="[b][color=ff3333]Not Today Partner...[/color][/b]", markup = True)

        self.button1 = Button(text="Exit")
        self.button1.bind(on_press=self.handle_button1_clicked)

        self.add_widget(self.textbox)
        self.add_widget(self.button1)

    def handle_button1_clicked(self, event):
        self.manager.current = "main_menu"

class VictoryScreen(BoxLayout, Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation='vertical'

        self.textbox = Label(text="[b][color=#50C878]You Win![/color][/b]", markup = True)

        self.button1 = Button(text="Exit")
        self.button1.bind(on_press=self.handle_button2_clicked)

        self.add_widget(self.textbox)
        self.add_widget(self.button1)

    def handle_button1_clicked(self, event):
        self.manager.current = 'shootout_screen'

    def handle_button2_clicked(self, event):
        self.manager.current = "main_menu"


class MyApp(App):
    def build(self):
        self.title = "Wild West!"

        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(MainWindow(name='main_menu'))
        sm.add_widget(ShootoutScreen(name='shootout_screen'))
        sm.add_widget(DeathScreen(name='death_screen'))
        sm.add_widget(VictoryScreen(name='victory_screen'))

        sm.current = "main_menu"

        return sm  


if __name__ == "__main__":
    MyApp().run()