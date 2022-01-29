import sqlite3

import tkinter.messagebox



def LandData():
    con = sqlite3.connect("resources/LandMan.db")
    cur = con.cursor() 
    cur.execute("CREATE TABLE IF NOT EXISTS LandMan (ids INTEGER PRIMARY KEY,nighber  TEXT NOT NULL,Land_typ TEXT,land_num TEXT NOT NULL,land_bluk TEXT NOT NULL,streetS TEXT,streetW TEXT,streetN TEXT,streetE TEXT,tall TEXT,bid TEXT,price TEXT,office TEXT,phone INTEGER, extra_f TEXT ,UNIQUE (nighber,land_num,land_bluk));")
    cur.execute("CREATE TABLE IF NOT EXISTS rentMan (idrent INTEGER PRIMARY KEY,nighrent TEXT,typerent TEXT,landnrent TEXT,landbrent TEXT,streetrentS TEXT,streetrentW TEXT,streetrentN TEXT,streetrentE TEXT,spacerent TEXT,pricerent TEXT,paymentrent TEXT,ownerrent TEXT,phonerent TEXT, conditionrent TEXT, extrarent TEXT);")
    cur.execute("CREATE TABLE IF NOT EXISTS Al3qar (id3qarr INTEGER PRIMARY KEY,nigh3qar TEXT,type3qarr TEXT,num3qar TEXT,bluk3qar TEXT,street3qar TEXT,street3qar2 TEXT,street3qar3 TEXT,where3qar TEXT,taal3qar TEXT,price3qar TEXT,bid3qar TEXT,phone3qar TEXT, office3qar TEXT, extra3qar TEXT);")                                                                         
    
    cur.execute("CREATE TABLE IF NOT EXISTS NOTE (idnote INTEGER PRIMARY KEY,subjecT TEXT,phonN TEXT,etcN TEXT);")                                                                         
    
    cur.execute("CREATE TABLE IF NOT EXISTS Orders (idOrders INTEGER PRIMARY KEY,nighorders  TEXT,landborders TEXT,streetorderS TEXT,streetorderW TEXT,streetorderN TEXT,streetorderE TEXT,typeorders  TEXT,spaceorders  TEXT,ownerorders  TEXT,phoneorders  TEXT,conditionorders  TEXT,priceorders  TEXT,extraorders TEXT);")
    con.commit()
    con.close()
#### ADD
def insert_note(subjecT,phonN,etcN):
    
    con = sqlite3.connect("resources/LandMan.db")
    cur = con.cursor()
    cur.execute("INSERT INTO NOTE VALUES(?,?,?,?)",[None,subjecT,phonN,etcN])
    con.commit()
    con.close()
def insert_rent(nighrent,typerent,landnrent,landbrent,streetrentS,streetrentW,streetrentN,streetrentE,spacerent,pricerent,paymentrent,ownerrent,phonerent,conditionrent, extrarent):
    
    con = sqlite3.connect("resources/LandMan.db")
    cur = con.cursor()
    cur.execute("INSERT INTO rentMan VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",[None,nighrent,typerent,landnrent,landbrent,streetrentS,streetrentW,streetrentN,streetrentE,spacerent,pricerent,paymentrent,ownerrent,phonerent,conditionrent,extrarent])
    con.commit()
    con.close()

def insert_data(nighber,Land_typ,land_num,land_bluk,streetS,streetW,streetN,streetE,tall,bid,price,office,phone, extra_f):
    try:
        
        con = sqlite3.connect("resources/LandMan.db")
        cur = con.cursor()
        cur.execute("INSERT INTO LandMan VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",[None,nighber,Land_typ,land_num,land_bluk,streetS,streetW,streetN,streetE,tall,bid,price,office,phone, extra_f])
        con.commit()
        con.close()
    except:
        result = tkinter.messagebox.showinfo('لم تتم اضافة الارض ', 'الارض موجودة مسبقا')
def insert_orders(nighorders, landborders , streetorderS ,streetorderW ,streetorderN ,streetorderE , typeorders ,spaceorders ,ownerorders , phoneorders ,conditionorders,priceorders, extraorders):
    
    con = sqlite3.connect("resources/LandMan.db")
    cur = con.cursor()
    cur.execute("INSERT INTO Orders VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",[None,nighorders, landborders ,streetorderS ,streetorderW ,streetorderN ,streetorderE  , typeorders ,spaceorders ,ownerorders , phoneorders ,conditionorders,priceorders, extraorders])
    con.commit()
    con.close()

