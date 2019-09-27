from Game.GameObjets import *
import os
class gameIA:
    def __init__(self,IA,deck,handLen,fieldsLen,dump):


        self.player1=player(hand([]),openField([]),closeField([]))
        self.player2=IA
        self.table = table(deck, handLen, fieldsLen,self.player1,self.player2)
        self.keepPlaying=True



    def printGame(self):
        self.table.printOponentHand()
        self.table.printTable()
        self.table.printPlayerHand()


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
        self.table.repartirCartas()

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



