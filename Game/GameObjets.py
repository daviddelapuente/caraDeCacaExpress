import random

class field:
    def __init__(self,cards):
        self.cards=cards

    def fieldLen(self):
        return len(self.cards)

    def sortField(self):
        auxField = []
        while (len(self.cards) > 0):
            maxI = 0
            for i in range(self.fieldLen()):
                if self.cards[i].getValue() >= self.cards[maxI].getValue():
                    maxI = i
            auxField.append(self.cards.pop(maxI))
        self.cards = auxField

    def getCards(self):
        return self.cards

    def shuffleField(self):
        random.shuffle(self.cards)

    def addCards(self,newCards):
        self.cards+=newCards
        self.sortField()

    def filterSemantic(self,jugadas,dump):
        if jugadas[0]=="draw":
            if dump.isEmpty():
                return False
        elif len(jugadas)==1:
            jugada=int(jugadas[0])
            if jugada>=self.fieldLen():
                return False
            cards=self.getCards()
            cardValue=cards[jugada].getValue()
            if not dump.isEmpty() and dump.getTop().getValue()>cardValue:
                return False
        else:
            jugada1=int(jugadas[0])
            jugada2=int(jugadas[1])
            if jugada1>=self.fieldLen() or jugada2>=self.fieldLen():
                return False
            cards=self.getCards()
            cardValue=cards[jugada1].getValue()
            for i in range(jugada1,jugada2+1):
                if cards[i].getValue()!=cardValue:
                    return False
            if not dump.isEmpty() and dump.getTop().getValue()>cardValue:
                return False
        return True

class hand(field):
    def __init__(self,cards):
        field.__init__(self,cards)

    def playCards(self,x,y=-1):
        cardsPlayed=[]
        if y==-1:
            cardsPlayed.append(self.cards.pop(x))
            return cardsPlayed
        else:
            for i in range(y-x+1):
                cardsPlayed.append(self.cards.pop(x))
            return cardsPlayed

class openField(field):
    def playCards(self,x,y=-1):
        cardsPlayed=[]
        if y==-1:
            cardsPlayed.append(self.cards.pop(x))
        else:
            for i in range(y-x+1):
                cardsPlayed.append(self.cards.pop(x))
        return cardsPlayed

class  closeField(field):
    def playCards(self, x):
        cardsPlayed = []
        cardsPlayed.append(self.cards.pop(x))
        return cardsPlayed

    def filterSemantic(self,jugadas,dump):
        if jugadas[0]=="draw":
            return True
        elif len(jugadas)>1 or int(jugadas[0])>=self.fieldLen():
            return False
        return True

class dumpster(field):
    def burn(self):
        self.dump=[]

    def draw(self):
        aux=self.cards
        self.cards=[]
        return aux

    def show(self):
        if self.fieldLen()==0:
            print("[ ]")
        elif self.fieldLen()<=4:
            print(self.showFirsts())
        else:
            print("[ ] "+self.showFirsts())

    def showFirsts(self):
        str=""
        for i in range(min(4,self.fieldLen())):
            str="["+ self.cards[(self.fieldLen()-1-i)].getChar() +"] "+str
        return str

    #push a group of cards in the top of the dumpster
    def pushCards(self,newCards):
        self.cards+=newCards
        return self

    def isEmpty(self):
        if len(self.cards)==0:
            return True
        return False
    
    def getTop(self):
        return self.cards[len(self.cards)-1]

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

class player:
    def __init__(self,hand,openField,closeField):
        self.hand=hand
        self.openField=openField
        self.closeField=closeField
        self.actualField=self.hand

    #getters
    def getHand(self):
        return self.hand
    def getOpenField(self):
        return self.openField
    def getCloseField(self):
        return self.closeField
    
    #adders(this add cards to a field and change the actualField)
    def addTohand(self,newCards):
        self.hand.addCards(newCards)
        self.actualField=self.hand
    def addToOpenField(self,newCards):
        self.openField.addCards(newCards)
    def addToCloseField(self,newCards):
        self.closeField.addCards(newCards)

    def getValidCards(self,cards,dumpster):
        if dumpster.isEmpty():
            return range(len(cards))
        else:
            #the idea is to returns the indexes of the valid cards
            top=dumpster.getTop().getValue()    
            validCardsI=[]
            for i in range(len(cards)):
                if cards[i].getValue()>=top:
                    validCardsI.append(i)
            return validCardsI

    def playFromHand(self,jugadas):
        if len(jugadas)==1:
            cards=self.hand.playCards(int(jugadas[0]),-1)
        else:
            cards=self.hand.playCards(int(jugadas[0]),int(jugadas[1]))
        #change actualField
        if self.hand.fieldLen()==0:
            if self.openField.fieldLen()>0:
                self.actualField=self.openField
            else:
                self.actualField=self.closeField
        return cards

    def playFromOpenField(self,jugadas):
        if len(jugadas)==1:
            x=int(jugadas[0])
            y=-1
            cards=self.openField.playCards(int(jugadas[0]),-1)
        else:
            cards=self.openField.playCards(int(jugadas[0]),int(jugadas[1]))
        if self.openField.fieldLen()==0:
            self.actualField=self.closeField
        return cards

    def playFromCloseField(self,jugadas):
        return self.closeField.playCards(int(jugadas[0]))
    
    def printHand(self):
        str=""
        hand=self.getHand()
        cards=hand.getCards()
        for i in range(hand.fieldLen()):
            str+="["+ cards[i].getChar() +"]"
        print(str)

class IAPlayer(player):
    def printHandReverse(self):
        str=""
        hand = self.getHand()
        for i in range(hand.fieldLen()):
            str+="[*]"
        print(str)

#now this isnt a big class, but in the future I plan to make this bigger so ia can have more context to take desicions
class gameState():
    def __init__(self,dump):
        self.dump=dump
    def getDumpster(self):
        return self.dump
    def setDumpster(self,newDump):
        self.dump=newDump

#this player will play a random cards from de subset of playable cards in the hand
#this is the simplest randomPlayer, it only can play 1 card at time
class randomPlayer(IAPlayer):
    def think(self,gs):
        p=random.random()
        if p<0.05 and not gs.dump.isEmpty():
            #decide que se las quiere llevar
            return "out"
        if isinstance(self.actualField,closeField):
            return str(random.randint(0,len(self.closeField.getCards())-1))
        else:
            validCards=self.getValidCards(self.actualField.getCards(),gs.getDumpster())
            if len(validCards)==0:
                return "out"
            else:
                return str(validCards[random.randint(0,len(validCards)-1)])