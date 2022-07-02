import sqlite3
con=sqlite3.connect('user.db')
con.execute("create table users(NAME,CAR,CAR NUMBER,CAR MODEL,YEAR);")
def insertData(name,car,car number,car model,year):
    qry=f'insert into users (NAME,CAR,CAR NUMBER,CAR MODEL,YEAR) values ("{name}","{car}","{car number}","{car model}","{year}");'
    con.execute(qry)
    con.commit()
    print("add")

def select(car):
    qry='select * from users where car="'+car+'";'
    result=con.execute(qry)
    print("carName \t car \t car \t car \t Year")
    for row in result:
        print("|\t    ".join(row))
def display():
    qry='select * from users;'
    result=con.execute(qry)
    print("car Name \t car \t car number \t car model \t Year")
    for row in result:
        print("|\t    ".join(row))

print("1.Insert Data \n2.search car \n3.display all")
ch="y"
while(ch.lower()=='y'):
    c=int(input())
    if(c==1):
        print("add record")
        name=input("Enter the name of the car:")
        actor=input("Enter the name of the car:")
        actress=input("Enter the name of the car number")
        director=input("Enter the name of the car model")
        year=input("Enter the year of car")
        insertData(name,car,car number,car model,year)
    elif (c==2):
        print("select")
        select(input("CAR NAME:"))
    elif(c==3):
        display()
    else:
        print("Invalied option:" + c)
    ch = input("Do you want to continue[Y/n]: ")
