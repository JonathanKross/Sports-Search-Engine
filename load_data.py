import csv
import psycopg2

conn = psycopg2.connect("dbname=sports user=JonathanKross host=/tmp/")

cur = conn.cursor()

cur.execute("CREATE TABLE roster (Name varchar PRIMARY KEY, Numb integer, Position varchar, Weight integer, Age integer,Years_Exp integer, College varchar);")

f = open('raiders_roster.csv')

cur.copy_from(f, 'roster', sep=",", columns=('Name', 'Numb', 'Position', 'Weight', 'Age', 'Years_Exp', 'College'))

f.close()

conn.commit()
cur.close()
conn.close()