# 3qar
def insert_3qar(nigh3qar,type3qarr,num3qar,bluk3qar,street3qar,street3qar2,street3qar3,where3qar,taal3qar,price3qar,bid3qar,phone3qar, office3qar,extra3qar):
    try:
        
        con = sqlite3.connect("resources/LandMan.db")
        cur = con.cursor() 
        cur.execute("INSERT INTO Al3qar VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",[None,nigh3qar,type3qarr,num3qar,bluk3qar,street3qar,street3qar2,street3qar3,where3qar,taal3qar,price3qar,bid3qar,phone3qar, office3qar,extra3qar])
        con.commit()
        con.close()
    except:
        result = tkinter.messagebox.showinfo('لم تتم اضافة الارض ', 'الارض موجودة مسبقا')
        
#### VIEW 
def viewnote():
    con = sqlite3.connect("resources/LandMan.db")
    
    cur = con.cursor()
    cur.execute("SELECT * FROM NOTE")
    rows=cur.fetchall()
    
    con.close()
    return rows
    
def viewrent():
    con = sqlite3.connect("resources/LandMan.db")
    
    cur = con.cursor()
    cur.execute("SELECT * FROM rentMan")
    rows=cur.fetchall()
    
    con.close()
    return rows
    
def viewData():
    con = sqlite3.connect("resources/LandMan.db")
    
    cur = con.cursor()
    cur.execute("SELECT * FROM LandMan")
    rows=cur.fetchall()
    
    con.close()
    return rows
def vieworders():
    con = sqlite3.connect("resources/LandMan.db")
    
    cur = con.cursor()
    cur.execute("SELECT * FROM Orders")
    rows=cur.fetchall()
    
    con.close()
    return rows
#view aqar
def Al3qarViewwData():
    con = sqlite3.connect("resources/LandMan.db")
    
    cur = con.cursor()
    cur.execute("SELECT * FROM Al3qar")
    rows=cur.fetchall()
    
    con.close()
    return rows


# UPDATA out of service
#DELETE

def delete_note(idnote):
    con = sqlite3.connect("resources/LandMan.db")
    cur = con.cursor()
    cur.execute("DELETE FROM NOTE where idnote= ?",(idnote,))
    
    con.commit()
    con.close()
def delete_data(ids):
    con = sqlite3.connect("resources/LandMan.db")
    cur = con.cursor()
    cur.execute("DELETE FROM LandMan where ids= ?",(ids,))
    
    con.commit()
    con.close()
def delete_rent(idrent):
    con = sqlite3.connect("resources/LandMan.db")
    cur = con.cursor()
    cur.execute("DELETE FROM rentMan where idrent= ?",(idrent,))
    
    con.commit()
    con.close()
   # Orders
def delete_orders(idOrders):
    con = sqlite3.connect("resources/LandMan.db")
    cur = con.cursor()
    cur.execute("DELETE FROM Orders where idOrders= ?",(idOrders,))
    
    con.commit()
    con.close()    
def delete_3qar(id3qarr):
    con = sqlite3.connect("resources/LandMan.db")
    cur = con.cursor()
    cur.execute("DELETE FROM Al3qar where id3qarr= ?",(id3qarr,))
    
    con.commit()
    con.close()
    
