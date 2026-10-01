

class Fixture(object):


    def __init__(self, fcode, homeTeam, awayTeam, date):
        self.fid = None
        self.fcode = fcode
        self.homeTeam = homeTeam
        self.homeScore = 0
        self.awayTeam = awayTeam
        self.awayScore = 0
        self.date = date
        self.played = False
        
    def __str__(self):
        return (f"{self.fcode:<8}"
                f"{self.date.isoformat():<12}"
                f"{self.homeTeam.name:<8}"
                f"{self.homeScore:<1}"
                f"-"
                f"{self.awayScore:<2}"
                f"{self.awayTeam.name:<10}"
            )
        
    def addResult(self, hScore, aScore):
        self.homeScore = hScore
        self.awayScore = aScore
        self.played = True
        
    def setStats(self, fid, homeScore, awayScore, played):
        self.fid = fid
        self.homeScore = homeScore
        self.awayScore = awayScore
        self.played = played