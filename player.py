class player:
    def __init__(self):
        self.score=0
        self.game=0
        self.sets=0
    def rein(self):
        self.score=0
        self.game=0
    def reinscore(self):
        self.score=0
    def updatescore(self,val):
        self.score+=val if self.score>25 else 15
    def updategame(self):
        self.game+=1
    def updateset(self):
        self.sets+=1
    def display_score(self,self2,no,st):
        print '%s%d  :  %s' %('Player',no,st)
        print 'P1 Score:','Advantage' if self.score==50 and self2.score==40 else ('Deuce' if self.score==40 and self2.score==40 else self.score)
        print 'P2 Score:','Advantage' if self2.score==50 and self.score==40 else ('Deuce' if self2.score==40 and self.score==40 else self2.score)
        print 'P1 Game Win Count:',self.game
        print 'P2 Game Win Count:',self2.game
        print 'P1 Set Win Count:',self.sets
        print 'P2 Set Win Count:',self2.sets
        print
