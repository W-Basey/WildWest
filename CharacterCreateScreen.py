from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

import Global

#Screen the enemy sees upon a game over
class CharacterCreateScreen(BoxLayout, Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.statLabels = []
        self.increaseButtons = []
        self.decreaseButtons = []

        self.boxlist = []

        self.orientation='horizontal'

        for x in Global.player.statistics.keys():
            self.boxlist.append(BoxLayout(orientation='vertical'))
            self.increaseButtons.append(Button(text="Increase"))
            self.increaseButtons[-1].bind(on_press=lambda *args, cred=x: self.increaseValue(cred))
            self.boxlist[-1].add_widget(self.increaseButtons[-1])
            self.statLabels.append(Label(text=f"{x} {Global.player.statistics[x]}", markup = True))
            self.boxlist[-1].add_widget(self.statLabels[-1])
            self.decreaseButtons.append(Button(text="Decrease"))
            self.decreaseButtons[-1].bind(on_press=lambda *args, cred=x: self.decreaseValue(cred))
            self.boxlist[-1].add_widget(self.decreaseButtons[-1])
            self.add_widget(self.boxlist[-1])
        

        self.exitButton = Button(text="Exit")
        self.exitButton.bind(on_press=self.gotoMainMenu)

        self.add_widget(self.exitButton)

    def gotoMainMenu(self, event):
        self.manager.current = "main_menu"

    def refreshLabels(self):
        i = 0
        for x in Global.player.statistics.keys():
            self.statLabels[i].text = f"{x} {Global.player.statistics[x]}"
            i+=1

    def increaseValue(self, currentkey):
        Global.player.statistics[currentkey] += 1
        self.refreshLabels()


    def decreaseValue(self, currentkey):
        Global.player.statistics[currentkey] -= 1
        self.refreshLabels()