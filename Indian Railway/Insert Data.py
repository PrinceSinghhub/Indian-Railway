import mysql.connector as mc
MySql = mc.connect(user='root',password='2005@Anushka',database='TrainInfo',host='localhost',port=3306)
print(MySql.is_connected())
print("connected with database")


sql_quari = "insert mytrain(Train_Number,Train_Name,Start_Station,End_Station) values(%s,%s,%s,%s)"
conn = MySql.cursor()


def insertion(Mytuple):
    try:
        conn.execute(sql_quari,Mytuple)
        MySql.commit()
        print("Insertion Sucessfull")
    except:
        MySql.rollback()
        print("Sorry Not Insert data")


def user_input():

    while True:
        trainNo = int(input())
        Train_Name = input()
        Start_Station = input()
        End_Station = input()

        Mytuple = (trainNo,Train_Name,Start_Station,End_Station)
        insertion(Mytuple)

        print("1 & 2")
        n = int(input())
        if n == 1:
            pass
        else:
            break
user_input()




