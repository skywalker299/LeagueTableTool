class Team(object):
 


    def __init__(self, tcode, name):
        self.tid = None
        self.tcode = tcode
        self.name = name
        self.points = 0
        self.goalDifference = 0
        self.goalScored = 0
        self.goalConceded = 0
        self.wins = 0
        self.draws = 0
        self.losses = 0
        self.gamesPlayed = 0
        self.pointsPerGame = 0
        self.homeFixtures = {}
        self.awayFixtures = {}
        
    def __str__(self):
        return (f"{self.tcode:<4}"
                f"{self.points:<4}"
                f"{self.goalDifference:<4}"
                f"{self.gamesPlayed:<4}"
                f"{self.wins:<4}"
                f"{self.draws:<4}"
                f"{self.losses:<4}"
                f"{self.goalScored:<4}"
                f"{self.goalConceded:<4}"
            )
        
    def addResult(self, goalsFor: int, goalsAgainst: int):
        if(goalsFor > goalsAgainst):
            self.points += 3
            self.wins += 1
            self.gamesPlayed += 1
            self.goalNumbers(goalsFor, goalsAgainst)
        elif(goalsFor == goalsAgainst):
            self.points += 1
            self.draws += 1
            self.gamesPlayed += 1
            self.goalNumbers(goalsFor, goalsAgainst)
        elif(goalsFor < goalsAgainst):
            self.losses += 1
            self.gamesPlayed += 1
            self.goalNumbers(goalsFor, goalsAgainst)
        print("Team.addResult(): Success")

    def goalNumbers(self, gFor: int, gAgainst: int):
            self.goalScored += gFor
            self.goalConceded += gAgainst
            self.goalDiffCalc()
        
    def goalDiffCalc(self):
            self.goalDifference = self.goalScored - self.goalConceded
        
    def calcPpg(self):
            self.pointsPerGame = self.points/self.gamesPlayed
    
    def set_stats(self, tid, points, goalDifference, goalScored, goalConceded, 
                  wins, draw, losses, gamesPlayed, pointsPerGame):
        self.tid = tid
        self.points = points
        self.goalDifference = goalDifference
        self.goalScored = goalScored
        self.goalConceded = goalConceded
        self.wins = wins
        self.draws = draw
        self.losses = losses
        self.gamesPlayed = gamesPlayed
        self.pointsPerGame = pointsPerGame
    
    def set_tid(self, tid):
        self.tid = tid
    
    def getFixtureAgainst(self, opponent):
        pass    
        
        