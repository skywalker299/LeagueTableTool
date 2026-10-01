import sqlite3
from db.connection import get_connection
from datetime import date

def create_Fixture(fcode, homeTeamId, awayTeamId, date):
    with get_connection() as conn:
        cursor = conn.cursor()
        
        cursor.execute(""" 
            INSERT INTO Fixture (
                fcode,
                homeTeamId,
                awayTeamId,
                date)
            VALUES (?, ?, ?, ?)
        """, (fcode, homeTeamId, awayTeamId, date.isoformat())
        )
        print("Fixture.create_Fixture(): Success")
        
def read_allFixtures():
    with get_connection() as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM Fixture")
        print("Fixture.read_allFixtures(): Success")
        return cursor.fetchall()
    
def read_Fixture(fcode):
    with get_connection() as conn:
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT * FROM Fixture
            WHERE fcode = ?
        """, (fcode,)
        )
        print("Fixture.read_Fixture(): Success!")
        return cursor.fetchone

def update_Fixture(f):
    with get_connection() as conn:
        cursor = conn.cursor()
        
        cursor.execute("""
            UPDATE Fixture SET
                homeScore = ?,
                awayScore = ?,
                played = ?
            WHERE fid = ?
        """, (f.homeScore, f.awayScore, 1,f.fid)
        )
    print("Fixture.update_Fixture(): Success")
    
def delete_AllFixture():
    with get_connection() as conn:
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM Fixture;")
        
        print("Fixture.delete_AllFixture(): Success!")
        
def delete_Fixture(fcode):
    with get_connection() as conn:
        cursor = conn.cursor()
        
        cursor.execute("""
            DELETE FROM Fixture
            WHERE fcode = ?;
        """, (fcode,)
        )
        print("Fixture.delete_Fixture(): Success")
        
        