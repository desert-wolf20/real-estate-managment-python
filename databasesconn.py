import mysql.connector
from mysql.connector import Error
import tkinter.messagebox


def connectsql():
    
    try:
        connection = mysql.connector.connect(host='Server-IP',
                                         database='Database name',
                                         user='Username',
                                         password='Password')
        if connection.is_connected():

            cur = connection.cursor()
#cracter set ? 
            cur.execute("CREATE TABLE IF NOT EXISTS shareS (idshare INTEGER primary key AUTO_INCREMENT,city TEXT,typesql TEXT,conditionsql TEXT,nighSQL TEXT,landnSQL TEXT,landbSQL TEXT,northSQL TEXT,southSQL TEXT,eastSQL TEXT,westSQL TEXT,spacesql TEXT,ownersql TEXT,phonesql TEXT,pricesql TEXT,bidsql TEXT,extrasql TEXT, UNIQUE (city(50),nighSQL(50),landnSQL(50),landbSQL(50)))")       
            connection.commit()

    except Error as e:
        print(e)
        
    finally:
        if (connection.is_connected()):
            cur.close()
            connection.close()
            print("MySQL connection is closed")
            
def addShare(city,typesql,conditionsql,nighSQL,landnSQL,landbSQL,northSQL,southSQL,eastSQL,westSQL,spacesql,ownersql,phonesql,pricesql,bidsql,extrasql):
    try:
        connection = mysql.connector.connect(host='Server-IP',
                                         database='Database name',
                                         user='Username',
                                         password='Password')
        if connection.is_connected():
            ownersql = open("resources/n65748382991.skm","r",encoding='utf-8').read()
            cur = connection.cursor()
            cur.execute("INSERT INTO shareS VALUES (%s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s)",\
                        [None,city,typesql,conditionsql,nighSQL,landnSQL,landbSQL,northSQL,southSQL,eastSQL,westSQL,spacesql,ownersql,phonesql,pricesql,bidsql,extrasql])
            connection.commit()
                                                                                  
    except Error as e:
        result = tkinter.messagebox.showinfo('الارض موجودة مسبقا' , e)
    finally:
        if (connection.is_connected()):
            cur.close()
            connection.close()
            print("MySQL connection is closed")

def viewShare():
    try:
        connection = mysql.connector.connect(host='Server-IP',
                                         database='Database name',
                                         user='Username',
                                         password='Password')
        if connection.is_connected():

            cur = connection.cursor(buffered=True)
            
            cur.execute("SELECT * FROM shareS")
            rows=cur.fetchall()
            return rows
                                                                                  
    except Error as e:
        result = tkinter.messagebox.showinfo('لا يوجد اتصال بالانترنت' , e)



def delete_sql(idshare):
    try:
        connection = mysql.connector.connect(host='Server-IP',
                                         database='Database name',
                                         user='Username',
                                         password='Password')
        if connection.is_connected():

            cur = connection.cursor()
            
            cur.execute("DELETE FROM shareS where idshare= %s",(idshare,))

                                                                                  
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        pass
            
            
            