#SEARCH
def SearchData(nighber="",Land_typ="",land_num="",land_bluk="",streetS="",streetW="",streetN="",streetE="",tall="",bid="",price="",office="",phone="", extra_f="",ids=""):
    con = sqlite3.connect("resources/LandMan.db")
    cur = con.cursor()
    # nigh
    if nighber != "" and Land_typ != "" and land_num !="" and land_bluk !="" and tall!="":
        cur.execute("SELECT * FROM LandMan WHERE nighber=?  AND Land_typ=? AND land_num=? AND land_bluk=? AND  tall=? ",\
                [nighber,Land_typ,land_num,land_bluk,tall])
    ### 444 ###    
    elif nighber != "" and Land_typ != "" and land_num !="" and land_bluk !="" :
        cur.execute("SELECT * FROM LandMan WHERE nighber=?  AND Land_typ=? AND land_num=? AND land_bluk=? ",\
                [nighber,Land_typ,land_num,land_bluk])
    elif nighber != "" and Land_typ != "" and tall !="" and land_bluk !="" :
        cur.execute("SELECT * FROM LandMan WHERE nighber=?  AND Land_typ=? AND tall=? AND land_bluk=? ",\
                [nighber,Land_typ,tall,land_bluk])
    ### 33333 ####    
    elif nighber != "" and Land_typ != "" and land_num !=""  :
        cur.execute("SELECT * FROM LandMan WHERE nighber=?  AND Land_typ=? AND land_num=?",\
                [nighber,Land_typ,land_num])
        
    elif nighber != "" and Land_typ != "" and land_bluk !=""  :
        cur.execute("SELECT * FROM LandMan WHERE nighber=?  AND Land_typ=? AND land_bluk=?",\
                [nighber,Land_typ,land_bluk]) 
    elif nighber != "" and Land_typ != "" and tall !=""  :
        cur.execute("SELECT * FROM LandMan WHERE nighber=?  AND Land_typ=? AND tall=?",\
                [nighber,Land_typ,tall]) 


    ### 2222 ####      
    elif nighber != "" and Land_typ != ""  :
        cur.execute("SELECT * FROM LandMan WHERE nighber=?  AND Land_typ=? ",\
                [nighber,Land_typ])

    elif nighber != "" and land_bluk != ""  :
        cur.execute("SELECT * FROM LandMan WHERE nighber=?  AND land_bluk=? ",\
                [nighber,land_bluk])
    elif nighber != "" and land_num != ""  :
        cur.execute("SELECT * FROM LandMan WHERE nighber=?  AND land_num=? ",\
                [nighber,land_num])
    elif nighber != "" and tall != ""  :
        cur.execute("SELECT * FROM LandMan WHERE nighber=?  AND tall=? ",\
                [nighber,tall])
    
    else:### 111 ###
        if nighber != "":
            cur.execute("SELECT * FROM LandMan WHERE nighber=?",[nighber])
        elif  Land_typ != "":
            cur.execute("SELECT * FROM LandMan WHERE Land_typ=?",[Land_typ])
        elif  land_num != "":
            cur.execute("SELECT * FROM LandMan WHERE land_num=?",[land_num])
        elif  land_bluk != "":
            cur.execute("SELECT * FROM LandMan WHERE land_bluk=?",[land_bluk])
        
        elif  tall != "":
            cur.execute("SELECT * FROM LandMan WHERE tall=?",[tall])
        elif  bid != "":
            cur.execute("SELECT * FROM LandMan WHERE bid=?",[bid])
        elif  price != "":
            cur.execute("SELECT * FROM LandMan WHERE price=?",[price])
        elif  office != "":
            cur.execute("SELECT * FROM LandMan WHERE office=?",[office])
        elif  phone != "":
            cur.execute("SELECT * FROM LandMan WHERE phone=?",[phone])
        elif  extra_f != "":
            cur.execute("SELECT * FROM LandMan WHERE extra_f=?",[extra_f])
        elif  streetS != "":
            cur.execute("SELECT * FROM LandMan WHERE streetS=?",[streetS])
        elif  streetN != "":
            cur.execute("SELECT * FROM LandMan WHERE streetN=?",[streetN])
        elif  streetW != "":
            cur.execute("SELECT * FROM LandMan WHERE streetW=?",[streetW])
        elif  streetE != "":
            cur.execute("SELECT * FROM LandMan WHERE streetE=?",[streetE])
    
    rows=cur.fetchall()
    if  not rows :
        result = tkinter.messagebox.showinfo('خطا في البحث', 'لا توجد نتيجة لبحثك')
    con.commit()
    con.close()
    return rows
