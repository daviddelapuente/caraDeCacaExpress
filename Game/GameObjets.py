import random

class dumpster:
    def __init__(self):
        self.dump=[]

    def addToDump(self,newCards):
        self.dump += newCards

    def burn(self):
        self.dump=[]

    def dumpLen(self):
        return len(self.dump)

    def getDump(self):
        cards=[]
        for i in range(len(self.cards)):
            cards.append(self.cards[i])
        return cards

    def cardsToTupple(self, objet):
        cardsTupple = []
        for i in range(len(objet)):
            cardsTupple.append(objet[i].getTupple())
        return cardsTupple

    def draw(self):
        aux=self.dump
        self.dump=[]
        return aux

    def show(self):
        if self.dumpLen()==0:
            print("[ ]")
        elif self.dumpLen()<=4:
            print(self.showFirsts())
        else:
            print("[ ] "+self.showFirsts())

    def showFirsts(self):
        str=""

        for i in range(min(4,self.dumpLen())):
            str+="["+ self.dump[(self.dumpLen()-1-i)].getChar() +"] "
        return str

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
    def getTupple(self):
        return [self.char,self.value,self.virtual_value]



class deck:
    def __init__(self,cards):
        self.cards=cards

    def lenDeck(self):
        return len(self.cards)

    def shuffleDeck(self):
        random.shuffle(self.cards)

    def drawX(self,x):
        drawSet=[]
        for i in range(x):
            drawSet.append(self.cards.pop(len(self.cards)-1))
        return drawSet

    def getCards(self):
        cards=[]
        for i in range(len(self.cards)):
            cards.append(self.cards[i].getTupple())
        return cards

    def cardsToTupple(self,objet):
        cardsTupple=[]
        for i in range(len(objet)):
            cardsTupple.append(objet[i].getTupple())
        return cardsTupple


class hand:
    def __init__(self,cards):
        self.cards=cards

    def handLen(self):
        return len(self.cards)

    def sortHand(self):
        auxHand=[]

        while (len(self.cards)>0):
            maxI=0
            for i in range(self.handLen()):
                if self.cards[i].getValue()>=self.cards[maxI].getValue():
                    maxI=i

            auxHand.append(self.cards.pop(maxI))
        self.cards=auxHand

    def getCards(self):
        cards=[]
        for i in range(len(self.cards)):
            cards.append(self.cards[i])
        return cards

    def shuffleHand(self):
        random.shuffle(self.cards)

    def addCards(self,newCards):
        self.cards+=newCards
        self.sortHand()

    def playCards(self,x,y=-1):
        cardsPlayed=[]
        if y==-1:
            cardsPlayed.append(self.cards.pop(x))
            return cardsPlayed
        else:
            for i in range(y-x+1):
                cardsPlayed.append(self.cards.pop(x))
            return cardsPlayed

    def cardsToTupple(self,objet):
        cardsTupple=[]
        for i in range(len(objet)):
            cardsTupple.append(objet[i].getTupple())
        return cardsTupple


class openField:
    def __init__(self,cards):
        self.cards=cards



    def fieldLen(self):
        return len(self.cards)

    def sortOpenField(self):
        auxHand=[]

        while (len(self.cards)>0):
            maxI=0
            for i in range(self.fieldLen()):
                if self.cards[i].getValue()>=self.cards[maxI].getValue():
                    maxI=i

            auxHand.append(self.cards.pop(maxI))
        self.cards=auxHand

    def getCards(self):
        cards=[]
        for i in range(len(self.cards)):
            cards.append(self.cards[i])
        return cards

    def shuffleOpenField(self):
        random.shuffle(self.cards)

    def addCards(self,newCards):
        self.cards+=newCards
        self.sortOpenField()

    def playCards(self,x,y=-1):
        cardsPlayed=[]
        if y==-1:
            cardsPlayed.append(self.cards.pop(x))
            return cardsPlayed
        else:
            for i in range(y-x+1):
                cardsPlayed.append(self.cards.pop(x))
            return cardsPlayed

    def cardsToTupple(self,objet):
        cardsTupple=[]
        for i in range(len(objet)):
            cardsTupple.append(objet[i].getTupple())
        return cardsTupple


class  closeField:
    def __init__(self, cards):
        self.cards = cards

    def fieldLen(self):
        return len(self.cards)

    def sortCloseField(self):
        auxHand = []

        while (len(self.cards) > 0):
            maxI = 0
            for i in range(self.fieldLen()):
                if self.cards[i].getValue() >= self.cards[maxI].getValue():
                    maxI = i

            auxHand.append(self.cards.pop(maxI))
        self.cards = auxHand

    def getCards(self):
        cards = []
        for i in range(len(self.cards)):
            cards.append(self.cards[i])
        return cards

    def shuffleOpenField(self):
        random.shuffle(self.cards)

    def addCards(self, newCards):
        self.cards += newCards
        self.sortCloseField()

    def playCards(self, x):
        cardsPlayed = []

        cardsPlayed.append(self.cards.pop(x))
        return cardsPlayed

    def cardsToTupple(self, objet):
        cardsTupple = []
        for i in range(len(objet)):
            cardsTupple.append(objet[i].getTupple())
        return cardsTupple


class player:
    def __init__(self,hand,openField,closeField):
        self.hand=hand
        self.openField=openField
        self.closeField=closeField

    def playFromHand(self,x,y=-1):
        return self.hand.playCards(x,y)

    def playFromOpenField(self,x,y=-1):
        return self.openField.playCards(x,y)

    def playFromCloseField(self,x):
        return self.closeField.playCards(x)


    def addTohand(self,newCards):
        self.hand.addCards(newCards)

    def addToOpenField(self,newCards):
        self.openField.addCards(newCards)

    def addToCloseField(self,newCards):
        self.closeField.addCards(newCards)

    def getHand(self):
        return self.hand
    def getOpenField(self):
        return self.openField
    def getCloseField(self):
        return self.closeField