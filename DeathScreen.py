from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

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