## rere                                                                                                                    
def searchRe(nighrent="",typerent="",landnrent="",landbrent="",streetrentS="",streetrentW="",streetrentN="",streetrentE="",spacerent="",pricerent="",paymentrent="",ownerrent="",phonerent="",conditionrent="", extrarent="",idrent=""):
    con = sqlite3.connect("resources/LandMan.db")
    cur = con.cursor()
        
    # 555 #
    if nighrent != "" and typerent != "" and conditionrent !="" and landbrent !="" and spacerent !="":
            cur.execute("SELECT * FROM rentMan WHERE nighrent=? and typerent=? and landnrent =? and landbrent =? and spacerent =?",\
                         [nighrent,typerent,conditionrent,landbrent,spacerent])     
    # 444 #
    elif nighrent != "" and typerent != "" and landbrent !="" and landnrent !="":
            cur.execute("SELECT * FROM rentMan WHERE nighrent=? and typerent=? and landbrent =? and landnrent =?",\
                         [nighrent,typerent,landbrent,landnrent])
    elif nighrent != "" and typerent != "" and landbrent !="" and conditionrent !="":
            cur.execute("SELECT * FROM rentMan WHERE nighrent=? and typerent=? and landbrent =? and conditionrent =?",\
                         [nighrent,typerent,landbrent,conditionrent])
    # 333 #        
    elif nighrent != "" and typerent != "" and landbrent !="":
            cur.execute("SELECT * FROM rentMan WHERE nighrent=? and typerent=? and landbrent =?",\
                         [nighrent,typerent,landbrent])
            
    elif nighrent != "" and typerent != "" and conditionrent !="":
            cur.execute("SELECT * FROM rentMan WHERE nighrent=? and typerent=? and conditionrent =?",\
                         [nighrent,typerent,conditionrent])
    # 222 @        
    elif nighrent != "" and typerent != "":
            cur.execute("SELECT * FROM rentMan WHERE nighrent=? and typerent=?",\
                         [nighrent,typerent])
    elif nighrent != "" and conditionrent != "":
            cur.execute("SELECT * FROM rentMan WHERE nighrent=? and conditionrent=?",\
                         [nighrent,conditionrent])
    else:### 111 ###

        if nighrent != "":
            cur.execute("SELECT * FROM rentMan WHERE nighrent=?",[nighrent])
        elif  typerent != "":
            cur.execute("SELECT * FROM rentMan WHERE typerent=?",[typerent])
        elif  landnrent != "":
            cur.execute("SELECT * FROM rentMan WHERE landnrent=?",[landnrent])
        elif  landbrent != "":
            cur.execute("SELECT * FROM rentMan WHERE landbrent=?",[landbrent])
        
        elif  streetrentS != "":
            cur.execute("SELECT * FROM rentMan WHERE streetrentS=?",[streetrentS])
        elif  streetrentW != "":
            cur.execute("SELECT * FROM rentMan WHERE streetrentW=?",[streetrentW])
        elif  streetrentN != "":
            cur.execute("SELECT * FROM rentMan WHERE streetrentN=?",[streetrentN])
        elif  streetrentE != "":
            cur.execute("SELECT * FROM rentMan WHERE streetrentE=?",[streetrentE])
        elif  spacerent != "":
            cur.execute("SELECT * FROM rentMan WHERE spacerent=?",[spacerent])
        elif  pricerent != "":
            cur.execute("SELECT * FROM rentMan WHERE pricerent=?",[pricerent])
        elif  paymentrent != "":
            cur.execute("SELECT * FROM rentMan WHERE paymentrent=?",[paymentrent])
        elif  ownerrent != "":
            cur.execute("SELECT * FROM rentMan WHERE ownerrent=?",[ownerrent])
        elif  phonerent != "":
            cur.execute("SELECT * FROM rentMan WHERE phonerent=?",[phonerent])
        elif  conditionrent != "":
            cur.execute("SELECT * FROM rentMan WHERE conditionrent=?",[conditionrent])
        elif  extrarent != "":
            cur.execute("SELECT * FROM rentMan WHERE extrarent=?",[extrarent])


             
    rows=cur.fetchall()
    if  not rows :
        result = tkinter.messagebox.showinfo('خطا في البحث', 'لا توجد نتيجة لبحثك')
    con.commit()
    con.close()
    return rows

