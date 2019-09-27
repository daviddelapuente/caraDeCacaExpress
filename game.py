from Game.GameObjets import *
import os
class gameIA:
    def __init__(self,IA,deck,handLen,fieldsLen,dump):
        self.player1=player(hand([]),openField([]),closeField([]))
        self.player2=IA
        self.deck=deck
        self.handLen=handLen
        self.fieldsLen=fieldsLen
        self.keepPlaying=True
        self.dump=dump



    def repartirCartas(self):

        self.deck.shuffleDeck()
        self.player1.addTohand(deck.drawX(self.handLen))
        self.player1.addToOpenField(deck.drawX(self.fieldsLen))
        self.player1.addToCloseField(deck.drawX(self.fieldsLen))

        self.player2.addTohand(deck.drawX(self.handLen))
        self.player2.addToOpenField(deck.drawX(self.fieldsLen))
        self.player2.addToCloseField(deck.drawX(self.fieldsLen))


    def printGame(self):
        self.printOponentHand()
        self.printTable()
        self.printYourHand()

    def printYourHand(self):
        str=""
        hand=self.player1.getHand()
        cards=hand.getCards()
        for i in range(hand.fieldLen()):
            str+="["+ cards[i].getChar() +"]"
        print(str)

    def printTable(self):
        print("-----------------------")
        self.printOponentCloseField()
        self.printOponentOpenField()
        self.dump.show()
        self.printYourOpenField()
        self.printYoutCloseField()

        print("-----------------------")

    def printOponentHand(self):
        str=""
        hand = self.player2.getHand()
        for i in range(hand.fieldLen()):
            str+="[*]"
        print(str)


    def printOponentCloseField(self):
        str=""
        closeField=self.player2.getCloseField()
        for i in range(closeField.fieldLen()):
            str+="[*]"
        print(str)

    def printOponentOpenField(self):
        str=""
        openField=self.player2.getOpenField()
        cards = openField.getCards()
        for i in range(openField.fieldLen()):
            str+="["+cards[i].getChar()+"]"
        print(str)

    def printYourOpenField(self):
        str=""
        openField=self.player1.getOpenField()
        cards = openField.getCards()
        for i in range(openField.fieldLen()):
            str+="["+cards[i].getChar()+"]"
        print(str)

    def printYoutCloseField(self):
        str=""
        closeField=self.player1.getCloseField()
        for i in range(closeField.fieldLen()):
            str+="[*]"
        print(str)

    def endGame(self):
        print("fin del juego")


    def play(self,jugada):
        jugadas = jugada.split("-")
        if len(jugadas)>1:
            self.player1.playFromHand(int(jugadas[0]),int(jugadas[1]))
        else:
            self.player1.playFromHand(int(jugada))


    def start(self):
        print("repartiendo cartas")
        self.repartirCartas()

        self.printGame()
        jugada = input("tu jugada: ")
        while(self.keepPlaying):
            clearscreen()
            self.play(jugada)
            self.printGame()
            jugada=input("tu jugada: ")
            if jugada=="exit":
                self.keepPlaying=False


        self.endGame()


def clearscreen(numlines=100):
  """Clear the console.
numlines is an optional argument used only as a fall-back.
"""
# Thanks to Steven D'Aprano, http://www.velocityreviews.com/forums

  if os.name == "posix":
    # Unix/Linux/MacOS/BSD/etc
    os.system('clear')
  elif os.name in ("nt", "dos", "ce"):
    # DOS/Windows
    os.system('CLS')
  else:
    # Fallback for other operating systems.
    print('\n' * numlines)

player2=player(hand([]),openField([]),closeField([]))
deck=deck([card('2',2,2),card('2',2,2),card('2',2,2),card('2',2,2),card('3',3,3),card('3',3,3),card('7',7,7),card('7',7,7),card('7',7,7),card('7',7,7),card('10',10,10),card('10',10,10),card('10',10,10),card('10',10,10),card('11',11,11),card('11',11,11),card('11',11,11),card('11',11,11),card('13',13,13),card('13',13,13),card('13',13,13),card('13',13,13),card('14',14,14),card('14',14,14)])
gameIA=gameIA(player2,deck,4,4,dumpster())
gameIA.start()



