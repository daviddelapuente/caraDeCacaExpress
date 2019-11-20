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
            if jugada1>=self.fieldLen() or jugada2>=self.fieldLen() or jugada1>jugada2:
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