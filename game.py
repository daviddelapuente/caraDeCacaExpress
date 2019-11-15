from Game.GameObjets import *
import os
class gameIA:
    def __init__(self,IA,deck,handLen,fieldsLen,dump):


        self.player1=realPlayer(hand([]),openField([]),closeField([]))
        self.player2=IA
        self.table = table(deck, handLen, fieldsLen,self.player1,self.player2)
        self.keepPlaying=True
        self.gameState=gameState(dump)



    def printGame(self):
        self.table.show()


    def endGame(self):
        print("fin del juego")


    def player1Play(self,jugada):
        jugadas = jugada.split("-")
        if len(jugadas)>1:
            cardsPlayed=self.player1.playFromHand(int(jugadas[0]),int(jugadas[1]))
        else:
            cardsPlayed=self.player1.playFromHand(int(jugada))
        
        newDump=self.table.dump.pushCards(cardsPlayed)
        self.gameState.refreshDumpster(newDump)
            
    
    #aqui es donde juega el player2
    def player2Play(self):
        #self.player2.playFromHand(self.gameState)
        
        #jugada es un string
        jugada=self.player2.think(self.gameState)
        if jugada=="out":
            print("player 2 draw the dumpster")
            self.player2.hand.addCards(self.table.dump.draw())
            self.gameState.refreshDumpster(self.table.dump)
        else:
            jugadas = jugada.split("-")
            if len(jugadas)>1:
                cardsPlayed=self.player2.playFromHand(int(jugadas[0]),int(jugadas[1]))
            else:
                cardsPlayed=self.player2.playFromHand(int(jugada))
            newDump=self.table.dump.pushCards(cardsPlayed)
            self.gameState.refreshDumpster(newDump)


    def start(self):
        print("repartiendo cartas")
        self.table.repartirCartas()

        self.printGame()
        jugada = input("tu jugada: ")
        while(self.keepPlaying):
            clearscreen()
            self.player1Play(jugada)
            self.player2Play()
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

player2=randomPlayer(hand([]),openField([]),closeField([]))
deck=deck([card('2',2,2),card('2',2,2),card('2',2,2),card('2',2,2),card('3',3,3),card('3',3,3),card('7',7,7),card('7',7,7),card('7',7,7),card('7',7,7),card('10',10,10),card('10',10,10),card('10',10,10),card('10',10,10),card('11',11,11),card('11',11,11),card('11',11,11),card('11',11,11),card('13',13,13),card('13',13,13),card('13',13,13),card('13',13,13),card('14',14,14),card('14',14,14)])
gameIA=gameIA(player2,deck,4,4,dumpster())
gameIA.start()



