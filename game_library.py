#!/usr/bin/python3
# game_library.py
# Rob Blocker
# 1/27/2020

import pickle
games = {}

'''Runs prototype for our Game Library database program'''

def add_game():
    new_key = len(games)+1
    entry = []
    valid = False
    while not valid:
        entry.append(input("What is the genre of the game? "))
        entry.append(input("What is the game title? "))
        entry.append(input("What is the game system? "))
        entry.append(input("What is the game release year? "))
        entry.append(input("Who is the game developer? "))
        entry.append(input("Who is the game publisher? "))
        entry.append(input("What is the game rating? "))
        entry.append(input("Is the game multi/single/either player? "))
        entry.append(input("What is the price of the game? "))
        entry.append(input("Did you beat the game? "))
        entry.append(input("When did you purchase the game? "))
        entry.append(input("Any notes on the game? "))
        answer = input("Is this correct? ")
        if answer in ("Yes","yes","Y","y"):
            valid = True
    games[new_key] = entry

def edit_game():
    print("----------------------")
    print("Here is your library: ") 
    print("----------------------")
    print()
    print("Genre: ", games[key][0])
    print("Title: ", games[key][1])
    print("Developer: ", games[key][2])
    print("Publisher: ", games[key][3])        
    print("System: ", games[key][4])
    print("Release Year: ", games[key][5])
    print("Rating: ", games[key][6])
    print("Players: ", games[key][7])
    print("Price: ", games[key][8])
    print("Finish: ", games[key][9])
    print("Purchase Date: ", games[key][10])
    print("Notes: ", games[key][11])
    print("----------------------")    
    

def print_all():
    #print("running print_all()")
    key_list = games.keys()
    for key in key_list:
        games_key_list = games.keys()
     
def search_by_genre():
    found_game = False
    genre = input("  What is the genre of the game? ")
    for key in games.keys():
        if genre == games[key][0]:
            found_game = True
            print()
            print("Genre: ", games[key][0])
            print("Title: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher: ", games[key][3])        
            print("System: ", games[key][4])
            print("Release Year: ", games[key][5])
            print("Rating: ", games[key][6])
            print("Players: ", games[key][7])
            print("Price: ", games[key][8])
            print("Finish: ", games[key][9])
            print("Purchase Date: ", games[key][10])
            print("Notes: ", games[key][11])
            print("----------------------")

def search_by_title():
    found_game = False
    title = input("  What is the title of the game? ")
    for key in games.keys():
        if title == games[key][1]:
            found_game = True
            print()
            print("Genre: ", games[key][0])
            print("Title: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher: ", games[key][3])        
            print("System: ", games[key][4])
            print("Release Year: ", games[key][5])
            print("Rating: ", games[key][6])
            print("Players: ", games[key][7])
            print("Price: ", games[key][8])
            print("Finish: ", games[key][9])
            print("Purchase Date: ", games[key][10])
            print("Notes: ", games[key][11])
            print("----------------------")

def search_by_dev():
    found_game = False
    dev = input("  Who is the developer of the game? ")
    for key in games.keys():
        if dev == games[key][2]:
            found_game = True
            print()
            print("Genre: ", games[key][0])
            print("Title: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher: ", games[key][3])        
            print("System: ", games[key][4])
            print("Release Year: ", games[key][5])
            print("Rating: ", games[key][6])
            print("Players: ", games[key][7])
            print("Price: ", games[key][8])
            print("Finish: ", games[key][9])
            print("Purchase Date: ", games[key][10])
            print("Notes: ", games[key][11])
            print("----------------------")
            
def search_by_pub():
    found_game = False
    pub = input("  Who is the publisher of the game? ")
    for key in games.keys():
        if pub == games[key][3]:
            found_game = True
            print()
            print("Genre: ", games[key][0])
            print("Title: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher: ", games[key][3])        
            print("System: ", games[key][4])
            print("Release Year: ", games[key][5])
            print("Rating: ", games[key][6])
            print("Players: ", games[key][7])
            print("Price: ", games[key][8])
            print("Finish: ", games[key][9])
            print("Purchase Date: ", games[key][10])
            print("Notes: ", games[key][11])
            print("----------------------")
            
def search_by_system():
    found_game = False
    system = input("  What is the system of the game? ")
    for key in games.keys():
        if system == games[key][4]:
            found_game = True
            print()
            print("Genre: ", games[key][0])
            print("Title: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher: ", games[key][3])        
            print("System: ", games[key][4])
            print("Release Year: ", games[key][5])
            print("Rating: ", games[key][6])
            print("Players: ", games[key][7])
            print("Price: ", games[key][8])
            print("Finish: ", games[key][9])
            print("Purchase Date: ", games[key][10])
            print("Notes: ", games[key][11])
            print("----------------------")
            
def search_by_year():
    found_game = False
    year = input("  What is the year the game came out? ")
    for key in games.keys():
        if year == games[key][5]:
            found_game = True
            print()
            print("Genre: ", games[key][0])
            print("Title: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher: ", games[key][3])        
            print("System: ", games[key][4])
            print("Release Year: ", games[key][5])
            print("Rating: ", games[key][6])
            print("Players: ", games[key][7])
            print("Price: ", games[key][8])
            print("Finish: ", games[key][9])
            print("Purchase Date: ", games[key][10])
            print("Notes: ", games[key][11])
            print("----------------------")
            