def search3q(nigh3qar="",type3qarr="",num3qar="",bluk3qar="",street3qar="",street3qar2="",street3qar3="",where3qar="",taal3qar="",price3qar="",bid3qar="",phone3qar="", office3qar="",extra3qar=""):
    con = sqlite3.connect("resources/LandMan.db")
    cur = con.cursor()
        # 555 #
    if nigh3qar != "" and type3qarr != "" and num3qar !="" and bluk3qar !="" and taal3qar !="":
            cur.execute("SELECT * FROM Al3qar WHERE nigh3qar=? and type3qarr=? and num3qar =? and bluk3qar =? and taal3qar =?",\
                         [nigh3qar,type3qarr,num3qar,bluk3qar,taal3qar])     
    # 444 #
    elif nigh3qar != "" and type3qarr != "" and bluk3qar !="" and taal3qar !="":
            cur.execute("SELECT * FROM Al3qar WHERE nigh3qar=? and type3qarr=? and bluk3qar =? and taal3qar =?",\
                         [nigh3qar,type3qarr,bluk3qar,taal3qar])

    # 333 #        
    elif nigh3qar != "" and type3qarr != "" and bluk3qar !="":
            cur.execute("SELECT * FROM Al3qar WHERE nigh3qar=? and type3qarr=? and bluk3qar =?",\
                         [nigh3qar,type3qarr,bluk3qar])
            
    elif taal3qar != "" and nigh3qar != "" and bluk3qar !="":
            cur.execute("SELECT * FROM Al3qar WHERE taal3qar=? and nigh3qar=? and bluk3qar =?",\
                         [taal3qar,nigh3qar,bluk3qar])
    # 222 @        
    elif nigh3qar != "" and bluk3qar != "":
            cur.execute("SELECT * FROM Al3qar WHERE nigh3qar=? and bluk3qar=?",\
                         [nigh3qar,bluk3qar])
    elif nigh3qar != "" and type3qarr != "":
            cur.execute("SELECT * FROM Al3qar WHERE nigh3qar=? and type3qarr=?",\
                         [nigh3qar,type3qarr])
    else:### 111 ###

        if nigh3qar != "":
            cur.execute("SELECT * FROM Al3qar WHERE nigh3qar=?",[nigh3qar])
        elif  type3qarr != "":
            cur.execute("SELECT * FROM Al3qar WHERE type3qarr=?",[type3qarr])
        elif  num3qar != "":
            cur.execute("SELECT * FROM Al3qar WHERE num3qar=?",[num3qar])
        elif  bluk3qar != "":
            cur.execute("SELECT * FROM Al3qar WHERE bluk3qar=?",[bluk3qar])
     
        elif  street3qar != "":
            cur.execute("SELECT * FROM Al3qar WHERE street3qar=?",[street3qar])
        elif  street3qar2 != "":
            cur.execute("SELECT * FROM Al3qar WHERE street3qar2=?",[street3qar2])
        elif  street3qar3 != "":
            cur.execute("SELECT * FROM Al3qar WHERE street3qar3=?",[street3qar3])
        elif  where3qar != "":
            cur.execute("SELECT * FROM Al3qar WHERE where3qar=?",[where3qar])
        elif  taal3qar != "":
            cur.execute("SELECT * FROM Al3qar WHERE taal3qar=?",[taal3qar])
        elif  price3qar != "":
            cur.execute("SELECT * FROM Al3qar WHERE price3qar=?",[price3qar])
        elif  bid3qar != "":
            cur.execute("SELECT * FROM Al3qar WHERE bid3qar=?",[bid3qar])
        elif  phone3qar != "":
            cur.execute("SELECT * FROM Al3qar WHERE phone3qar=?",[phone3qar])
        elif  office3qar != "":
            cur.execute("SELECT * FROM Al3qar WHERE office3qar=?",[office3qar])
        elif  extra3qar != "":
            cur.execute("SELECT * FROM Al3qar WHERE extra3qar=?",[extra3qar])

             
    rows=cur.fetchall()
    if  not rows :
        result = tkinter.messagebox.showinfo('خطا في البحث', 'لا توجد نتيجة لبحثك')
    con.commit()
    con.close()
    return rows
