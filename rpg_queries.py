import sqlite3

def total_characters():
    conn = sqlite3.connect('rpg_db.sqlite3')
    curs = conn.cursor()
    query = 'SELECT COUNT (*) FROM charactercreator_character'
    result = curs.execute(query).fetchall()
    print('There are', result[0][0] ,'Characters')

def total_subclasses():
    conn = sqlite3.connect('rpg_db.sqlite3')
    curs = conn.cursor()
    query = 'SELECT COUNT () FROM charactercreator_cleric'
    result = curs.execute(query).fetchall()
    print('There are', result[0][0] ,'Clerics')
    query = 'SELECT COUNT () FROM charactercreator_fighter'
    result = curs.execute(query).fetchall()
    print('There are', result[0][0] ,'Fighters')
    query = 'SELECT COUNT () FROM charactercreator_mage'
    result = curs.execute(query).fetchall()
    print('There are', result[0][0] ,'Mages')
    query = 'SELECT COUNT () FROM charactercreator_thief'
    result = curs.execute(query).fetchall()
    print('There are', result[0][0] ,'Thieves')
    query = 'SELECT COUNT (*) FROM charactercreator_necromancer'
    result = curs.execute(query).fetchall()
    print('There are', result[0][0] ,'Necromancers')

def total_items():
    conn = sqlite3.connect('rpg_db.sqlite3')
    curs = conn.cursor()
    query = 'SELECT COUNT (*) FROM armory_item'
    result1 = curs.execute(query).fetchall()
    print('There are', result1[0][0] ,'Items')
    query = 'SELECT COUNT (*) FROM armory_weapon'
    result = curs.execute(query).fetchall()
    print('There are', result[0][0] ,'of the weap')
    difference = result1[0][0] - result[0][0]
    print('There are', difference,'non weap itrwme')

def character_items():
    conn = sqlite3.connect('rpg_db.sqlite3')
    curs = conn.cursor()
    query = 'SELECT COUNT (*) FROM armory_item'
    result1 = curs.execute(query).fetchall()
    print('There are', result1[0][0],'items in the game,')
