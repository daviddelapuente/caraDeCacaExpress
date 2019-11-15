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
        #tal vez puede ser solo return self.cards
        cards=[]
        for i in range(len(self.cards)):
            cards.append(self.cards[i])
        return cards

    def shuffleField(self):
        random.shuffle(self.cards)

    def addCards(self,newCards):
        self.cards+=newCards
        self.sortField()

    def cardsToTupple(self,objet):
        cardsTupple=[]
        for i in range(len(objet)):
            cardsTupple.append(objet[i].getTupple())
        return cardsTupple

    def show(self):
        pass

class openField(field):
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


class  closeField(field):
    def __init__(self, cards):
        field.__init__(self,cards)

    def playCards(self, x):
        cardsPlayed = []

        cardsPlayed.append(self.cards.pop(x))
        return cardsPlayed


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

class dumpster(field):
    def __init__(self):
        field.__init__(self,[])

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
        else:
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




class table:
    def __init__(self,deck,handLen,fieldsLen,player1,player2):
        self.deck=deck
        self.handLen=handLen
        self.fieldsLen=fieldsLen
        self.dump=dumpster()
        self.player1=player1
        self.player2=player2


    def repartirCartas(self):

        self.deck.shuffleDeck()
        self.player1.addTohand(self.deck.drawX(self.handLen))
        self.player1.addToOpenField(self.deck.drawX(self.fieldsLen))
        self.player1.addToCloseField(self.deck.drawX(self.fieldsLen))

        self.player2.addTohand(self.deck.drawX(self.handLen))
        self.player2.addToOpenField(self.deck.drawX(self.fieldsLen))
        self.player2.addToCloseField(self.deck.drawX(self.fieldsLen))



    def show(self):
        self.player2.printHand()
        self.printTable()
        self.player1.printHand()




    def printTable(self):
        print("-----------------------")
        self.printOponentCloseField()
        self.printOponentOpenField()
        self.dump.show()
        self.printPlayerOpenField()
        self.printPlayerCloseField()

        print("-----------------------")





    def printOponentCloseField(self):
        str = ""
        closeField = self.player2.getCloseField()
        for i in range(closeField.fieldLen()):
            str += "[*]"
        print(str)

    def printOponentOpenField(self):
        str = ""
        openField = self.player2.getOpenField()
        cards = openField.getCards()
        for i in range(openField.fieldLen()):
            str += "[" + cards[i].getChar() + "]"
        print(str)

    def printPlayerOpenField(self):
        str = ""
        openField = self.player1.getOpenField()
        cards = openField.getCards()
        for i in range(openField.fieldLen()):
            str += "[" + cards[i].getChar() + "]"
        print(str)

    def printPlayerCloseField(self):
        str = ""
        closeField = self.player1.getCloseField()
        for i in range(closeField.fieldLen()):
            str += "[*]"
        print(str)





class player:
    def __init__(self,hand,openField,closeField):
        self.hand=hand
        self.openField=openField
        self.closeField=closeField

    def getValidCards(self,cards,dumpster):
        
        if dumpster.isEmpty():
            validCardsI=[]
            for i in range(len(cards)):
                validCardsI.append(i)
            return validCardsI
        else:
            top=dumpster.getTop().getValue()
            #this are the indexes
            validCardsI=[]

            for i in range(len(cards)):
                if cards[i].getValue()>=top:
                    validCardsI.append(i)
            return validCardsI

        
    def addTohand(self,newCards):
        self.hand.addCards(newCards)

    def addToOpenField(self,newCards):
        self.openField.addCards(newCards)

    def addToCloseField(self,newCards):
        self.closeField.addCards(newCards)


    def playFromHand(self,x,y=-1):
        return self.hand.playCards(x,y)

    def playFromOpenField(self,x,y=-1):
        return self.openField.playCards(x,y)

    def playFromCloseField(self,x):
        return self.closeField.playCards(x)

    def getHand(self):
        return self.hand
    def getOpenField(self):
        return self.openField
    def getCloseField(self):
        return self.closeField




class IAPlayer(player):
    def __init__(self,hand,openField,closeField):
        player.__init__(self,hand,openField,closeField)

    def printHandReverse(self):
        str=""
        hand = self.getHand()
        for i in range(hand.fieldLen()):
            str+="[*]"
        print(str)

    
    def printHand(self):
        str=""
        hand=self.getHand()
        cards=hand.getCards()
        for i in range(hand.fieldLen()):
            str+="["+ cards[i].getChar() +"]"
        print(str)

#this player will play a random cards from de subset of playable cards in the hand

class gameState():
    def __init__(self,dump):
        self.dump=dump
    def getDumpster(self):
        return self.dump
    def refreshDumpster(self,newDump):
        self.dump=newDump

#this is the simplest randomPlayer, it only can play 1 card at time
#(im planing to create another randomPlayer that can play 1 or more cards of the same type)
class randomPlayer(IAPlayer):
    def __init__(self,hand,openField,closeField):
        player.__init__(self,hand,openField,closeField)

    def think(self,gs):
        validCards=self.getValidCards(self.hand.getCards(),gs.getDumpster())
        if len(validCards)==0:
            return "out"
        else:
            p=random.random()
            if p<0.05:
                #decide que se las quiere llevar
                return "out"
            else:
                p2=random.randint(0,len(validCards)-1)
                return str(validCards[p2])
    
    def thinkOpenField(self,gs):
        validCards=self.getValidCards(self.openField.getCards(),gs.getDumpster())
        if len(validCards)==0:
            return "out"
        else:
            p=random.random()
            if p<0.05:
                #decide que se las quiere llevar
                return "out"
            else:
                p2=random.randint(0,len(validCards)-1)
                return str(validCards[p2])

    def thinkCloseField(self,gs):
        p=random.random()
        if p<0.05:
            #decide que se las quiere llevar
            return "out"
        else:
            #esto podria ser mas inteligente y elegir uno al azar, aunque azar sobre azar es azar no lo se
            p2=random.randint(0,len(self.closeField.getCards())-1)
            return str(p2)





class realPlayer(player):
    def __init__(self,hand,openField,closeField):
        player.__init__(self,hand,openField,closeField)

    def printHand(self):
        str=""
        hand=self.getHand()
        cards=hand.getCards()
        for i in range(hand.fieldLen()):
            str+="["+ cards[i].getChar() +"]"
        print(str)

    def playFromHand(self,x,y=-1):
        return self.hand.playCards(x,y)

    def playFromOpenField(self,x,y=-1):
        return self.openField.playCards(x,y)

    def playFromCloseField(self,x):
        return self.closeField.playCards(x)