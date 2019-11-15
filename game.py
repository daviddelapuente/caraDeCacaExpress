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
        if jugada=="draw":
            print("player 1 draw the dumpster")
            self.player1.hand.addCards(self.table.dump.draw())
            self.gameState.refreshDumpster(self.table.dump)
        elif len(self.player1.hand.cards)>0:
            jugadas = jugada.split("-")
            if len(jugadas)>1:
                cardsPlayed=self.player1.playFromHand(int(jugadas[0]),int(jugadas[1]))
            else:
                cardsPlayed=self.player1.playFromHand(int(jugada))
            
            newDump=self.table.dump.pushCards(cardsPlayed)
            self.gameState.refreshDumpster(newDump)
        elif len(self.player1.openField.cards)>0:
            jugadas = jugada.split("-")
            if len(jugadas)>1:
                cardsPlayed=self.player1.playFromOpenField(int(jugadas[0]),int(jugadas[1]))
            else:
                cardsPlayed=self.player1.playFromOpenField(int(jugada))
            
            newDump=self.table.dump.pushCards(cardsPlayed)
            self.gameState.refreshDumpster(newDump)
        else:
            cardsPlayed=self.player1.playFromCloseField(int(jugada))
            self.player1.hand.addCards(cardsPlayed)
            self.askPlayer1ToPlay()
            
    
    #aqui es donde juega el player2
    def player2Play(self):
        if len(player2.hand.cards)>0:
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
        elif len(player2.openField.cards)>0:
            #jugar con openField
            jugada=self.player2.thinkOpenField(self.gameState)
            if jugada=="out":
                print("player 2 draw the dumpster")
                self.player2.hand.addCards(self.table.dump.draw())
                self.gameState.refreshDumpster(self.table.dump)
            else:
                jugadas = jugada.split("-")
                if len(jugadas)>1:
                    cardsPlayed=self.player2.playFromOpenField(int(jugadas[0]),int(jugadas[1]))
                else:
                    cardsPlayed=self.player2.playFromOpenField(int(jugada))
                
                newDump=self.table.dump.pushCards(cardsPlayed)
                self.gameState.refreshDumpster(newDump)
        else:
            #jugar con closeField
            jugada=self.player2.thinkCloseField(self.gameState)
            if jugada=="out":
                print("player 2 draw the dumpster")
                self.player2.hand.addCards(self.table.dump.draw())
                self.gameState.refreshDumpster(self.table.dump)
            else:
                cardsPlayed=self.player2.playFromCloseField(int(jugada))
                if self.table.dump.isEmpty():
                    newDump=self.table.dump.pushCards(cardsPlayed)
                    self.gameState.refreshDumpster(newDump)
                elif cardsPlayed[0].getValue()<self.table.dump.getTop().getValue():
                    self.player2.hand.addCards(cardsPlayed)
                    self.player2.hand.addCards(self.table.dump.draw())
                    self.gameState.refreshDumpster(self.table.dump)
                else:
                    newDump=self.table.dump.pushCards(cardsPlayed)
                    self.gameState.refreshDumpster(newDump)
                    
    def askPlayer1ToPlay(self):
        clearscreen()
        self.printGame()
        jugada = input("tu jugada: ")
        self.player1Play(jugada)
        

    def start(self):
        clearscreen()
        print("repartiendo cartas")
        self.table.repartirCartas()    
        while(self.keepPlaying):
            self.askPlayer1ToPlay()
            self.player2Play()
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



