# pokerapp.py

from dice import Dice

class PokerApp:

    def __init__(self, interface):
        self.dice = Dice()
        self.interface = interface
        self.money = 100
        self.betAmt=0

    def run(self):
        while self.money >= 10 and self.interface.wantToPlay:
            self.betAmt = self.interface.inputBet()
            if self.money<self.betAmt:
                break
            if self.betAmt ==0:
                break
            self.playRound()            
        self.interface.close()

    def playRound(self):
        self.money = self.money - self.betAmt
        self.interface.setMoney(self.money)
        self.doRolls()
        result, score = self.dice.score()
        score = int(self.betAmt*score/10)
        self.interface.showResult(result, score, self.betAmt)
        self.money = self.money + score
        self.interface.setMoney(self.money)
    def doRolls(self):
        self.dice.rollAll()
        roll = 1
        self.interface.setDice(self.dice.values())
        toRoll = self.interface.chooseDice()
        while roll < 3 and toRoll != []:
            self.dice.roll(toRoll)
            roll = roll + 1
            self.interface.setDice(self.dice.values())
            if roll < 3:
                toRoll = self.interface.chooseDice()
