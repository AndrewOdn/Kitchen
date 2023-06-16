import sqlite3


def create_tables():
    conn = sqlite3.connect('database.db')
    conn.execute(
        'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE, password TEXT)')
    conn.execute(
        'CREATE TABLE IF NOT EXISTS panel_const (temperature INTEGER, lights BOOL, humidity INTEGER, water BOOL, temperature_fridge INTEGER)')
    conn.execute(
        'CREATE TABLE IF NOT EXISTS panel_temp (kettle BOOL, grill BOOL, coffee BOOL)')
    conn.close()
