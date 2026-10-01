from models import Team
from models import Fixture
from datetime import date
from repositories import create_team, read_allTeams, update_Team, delete_team, read_tid,\
    fixture_repository
from repositories import create_Fixture, update_Fixture, read_allFixtures, delete_Fixture



class Table(object):

    def __init__(self, xid, name):
        self.xid = xid
        self.name = name
        self.teams = {}
        self.teams_by_id = {}
        self.fixtures = {}


# Team methods       
# Creates Team and adds it to the DB
    def addTeam(self, tcode, name):
        temp = Team(tcode, name)
        self.teams[temp.tcode] = temp
        create_team(tcode, name)
        tid = read_tid(tcode)
        print(tid)
        self.teams[temp.tcode].set_tid(tid)
        self.teams_by_id[tid] = temp
        print("Table.addTeam():Success")

# Creates and initialises a Team instance    
    def initialise_team(self):
        rows = read_allTeams()
        if not rows:
            print("No teams exist")
        else:  
            for row in rows:
                team = Team(row["tcode"], row["name"])
                team.set_stats(row["tid"], row["points"], row["goalDifference"], row["goalScored"],
                                row["goalConceded"], row["wins"], row["draws"], row["losses"], row["gamesPlayed"], row["pointsPerGame"])
                self.teams[team.tcode] = team
                self.teams_by_id[team.tid] = team
        print("Table.initiliase_team(): success")

    
    def update_TeamInfo(self, tcode):
        update_Team(self.teams[tcode])

# Adds Fixture to team      
    def addFtoTeam(self, fcode, searchTcode):
        if self.fixtures[fcode].homeTeam.tcode == searchTcode:
            self.teams[searchTcode].homeFixtures[fcode] = self.fixtures[fcode]
        elif self.fixtures[fcode].awayTeam.tcode == searchTcode:
            self.teams[searchTcode].awayFixtures[fcode] = self.fixtures[fcode]

# removes team from db and memory    
    def remove_team(self, tcode):
        if tcode in self.teams:
            self.pop_team(tcode)
        delete_team(tcode)
        print("Table.remove_team(): Success")
    
    def pop_team(self, tcode):
        self.teams_by_id.pop(self.teams[tcode].tid)
        self.teams.pop(tcode)
        
      
     
        
# Fixture methods   
    
# Creates Fixture and adds it to the respective Teams    
    def createFixture(self, homeTeam, awayTeam, date):
        fullCode = self.teams[homeTeam].tcode+self.teams[awayTeam].tcode
        self.fixtures[fullCode] = Fixture(fullCode, self.teams[homeTeam], self.teams[awayTeam], date)
        self.addFtoTeam(fullCode, homeTeam)
        self.addFtoTeam(fullCode, awayTeam)
        create_Fixture(fullCode, self.teams[homeTeam].tid, self.teams[awayTeam].tid, date)
        print("Table.createFixture(): Success")

# Adds User Input (Result) to both Fixture and Team         
    def addResults(self, fcode, homeResult, awayResult):
        self.fixtures[fcode].addResult(homeResult, awayResult)
        self.fixtures[fcode].homeTeam.addResult(homeResult, awayResult)
        self.fixtures[fcode].awayTeam.addResult(awayResult, homeResult)
        update_Fixture(self.fixtures[fcode])
        self.update_TeamInfo(self.fixtures[fcode].homeTeam.tcode)
        self.update_TeamInfo(self.fixtures[fcode].awayTeam.tcode)
        print("Table.addResults(): Success")

# Initialises the Fixture, creates the instance and adds it to the Team instance 
    def initialise_Fixture(self):
        rows = read_allFixtures()
        if not rows:
            print("No fixtures available")
        else:
            for row in rows:
                datestring = row["date"]
                d = date.fromisoformat(datestring)     
                fixture = Fixture(row["fcode"], self.teams_by_id[row["homeTeamId"]], 
                                  self.teams_by_id[row["awayTeamId"]], d)
                fixture.setStats(row["fid"],row["homeScore"], row["awayScore"], row["played"])
                self.fixtures[fixture.fcode] = fixture
                self.addFtoTeam(fixture.fcode, fixture.homeTeam.tcode)
                self.addFtoTeam(fixture.fcode, fixture.awayTeam.tcode)
        print("Table.initialise_Fixture(): Success")

# Deletes the fixture and removes it from memory        
    def remove_Fixture(self, fcode):
        delete_Fixture(fcode)
        self.fixtures.pop(fcode)
        
        
# Table methods

# Sorts the table initially
    def sortTable(self):
        return sorted(
            self.teams.values(),
            key=lambda t: (
                t.points,
                t.goalDifference,
                t.goalScored
                ),
            reverse=True
        )


