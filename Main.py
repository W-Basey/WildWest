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
        #Temporary: Reset player and enemy stats for the fight
        player.statistics = {
            "max_health": 3,
            "dexterity": 2,
            "accuracy": 4,
            "speed": 3,
            "damage": 1,
            "strength": 1
        }

        player.health = player.statistics.get('max_health')
        enemy.health = enemy.statistics.get('max_health')

        player.currentDamage = player.statistics.get('damage')
        enemy.currentDamage = enemy.statistics.get('damage')

        player.ammunition = 6
        enemy.ammunition = 6

        sm.current = "shootout_screen"

    #Closes the application
    def handle_button2_clicked(self, event):
        sys.exit()

#shoot-out screen creation
class ShootoutScreen(BoxLayout, Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #Create the layout for the screen, two smaller boxes placed vertically to each other
        self.orientation='vertical'

        self.toolBar         = BoxLayout(orientation='horizontal')
        self.horizontalBox   = BoxLayout(orientation='horizontal')
        self.verticalBox     = BoxLayout(orientation='vertical')

        #Create the player attack option buttons
        for i in player.attackList:
            self.button = Button(text=i)
            self.button.bind(on_press=self.shoot_out)
            self.horizontalBox.add_widget(self.button)

        #Create button to return user to main menu
        self.button2 = Button(text="Back")
        self.button2.bind(on_press=self.handle_button2_clicked)
        self.horizontalBox.add_widget(self.button2)

        #Create Main text area for shootout screen
        self.textbox = Label(text="Prepare to Duel!", markup = True)
        self.verticalBox.add_widget(self.textbox)

        #Create Toolbar for info
        self.healthBox = Label(text=f"Health: {player.health}", markup = True)
        self.toolBar.add_widget(self.healthBox)
        self.ammoBox = Label(text=f"Ammo: {player.ammunition}", markup = True)
        self.toolBar.add_widget(self.ammoBox)


        #Add the two subboxes to the screen
        self.add_widget(self.toolBar)
        self.add_widget(self.verticalBox)
        self.add_widget(self.horizontalBox)

    #Setter for main text area
    def setText(self, newText):
        self.textbox.text = newText

    def refreshText(self):
        self.ammoBox.text = f"Ammo: {player.ammunition}"
        self.healthBox.text = f"Health: {player.health}"
            
    def enemy_damaged(self):
        print ("enemy Damaged")
        enemy.health-=player.currentDamage
        if enemy.health<=0:
            sm.current = 'victory_screen'
        else:
            print (f"Health of the enemy: {enemy.health}, The enemy took {player.currentDamage}")
            self.setText ("He's hit but not down, go again!")
        
    def player_damaged(self):
        print ("player damaged")
        player.health-=enemy.currentDamage
        if player.health<=0:
            sm.current = 'death_screen'
        else:
            print (f"Health of the player: {player.health}, The player took {enemy.currentDamage}")
            self.setText ("You're hit but it's not over yet!")

    def handle_button2_clicked(self, event):
        sm.current = "main_menu"

    def shoot_out_round():
        pass

    def match_stats(self, input, entity):
        print (f"{entity} chose {input}")
        entity.currentDamage = enemy.statistics.get('damage')
        match input:
            case 'Dodge':
                stat = entity.statistics.get('dexterity')
                entity.currentDamage = 0
            case 'Single-Shot':
                stat = entity.statistics.get('accuracy')
                if entity.ammunition < 1:
                    print(f"{entity} click.....")
                    entity.currentDamage = 0
                else:
                    entity.ammunition -=1
            case 'Bullet Spray':
                stat = entity.statistics.get('speed')
                if entity.ammunition < 1:
                    print(f"{entity} click.....")
                    entity.currentDamage = 0
                else:
                    entity.currentDamage = min(max(stat/3,1),entity.ammunition)*entity.currentDamage
                    entity.ammunition -= min(max(stat//3,1),entity.ammunition)
            case 'Brawl':
                stat = entity.statistics.get('strength')
                entity.currentDamage = stat
        return stat

    def compare_stats(self, player, enemy):
        winner = random.randint(1,player+enemy)
        if winner < player:
            self.enemy_damaged()
            print (f"Player Win")
        elif winner > player:
            self.player_damaged()
            print (f"Enemy Win")
        else:
            self.setText ("Neither party succeeds")
            print (f"Draw")
        print (f"Player: {player} Enemy: {enemy} Rolled: {winner}")


    #Player vs Enemy RPS battle main function, activated by button
    def shoot_out(self, button):

        player.currentDamage = enemy.statistics.get('damage')
        enemy.currentDamage = player.statistics.get('damage')

        enemyChoice = random.choice(enemy.attackList)

        playerStat = self.match_stats(button.text, player)
        enemyStat = self.match_stats(enemyChoice, enemy)

        if (button.text,enemyChoice) in a:
            playerStat+=3
        elif (button.text == enemyChoice):
            pass
        else:
            enemyStat+=3
        self.compare_stats(playerStat, enemyStat)

        self.refreshText()
        
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
        self.currentDamage = 0

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
    enemy = Enemy()
    app.run()