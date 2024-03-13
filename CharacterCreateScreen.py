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

        self.orientation='horizontal'

        for x in Global.player.statistics.keys():
            self.box = BoxLayout(orientation='vertical')
            self.up = Button(text="Increase")
            self.up.bind(on_press=lambda *args: self.increaseValue(x))
            self.box.add_widget(self.up)
            self.text = Label(text=f"{x} {Global.player.statistics[x]}", markup = True)
            self.statLabels.append(self.text)
            self.box.add_widget(self.text)
            self.down = Button(text="Decrease")
            self.down.bind(on_press=lambda *args: self.decreaseValue(x))


            self.box.add_widget(self.down)

            self.add_widget(self.box)
        

        self.exitButton = Button(text="Exit")
        self.exitButton.bind(on_press=self.gotoMainMenu)

        self.add_widget(self.exitButton)

    def gotoMainMenu(self, event):
        self.manager.current = "main_menu"

    def refreshLabels(self):
        i = 0
        print (self.statLabels)
        for x in Global.player.statistics.keys():
            self.statLabels[i].text = f"{x} {Global.player.statistics[x]}"
            i+=1

    def increaseValue(self, currentkey):
        print (f"Increased {currentkey}")
        Global.player.statistics[currentkey] += 1
        self.refreshLabels()
        return 1


    def decreaseValue(self, currentkey):
        print(f"Decreased {currentkey}")
        Global.player.statistics[currentkey] -= 1
        self.refreshLabels()
        return 1