from db.connection import get_connection
from _sqlite3 import Cursor, connect

def initialise_database():
    with get_connection() as conn:
        cursor = conn.cursor()
        
        conn.execute("PRAGMA foreign_keys = on")
        
        
        cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS Team (
                tid INTEGER PRIMARY KEY AUTOINCREMENT,
                tcode TEXT,
                name TEXT,
                points INTEGER DEFAULT 0,
                goalDifference INTEGER DEFAULT 0,
                goalScored INTEGER DEFAULT 0,
                goalConceded INTEGER DEFAULT 0,
                wins INTEGER DEFAULT 0,
                draws INTEGER DEFAULT 0,
                losses INTEGER DEFAULT 0,
                gamesPlayed INTEGER DEFAULT 0,
                pointsPerGame REAL DEFAULT 0
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Fixture (
                fid INTEGER PRIMARY KEY AUTOINCREMENT,
                fcode TEXT,
                homeTeamId INTEGER NOT NULL,
                awayTeamId INTEGER NOT NULL,
                homeScore INTEGER DEFAULT 0,
                awayScore INTEGER DEFAULT 0,
                played INTEGER DEFAULT 0,
                date TEXT,
                FOREIGN KEY (homeTeamId) REFERENCES Team(tid),
                FOREIGN KEy (awayTeamId) REFERENCES Team(tid)
            )
        """)
    print("schema.initiliase_database(): Success")    
        