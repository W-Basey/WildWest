from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window

import sys

Window.size = (300, 200)
a = [(1,2), (2,3), (3,1),]
sm = ScreenManager()

class MainWindow(BoxLayout, Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.button1 = Button(text="ShootOut!")
        self.button1.bind(on_press=self.handle_button1_clicked)

        self.button2 = Button(text="Exit")
        self.button2.bind(on_press=self.handle_button2_clicked)

        self.add_widget(self.button1)
        self.add_widget(self.button2)

    def handle_button1_clicked(self, event):
        print ("Yee HAW")
        sm.current = "shootout_screen"

    def handle_button2_clicked(self, event):
        sys.exit()

class ShootoutScreen(BoxLayout, Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.button1 = Button(text="HELLO!")
        self.button1.bind(on_press=self.handle_button1_clicked)

        self.button2 = Button(text="Back")
        self.button2.bind(on_press=self.handle_button2_clicked)

        self.add_widget(self.button1)
        self.add_widget(self.button2)



    def handle_button1_clicked(self, event):
        print ("Yee HAW")
        

    def handle_button2_clicked(self, event):
        sm.current = "main_menu"

class WindowManager(ScreenManager):
    pass



class MyApp(App):
    def build(self):
        self.title = "Wild West!"
        # Create the screen manager
        sm.add_widget(MainWindow(name="main_menu"))
        sm.add_widget(ShootoutScreen(name="shootout_screen"))

        sm.current = "main_menu"
        return sm  


def shoot_out():
    #Input1
    #Random Choice 2
    give_winner()


def give_winner(first_selection, second_selection):
    return (first_selection, second_selection) in a








if __name__ == "__main__":
    app = MyApp()
    app.run()