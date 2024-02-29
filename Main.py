import random
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import StringProperty
from kivy.core.window import Window

import sys

#Define Globals

#Define overall app charicteristics
Window.size = (600, 400)
a = [("Dodge","Single-Shot"), 
     ("Single-Shot","Bullet Spray"), 
     ("Bullet Spray","Dodge"), 
     ("Single-Shot","Brawl"), 
     ("Bullet Spray","Brawl"),
     ("Brawl","Dodge")]
sm = ScreenManager()


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
        sm.current = "shootout_screen"

    #Closes the application
    def handle_button2_clicked(self, event):
        sys.exit()

#shoot-out screen creation
class ShootoutScreen(BoxLayout, Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #Create the enemy for the shootout
        self.enemy = Enemy()
        #Temporary: Reset player and enemy stats for the fight
        player.health = player.statistics.get('max_health')
        self.enemy.health = self.enemy.statistics.get('max_health')


        #Create the layout for the screen, two smaller boxes placed vertically to each other
        self.orientation='vertical'
        self.horizontalBox   = BoxLayout(orientation='horizontal')
        self.verticalBox     = BoxLayout(orientation='vertical')

        #Create the player attack option buttons
        for i in player.attackList:
            self.button = Button(text=i)
            self.button.bind(on_press=self.shoot_out)
            self.horizontalBox.add_widget(self.button)

        #Creat button to return user to main menu
        self.button2 = Button(text="Back")
        self.button2.bind(on_press=self.handle_button2_clicked)
        self.horizontalBox.add_widget(self.button2)

        #Create Main text area for shootout screen
        self.textbox = Label(text="Prepare to Duel!", markup = True)
        self.verticalBox.add_widget(self.textbox)

        #Add the two subboxes to the screen
        self.add_widget(self.verticalBox)
        self.add_widget(self.horizontalBox)

    #Setter for main text area
    def setText(self, newText):
        self.textbox.text = newText
    
    #Player vs Enemy RPS battle main function, activated by button
    def shoot_out(self, button):

        enemyChoice = random.choice(self.enemy.attackList)
        print (f"Enemy Chose: {enemyChoice} You Chose: {button.text}")
        if (button.text,enemyChoice) in a:
            self.enemy.health-=player.statistics.get('damage')
            if (self.enemy.health<=0):
                sm.current = 'victory_screen'
            else:
                print (f"Health of the enemy: {self.enemy.health}\nThe enemy took {player.statistics['damage']}")
                self.setText ("He's hit but not down, go again!")
        elif (button.text == enemyChoice):
            self.setText ("Quick again!")
        else:
            player.health-=self.enemy.statistics.get('damage')
            if (player.health<=0):
                sm.current = 'death_screen'
            else:
                print (f"Health of the player: {player.health}")
                self.setText ("You're hit but it's not over yet!")
            

    def handle_button2_clicked(self, event):
        sm.current = "main_menu"

    def shoot_out_round():
        pass

#Screen the enemy sees upon a game over
class DeathScreen(BoxLayout, Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation='vertical'

        self.textbox = Label(text="[b][color=ff3333]Not Today Partner...[/color][/b]", markup = True)

        self.button1 = Button(text="Exit")
        self.button1.bind(on_press=self.handle_button2_clicked)

        self.add_widget(self.textbox)
        self.add_widget(self.button1)

    def handle_button1_clicked(self, event):
        sm.current = 'shootout_screen'

    def handle_button2_clicked(self, event):
        sm.current = "main_menu"

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
        sm.current = 'shootout_screen'

    def handle_button2_clicked(self, event):
        sm.current = "main_menu"
    

class WindowManager(ScreenManager):
    pass

class Entity():
    def __init__(self, ):
        self.name = ""

        self.health = 3
        self.ammunition = 5

        self.statistics = {
            "max_health": 3,
            "dexterity": 1,
            "accuracy": 1,
            "speed": 1,
            "damage": 1,
            "strength": 1
        }
        self.attackList = ["Dodge", "Single-Shot", "Bullet Spray", "Brawl"]

class Enemy(Entity):
    def __init__(self):
        super().__init__()
        pass



class Player(Entity):
    def __init__(self):
        super().__init__()
        pass


class MyApp(App):
    def build(self):
        self.title = "Wild West!"
        # Create the screen manager
        sm.add_widget(MainWindow(name='main_menu'))
        sm.add_widget(ShootoutScreen(name='shootout_screen'))
        sm.add_widget(DeathScreen(name='death_screen'))
        sm.add_widget(VictoryScreen(name='victory_screen'))

        sm.current = "main_menu"

        return sm  


if __name__ == "__main__":
    app = MyApp()
    player = Player()
    app.run()