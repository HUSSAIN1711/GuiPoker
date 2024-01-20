class Help:

    def __init__(self,win):
        Help = Rectangle(Point(595,50),Point(555,10))
        Help.setFill('white')
        Helptext = Text(Point(575,30),"Help")
        Help.draw(win)
        Helptext.draw(win)

    def clicked(self,p):
        if 555 <= p.getX() <= 595 and 10 <= p.getY() <= 50:
            return True
        else:
            return False

    def HelpButton():
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
