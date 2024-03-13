from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

import random
import Global

#shoot-out screen creation
class ShootoutScreen(BoxLayout, Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #Create the layout for the screen, two smaller boxes placed vertically to each other
        self.orientation='vertical'

        self.rps = [    ("Dodge","Single-Shot"), 
                        ("Single-Shot","Bullet Spray"), 
                        ("Bullet Spray","Dodge"), 
                        ("Single-Shot","Brawl"), 
                        ("Bullet Spray","Brawl"),
                        ("Brawl","Dodge")]
        
        self.toolBar         = BoxLayout(orientation='horizontal')
        self.horizontalBox   = BoxLayout(orientation='horizontal')
        self.verticalBox     = BoxLayout(orientation='vertical')

        #Create the player attack option buttons
        for i in Global.player.attackList:
            self.button = Button(text=i)
            self.button.bind(on_press=self.shoot_out)
            self.horizontalBox.add_widget(self.button)

        #Create button to return user to main menu
        self.button2 = Button(text="Back")
        self.button2.bind(on_press=self.toMainMenu)
        self.horizontalBox.add_widget(self.button2)

        #Create Main text area for shootout screen
        self.textbox = Label(text="Prepare to Duel!", markup = True)
        self.verticalBox.add_widget(self.textbox)

        #Create Toolbar for info
        self.healthBox = Label(text=f"Health: {Global.player.health}", markup = True)
        self.toolBar.add_widget(self.healthBox)
        self.ammoBox = Label(text=f"Ammo: {Global.player.ammunition}", markup = True)
        self.toolBar.add_widget(self.ammoBox)


        #Add the two subboxes to the screen
        self.add_widget(self.toolBar)
        self.add_widget(self.verticalBox)
        self.add_widget(self.horizontalBox)

    #Setter for main text area
    def setText(self, newText):
        self.textbox.text = newText

    def refreshText(self):
        self.ammoBox.text = f"Ammo: {Global.player.ammunition}"
        self.healthBox.text = f"Health: {Global.player.health}"
            
    def enemy_damaged(self):
        print ("enemy Damaged")
        Global.enemy.health-=Global.player.currentDamage
        if Global.enemy.health<=0:
            self.manager.current = 'victory_screen'
        else:
            print (f"Health of the enemy: {Global.enemy.health}, The enemy took {Global.player.currentDamage}")
            self.setText ("He's hit but not down, go again!")
        
    def player_damaged(self):
        print ("player damaged")
        Global.player.health-=Global.enemy.currentDamage
        if Global.player.health<=0:
            self.manager.current = 'death_screen'
        else:
            print (f"Health of the player: {Global.player.health}, The player took {Global.enemy.currentDamage}")
            self.setText ("You're hit but it's not over yet!")

    def toMainMenu(self, event):
        self.manager.current = "main_menu"
        #self.manager.current = "main_menu"

    def shoot_out_round():
        pass

    def match_stats(self, input, entity):
        print (f"{entity} chose {input}")
        entity.currentDamage = Global.enemy.statistics.get('damage')
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

        Global.player.currentDamage = Global.enemy.statistics.get('damage')
        Global.enemy.currentDamage = Global.player.statistics.get('damage')

        enemyChoice = random.choice(Global.enemy.attackList)

        playerStat = self.match_stats(button.text, Global.player)
        enemyStat = self.match_stats(enemyChoice, Global.enemy)

        if (button.text,enemyChoice) in self.rps:
            playerStat+=3
        elif (button.text == enemyChoice):
            pass
        else:
            enemyStat+=3
        self.compare_stats(playerStat, enemyStat)

        self.refreshText()