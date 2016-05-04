import psycopg2
import argparse



#Connect to 'sport' database
conn = psycopg2.connect("dbname=sports user=JonathanKross host=/tmp/")
cur = conn.cursor()



#to insert new player stats:
def add_player():

    """Prompts user for all necessary stats. Inserts new stats into the 'roster'
    table in the 'sports' database"""

    conn = psycopg2.connect("dbname=sports user=JonathanKross host=/tmp/")
    cur = conn.cursor()

    new_name = input("Full Name of new player: ")
    new_numb = input("New Player's number: ")
    new_position = input("New Player's position: ")
    new_weight = input("New Player's weight: ")
    new_age = input("New Player's age: ")
    new_years = input("New Player's years of experience: ")
    new_college = input("New Player's college: ")

    cur.execute("INSERT INTO roster (Name, Numb, Position, Weight, Age, Years_Exp, College) VALUES (%s, %s, %s, %s, %s, %s, %s)", (new_name, new_numb, new_position, new_weight, new_age, new_years, new_college))
    conn.commit()


#search for stats by player Name
def search_player():

    player = input("Which player stats would you like to see? ")
    cur.execute("SELECT * FROM roster WHERE Name = %s", (player,))
    # cur.execute("SELECT * FROM roster WHERE Name LIKE '%player%'")

    rows = cur.fetchall()
    for row in rows:
        print("Name = ", row[0])
        print("Number = ", row[1])
        print("Position = ", row[2])
        print("Weight = ", row[3])
        print("Age = ", row[4])
        print("Years of Experience = ", row[5])
        print("College = ", row[6], "\n")


#display entire 'roster' table
def display_table():

    cur.execute("SELECT * FROM roster;")
    rows = cur.fetchall()
    for row in rows:
        print("Name = ", row[0])
        print("Number = ", row[1])
        print("Position = ", row[2])
        print("Weight = ", row[3])
        print("Age = ", row[4])
        print("Years of Experience = ", row[5])
        print("College = ", row[6], "\n")


def main():
    if args.add:
    else:
        conn = psycopg2.connect("dbname=sports user=JonathanKross host=/tmp/")
        cur = conn.cursor()
        new_name = input("Full Name of new player: ")
        new_numb = input("New Player's number: ")
        new_position = input("New Player's position: ")
        new_weight = input("New Player's weight: ")
        new_age = input("New Player's age: ")
        new_years = input("New Player's years of experience: ")
        new_college = input("New Player's college: ")

        cur.execute("INSERT INTO roster (Name, Numb, Position, Weight, Age, Years_Exp, College) VALUES (%s, %s, %s, %s, %s, %s, %s)", (new_name, new_numb, new_position, new_weight, new_age, new_years, new_college))
        conn.commit()
        cur.close()
        conn.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Insert stats into roster table')
    parser.add_argument('--add', type=str, nargs='*', default="", help='Columns= Name, Number, Position, Weight, Age, Years of Experience, College')
    args = parser.parse_args()
    main(args.add)
