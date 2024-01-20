# guipoker.py

from graphics import *
from pokerapp import PokerApp
from button import Button
from cdieview import ColorDieView


class GraphicsInterface:

    def __init__(self):
        self.win = GraphWin("Dice Poker", 600, 400)
        self.win.setBackground("green3")
        banner = Text(Point(300,30), "Python  Poker  Parlor")
        banner.setSize(24)
        banner.setFill("yellow2")
        banner.setStyle("bold")
        banner.draw(self.win)
        self.msg = Text(Point(300,380), "Welcome to the Dice Table")
        self.msg.setSize(18)
        self.msg.draw(self.win)
        self.createDice(Point(300,100), 75)
        self.buttons = []
        self.addDiceButtons(Point(300,170), 75, 30)
        b = Button(self.win, Point(300, 230), 400, 40, "Roll Dice")
        self.buttons.append(b)
        b = Button(self.win, Point(300, 280), 150, 40, "Score")
        self.buttons.append(b)
        b = Button(self.win, Point(570,375), 40, 30, "Quit")
        self.buttons.append(b)
        self.money = Text(Point(300,325), "$100")
        self.money.setSize(18)
        self.money.draw(self.win)
        Help = Rectangle(Point(595,50),Point(555,10))
        Help.setFill('white')
        Helptext = Text(Point(575,30),"Help")
        Help.draw(self.win)
        Helptext.draw(self.win)
        self.default = 10
    def HelpButton(self):
        window = GraphWin("Help", 300,280)
        window.setBackground("green1")
        Exit = Rectangle(Point(275,25),Point(295,5))
        Exit.setFill("white")
        Exit.draw(window)
        cross = Text(Point(285,15),'X')
        cross.draw(window)
        box = Rectangle(Point(20,250),Point(260,30))
        box.setFill("white")
        line = Line(Point(200,40),Point(200,250))
        line.draw(window)
        for i in range(6):
            line = Line(Point(20,220-30*i),Point(260,220-30*i))
            line.draw(window)
        box.draw(window)
        Title = Text(Point(150,20),"For each $10 bet: ")
        Title.draw(window)
        Concl = Text(Point(150,265),"Winnings proportional to the bet amount")
        Concl.draw(window)
        win1_1 = Text(Point(120,45),"Hand")
        win1_2 = Text(Point(230,45),"Pay")
        win1_1.draw(window)
        win1_2.draw(window)
        win2_1 = Text(Point(120,75),"Two Pairs")
        win3_1 = Text(Point(120,105),"Three of a Kind")
        win4_1 = Text(Point(120,135),"Full House")
        win5_1 = Text(Point(120,165),"Four of a Kind")
        win6_1 = Text(Point(120,195),"Straight")
        win7_1 = Text(Point(120,225),"Five of a Kind")
        win2_1.draw(window)
        win3_1.draw(window)
        win4_1.draw(window)
        win5_1.draw(window)
        win6_1.draw(window)
        win7_1.draw(window)
        win2_2 = Text(Point(230,75),"5")
        win3_2 = Text(Point(230,105),"8")
        win4_2 = Text(Point(230,135),"12")
        win5_2 = Text(Point(230,165),"15")
        win6_2 = Text(Point(230,195),"20")
        win7_2 = Text(Point(230,225),"30")
        win2_2.draw(window)
        win3_2.draw(window)
        win4_2.draw(window)
        win5_2.draw(window)
        win6_2.draw(window)
        win7_2.draw(window)
        while True:
            click = window.getMouse()
            if click.getX()<=295 and click.getX()>=275 and click.getY()<=25 and click.getY()>=5:
                break
            else:
                continue
        window.close()
        return


    def inputBet(self):
        inpText = Text(Point(130,320),"Enter the value you want to bet")
        inptextbox = Entry(Point(130,340), 10)
        inpText.draw(self.win)
        inptextbox.draw(self.win)
        inptextbox.setText(self.default)
        if self.wantToPlay():
             self.default = float(eval(inptextbox.getText()))
             return self.default
        else:
            return 0
    
    def createDice(self, center, size):
        center.move(-3*size,0)
        self.dice = []
        for i in range(5):
            view = ColorDieView(self.win, center, size)
            self.dice.append(view)
            center.move(1.5*size,0)

    def addDiceButtons(self, center, width, height):
        center.move(-3*width, 0)
        for i in range(1,6):
            label = "Die {0}".format(i)
            b = Button(self.win, center, width, height, label)
            self.buttons.append(b)
            center.move(1.5*width, 0)

    def setMoney(self, amt):
        self.money.setText("${0}".format(amt))

    def showResult(self, msg, score, betAmt):
        if score > 0:
            text = "{0}! You win ${1}".format(msg, score)
        else:
            text = "You rolled {0}".format(msg)
        self.msg.setText(text)

    def setDice(self, values):
        for i in range(5):
            self.dice[i].setValue(values[i])

    def wantToPlay(self):
        ans = self.choose(["Roll Dice", "Quit"])
        self.msg.setText("")
        return ans == "Roll Dice"

    def close(self):
        self.win.close()

    def chooseDice(self):
        # choices is a list of the indexes of the selected dice
        choices = []                   # No dice chosen yet
        while True: 
            # wait for user to click a valid button
            b = self.choose(["Die 1", "Die 2", "Die 3", "Die 4", "Die 5",
                             "Roll Dice", "Score"])

            if b[0] == "D":            # User clicked a die button
                i = int(b[4]) - 1      # Translate label to die index
                if i in choices:       # Currently selected, unselect it
                    choices.remove(i)
                    self.dice[i].setColor("black")
                else:                  # Currently unselected, select it
                    choices.append(i)
                    self.dice[i].setColor("gray")
            else:                      # User clicked Roll or Score
                for d in self.dice:    # Revert appearance of all dice
                    d.setColor("black")
                if b == "Score":       # Score clicked, ignore choices
                    return []
                elif choices != []:    # Don't accept Roll unless some
                    return choices     #   dice are actually selected

    
    def choose(self, choices):
        buttons = self.buttons

        # activate choice buttons, deactivate others
        for b in buttons:
            if b.getLabel() in choices:
                b.activate()
            else:
                b.deactivate()

        # get mouse clicks until an active button is clicked
        while True:
            p = self.win.getMouse()
            for b in buttons:
                if b.clicked(p):
                    return b.getLabel()  # function exit here.
            self.checkforhelp(p)
        
    def checkforhelp(self,p):
        if 555 <= p.getX() <= 595 and 10 <= p.getY() <= 50:
            self.HelpButton()
        
            
inter = GraphicsInterface()
app = PokerApp(inter)
app.run()
