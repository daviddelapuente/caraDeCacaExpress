from Game.players import *
class card:
    def __init__(self,char,value,virtual_value):
        self.char=char
        self.value=value
        self.virtual_value=virtual_value

    def getChar(self):
        return self.char
    def getValue(self):
        return self.value
    def getVirtualValue(self):
        return self.virtual_value

class deck:
    def __init__(self,cards):
        self.cards=cards

    def lenDeck(self):
        return len(self.cards)

    def shuffleDeck(self):
        random.shuffle(self.cards)

    def drawX(self,x):
        drawSet=[]
        for i in range(min(x,len(self.cards))):
            drawSet.append(self.cards.pop(len(self.cards)-1))
        return drawSet

class table:
    def __init__(self,deck,handLen,fieldsLen,players):
        self.deck=deck
        self.handLen=handLen
        self.fieldsLen=fieldsLen
        self.dump=dumpster([])
        self.players=players

    def repartirCartas(self):
        self.deck.shuffleDeck()
        for player in self.players:
            player.addTohand(self.deck.drawX(self.handLen))
            player.addToOpenField(self.deck.drawX(self.fieldsLen))
            player.addToCloseField(self.deck.drawX(self.fieldsLen))

    def show(self):
        self.players[1].printHand()
        self.printTable()
        self.players[0].printHand()

    def printTable(self):
        print("-----------------------")
        self.printPlayerCloseField(self.players[1])
        self.printPlayerOpenField(self.players[1])
        self.dump.show()
        self.printPlayerOpenField(self.players[0])
        self.printPlayerCloseField(self.players[0])
        print("-----------------------")

    def printPlayerCloseField(self,player):
        str = ""
        closeField = player.getCloseField()
        for i in range(closeField.fieldLen()):
            str += "[*]"
        print(str)

    def printPlayerOpenField(self,player):
        str = ""
        openField = player.getOpenField()
        cards = openField.getCards()
        for i in range(openField.fieldLen()):
            str += "[" + cards[i].getChar() + "]"
        print(str)