import random
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import StringProperty
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

        self.orientation='vertical'
        self.horizontalBox   = BoxLayout(orientation='horizontal')
        self.verticalBox     = BoxLayout(orientation='vertical')

        for i in range(1,4):
            self.button = Button(text=str(i))
            self.button.bind(on_press=self.shoot_out)
            self.horizontalBox.add_widget(self.button)

        self.button2 = Button(text="Back")
        self.button2.bind(on_press=self.handle_button2_clicked)
        self.horizontalBox.add_widget(self.button2)

        self.textbox = Label(text="Prepare to Duel!", markup = True)
        self.verticalBox.add_widget(self.textbox)

        self.add_widget(self.verticalBox)
        self.add_widget(self.horizontalBox)

    def setText(self, newText):
        self.textbox.text = newText
        
    def shoot_out(self, button):
        #Input1
        buttonId = int(button.text)
        enemyChoice = random.randint(1,3)
        print (f"Enemy Chose: {enemyChoice} You Chose: {buttonId}")
        if (int(buttonId),enemyChoice) in a:
            self.setText ("[b][color=#50C878]You Win![/color][/b]")
        elif (int(buttonId) == enemyChoice):
            self.setText ("Quick again!")
        else:
            self.setText ("[b][color=ff3333]Not Today Partner...[/color][/b]")

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


if __name__ == "__main__":
    app = MyApp()
    app.run()