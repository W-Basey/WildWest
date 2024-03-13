from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from ShootoutScreen import ShootoutScreen
from DeathScreen import DeathScreen
from VictoryScreen import VictoryScreen
from MainWindow import MainWindow
from CharacterCreateScreen import CharacterCreateScreen

class Application(App):
    def build(self):
        self.title = "Wild West!"

        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(MainWindow(name='main_menu'))
        sm.add_widget(ShootoutScreen(name='shootout_screen'))
        sm.add_widget(DeathScreen(name='death_screen'))
        sm.add_widget(VictoryScreen(name='victory_screen'))
        sm.add_widget(CharacterCreateScreen(name='character_create_screen'))

        sm.current = "main_menu"

        return sm  