from Game.GameObjets import *
from displayThings.consoleDisplay import *

class gameIA:
    def __init__(self,IA,deck,handLen,fieldsLen):
        self.boardMessage=""
        self.player1=realPlayer(hand([]),openField([]),closeField([]))
        self.player2=IA
        self.table = table(deck, handLen, fieldsLen,self.player1,self.player2)
        self.keepPlaying=True
        self.gameState=gameState(self.table.dump)

    def printGame(self):
        clearscreen()
        print(self.boardMessage)
        self.table.show()
        #is important to set the board message to "" because if not, then the massege will be printed on every turn.
        self.boardMessage=""

    def endGame(self,winnerMessage):
        print("end of the game")
        print(winnerMessage)

    def player1Play(self,jugada):
        if jugada=="draw":
            self.boardMessage="jugador 1 roba el pozo"
            self.player1.addTohand(self.table.dump.draw())
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
            self.player1.addTohand(cardsPlayed)
            self.askPlayer1ToPlay()
            
    
    #aqui es donde juega el player2
    def player2Play(self):
        if len(player2.hand.cards)>0:
            #player2 plays from the hand
            jugada=self.player2.think(self.gameState)
            if jugada=="out":
                self.boardMessage="jugador 2 roba el pozo"
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
                self.boardMessage="jugador 2 roba el pozo"
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
                self.boardMessage="jugador 2 roba el pozo"
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
        self.printGame()
        jugada = input("tu jugada: ")
        jugadas=jugada.split("-")
        if filterJugadaSintaxis(jugadas) and self.player1.actualField.filterSemantic(jugadas,self.table.dump):
            self.player1Play(jugada)
        else:
            self.boardMessage="ingresa una jugada valida"
            self.askPlayer1ToPlay()
        
    def playerWin(self,player):
        if player.hand.fieldLen()==0 and player.closeField.fieldLen()==0:
            return True
        return False

    def start(self):
        clearscreen()
        self.table.repartirCartas()
        #here is a while true that keep the game alive but it will eventualy end when someone wins
        while(True):
            self.askPlayer1ToPlay()
            if self.playerWin(self.player1):
                self.printGame()
                winnerMessage="gana jugador " + "1"
                break
            self.player2Play()
            if self.playerWin(self.player2):
                self.printGame()
                winnerMessage="gana jugador " + "2"
                break
        self.endGame(winnerMessage)

player2=randomPlayer(hand([]),openField([]),closeField([]))
deck=deck([card('2',2,2),card('2',2,2),card('2',2,2),card('2',2,2),card('3',3,3),card('3',3,3),card('7',7,7),card('7',7,7),card('7',7,7),card('7',7,7),card('10',10,10),card('10',10,10),card('10',10,10),card('10',10,10),card('11',11,11),card('11',11,11),card('11',11,11),card('11',11,11),card('13',13,13),card('13',13,13),card('13',13,13),card('13',13,13),card('14',14,14),card('14',14,14)])
gameIA=gameIA(player2,deck,4,4)
gameIA.start()



