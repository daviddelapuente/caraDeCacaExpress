from Game.GameObjets import *
from game import *
#return a population of players with a random genoma
def initPopulation(populationLen,a,d):
    population=[]
    for i in range(populationLen):
        gp=gPlayer(hand([]),openField([]),closeField([]),a,d)
        population.append(gp)
    return population

#return an array of len=n of random indexes between 0 and l-1
#warning: this can return duplicated indexes
def randIndex(l,n):
    r=[]
    for i in range(n):
        r.append(random.randint(0, l - 1))
    return r

#return an array of the fitnesses of Ncompetitors
#remember Ncompetitors is an array of indexes
def fitnessesI(population,competitors,fit):
    fitness=[]
    for i in range(len(competitors)):
        f=fit(population[competitors[i]])
        fitness.append(f)
    return fitness


def mutatePlayer(player):
    player.mutate()

#fitness function, this function return the amount of times that a player wins to a random player
def fit(player):
    rp=goodDeterministicPlayer(hand([]),openField([]),closeField([]))
    wins=0
    rplayers=20
    for i in range(rplayers):
        rp.setFields([hand([]),openField([]),closeField([])])
        player.setFields([hand([]),openField([]),closeField([])])
        deck0=deck([card('2',2,2),card('2',2,2),card('2',2,2),card('2',2,2),card('3',3,3),card('3',3,3),card('7',7,7),card('7',7,7),card('7',7,7),card('7',7,7),card('10',10,10),card('10',10,10),card('10',10,10),card('10',10,10),card('11',11,11),card('11',11,11),card('11',11,11),card('11',11,11),card('13',13,13),card('13',13,13),card('13',13,13),card('13',13,13),card('14',14,14),card('14',14,14)])
        gameIAvIA0=gameIAvIA([player,rp],deck0,4,4)
        winner=gameIAvIA0.play()
        if winner==0:
            wins+=1
    return 100*(wins/rplayers)

#Version one of a genetic algorithm that will tray to find a competent careKK player.
#competent player is someone thah has a winrate>50% over a population of random players
#and a winrate>70% of a population of bad players
#also i hope a winrate>10% over a deterministic population
#trys=number of epochs
#populationLen=number of players of this society jeje
#Ncompetitors=number of competitors for the tournament that will determine who replicate it genoma
#F=functions for AST
#T=Terminals for AST
#depth=dept of the initials trees of the initial population
def findPlayer(trys,populationLen,Ncompetitors,F,T,depth,fitnessFunction):
    b=False
    a=AST(F,T,0.5)
    print("buscando jugador competente para careKKExpres")

    population = initPopulation(populationLen,a,depth)

    for t in range(trys):

        #the decendency
        newPopulation=[]

        #queremos que el largo de la poblacion sea  el mismo siempre, por lo que vamos
        #agregando nuevos valores a newPopulation hasta que sus valores sean iguales.
        while(len(newPopulation)<len(population)):

            #random indexes that represent a subPopulation of Ncompetitors
            competitors=randIndex(len(population),Ncompetitors)

            #now the competitors will enter a tournament to calculate the best fitnesses
            fitness=fitnessesI(population,competitors,fitnessFunction)
              
            # tournament
            max1 = fitness[0]
            max2 = fitness[0]

            winner1 = 0
            winner2 = 0

            for i in range(len(competitors)):
                
                if fitness[i] > max1:
                    max1=fitness[i]
                    winner1 = competitors[i]

            for i in range(len(competitors)):
                if competitors[i] != winner1 and fitness[i] > max2:
                    max2=fitness[i]
                    winner2 = competitors[i]
            

            son = crossOverPlayers(population[winner1], population[winner2])
            son.mutate()
            newPopulation.append(son)

        population=newPopulation

        maxfit=-1
        best=0

        F=fitnessesI(population,range(len(population)),fit)

        for i in range(len(F)):
            if F[i]>maxfit:
                maxfit=F[i]
                best=i

            if maxfit==100:
               
                print("jugador competente encontrado!")
                print("en iteracion "+str(t))
                b=True
                break

        if b:
            break

    print("bets winnRate = "+str(F[best])+"%")


trys=3
populationLen=15
depth=5
F=[AddNode,SubNode,MultNode]
T=list(range(-10,10))
T.append("x")
T.append("x")
T.append("x")
T.append("x")
T.append("x")
T.append("x")
T.append("x")
T.append("x")
T.append("x")
T.append("x")
T.append("x")
T.append("x")
T.append("x")
T.append("x")
T.append("x")
T.append("x")
T.append("x")
T.append("x")
T.append("x")
T.append("x")
Ncompetitors=4

findPlayer(trys,populationLen,Ncompetitors,F,T,depth,fit)

