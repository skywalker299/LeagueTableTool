import sys

from flask import Flask
from db import initialise_database
from models import Table
from console import run_console
from web import run_web
from datetime import date



def main():
    
    
    initialise_database()
    
    t = Table(0, "Basic")
    t.initialise_team()
    t.initialise_Fixture()
        
    if len(sys.argv) < 2:
        run_web(t)
        
    else:
        mode = sys.argv[1]
        
        if mode == "console":
            run_console(t)
            
        elif mode == "web":
            run_web(t)
            
        else:
            print(f"Unknown mode: {mode}")
    print("ShutDown!")

    
if __name__ == '__main__':
    main()