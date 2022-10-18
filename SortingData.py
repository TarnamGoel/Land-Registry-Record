import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "12345",
    database="samplevideo_db"
)

d={}
start=65
for i in range(start,start+26):
    d[chr(i)]=[]

mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM `user_details`')
for x in mycursor:
    if x[1][0]=='a' or x[1][0]=='A':
        d['A']+=[list(x)]
    if x[1][0]=='b' or x[1][0]=='B':
        d['B']+=[list(x)]
    if x[1][0]=='c' or x[1][0]=='C':
        d['C']+=[list(x)]
    if x[1][0]=='d' or x[1][0]=='D':
        d['D']+=[list(x)]
    if x[1][0]=='e' or x[1][0]=='E':
        d['E']+=[list(x)]
    if x[1][0]=='f' or x[1][0]=='F':
        d['F']+=[list(x)]
    if x[1][0]=='g' or x[1][0]=='G':
        d['G']+=[list(x)]
    if x[1][0]=='h' or x[1][0]=='H':
        d['H']+=[list(x)]
    if x[1][0]=='i' or x[1][0]=='I':
        d['I']+=[list(x)]
    if x[1][0]=='j' or x[1][0]=='J':
        d['J']+=[list(x)]
    if x[1][0]=='k' or x[1][0]=='K':
        d['K']+=[list(x)]
    if x[1][0]=='l' or x[1][0]=='L':
        d['L']+=[list(x)]
    if x[1][0]=='m' or x[1][0]=='M':
        d['M']+=[list(x)]
    if x[1][0]=='n' or x[1][0]=='N':
        d['N']+=[list(x)]
    if x[1][0]=='o' or x[1][0]=='O':
        d['O']+=[list(x)]
    if x[1][0]=='p' or x[1][0]=='P':
        d['P']+=[list(x)]
    if x[1][0]=='q' or x[1][0]=='Q':
        d['Q']+=[list(x)]
    if x[1][0]=='r' or x[1][0]=='R':
        d['R']+=[list(x)]
    if x[1][0]=='s' or x[1][0]=='S':
        d['S']+=[list(x)]
    if x[1][0]=='t' or x[1][0]=='T':
        d['T']+=[list(x)]
    if x[1][0]=='u' or x[1][0]=='U':
        d['U']+=[list(x)]
    if x[1][0]=='v' or x[1][0]=='V':
        d['V']+=[list(x)]
    if x[1][0]=='w' or x[1][0]=='W':
        d['W']+=[list(x)]
    if x[1][0]=='x' or x[1][0]=='X':
        d['X']+=[list(x)]
    if x[1][0]=='y' or x[1][0]=='Y':
        d['']+=[list(x)]
    if x[1][0]=='z' or x[1][0]=='Z':
        d['Z']+=[list(x)]
print(d)
