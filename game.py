from Game.GameObjets import *
from displayThings.consoleDisplay import *

class game:
    def __init__(self,players,deck,handLen,fieldsLen):
        self.players=players
        self.table = table(deck, handLen, fieldsLen,self.players)
        self.gameState=gameState(self.table.dump)

    def endGame(self,winnerMessage):
        print("end of the game")
        print(winnerMessage)
      
    #aqui es donde juega el player2
    def IAPlayerPlay(self,i):
        jugada=self.players[i].think(self.gameState)
        jugadas = jugada.split("-")
        if jugadas[0]=="out":
                self.boardMessage="jugador 2 roba el pozo"
                self.players[i].addTohand(self.table.dump.draw())
                self.gameState.setDumpster(self.table.dump)
        elif len(self.players[i].hand.cards)>0:
                #players[i] plays from the hand
                cardsPlayed=self.players[i].playFromHand(jugadas)
                newDump=self.table.dump.pushCards(cardsPlayed)
                self.gameState.setDumpster(newDump)
        elif len(self.players[i].openField.cards)>0:
            #jugar con openField
                cardsPlayed=self.players[i].playFromOpenField(jugadas)
                newDump=self.table.dump.pushCards(cardsPlayed)
                self.gameState.setDumpster(newDump)
        else:
            #jugar con closeField            
            cardsPlayed=self.players[i].playFromCloseField(jugadas)
            if self.table.dump.isEmpty() or cardsPlayed[0].getValue()>=self.table.dump.getTop().getValue():
                newDump=self.table.dump.pushCards(cardsPlayed)
                self.gameState.setDumpster(newDump)
            else:
                self.players[i].addTohand(cardsPlayed)
                self.players[i].addTohand(self.table.dump.draw())
                self.gameState.setDumpster(self.table.dump)
        
    def playerWin(self,player):
        if player.hand.fieldLen()==0 and player.closeField.fieldLen()==0:
            return True
        return False

#real player VS IA
class gamePvIA(game):
    def __init__(self,players,deck,handLen,fieldsLen):
        self.boardMessage=""
        game.__init__(self,players,deck,handLen,fieldsLen)

    def printGame(self):
        clearscreen()
        print(self.boardMessage)
        self.table.show()
        #is important to set the board message to "" because if not, then the massege will be printed on every turn.
        self.boardMessage=""

    def RealPlayerPlay(self,jugadas,i):
        if jugadas[0]=="draw":
            self.boardMessage="jugador 1 roba el pozo"
            self.players[i].addTohand(self.table.dump.draw())
            self.gameState.setDumpster(self.table.dump)
        elif len(self.players[i].hand.cards)>0:
            cardsPlayed=self.players[i].playFromHand(jugadas)       
            newDump=self.table.dump.pushCards(cardsPlayed)
            self.gameState.setDumpster(newDump)
        elif len(self.players[i].openField.cards)>0:
            cardsPlayed=self.players[i].playFromOpenField(jugadas)
            newDump=self.table.dump.pushCards(cardsPlayed)
            self.gameState.setDumpster(newDump)
        else:
            cardsPlayed=self.players[i].playFromCloseField(jugadas)
            self.players[i].addTohand(cardsPlayed)
            self.askRealPlayerToPlay(i)

    def askRealPlayerToPlay(self,i):
        self.printGame()
        jugada = input("tu jugada: ")
        jugadas=jugada.split("-")
        if filterJugadaSintaxis(jugadas) and self.players[i].actualField.filterSemantic(jugadas,self.table.dump):
            self.RealPlayerPlay(jugadas,0)
        else:
            self.boardMessage="ingresa una jugada valida"
            self.askRealPlayerToPlay(i)
        
    def play(self):
        clearscreen()
        self.table.repartirCartas()
        #here is a while true that keep the game alive but it will eventualy end when someone wins
        while(True):
            self.askRealPlayerToPlay(0)
            if self.playerWin(self.players[0]):
                self.printGame()
                winnerMessage="gana jugador " + "1"
                break
            self.IAPlayerPlay(1)
            if self.playerWin(self.players[1]):
                self.printGame()
                winnerMessage="gana jugador " + "2"
                break
        self.endGame(winnerMessage)

#Ia vs IA
class gameIAvIA(game):
    def printGame(self):
        clearscreen2()
        self.table.show()
        #is important to set the board message to "" because if not, then the massege will be printed on every turn.

    def play(self):
        self.table.repartirCartas()
        #here is a while true that keep the game alive but it will eventualy end when someone wins
        while(True):
            self.IAPlayerPlay(0)
            if self.playerWin(self.players[0]):
                winnerMessage="gana jugador " + "1"
                winner=0
                break
            self.IAPlayerPlay(1)
            if self.playerWin(self.players[1]):
                winnerMessage="gana jugador " + "2"
                winner=1
                break
        return winner
