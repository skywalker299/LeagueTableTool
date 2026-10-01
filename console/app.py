from models import Table
from datetime import date

def run_console(t):
    t.printTable()
    while(1):
        print("Choose Category")
        cat = input()
        match cat:
            case 't'|'T':
                print("Choose Action:")
                op = input()   
                match op:
                    case 'c'|'c':
                        print("Create team")
                        print("Input Full team name")
                        name = input()
                        print("Input 3 letter team code")
                        tcode = input()
                        t.addTeam(tcode, name)
                    case 'i'|'I':
                        print("Team information. Enter 3 Letter code")
                        tcode = input()
                        print(t.teams[tcode])
                        print("Home Fixtures")
                        print(*t.teams[tcode].homeFixtures, sep='\n')
                        print("Away Fixtures")
                        print(*t.teams[tcode].awayFixtures, sep='\n')
                        print("ID: {}".format(t.teams[tcode].tid))
                    case 'x'|'X':
                        break
                    case 'h'|'H':
                        helpMenu()
                    case 'p'|'P':
                        print("Print table")
                        t.printTable()
                    case 'a'|'A':
                        print("Add Result:")
                        print("Enter Fixture Code:")
                        fcode = input()
                        t.printOneFixture(fcode)
                        print("Enter Home Score")
                        homeResult = input()
                        print("Enter Away Score")
                        awayResult = input()
                        t.addResults(fcode, int(homeResult), int(awayResult))
                        t.printTable()
                    case 'r'|'R':
                        print("Remove Team. Enter Team Code")
                        tcode = input()
                        t.remove_team(tcode)
                    case _:
                        helpMenu()
            case 'f'|'f':
                print("Choose Action:")
                op = input()
                match op:
                    case 'p'|'P':
                        print("Fixture list:")
                        t.printFixtures()
                    case 'x'|'X':
                        break
                    case 'h'|'H':
                        helpMenu()
                    case 'c'|'C':
                        print("Create Fixture")
                        print("Enter Home Team Code:")
                        homeTeam = input()
                        print("Enter Away Team Code")
                        awayTeam = input()
                        print("Enter Day:")
                        day = input()
                        print("Enter Month")
                        month = input()
                        print("Enter Year")
                        year = input()
                        d = date(int(year), int(month), int(day))
                        t.createFixture(homeTeam, awayTeam, d)
                    case 'r'|'R':
                        print("Remove Fixture. Enter Fixture Code:")
                        fcode = input()
                        t.remove_Fixture(fcode)
                    case _:
                        helpMenu()
            case 'x'|'X':
                break
            case 'h'|'H':
                helpMenu()
            case 'p'|'P':
                t.printTable()
            case _:
                helpMenu()
    print("finish!")
    
def helpMenu():
    print("Team menu: t")
    print("Help: h")
    print("Create Team: c")
    print("Close: x")
    print("Print table: p")