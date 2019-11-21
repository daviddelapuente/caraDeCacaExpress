from Game.fields import *
from Game.arboles import *
from Game.astD import *
from math import ceil
from math import exp
from math import floor
from math import cos

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

    def setFields(self,fields):
        self.hand=fields[0]
        self.openField=fields[1]
        self.closeField=fields[2]
    
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
    def printHand(self):
        str=""
        hand = self.getHand()
        for i in range(hand.fieldLen()):
            str+="[*]"
        print(str)

def crossOverPlayers(player1,player2):
    gp=gPlayer(hand([]),openField([]),closeField([]),player1.getA(),player1.getDepth())
    gp.setGenoma(player1.getGenoma(),player2.getGenoma())
    return gp

class genoma():
    def __init__(self,a,depth):
        self.a=a
        self.depth=depth
        self.arbol1=a.__call__(depth)
        self.arbol2=a.__call__(depth)
        self.arbol3=a.__call__(depth)

    def getArbol1(self):
        return self.arbol1
    def getArbol2(self):
        return self.arbol2
    def getArbol3(self):
        return self.arbol3
    
    def setArbol1(self,newArbol1):
        self.arbol1=newArbol1
    def setArbol2(self,newArbol2):
        self.arbol2=newArbol2
    def setArbol3(self,newArbol3):
        self.arbol3=newArbol3
    
    def mutate(self):
        h=self.arbol1.serialize()
        i=random.randint(0,len(h)-1)
        h[i].replace(self.a.__call__(max(1,self.depth/3)))

        h2=self.arbol2.serialize()
        i2=random.randint(0,len(h2)-1)
        h2[i2].replace(self.a.__call__(max(1,self.depth/3)))

        h3=self.arbol3.serialize()
        i3=random.randint(0,len(h3)-1)
        h3[i3].replace(self.a.__call__(max(1,self.depth/3)))
    

    def g1(self,x):
        d={"x":x}
        return self.arbol1.eval(d)
    
    def g2(self,x):
        d={"x":x}
        return self.arbol2.eval(d)

    def g3(self,x):
        d={"x":x}
        return self.arbol3.eval(d)

    
    def sig(self,x):
        return cos(x)
    
    def g(self,validCards):
        return (self.g1(validCards[0])+self.g2(validCards[floor(len(validCards)/2)])+self.g3(validCards[len(validCards)-1]))/3

    def evaluate(self,validCards):
        return self.sig(self.g(validCards))

#now this isnt a big class, but in the future I plan to make this bigger so ia can have more context to take desicions
class gameState():
    def __init__(self,dump):
        self.dump=dump
    def getDumpster(self):
        return self.dump
    def setDumpster(self,newDump):
        self.dump=newDump


class gPlayer(IAPlayer):
    def __init__(self,hand,openField,closeField,a,depth):
        self.a=a
        self.depth=depth
        self.genoma=genoma(self.a,self.depth)
        self.pForDraw=0.05
        player.__init__(self,hand,openField,closeField)

    def mutate(self):
        self.genoma.mutate()
    def getGenoma(self):
        return self.genoma
    def getA(self):
        return self.a
    def getDepth(self):
        return self.depth

    def setGenoma(self,genoma1,genoma2):
        if random.random()>=0:
            tree1Copy=genoma1.getArbol1().copy()

            h1=tree1Copy.serialize()

            h2=genoma2.getArbol1().serialize()

            i=random.randint(0,len(h1)-1)

            j=random.randint(0,len(h2)-1)

            h1[i].replace(h2[j])

            self.genoma.setArbol1(tree1Copy)

            tree2Copy=genoma1.getArbol2().copy()

            h1=tree2Copy.serialize()

            h2=genoma2.getArbol2().serialize()

            i=random.randint(0,len(h1)-1)

            j=random.randint(0,len(h2)-1)

            h1[i].replace(h2[j])

            self.genoma.setArbol2(tree2Copy)

            tree3Copy=genoma1.getArbol3().copy()

            h1=tree3Copy.serialize()

            h2=genoma2.getArbol3().serialize()

            i=random.randint(0,len(h1)-1)

            j=random.randint(0,len(h2)-1)

            h1[i].replace(h2[j])

            self.genoma.setArbol3(tree1Copy)

    def think(self,gs):
        p=random.random()
        if p<self.pForDraw and not gs.dump.isEmpty():
            return "out"
        if isinstance(self.actualField,closeField):
            return str(random.randint(0,len(self.closeField.getCards())-1))
        else:
            validCards=self.getValidCards(self.actualField.getCards(),gs.getDumpster())
            if len(validCards)==0:
                return "out"
            else:
                #here is when the genoma take place
                
                #this is a number in (0,1)
                r=self.genoma.evaluate(validCards)
                index= ceil(r*(len(validCards)-1))
                return str(validCards[index])

    def printHand(self):
        str=""
        hand = self.getHand()
        for i in range(hand.fieldLen()):
            str+="[*]"
        print(str)

