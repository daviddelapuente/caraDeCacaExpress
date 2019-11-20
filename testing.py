from game import *
realPlayer=player(hand([]),openField([]),closeField([]))
player2=goodDeterministicPlayerV2(hand([]),openField([]),closeField([]))
deck=deck([card('2',2,2),card('2',2,2),card('2',2,2),card('2',2,2),card('3',3,3),card('3',3,3),card('7',7,7),card('7',7,7),card('7',7,7),card('7',7,7),card('10',10,10),card('10',10,10),card('10',10,10),card('10',10,10),card('11',11,11),card('11',11,11),card('11',11,11),card('11',11,11),card('13',13,13),card('13',13,13),card('13',13,13),card('13',13,13),card('14',14,14),card('14',14,14)])
gamePvIA=gamePvIA([realPlayer,player2],deck,4,4)
gamePvIA.play()


#player1=randomPlayerV2(hand([]),openField([]),closeField([]))
#player2=randomPlayerV2(hand([]),openField([]),closeField([]))
#deck=deck([card('2',2,2),card('2',2,2),card('2',2,2),card('2',2,2),card('3',3,3),card('3',3,3),card('7',7,7),card('7',7,7),card('7',7,7),card('7',7,7),card('10',10,10),card('10',10,10),card('10',10,10),card('10',10,10),card('11',11,11),card('11',11,11),card('11',11,11),card('11',11,11),card('13',13,13),card('13',13,13),card('13',13,13),card('13',13,13),card('14',14,14),card('14',14,14)])
#gameIAvIA=gameIAvIA([player1,player2],deck,4,4)
#gameIAvIA.play()



#print("random player vs random player")

#p0wins=0
#p1wins=0
#for i in range(0,100):
#    player0=randomPlayerV2(hand([]),openField([]),closeField([]))
#    player1=goodDeterministicPlayerV2(hand([]),openField([]),closeField([]))
#    deck0=deck([card('2',2,2),card('2',2,2),card('2',2,2),card('2',2,2),card('3',3,3),card('3',3,3),card('7',7,7),card('7',7,7),card('7',7,7),card('7',7,7),card('10',10,10),card('10',10,10),card('10',10,10),card('10',10,10),card('11',11,11),card('11',11,11),card('11',11,11),card('11',11,11),card('13',13,13),card('13',13,13),card('13',13,13),card('13',13,13),card('14',14,14),card('14',14,14)])
#    gameIAvIA0=gameIAvIA([player0,player1],deck0,4,4)
#    winner=gameIAvIA0.play()
#    if winner==0:
#        p0wins+=1
#    elif winner==1:
#        p1wins+=1
#print("p0 winrate = "+str(p0wins/(p0wins+p1wins)))
#print("p1 winrate = "+str(p1wins/(p0wins+p1wins)))

#notas 1: un random vs randomV2 pueden causar loops infinitos de juego si la prob de robar cartas es 0 en ambos casos.