def search_sql(city ='',typesql='',conditionsql='',nighSQL='',landnSQL='',landbSQL='',northSQL ='',southSQL ='',eastSQL ='',westSQL ='',spacesql ='',ownersql ='',phonesql ='',pricesql ='',bidsql='',extrasql=''):
    try:
        connection = mysql.connector.connect(host='Server-IP',
                                         database='Database name',
                                         user='Username',
                                         password='Password')
        if connection.is_connected():

            cur = connection.cursor()
            ### 666 ###
            if typesql != "" and city != "" and conditionsql != "" and nighSQL != "" and landbSQL != "" and spacesql != "" and ownersql != "":
                cur.execute("SELECT * FROM shareS WHERE typesql= %s AND city=%s AND conditionsql = %s AND nighSQL = %s AND landbSQL = %s AND spacesql = %s AND ownersql = %s",\
                         [typesql,city,conditionsql,nighSQL,landbSQL,spacesql,ownersql])
            ### 555 ###
            elif typesql != "" and city != "" and conditionsql != "" and nighSQL != "" and landbSQL != "" and spacesql != "" :
                cur.execute("SELECT * FROM shareS WHERE typesql= %s AND city=%s AND conditionsql = %s AND nighSQL = %s AND landbSQL = %s AND spacesql = %s",\
                         [typesql,city,conditionsql,nighSQL,landbSQL,spacesql])
            ### 555 ###
            elif typesql != "" and city != "" and conditionsql != "" and nighSQL != "" and landbSQL != "" :
                cur.execute("SELECT * FROM shareS WHERE typesql= %s AND city=%s AND conditionsql = %s AND nighSQL = %s AND landbSQL = %s",\
                         [typesql,city,conditionsql,nighSQL,landbSQL])
            elif typesql != "" and city != "" and conditionsql != "" and nighSQL != "" and spacesql != "" :
                cur.execute("SELECT * FROM shareS WHERE typesql= %s AND city=%s AND conditionsql = %s AND nighSQL = %s AND spacesql = %s",\
                         [typesql,city,conditionsql,nighSQL,spacesql])
            ### 444 ### R
            elif typesql != "" and city != "" and conditionsql != "" and nighSQL != "" :
                cur.execute("SELECT * FROM shareS WHERE typesql=%s AND city=%s AND conditionsql =%s AND nighSQL =%s",\
                         [typesql,city,conditionsql,nighSQL])
            elif typesql != "" and city != "" and landbSQL != "" and nighSQL != "" :
                cur.execute("SELECT * FROM shareS WHERE typesql=%s AND city=%s AND landbSQL =%s AND nighSQL =%s",\
                         [typesql,city,landbSQL,nighSQL])
            elif landbSQL != "" and city != "" and conditionsql != "" and nighSQL != "" :
                cur.execute("SELECT * FROM shareS WHERE landbSQL=%s AND city=%s AND conditionsql =%s AND nighSQL =%s",\
                         [landbSQL,city,conditionsql,nighSQL])
            ### 333 ### R
            elif typesql != "" and city != "" and conditionsql != "" :
                cur.execute("SELECT * FROM shareS WHERE typesql=%s AND city=%s AND conditionsql =%s",\
                         [typesql,city,conditionsql])    
            elif landbSQL != "" and city != "" and nighSQL != "":
                cur.execute("SELECT * FROM shareS WHERE landbSQL=%s AND city=%s AND nighSQL =%s",\
                         [landbSQL,nighSQL])  
            elif typesql != "" and city != "" and nighSQL != "":
                cur.execute("SELECT * FROM shareS WHERE typesql=%s AND city=%s AND nighSQL =%s",\
                         [typesql,city,nighSQL])
            elif conditionsql != "" and city != "" and nighSQL != "":
                cur.execute("SELECT * FROM shareS WHERE conditionsql=%s AND city=%s AND nighSQL =%s",\
                         [conditionsql,city,nighSQL])
            ### 222 ###
            elif typesql != "" and city != "":
                cur.execute("SELECT * FROM shareS WHERE typesql=%s AND city=%s",\
                         [typesql,city])  
                  
            elif city != "" and nighSQL != "":
                cur.execute("SELECT * FROM shareS WHERE city=%s AND nighSQL =%s",\
                         [city,nighSQL])
            elif conditionsql != "" and city != "":
                cur.execute("SELECT * FROM shareS WHERE conditionsql=%s AND city=%s",\
                         [conditionsql,city])
                      
            ### 111 ###

            else:
                if northSQL != "":
                    cur.execute("SELECT * FROM shareS WHERE northSQL=%s",[northSQL])
                    
                    ###
                elif  typesql != "":
                    cur.execute("SELECT * FROM shareS WHERE typesql=%s",[typesql])
                elif  conditionsql != "":
                    cur.execute("SELECT * FROM shareS WHERE conditionsql=%s",[conditionsql])
                elif  nighSQL != "":
                    cur.execute("SELECT * FROM shareS WHERE nighSQL=%s",[nighSQL])
                elif  landbSQL != "":
                    cur.execute("SELECT * FROM shareS WHERE landbSQL=%s",[landbSQL])
                elif  spacesql != "":
                    cur.execute("SELECT * FROM shareS WHERE spacesql=%s",[spacesql])
                elif  ownersql != "":
                    cur.execute("SELECT * FROM shareS WHERE ownersql=%s",[ownersql])
                    ####
                elif  southSQL != "":
                    cur.execute("SELECT * FROM shareS WHERE southSQL=%s",[southSQL])
                elif  eastSQL != "":
                    cur.execute("SELECT * FROM shareS WHERE eastSQL=%s",[eastSQL])
                elif  westSQL != "":
                    cur.execute("SELECT * FROM shareS WHERE westSQL=%s",[westSQL])
                elif  extrasql != "":
                    cur.execute("SELECT * FROM shareS WHERE extrasql=%s",[extrasql])
                elif  landnSQL != "":
                    cur.execute("SELECT * FROM shareS WHERE landnSQL=%s",[landnSQL])
                elif  phonesql != "":
                    cur.execute("SELECT * FROM shareS WHERE phonesql=%s",[phonesql])
                elif  pricesql != "":
                    cur.execute("SELECT * FROM shareS WHERE pricesql=%s",[pricesql])
                elif  bidsql != "":
                    cur.execute("SELECT * FROM shareS WHERE bidsql=%s",[bidsql])
                elif  city != "":
                    cur.execute("SELECT * FROM shareS WHERE city=%s",[city])

                               
            rows=cur.fetchall()
            
            if  not rows :
                result = tkinter.messagebox.showinfo('خطا في البحث', 'لا توجد نتيجة لبحثك')
           
            return rows
                                                                                  
    except Error as e:
            result = tkinter.messagebox.showinfo('لا يوجد اتصال بالانترنت' , e)
            