#this player will play a random cards from de subset of playable cards in the hand
#this is the simplest randomPlayer, it only can play 1 card at time
class randomPlayer(IAPlayer):
    def __init__(self,hand,openField,closeField):
        IAPlayer.__init__(self,hand,openField,closeField)
        self.pForDraw=0.05

    def think(self,gs):
        p=random.random()
        if p<self.pForDraw and not gs.dump.isEmpty():
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

#this is another random player but it can play 1 or more of the same cards when it can
#this player should be more competent than the other because it has more adaptability
class randomPlayerV2(IAPlayer):
    def __init__(self,hand,openField,closeField):
        IAPlayer.__init__(self,hand,openField,closeField)
        self.pForDraw=0.05
        self.pForMoreThanOne=0.75

    def getValidSets(self,cards,dumpster):
        if dumpster.isEmpty():
            validSets=[]
            aux=[]
            auxValue=cards[0].getValue()
            for i in range(len(cards)):
                if auxValue==cards[i].getValue():
                    aux.append(i)
                else:
                    if len(aux)>0:
                        validSets.append(aux)
                    auxValue=cards[i].getValue()
                    aux=[i]
            if len(aux)>0:
                validSets.append(aux)
            return validSets
        else:
            validSets=[]
            aux=[]
            auxValue=cards[0].getValue()
            top=dumpster.getTop().getValue()
            for i in range(len(cards)):
                if top>cards[i].getValue():
                    auxValue=cards[i].getValue()
                elif auxValue==cards[i].getValue():
                    aux.append(i)
                else:
                    if len(aux)>0:
                        validSets.append(aux)
                    auxValue=cards[i].getValue()
                    aux=[]
                    aux.append(i)
            if len(aux)>0:
                validSets.append(aux)
            return validSets

    def think(self,gs):
        p=random.random()
        if p<self.pForDraw and not gs.dump.isEmpty():
            #decide que se las quiere llevar
            return "out"
        elif isinstance(self.actualField,closeField):
            return str(random.randint(0,len(self.closeField.getCards())-1))
        else:
            #this return an array of arrays of indexes
            validSets=self.getValidSets(self.actualField.getCards(),gs.getDumpster())
            if len(validSets)==0:
                return "out"
            else:
                #first select some set
                firstIndex=random.randint(0,len(validSets)-1)
                if len(validSets[firstIndex])==1:
                    #if the set only has one index, then return that
                    return str(validSets[firstIndex][0])
                else:
                    #if the set has more than one posible index
                    r1=0
                    r2=0
                    while(r2<(len(validSets[firstIndex])-1)):
                        if random.random()>self.pForMoreThanOne:
                            break
                        else:
                            r2+=1
                    return str(validSets[firstIndex][r1])+"-"+str(validSets[firstIndex][r2])

#this is a bad deterministic player that always plays one card
class badDeterministicPlayer(IAPlayer):
    def think(self,gs):
        if isinstance(self.actualField,closeField):
            return str(random.randint(0,len(self.closeField.getCards())-1))
        else:
            validCards=self.getValidCards(self.actualField.getCards(),gs.getDumpster())
            if len(validCards)==0:
                return "out"
            else:
                return str(validCards[0])

