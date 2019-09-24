import sqlite3

def connect(name):
    conn = sqlite3.connect(name)
    if conn is not None:
        return conn