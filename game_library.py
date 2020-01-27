#!/usr/bin/python3
# game_library.py
# Rob Blocker
# 1/26/2020

import pickle
games = {}

'''Runs prototype for our Game Library database program'''

def add_game():
    title = input("What is the game title? ")
    if title in games:
        print("*** Edit Game Info? ***\n")
        update_game(title)
    else:
        update_game(title)

def print_all():
    #print("running print_all()")
    key_list = games.keys()
    for key in key_list:
        print()
        print("Title: ", key)
        print("System: ", games[key][0])
        print("Genre: ", games[key][1])
        print("Release Date: ", games[key][2])
        print("Developer: ", games[key][3])
        print("Publisher: ", games[key][4])
        print("Rating: ", games[key][5])
        print("Players: ", games[key][6])
        print("Price: ", games[key][7])
        print("Finish: ", games[key][8])
        print("Purchase Date: ", games[key][9])
        print("Notes: ", games[key][10])
        print("----------------------")

def search_by_title():
    found_game = False
    title = input("  What is the title of the game? ")
    for key in games.keys():
        if title == games[key][1]:
            found_game = true
            print()
            print("Title: ", key)
            print("System: ", games[key][0])
            print("Genre: ", games[key][1])
            print("Release Date: ", games[key][2])
            print("Developer: ", games[key][3])
            print("Publisher: ", games[key][4])
            print("Rating: ", games[key][5])
            print("Players: ", games[key][6])
            print("Price: ", games[key][7])
            print("Finish: ", games[key][8])
            print("Purchase Date: ", games[key][9])
            print("Notes: ", games[key][10])
            print("----------------------")            
            

def delete_game():
    title = input("What is the game title? ")
    if title not in games:
        print("*** Are you sure that's the right game? ***")
    else:
        entry = games.pop(title)
        print(title, ":", entry[0], entry[1]+", removed.")
        
def save_database():
    #print("Leaving Library")
    pickle_file = open("datafile.pickle", "wb")
    pickle.dump(games, pickle_file)
    pickle_file.close()
        
def update_game(title):
    system = input("   What is the system? ")
    genre = input("   What is the genre? ")
    year = input("   What is their release year? ")
    dev = input("   Who is the game developer?  ")
    pub = input("   Who is the game publisher?  ")
    rate = input("   What is the game rating?  ")
    players = input("  Is the game multi/single/either player?  ")
    price = input("   What is the price of the game?  ")
    finish = input("   Did you beat the game?  ")
    pur_date = input("   When did you purchase the game?  ")
    notes = input("   Notes on the game?  ")
    games[title] = [system, genre, year, dev, pub, rate, 
                    players, price, finish, pur_date, notes]    

pickle_file = open("datafile.pickle", "rb")
people = pickle.load(pickle_file)
#print(games)
pickle_file.close()

keep_going = True

while keep_going:
    print("""
    Your Game Library
    -----------------
    
    MAIN MENU
    1) Add/Edit Game
    2) Print All Games
    3) Search by Title
    4) Remove a Game
    5) Save Database
    
    Q) Quit
    
    """)