#this is a bad deterministic player that can play more than one card
class badDeterministicPlayerV2(IAPlayer):
    def __init__(self,hand,openField,closeField):
        IAPlayer.__init__(self,hand,openField,closeField)
        self.pForDraw=0.05
        self.pForMoreThanOne=1

    def getValidSets(self,cards,dumpster):
        if dumpster.isEmpty():
            validSets=[]
            aux=[]
            auxValue=cards[0].getValue()
            for i in range(len(cards)):
                if auxValue==cards[i].getValue():
                    aux.append(i)
                else:
                    if len(aux)>0:
                        validSets.append(aux)
                    auxValue=cards[i].getValue()
                    aux=[i]
            if len(aux)>0:
                validSets.append(aux)
            return validSets
        else:
            validSets=[]
            aux=[]
            auxValue=cards[0].getValue()
            top=dumpster.getTop().getValue()
            for i in range(len(cards)):
                if top>cards[i].getValue():
                    auxValue=cards[i].getValue()
                elif auxValue==cards[i].getValue():
                    aux.append(i)
                else:
                    if len(aux)>0:
                        validSets.append(aux)
                    auxValue=cards[i].getValue()
                    aux=[]
                    aux.append(i)
            if len(aux)>0:
                validSets.append(aux)
            return validSets

    def think(self,gs):
        p=random.random()
        if p<self.pForDraw and not gs.dump.isEmpty():
            #decide que se las quiere llevar
            return "out"
        elif isinstance(self.actualField,closeField):
            return str(random.randint(0,len(self.closeField.getCards())-1))
        else:
            #this return an array of arrays of indexes
            validSets=self.getValidSets(self.actualField.getCards(),gs.getDumpster())
            if len(validSets)==0:
                return "out"
            else:
                #first select some set
                firstIndex=0
                if len(validSets[firstIndex])==1:
                    #if the set only has one index, then return that
                    return str(validSets[firstIndex][0])
                else:
                    #if the set has more than one posible index
                    r1=0
                    r2=0
                    while(r2<(len(validSets[firstIndex])-1)):
                        if random.random()>self.pForMoreThanOne:
                            break
                        else:
                            r2+=1
                    return str(validSets[firstIndex][r1])+"-"+str(validSets[firstIndex][r2])


#this is a good deterministic player that always plays one card
class goodDeterministicPlayer(IAPlayer):
    def think(self,gs):
        if isinstance(self.actualField,closeField):
            return str(random.randint(0,len(self.closeField.getCards())-1))
        else:
            validCards=self.getValidCards(self.actualField.getCards(),gs.getDumpster())
            if len(validCards)==0:
                return "out"
            else:
                return str(validCards[len(validCards)-1])

#this is a good deterministic player that can play more than one card
class goodDeterministicPlayerV2(IAPlayer):
    def __init__(self,hand,openField,closeField):
        IAPlayer.__init__(self,hand,openField,closeField)
        self.pForDraw=0.05

    def getValidSets(self,cards,dumpster):
        if dumpster.isEmpty():
            validSets=[]
            aux=[]
            auxValue=cards[0].getValue()
            for i in range(len(cards)):
                if auxValue==cards[i].getValue():
                    aux.append(i)
                else:
                    if len(aux)>0:
                        validSets.append(aux)
                    auxValue=cards[i].getValue()
                    aux=[i]
            if len(aux)>0:
                validSets.append(aux)
            return validSets
        else:
            validSets=[]
            aux=[]
            auxValue=cards[0].getValue()
            top=dumpster.getTop().getValue()
            for i in range(len(cards)):
                if top>cards[i].getValue():
                    auxValue=cards[i].getValue()
                elif auxValue==cards[i].getValue():
                    aux.append(i)
                else:
                    if len(aux)>0:
                        validSets.append(aux)
                    auxValue=cards[i].getValue()
                    aux=[]
                    aux.append(i)
            if len(aux)>0:
                validSets.append(aux)
            return validSets

    def think(self,gs):
        p=random.random()
        if p<self.pForDraw and not gs.dump.isEmpty():
            #decide que se las quiere llevar
            return "out"
        elif isinstance(self.actualField,closeField):
            return str(random.randint(0,len(self.closeField.getCards())-1))
        else:
            #this return an array of arrays of indexes
            validSets=self.getValidSets(self.actualField.getCards(),gs.getDumpster())
            if len(validSets)==0:
                return "out"
            else:
                #first select some set
                firstIndex=len(validSets)-1
                if len(validSets[firstIndex])==1:
                    #if the set only has one index, then return that
                    return str(validSets[firstIndex][0])
                else:
                    return str(validSets[firstIndex][0])+"-"+str(validSets[firstIndex][len(validSets[firstIndex])-1])