def searchOr(nighorders="",landborders="",streetorderS="",streetorderW="",streetorderN="",streetorderE="",typeorders="",spaceorders="",ownerorders="",phoneorders="",conditionorders="",priceorders="",extraorders=""):
    con = sqlite3.connect("resources/LandMan.db")
    cur = con.cursor()
    if nighorders != "" and landborders  != "" and typeorders  != "" and  spaceorders != "" and conditionorders != "":
            cur.execute("SELECT * FROM Orders WHERE nighorders=? and landborders=? and typeorders=? and spaceorders=? and conditionorders=?",\
                        [nighorders,landborders,typeorders,spaceorders,conditionorders])
    # 444 #
    elif nighorders != "" and landborders  != "" and typeorders  != "" and  spaceorders != "":
            cur.execute("SELECT * FROM Orders WHERE nighorders=? and landborders=? and typeorders=? and spaceorders=?",\
                         [nighorders,landborders,typeorders,spaceorders])
    elif nighorders != "" and landborders  != "" and typeorders  != "" and  conditionorders != "":
            cur.execute("SELECT * FROM Orders WHERE nighorders=? and landborders=? and typeorders=? and conditionorders=?",\
                         [nighorders,landborders,typeorders,conditionorders])
    # 333 #
    elif nighorders != ""  and typeorders  != "" and  conditionorders != "":
            cur.execute("SELECT * FROM Orders WHERE nighorders=? and typeorders=? and conditionorders=?",\
                         [nighorders,typeorders,conditionorders])
    elif nighorders != ""  and typeorders  != "" and  spaceorders != "":
            cur.execute("SELECT * FROM Orders WHERE nighorders=? and typeorders=? and spaceorders=?",\
                         [nighorders,typeorders,spaceorders])
    elif nighorders != ""  and typeorders  != "" and  landborders != "":
            cur.execute("SELECT * FROM Orders WHERE nighorders=? and typeorders=? and landborders=?",\
                         [nighorders,typeorders,landborders])
    # 222 #
    elif nighorders != ""  and typeorders  != "":
            cur.execute("SELECT * FROM Orders WHERE nighorders=? and typeorders=?",\
                         [nighorders,typeorders])
    elif nighorders != ""  and landborders  != "":
            cur.execute("SELECT * FROM Orders WHERE nighorders=? and landborders=?",\
                         [nighorders,landborders])
    elif nighorders != ""  and conditionorders  != "":
            cur.execute("SELECT * FROM Orders WHERE nighorders=? and conditionorders=?",\
                         [nighorders,conditionorders])
    elif typeorders != ""  and spaceorders  != "":
            cur.execute("SELECT * FROM Orders WHERE typeorders=? and spaceorders=?",\
                         [typeorders,spaceorders])
    else:### 111 ###

        if nighorders != "":
            cur.execute("SELECT * FROM Orders WHERE nighorders=?",[nighorders])
        elif  landborders != "":
            cur.execute("SELECT * FROM Orders WHERE landborders=?",[landborders])
        elif  streetorderS != "":
            cur.execute("SELECT * FROM Orders WHERE streetorderS=?",[streetorderS])
        elif  streetorderW != "":
            cur.execute("SELECT * FROM Orders WHERE streetorderW=?",[streetorderW])
        
        elif  streetorderN != "":
            cur.execute("SELECT * FROM Orders WHERE streetorderN=?",[streetorderN])
        elif  streetorderE != "":
            cur.execute("SELECT * FROM Orders WHERE streetorderE=?",[streetorderE])
        elif  typeorders != "":
            cur.execute("SELECT * FROM Orders WHERE typeorders=?",[typeorders])
        elif  spaceorders != "":
            cur.execute("SELECT * FROM Orders WHERE spaceorders=?",[spaceorders])
        elif  ownerorders != "":
            cur.execute("SELECT * FROM Orders WHERE ownerorders=?",[ownerorders])
        elif  phoneorders != "":
            cur.execute("SELECT * FROM Orders WHERE phoneorders=?",[phoneorders])
        elif  conditionorders != "":
            cur.execute("SELECT * FROM Orders WHERE conditionorders=?",[conditionorders])
        elif  priceorders != "":
            cur.execute("SELECT * FROM Orders WHERE priceorders=?",[priceorders])
        elif  extraorders != "":
            cur.execute("SELECT * FROM Orders WHERE extraorders=?",[extraorders])

             
    rows=cur.fetchall()
    if  not rows :
        result = tkinter.messagebox.showinfo('خطا في البحث', 'لا توجد نتيجة لبحثك')
    con.commit()
    con.close()
    return rows

def searchnote(subjecT="",phonN="",etcN=""):
    con = sqlite3.connect("resources/LandMan.db")
    cur = con.cursor()
    if subjecT != "" and phonN != "" :
            cur.execute("SELECT * FROM NOTE WHERE subjecT=? and phonN=?",\
                         [subjecT,phonN])
    elif subjecT != "":
            cur.execute("SELECT * FROM NOTE WHERE subjecT=?",\
                         [subjecT])
    elif phonN != "":
            cur.execute("SELECT * FROM NOTE WHERE phonN=?",\
                         [phonN])
    elif etcN != "":
            cur.execute("SELECT * FROM NOTE WHERE etcN=?",\
                         [etcN])
             
    rows=cur.fetchall()
    if  not rows :
        result = tkinter.messagebox.showinfo('خطا في البحث', 'لا توجد نتيجة لبحثك')
    con.commit()
    con.close()
    return rows
  

