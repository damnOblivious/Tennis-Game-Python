from player import player 
from updation import updation
from sys import argv
script=argv[1]
fp1=argv[1]
obj=updation()

with open(fp1) as fp:
    obj.start=obj.mainstart
    flag=0
    playerno=1
    for line in fp:
        field = line.split( )
        if len(field) > 1:
            if flag==1:
                playerno=obj.start
                flag=0
            f=field[1].split('-')
            if (len(f) > 1 and field[1].find("SameSide")==-1) or field[1]=='Ace':
                playerno=obj.pointloseace(playerno)
                flag=1
            elif field[1]=='Fault' or field[1]=='Nets' or field[1].find("SameSide")!=-1:
                obj.faultnet(playerno)
               # if field[1]=='Nets':
                flag=1
            elif field[1]=='Backhand' or field[1]=='Forehand':
                playerno*=-1
            obj.disp(playerno%3,field[1])
