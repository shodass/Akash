import random
import mysql.connector as p
import getpass

def signing_up():
    name=input("enter the name for the user: ")
    password_1=getpass.getpass("enter the password :")
    password_2=getpass.getpass("confirm password")
    if password_1==password_2:
        id_=int(input("enter the ID"))
        cursor.execute("select id from USERS;")
        result=cursor.fetchall()
        for i in result:
            if i==(id_,):
                print("id given exists")
                signing_up()

        special_question=input("enter the question for you")
        special_answer=input("ebter your answer")
        cursor.execute("insert into USERS(name,password,id,special_qestion,special_answer) values(%s,%s,%s,%s,%s);",(name,password_,id_,special_question,special_answer))
        mydb.commit()

def createrecord(number):
    if n==0:
        print("Now you can contiue...")
    else:
        name=input("enter the name for the user: ")
        password_1=getpass.getpass("enter the password :")
        password_2=getpass.getpass("confirm password")
        if password_1==password_2:
            id_=int(input("enter the ID"))
            special_question=input("enter the question for you")
            special_answer=input("ebter your answer")
            cursor.execute("insert into USERS(name,password,id,special_qestion,special_answer) values(%s,%s,%s,%s,%s);",(name,password_,id_,special_question,special_answer))
            mydb.commit()
            createrecord(number-1)
        else:
            print("password and confirm password different")
            createrecord(number)

def random_password(password):
    a=15
    while a>0:
        b=random.randrange(0,2)
        if b==0:
            l=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
            e=random.choice(l)
            password+=e
            a-=1
        if b==1:
            f=random.randrange(0,10)
            password+=str(f)
            a-=1
    return password

def log_in():
    cursor.execute("select password from USERS;")
    result=cursor.fetchone()
    counter="a"
    pd=getpass.getpass("enter the password")
    while counter=="a":
        p1=(pd,)
        if p1==result:
            return True
            counter="b"
        result=cursor.fetchone()

mydb=p.connect(host="localhost",user="root",password="abhinav",database="dashline")
password=""
cursor=mydb.cursor()
print("Are you using this for the first time,enter yes or no")
intial=input("enter yes or no : ")

if intial=="yes":
    cursor.execute("create table USERS(name varchar(50),password varchar(15),id integer,special_qestion varchar(70),special_answer varchar(70));")
    print("""you hmave to give your name,password,id
             and a special question and answer
             so that if you forgot your password
             you could recover it""")
    number=int(input("enter the number of users to be entered: "))
    createrecord(number)


print("""
commands
=======================
li for log_in
su for sign_up
fp for forgot password
=======================
""")

command=input("enter the command: ")
if command=="su":
    signing_up()
    command="li"

if command=="fp":
    print("""why man?.....
             Okay Now input
             your id """)
    id_=int(imput("enter your id"))
    cursor.execute("select special_qestion from USERS where id=%s;",(id_))
    question=cursor.fetchone()
    print(question)
    special_answer=input("enter your answer")
    cursor.execute("select special_answer from USERS where id=%s;",(id_))
    answer=cursor.fetchone()
    if answer==special_answer:
        print("Correct Answer")
        cursor.execute("select * from USERS where id=%s;",(id_))
        response=cursor.fetchone()
        print(response)
        command="li"
    else:
        print("wrong answer")


if command=="li":
    log_in=log_in()
    if log_in==True:
        print("""
            COMANDS
            ----------------
            ---------------
            s=store_password
            l=look_password
        """)
        command2=str(input("enter command"))
        print("Logged_In for the first time")
        reply=input("yes or no")
        if reply=="yes":
            tablename=input("enter your table name ")
            cursor.execute("create table "+tablename+"(username varchar(70),name_of_the_platform varchar(70),password varchar(17));")

        if command2=="s":
            tablename=input("enter your table name")
            n=int(input("enter the number of record to be stored"))
            for i in range(n):
                username=input("enter user name")
                name_of_the_platform=input("enter the name_of_the_platform")
                password=random_password(password)
                print("The Password Is:",password)
                cursor.execute("insert into "+tablename+"(username,name_of_the_platform,password) values(%s,%s,%s)",(username,name_of_the_platform,password))
                mydb.commit()
        if command2=="l":
            tablename=input("enter the table name")
            print("Have you stored any password before")
            reply=input("yes or no: ")
            if reply=="yes":
                cursor.execute("select * from "+tablename)
                record=cursor.fetchall()
                for d in record:
                    print(d)

    else:
        print("Invalid Password")
