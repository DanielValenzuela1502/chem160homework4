from cards import * #Homeowork 4 wargame similar to cardgame
ntrials=10000  #Final list must print difference of cards vs ratio this difference occurs
difference=53*[0]   #Remember module 6 had carda and cardgame
for i in range(ntrials):
    adeck=deck()
    adeck.shuffle()
    ascore=0
    bdeck=deck()
    bdeck.shuffle()
    bscore=0
    while adeck.cardsleft()>0:
        acard1=adeck.dealcard()
        bcard=bdeck.dealcard()
        if acard1.value()>bcard.value():
            ascore+=2
        if bcard.value() == acard1.value():
            bscore+=1
            ascore+=1
        if bcard.value() > acard1.value():
            bscore+=2
    differ=abs(ascore-bscore)
    difference[differ]+=1
for i in range(0,53,2):
    print(i, difference[i]/ntrials)