# Separates the teams still tied after the first sort for further comparison       
    def tiedGroupSort(self, standings):
        i = 0
        while i < len(standings):
            tied_group = [standings[i]]
            while(
                i + 1 < len(standings)
                and standings[i].points == standings[i + 1].points
                and standings[i].goalDifference == standings[i + 1].goalDifference
                and standings[i].goalScored == standings[i + 1].goalScored
            ):
                tied_group.append(standings[i + 1])
                i += 1
        
            if len(tied_group) > 1:
                tied_group = self.head_to_headSort(tied_group)
                
                start = i -len(tied_group) + 1
                end = i + 1
                standings[start:end] = tied_group
            i += 1
        
        print("tiedGroupSort finished!")
        return standings
    
 
# Non functional head to head comparison
    def head_to_headTable(self, tied_group):
        i = 0
        limit = len(tied_group)
        j = limit-1
        print(tied_group)
        print("Value of limit: ",limit,"Value of j: ",j)
        while (i < limit):
            while (j >= 0):
                if (i == j):
                    j -= 1
                else:
                    f1 = tied_group[i].tcode+tied_group[j].tcode
                    f2 = tied_group[j].tcode+tied_group[i].tcode
                    t1_result = tied_group[i].homeFixtures[f1].homeScore+tied_group[i].awayFixtures[f2].awayScore
                    t2_result = tied_group[j].awayFixtures[f1].awayScore+tied_group[j].homeFixtures[f2].homeScore
                    print("t1_Result: ",t1_result," | t2_Result: ",t2_result)
                    print("Home Fixture: ",f1," | Away Fixture: ",f2)
                    if (t1_result > t2_result):
                        print("Team one wins")
                        pass
                    elif (t1_result < t2_result):
                        print("team2 wins")
                        temp = tied_group[i]
                        tied_group[i] = tied_group[j]
                        tied_group[j] = temp
                    elif (t1_result == t2_result):
                        if (self.fixtures[f2].awayScore > self.fixtures[f1].awayScore):
                            print("team 1 away")
                            pass
                        elif (self.fixtures[f1].awayScore > self.fixtures[f2].awayScore):
                            print("team2 away")
                            temp = tied_group[i]
                            tied_group[i] = tied_group[j]
                            tied_group[j] = temp
                    j -= 1
            i += 1
            j = limit - 1
        print("HeadToHeadTable Finished!")
        return tied_group

# Sorts teams compared to their head to head(Results against each other)
# If still not separated it compares their away goals       
    def head_to_headSort(self, tied_group):
        minitable = {
            team: {
                "points": 0,
                "away_goals": 0
                }
            for team in tied_group
        }
        for fixture in self.fixtures.values():
            if not fixture.played:
                continue
            
            if (fixture.homeTeam not in tied_group or 
                fixture.awayTeam not in tied_group):
                continue
                
            if fixture.homeScore > fixture.awayScore:
                minitable[fixture.homeTeam]["points"] += 3
            elif fixture.homeScore < fixture.awayScore:
                minitable[fixture.awayTeam]["points"] += 3
            elif fixture.homeScore == fixture.awayScore:
                minitable[fixture.homeTeam] += 1
                minitable[fixture.awayTeam] += 1
            
            minitable[fixture.awayTeam]["away_goals"] += fixture.awayScore
            
        sorted_group = sorted(
            tied_group,
            key=lambda team: (
                minitable[team]["points"],
                minitable[team]["away_goals"]
            ),
            reverse = True
        )
        
        return sorted_group

# Sorts the tables first, and then prints it    
    def printTable(self):
        standings = self.sortTable()
        self.tiedGroupSort(standings)
        for position, team in enumerate(standings, start=1):
            print(position, team.name, team.points, team.goalDifference, team.gamesPlayed)

# Returns the table. Equivalent to printTable, used for the web app           
    def return_table(self):
        standings = self.sortTable()
        self.tiedGroupSort(standings)
        return standings
        
                    
    def show_table(self):
        standings = self.sortTable()
        self.tiedGroupSort(standings)       
    
# Sorts the fixtures by date, earliest date first   
    def sortFixture(self):
        return sorted(
            self.fixtures.values(),
            key=lambda f: (
                f.date
                ),
            reverse=False          
        )

#Print Fixture in this style: TE1TE2 1970-01-01 Team 1 FC  0 - 0 Team 2 FC   
    def printFixtures(self):
        fixtureList = self.sortFixture()
        for fixture in fixtureList:
            print("%s %s %s %d - %d %s" % (fixture.fcode, 
                                        fixture.date.isoformat(), 
                                        fixture.homeTeam.name, 
                                        fixture.homeScore, 
                                        fixture.awayScore, 
                                        fixture.awayTeam.name)
            )

# Returns the Fixture. Equivalent to printFixtures, used for web app   
    def return_fixtures(self):
        fixtureList = self.sortFixture()
        return fixtureList
    

    def printOneFixture(self, fcode):
        print(self.fixtures[fcode])
    
    def saveTeam(self):
        for i in self.teams.values():
            update_Team(i)
            
    def save_results(self):
        pass