def search_by_rate():
    found_game = False
    rate = input("  What is the game's rating? ")
    for key in games.keys():
        if rate == games[key][6]:
            found_game = True
            print()
            print("Genre: ", games[key][0])
            print("Title: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher: ", games[key][3])        
            print("System: ", games[key][4])
            print("Release Year: ", games[key][5])
            print("Rating: ", games[key][6])
            print("Players: ", games[key][7])
            print("Price: ", games[key][8])
            print("Finish: ", games[key][9])
            print("Purchase Date: ", games[key][10])
            print("Notes: ", games[key][11])
            print("----------------------")
            
def search_by_players():
    found_game = False
    players = input("  What is the title of the game? ")
    for key in games.keys():
        if players == games[key][7]:
            found_game = True
            print()
            print("Genre: ", games[key][0])
            print("Title: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher: ", games[key][3])        
            print("System: ", games[key][4])
            print("Release Year: ", games[key][5])
            print("Rating: ", games[key][6])
            print("Players: ", games[key][7])
            print("Price: ", games[key][8])
            print("Finish: ", games[key][9])
            print("Purchase Date: ", games[key][10])
            print("Notes: ", games[key][11])
            print("----------------------")
            
def search_by_price():
    found_game = False
    price = input("  What is the price of the game? ")
    for key in games.keys():
        if price == games[key][8]:
            found_game = True
            print()
            print("Genre: ", games[key][0])
            print("Title: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher: ", games[key][3])        
            print("System: ", games[key][4])
            print("Release Year: ", games[key][5])
            print("Rating: ", games[key][6])
            print("Players: ", games[key][7])
            print("Price: ", games[key][8])
            print("Finish: ", games[key][9])
            print("Purchase Date: ", games[key][10])
            print("Notes: ", games[key][11])
            print("----------------------")
            
def search_by_finish():
    found_game = False
    finish = input("  Did you finish the game? ")
    for key in games.keys():
        if finish == games[key][9]:
            found_game = True
            print()
            print("Genre: ", games[key][0])
            print("Title: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher: ", games[key][3])        
            print("System: ", games[key][4])
            print("Release Year: ", games[key][5])
            print("Rating: ", games[key][6])
            print("Players: ", games[key][7])
            print("Price: ", games[key][8])
            print("Finish: ", games[key][9])
            print("Purchase Date: ", games[key][10])
            print("Notes: ", games[key][11])
            print("----------------------")
            
def search_by_purchase():
    found_game = False
    pur_date = input("  What is the purchase date of the game? ")
    for key in games.keys():
        if pur_date == games[key][10]:
            found_game = True
            print()
            print("Genre: ", games[key][0])
            print("Title: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher: ", games[key][3])        
            print("System: ", games[key][4])
            print("Release Year: ", games[key][5])
            print("Rating: ", games[key][6])
            print("Players: ", games[key][7])
            print("Price: ", games[key][8])
            print("Finish: ", games[key][9])
            print("Purchase Date: ", games[key][10])
            print("Notes: ", games[key][11])
            print("----------------------")
            
def remove_game():
    title = input("What is the game title? ")
    if title not in games:
        print("*** Are you sure that's the right game? ***")
    else:
        entry = games.pop(title)
        print(title, ":", entry[0], entry[1]+", removed.")
        
def save_database():
    print("Leaving Library")
    datafile = open("gamelib.pickle", "wb")
    pickle.dump(games, datafile)
    #print(games)
    datafile.close()    

def search_by():
    print("""
    What Will You Search By?
    ------------------------
    
    SEARCH MENU
    a) Genre
    s) Title
    d) Developer
    f) Publisher
    g) System
    h) Release Year
    j) Rating
    k) Players
    l) Price
    ;) Finish
    ') Purchase Date (mm/dd/yyyy)
    
    Q) Quit
    
    """)    
    
    search_term = print("How would you like to search for your game? ")
    if search_term == "a":
        search_by_genre()
    elif search_term == "s":
        search_by_title()
    elif search_term == "d":
        search_by_dev()
    elif search_term == "f":
        search_by_pub()
    elif search_term == "g":
        search_by_system()
    elif search_term == "h":
        search_by_year()
    elif search_term == "j":
        search_by_rate()
    elif search_term == "k":
        search_by_players()
    elif search_term == "l":
        search_by_price()
    elif search_term == ";":
        search_by_finish()
    elif search_term == "'":
        search_by_purchase()  
    elif search_term == "Q" or search_term == "q":
        quit()
    else:
        print("*** SORRY WE CAN'T DO THAT FOR YOU ***\n")
        
print("Goodbye.")

datafile = open("gamelib.pickle", "rb")
games = pickle.load(datafile)
#print(games)
datafile.close()

keep_going = True

while keep_going:
    print("""
    Your Game Library
    -----------------
    
    MAIN MENU
    1) Add Game
    2) Edit Game
    3) Print All Games
    4) Search by Title
    5) Remove a Game
    6) Save Database
    
    Q) Quit
    
    """)

    choice = input("What would you like to do? ")
    if choice == "1":
        add_game()
    elif choice == "2":
        edit_game()
    elif choice == "3":
        print_all()
    elif choice == "4":
        search_by_title()
    elif choice == "5":
        remove_game()
    elif choice == "6":
        save_database()
    elif choice == "Q" or choice == "q":
        quit()
        keep_going = False
    else:
        print("*** SORRY WE CAN'T DO THAT FOR YOU ***\n")
        
print("Goodbye.")