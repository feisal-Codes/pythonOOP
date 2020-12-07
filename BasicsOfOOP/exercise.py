class Player:
    def __init__(self,id,name,teamName):
        self.id=id
        self.name=name
        self.teamName=teamName
    

class Team:
    def __init__(self,name=None):
        self.name=name
        self.players=[]

    def addPlayer(self,player):
        self.players.append(player)

    def getNumberOfPlayers(self):
        return len(self.players)

class School:
    def __init__(self,name):
        self.name=name
        self.teams=[]
    
    def addTeam(self,team):
        self.teams.append(team)

    def getNumberOfPlayersinschool(self):
      
      count=0
      for n in self.teams:
          count= count + n.getNumberOfPlayers()
          
      return count 
                     


player1=Player(1,'Feisal','Red')
player2=Player(2,'keisal','Red')
player5=Player(1,'Fesal','Red')
player6=Player(1,'Fisal','Red')
player7=Player(1,'Feis','Red')


player3=Player(3,'Ibrahim','Blue')
player4=Player(4,'Mohamed','Blue')


red_team=Team('Red Team')
red_team.players.append(player1)
red_team.players.append(player2)
red_team.players.append(player5)
red_team.players.append(player6)
red_team.players.append(player7)


Blue_team=Team('Blue Team')
Blue_team.players.append(player3)
Blue_team.players.append(player4)




mySchool=School('My School')
mySchool.teams.append(red_team)
mySchool.teams.append(Blue_team)


print('Total Number of players in my school is:',mySchool.getNumberOfPlayersinschool())

del mySchool
print(red_team.getNumberOfPlayers())









































