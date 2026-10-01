from db.connection import get_connection
import sqlite3

def create_team(tcode, name):
    with get_connection() as conn:
        cursor = conn.cursor()
        
        cursor.execute(""" 
            INSERT INTO Team (tcode, name)
            VALUES (?, ?)
        """, (tcode, name)
        )
    print("team_repository.create_team(): Success")
        
def read_allTeams():
    with get_connection() as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM Team;")
        print("team_repository.read_allTeam(): Success")
        return cursor.fetchall()   
                
def read_Team(tcode):
    with get_connection() as conn:
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT * FROM Team
            WHERE tcode = ?;
        """, (tcode,)
        )
        print("team_repository.read_team(): Success")
        
        return cursor.fetchone()
    
    
def read_tid(tcode):
    with get_connection() as conn:
        cursor = conn.cursor()
        
        cursor.execute("SELECT tid FROM Team WHERE tcode = ?", (tcode,))
        
        row = cursor.fetchone()
        print("REpo: ",row)
        if row is None:
            return None
        return row[0]

def update_Team(team):
    with get_connection() as conn:
        cursor = conn.cursor()
        
        cursor.execute("""
            UPDATE Team SET 
                points = ?,
                goalDifference = ?,
                goalScored = ?,
                goalConceded = ?,
                wins = ?,
                draws = ?,
                losses = ?,
                gamesPlayed = ?,
                pointsPerGame = ?
            WHERE tid = ?;
                
        """, (team.points, team.goalDifference, team.goalScored, team.goalConceded,
              team.wins, team.draws, team.losses, team.gamesPlayed, team.pointsPerGame, team.tid)
        )
    print("team_repository.update_team(): Success")
        
def delete_team(tcode):
    with get_connection() as conn:
        cursor = conn.cursor()
        
        cursor.execute("""
            DELETE FROM Team
            WHERE tcode = ?;
        """, (tcode,)
        )
    print("team_repository.delete_team(): Success")
        
def delete_allTeam():
    with get_connection() as conn:
        cursor = conn.cursor
        
        cursor.execute("DELETE FROM Team;")
        
    print("team_repository.delete_allTeam(): Success")