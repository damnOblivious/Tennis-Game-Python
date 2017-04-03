from player import player
class updation:
    def __init__(self):
        self.p=[]
        self.p0=player() #dummy for simplicity in list operations
        self.p1=player()
        self.p2=player()
        self.p.append(self.p0) 
        self.p.append(self.p1)
        self.p.append(self.p2)
        self.mainstart=1
        self.start=1
    def pointloseace(self,playerno):
        if self.p[playerno%3].score==40 and self.p[(playerno*-1)%3].score==50:
            self.p[(playerno*-1)%3].updatescore(-10)
        else:
            self.p[playerno%3].updatescore(10)
        self.checkgame()
        return playerno*-1
    def faultnet(self,playerno):
        if self.p[playerno%3].score==50 and self.p[(playerno*-1)%3].score==40:
            self.p[playerno%3].updatescore(-10)
        else:
            self.p[(playerno*-1)%3].updatescore(10)
        self.checkgame()
    def checkgame(self):
        if abs(self.p1.score-self.p2.score)>=20 and (self.p1.score>40 or self.p2.score>40):
            self.p[1 if self.p1.score>self.p2.score else 2].updategame()
            self.p1.reinscore()
            self.p2.reinscore()
            self.start*=-1
            flag=1
            self.checkset()
    def checkset(self):
        if (abs(self.p1.game-self.p2.game)>1 and (self.p1.game==6 or self.p2.game==6)) or (abs(self.p1.game-self.p2.game)==1 and (self.p1.game>6 or self.p2.game>6)):
            self.p[1 if self.p1.game>self.p2.game else 2].updateset()
            self.p[1].rein()
            self.p[2].rein()
            self.mainstart*=-1
            self.start=self.mainstart
    def disp(self,no,st):
        self.p1.display_score(self.p[2],no,st)
