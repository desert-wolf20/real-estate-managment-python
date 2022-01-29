from licensing.models import *
from licensing.methods import Key, Helpers
from tkinter import *
import tkinter.messagebox
import databasefile
import databasesconn
from tkinter import ttk
import tkinter as tk
from tkinter.font import BOLD
import sys
import time
import os ,socket
from tkinter import simpledialog
from datetime import *


class Land:

    def __init__(self,root):
        
        if os.stat("resources/n65748382991.skm").st_size == 0:
            root.withdraw()
            USER_name = simpledialog.askstring(title="تعبئة معلوماتك هنا",
                                  prompt="اكتب اسم مكتبك الكامل هنا لعرضة في شاشة البرنامج ")
            with open('resources/n65748382991.skm', "w", encoding="utf-8") as f:
                f.write(USER_name)
                f.close()

        else:
            pass

        self.root = root
        self.root.title("عقاري برنامج ادارة مكاتب العقار")
        self.root.geometry("1550x7500+0+0")
        self.root.config(bg="#808080")
        self.root.state('zoomed')
        self.root.iconbitmap("resources/a.ico")

        #################################      MMMEEENNNUUU      #######################################
        # 1
        self.menubar = Menu(self.root) 
        self.menubar.add_command(label="تواصل معنــا !"  ,command=lambda: tkinter.messagebox.showinfo("التواصل مع المبرمج",' للاقتراحات و الطلبات يرجئ التواصل علئ \n هشام العطني \n 0534506914 واتساب \n HISHAMALATNI@Gmail.Com \n شرح البرنامج موجود على موقعنا الالكتروني \n WWW.5Dimsa.COM'))
        # 2
        filemenu = Menu(self.menubar, tearoff=0)

        # show
        self.root.config(menu=self.menubar)  
        ################################ END ###################################################
        ################################ VAR ###################################################
        #tap6
        nighSQL = StringVar()
        landnSQL = StringVar()
        landbSQL = StringVar() 
        northSQL = StringVar() 
        southSQL = StringVar() 
        eastSQL = StringVar()
        westSQL = StringVar()
        spacesql = StringVar()
        ownersql = StringVar()
        phonesql = StringVar() 
        pricesql = StringVar() 
        extrasql = StringVar() 
        typesql = StringVar()
        bidsql = StringVar()
        conditionsql = StringVar()
        city = StringVar()
        
        

        #tapland
        nighber = StringVar()
        Land_typ = StringVar()
        land_num = StringVar() 
        land_bluk = StringVar() 
        streetS = StringVar() 
        streetW = StringVar()
        streetN = StringVar()
        streetE = StringVar()
        tall = StringVar()
        bid = StringVar()
        price = StringVar() 
        office = StringVar()
        phone = StringVar()
        extra_f = StringVar()
        #3qar Var
        nigh3qar = StringVar()
        type3qarr = StringVar()
        num3qar = StringVar()
        bluk3qar = StringVar()
        street3qar = StringVar()
        street3qar2 = StringVar()
        where3qar = StringVar()
        street3qar3 = StringVar()
        taal3qar = StringVar()
        price3qar   = StringVar() 
        bid3qar   = StringVar() 
        phone3qar = StringVar()
        office3qar = StringVar()
        extra3qar = StringVar()
        #rent VAR
        nighrent = StringVar()
        typerent = StringVar()
        landnrent = StringVar()
        landbrent = StringVar()
        streetrentS = StringVar()
        streetrentW = StringVar()
        streetrentN = StringVar()
        streetrentE = StringVar()
        spacerent = StringVar()
        pricerent = StringVar()
        paymentrent = StringVar()
        ownerrent = StringVar()
        phonerent = StringVar()
        conditionrent = StringVar()
        extrarent = StringVar()

        #orders VAR
        nighorders = StringVar()
        landborders = StringVar()
#ADD
        streetorderS = StringVar()
        streetorderW = StringVar()
        streetorderN = StringVar()
        streetorderE = StringVar()
#END
        typeorders = StringVar()
        spaceorders = StringVar()
        ownerorders = StringVar()
        phoneorders = StringVar()
        conditionorders = StringVar()
        priceorders = StringVar()
        extraorders = StringVar()

        #note
        passW = StringVar()
        phonN = StringVar()
        subjecT = StringVar()
        etcN = StringVar()
        
        ################################## END #################################################
        ############################## FUNCTIONS ###############################################
        
        def iExit():
            iExit= tkinter.messagebox.askyesno("بحفظ الله","هل ترغب بالخروج" )
            if iExit > 0:
                root.destroy()
                return   
            
        ### clear Data ###
        def clearnote():

            self.txtphonN.delete(0,END)
            self.txtsubject.delete(0,END)
            inputtxt.delete('1.0', END)
           
        def clearorders():

            self.txtnighorders.delete(0,END)
            self.txtlandborders.delete(0,END)
##added
            self.txtstreetorderS.delete(0,END)
            self.txtstreetorderW.delete(0,END)
            self.txtstreetorderN.delete(0,END)
            self.txtstreetorderE.delete(0,END)
        
            self.txtspaceorders.delete(0,END)
            self.txtownerorders.delete(0,END)
            self.txttaal3qar.delete(0,END)
            self.txtphoneorders.delete(0,END)
            pyor.set('')
            self.txtpriceorders.delete(0,END)
            self.txtextraorders.delete(0,END)
            typeorders.set('')

            
        def clearland():
            self.txtphone.delete(0,END)
            self.txtbid.delete(0,END)
            self.txtland_bluk.delete(0,END)
            self.txtland_num.delete(0,END)
            self.txtnighber.delete(0,END)
            self.txttall.delete(0,END)
            self.txtstreetS.delete(0,END)
            self.txtstreetW.delete(0,END)
            self.txtstreetN.delete(0,END)
            self.txtstreetE.delete(0,END)
            self.txtoffice.delete(0,END)
            self.txtprice.delete(0,END)
            self.txtextra_f.delete(0,END)
            Land_typ.set('')
            
        def clearRent():

            self.txtnighrent.delete(0,END)
            self.txtlandnrent.delete(0,END)
            self.txtstreetrentS.delete(0,END)
            self.txtstreetrentW.delete(0,END)
            self.txtstreetrentN.delete(0,END)
            self.txtstreetrentE.delete(0,END)
            self.txtspacerent.delete(0,END)
            self.txtpricerent.delete(0,END)
            self.txtpaymentrent.delete(0,END)
            self.txtownerrent.delete(0,END)
            self.txtphonerent.delete(0,END)
            self.txtextrarent.delete(0,END)
            self.txtlandbrent.delete(0,END)
            conditionre.set('')
            typerent.set('')

            
        def clear3qar():

            self.txtphone3qar.delete(0,END)
            self.txtbid3qar.delete(0,END)
            self.txtbluk3qar.delete(0,END)
            self.txtnum3qar.delete(0,END)
            self.txtnigh3qar.delete(0,END)
            self.txttaal3qar.delete(0,END)
            self.txtwhere3qar.delete(0,END)
            self.txtstreet3qar.delete(0,END)
            self.txtstreet3qar2.delete(0,END)
            self.txtstreet3qar3.delete(0,END)
            self.txtprice3qar.delete(0,END)
            self.txtextra3qar.delete(0,END)
            self.txtoffice3qar.delete(0,END)
            type3qarr.set('')
            
        def clearSQL():
            self.txtcitySQL.delete(0,END)
            self.txtnighrent.delete(0,END)
            self.txtnighSQL.delete(0,END)
            self.txtlandnSQL.delete(0,END)
            self.txtlandbSQL.delete(0,END)
            self.txtnorthSQL.delete(0,END)
            self.txtsouthSQL.delete(0,END)
            self.txteastSQL.delete(0,END)
            self.txtwestSQL.delete(0,END)
            self.txtspaceSQL.delete(0,END)
            self.txtownersql.delete(0,END)
            self.txtphonesql.delete(0,END)
            self.txtpricesql.delete(0,END)
            self.txtbidsql.delete(0,END)
            self.txtextrasql.delete(0,END)
            tyor6.set('')
            pyor6.set('')
            
        # ADD #
        def addrent():
            if(len(nighrent.get())!=0):
                databasefile.insert_rent(nighrent.get(),typerent.get(),landnrent.get(),landbrent.get(),streetrentS.get(),streetrentW.get(),streetrentN.get(),streetrentE.get(),spacerent.get(),pricerent.get(),paymentrent.get(),ownerrent.get(),phonerent.get(),conditionrent.get(),extrarent.get())
                recourd1.delete(*recourd1.get_children())
                ### need orgonize ###
                recourd1.insert('',END,values=(extrarent.get(),conditionrent.get(),ownerrent.get(),paymentrent.get(),phonerent.get(),pricerent.get(),spacerent.get(),streetrentE.get(),streetrentN.get(),streetrentW.get(),streetrentS.get(),landbrent.get(),landnrent.get(),typerent.get(),nighrent.get()))
                rentDisplay()

        #note
        def addnote():  
            if(len(subjecT.get())!=0):
                etcN = inputtxt.get("1.0",END)
                databasefile.insert_note(subjecT.get(),phonN.get(),etcN)
                recourd5.delete(*recourd5.get_children())
                
                recourd5.insert('',END,values=(etcN,phonN.get(),subjecT.get()))
                Displaynote()
        # ADD share #
        def addSQL():
            if(len(typesql.get())!=0):
                databasesconn.addShare(city.get(),typesql.get(),conditionsql.get(),nighSQL.get(),landnSQL.get(),landbSQL.get(),\
                                         northSQL.get(),southSQL.get(),eastSQL.get(),westSQL.get(),spacesql.get() ,ownersql.get(),\
                                         phonesql.get(),pricesql.get(),bidsql.get(),extrasql.get())
                recourd6.delete(*recourd6.get_children()) 
                recourd6.insert('',END,values=(extrasql.get(),bidsql.get(),pricesql.get(),phonesql.get(),\
                                                ownersql.get(),spacesql.get(),westSQL.get(),eastSQL.get(),\
                                                 southSQL.get(),northSQL.get(),landbSQL.get(),landnSQL.get(),nighSQL.get(),conditionsql.get(),typesql.get(),city.get()))          
                SQLDisplay()
        # 3qar
        def add3qar():
            if(len(nigh3qar.get())!=0):
                databasefile.insert_3qar(nigh3qar.get(), type3qarr.get(),num3qar.get(), bluk3qar.get(), street3qar.get(), street3qar2.get(),street3qar3.get(), where3qar.get(), taal3qar.get(),price3qar.get(),bid3qar.get(),phone3qar.get(),office3qar.get(), extra3qar.get() )
                recourd3.delete(*recourd3.get_children()) 
                recourd3.insert('',END,values=(extra3qar.get(), office3qar.get(), phone3qar.get(), bid3qar.get(), price3qar.get(), taal3qar.get(), where3qar.get(),street3qar3.get(), street3qar2.get(), street3qar.get(), bluk3qar.get(), num3qar.get(), type3qarr.get(), nigh3qar.get()))   
        
        def addData():
            if(len(nighber.get())!=0):
                databasefile.insert_data(nighber.get(),Land_typ.get(),land_num.get(),land_bluk.get(),streetS.get(),streetW.get(),streetN.get(),streetE.get(),tall.get(),bid.get(),price.get(),office.get(),phone.get(), extra_f.get())
                recourd.delete(*recourd.get_children())
                
                recourd.insert('',END,values=( extra_f.get(),phone.get(),office.get(),price.get(),bid.get(),tall.get(),streetE.get(),streetN.get(),streetW.get(),streetS.get(),land_bluk.get(),land_num.get(),Land_typ.get(),nighber.get()))
        def addorders():
            if(len(nighorders.get())!=0):
                databasefile.insert_orders(nighorders.get(), landborders.get() , streetorderS.get() ,streetorderW.get() ,streetorderN.get() ,streetorderE.get() ,typeorders.get() ,spaceorders.get() ,ownerorders.get() ,  phoneorders.get() ,conditionorders.get(),priceorders.get(), extraorders.get())
                recourd4.delete(*recourd4.get_children())

                
                recourd4.insert('',END,values=(extraorders.get(), priceorders.get(),conditionorders.get(), phoneorders.get(), ownerorders.get(), spaceorders.get(), typeorders.get(),streetorderE.get() ,streetorderN.get() ,streetorderW.get() ,streetorderS.get(), landborders.get(), nighorders.get()))
        # DISPLAY #
        def ordersDisplay():

            recourd4.delete(*recourd4.get_children())
            for rows in databasefile.vieworders():
                recourd4.insert('',END,values=(rows[13],rows[12],rows[11], rows[10],rows[9], rows[8], rows[7],rows[6], rows[5], rows[4],rows[3], rows[2], rows[1],rows[0]))
                
        def rentDisplay():

            recourd1.delete(*recourd1.get_children())
            for rows in databasefile.viewrent():
                recourd1.insert('',END,values=(rows[15],rows[14],rows[13],rows[12], rows[11], rows[10],rows[9], rows[8], rows[7],rows[6], rows[5], rows[4],rows[3], rows[2], rows[1],rows[0]))  

        def Al3qartDisplay():

            recourd3.delete(*recourd3.get_children())
            for rows in databasefile.Al3qarViewwData():
                recourd3.insert('',END,values=(rows[14],rows[13],rows[12],rows[11],rows[10],rows[9],rows[8],rows[7],rows[6],rows[5],rows[4],rows[3],rows[2],rows[1],rows[0]))          
        def Display():

            recourd.delete(*recourd.get_children())
            for rows in databasefile.viewData():
                recourd.insert('',END,values=(rows[14],rows[13],rows[12],rows[11],rows[10],rows[9], rows[8], rows[7],rows[6], rows[5], rows[4],rows[3], rows[2], rows[1],rows[0]))  
        def Displaynote():

            recourd5.delete(*recourd5.get_children())
            for rows in databasefile.viewnote():
                recourd5.insert('',END,values=(rows[3],rows[2], rows[1],rows[0])) 
                
        def SQLDisplay():

            recourd6.delete(*recourd6.get_children())
            for rows in databasesconn.viewShare():
                recourd6.insert('',END,values=(rows[16],rows[15],rows[14],rows[13],rows[12], rows[11],rows[10],rows[9],rows[8],rows[7],rows[6],rows[5],rows[4],rows[3],rows[2],rows[1],rows[0]))  
                  
        # Land record #
        def SQLRec(ev):
            viewinfo6 = recourd6.focus()
            global rowm6
            learnData6 = recourd6.item(viewinfo6)
            rowm6 = learnData6['values']
            city.set(rowm6[15])
            typesql.set(rowm6[14])
            conditionsql.set(rowm6[13])
            nighSQL.set(rowm6[12])
            landnSQL.set(rowm6[11])
            landbSQL.set(rowm6[10])
            northSQL.set(rowm6[9])
            southSQL.set(rowm6[8])
            eastSQL.set(rowm6[7])
            westSQL.set(rowm6[6])
            spacesql.set(rowm6[5])
            ownersql.set(rowm6[4])
            phonesql.set(rowm6[3])
            pricesql.set(rowm6[2])
            bidsql.set(rowm6[1])
            extrasql.set(rowm6[0])
            
        
        def ordersRec(ev):
            viewinfo4 = recourd4.focus()
            global rowm4
            learnData4 = recourd4.item(viewinfo4)
            rowm4 = learnData4['values']
            
            nighorders.set(rowm4[12])
            landborders.set(rowm4[11])
            streetorderS.set(rowm4[10])
            streetorderW.set(rowm4[9])
            streetorderN.set(rowm4[8])
            streetorderE.set(rowm4[7])
            typeorders.set(rowm4[6])
            spaceorders.set(rowm4[5])
            ownerorders.set(rowm4[4])
            phoneorders.set(rowm4[3])
            conditionorders.set(rowm4[2])
            priceorders.set(rowm4[1])
            extraorders.set(rowm4[0])

        def noteRec(ev):
            viewinfo5 = recourd5.focus()
            global rowm5
            learnData5 = recourd5.item(viewinfo5)
            rowm5 = learnData5['values']
            
            
            subjecT.set(rowm5[2])
            phonN.set(rowm5[1])
            inputtxt.delete('1.0', END)
            inputtxt.insert("1.0",rowm5[0])
            
            
        def RentRec(ev):
            viewinfo1 = recourd1.focus()
            global rowm1
            learnData1 = recourd1.item(viewinfo1)
            rowm1 = learnData1['values']
            
            nighrent.set(rowm1[14])
            typerent.set(rowm1[13])
            landnrent.set(rowm1[12])
            landbrent.set(rowm1[11])
            streetrentS.set(rowm1[10])
            streetrentW.set(rowm1[9])
            streetrentN.set(rowm1[8])
            streetrentE.set(rowm1[7])
            spacerent.set(rowm1[6])
            pricerent.set(rowm1[5])
            paymentrent.set(rowm1[4])
            ownerrent.set(rowm1[3])
            phonerent.set(rowm1[2])
            conditionrent.set(rowm1[1])
            extrarent.set(rowm1[0])

        def LandRec(ev):
            viewinfo = recourd.focus()
            global rowm
            learnData = recourd.item(viewinfo)
            rowm = learnData['values']
            
            nighber.set(rowm[13])
            Land_typ.set(rowm[12])
            land_num.set(rowm[11])
            land_bluk.set(rowm[10])
            streetS.set(rowm[9])
            streetW.set(rowm[8])
            streetN.set(rowm[7])
            streetE.set(rowm[6])
            tall.set(rowm[5])
            bid.set(rowm[4])
            price.set(rowm[3])
            office.set(rowm[2])
            phone.set(rowm[1])
            extra_f.set(rowm[0])
         #3qar   
        def AQR(ev):
            viewinfo3 = recourd3.focus()
            global rowm3
            learnData3 = recourd3.item(viewinfo3)
            rowm3 = learnData3['values']
            
            nigh3qar.set(rowm3[13])
            type3qarr.set(rowm3[12])
            num3qar.set(rowm3[11])
            bluk3qar.set(rowm3[10])
            street3qar.set(rowm3[9])
            street3qar2.set(rowm3[8])
            street3qar3.set(rowm3[7])
            where3qar.set(rowm3[6])
            taal3qar.set(rowm3[5])
            price3qar.set(rowm3[4])
            bid3qar.set(rowm3[3])
            phone3qar.set(rowm3[2])
            office3qar.set(rowm3[1])
            extra3qar.set(rowm3[0])
             
         ### DELETE ###   
           
        def Delete():
            result = tkinter.messagebox.askyesno('حذف', "هل انت متاكد تريد الحذف؟")
            if result == True:
            
                if(len(nighber.get())!=0):
                    
                    databasefile.delete_data(rowm[14])
            clearland()
            Display()
            clearland()

        def Deleterent():
            result = tkinter.messagebox.askyesno('حذف', "هل انت متاكد تريد الحذف؟")
            if result == True:
            
                if(len(nighrent.get())!=0):
                    
                    databasefile.delete_rent(rowm1[15])
            clearRent()
            rentDisplay()
            clearRent()
        def Delete3qar():
            result = tkinter.messagebox.askyesno('حذف', "هل انت متاكد تريد الحذف؟")
            if result == True:
            
                if(len(nigh3qar.get())!=0):
                    
                    databasefile.delete_3qar(rowm3[14])
            clear3qar()
            Al3qartDisplay()
            clear3qar()
        def Deleteorders():
            result = tkinter.messagebox.askyesno('حذف', "هل انت متاكد تريد الحذف؟")
            if result == True:
            
                if(len(nighorders.get())!=0):
                    
                    databasefile.delete_orders(rowm4[13])
            clearorders()
            ordersDisplay()
            clearorders()
        def DeleteNOTE():
            result = tkinter.messagebox.askyesno('حذف', "هل انت متاكد تريد الحذف؟")
            if result == True:
            
                if(len(subjecT.get())!=0):
                    
                    databasefile.delete_note(rowm5[3])
            clearnote()
            Displaynote()
            clearnote()
        def DeleteSQL():
            result = tkinter.messagebox.askyesno('حذف', "هل انت متاكد تريد الحذف؟")
            if result == True:
                txt101 = open("resources/n65748382991.skm","r",encoding='utf-8').read()
                if(ownersql.get() == txt101):
                    
                    databasesconn.delete_sql(rowm6[16])
                else:
                    result = tkinter.messagebox.showinfo('لم ينم الحذف', "لا تستطيع حذف عروض غيرك")
            clearSQL()
            SQLDisplay()
            clearSQL()
        
            
        ### SEARCH ###  
        
        def SQLSearch():

            recourd6.delete(*recourd6.get_children())
            for rows in databasesconn.search_sql(city.get(),typesql.get(),conditionsql.get(),nighSQL.get(),landnSQL.get(),landbSQL.get(),northSQL.get(),southSQL.get(),eastSQL.get(),westSQL.get(),spacesql.get(),ownersql.get(),phonesql.get(),pricesql.get(),bidsql.get(),extrasql.get()):
                recourd6.insert('',END,values=(rows[16],rows[15],rows[14],rows[13],rows[12],rows[11],rows[10],rows[9],rows[8],rows[7],rows[6],rows[5],rows[4],rows[3],rows[2],rows[1],rows[0]))  

        def searchrentbase():
                
            recourd.delete(*recourd.get_children())
            for rows in databasefile.SearchData(nighber.get(),Land_typ.get(),land_num.get(),land_bluk.get(),streetS.get(),streetW.get(),streetN.get(),streetE.get(),tall.get(),bid.get(),price.get(),office.get(),phone.get(),extra_f.get()):
            
                recourd.insert('',END,values=(rows[14],rows[13],rows[12],rows[11],rows[10],rows[9],rows[8],rows[7],rows[6],rows[5],rows[4],rows[3],rows[2],rows[1],rows[0]))
        
        def searchrent():
            
            recourd1.delete(*recourd1.get_children())
            
            for rows in databasefile.searchRe(nighrent.get(),typerent.get(),landnrent.get(),landbrent.get(),streetrentS.get(),streetrentW.get(),streetrentN.get(),streetrentE.get(),spacerent.get(),pricerent.get(),paymentrent.get(),ownerrent.get(),phonerent.get(),conditionrent.get(), extrarent.get()):
                
                recourd1.insert('',END,values=(rows[15],rows[14],rows[13],rows[12],rows[11],rows[10],rows[9],rows[8],rows[7],rows[6],rows[5],rows[4],rows[3],rows[2],rows[1],rows[0]))  

        def search3qar():
            
            recourd3.delete(*recourd3.get_children())
            
            for rows in databasefile.search3q(nigh3qar.get(),type3qarr.get(),num3qar.get(),bluk3qar.get(),street3qar.get(),street3qar2.get(),street3qar3.get(),where3qar.get(),taal3qar.get(),price3qar.get(),bid3qar.get(),phone3qar.get(),office3qar.get(),extra3qar.get()):
                
                recourd3.insert('',END,values=(rows[14],rows[13],rows[12],rows[11],rows[10],rows[9],rows[8],rows[7],rows[6],rows[5],rows[4],rows[3],rows[2],rows[1],rows[0]))
        def searchorders():
            
            recourd4.delete(*recourd4.get_children())
            
            for rows in databasefile.searchOr(nighorders.get(),landborders.get(),streetorderS.get(),streetorderW.get(),streetorderN.get(),streetorderE.get(),typeorders.get(),spaceorders.get(),ownerorders.get(),phoneorders.get(),conditionorders.get(),priceorders.get(),extraorders.get()):

                recourd4.insert('',END,values=(rows[13],rows[12],rows[11],rows[10],rows[9],rows[8],rows[7],rows[6],rows[5],rows[4],rows[3],rows[2],rows[1],rows[0]))  

         
        def searchNOTE():
            
            recourd5.delete(*recourd5.get_children())
            
            for rows in databasefile.searchnote(subjecT.get(),phonN.get(),etcN.get()):

                recourd5.insert('',END,values=(rows[3],rows[2],rows[1],rows[0]))     
            
        ### UPDATE ###    
        def update():
            if(len(nighber.get())!=0):
                databasefile.delete_data(rowm[14])
                databasefile.insert_data(nighber.get(),Land_typ.get(),land_num.get(),land_bluk.get(),streetS.get(),streetW.get(),streetN.get(),streetE.get(),tall.get(),bid.get(),price.get(),office.get(),phone.get(), extra_f.get())
                recourd.delete(*recourd.get_children())
                result = tkinter.messagebox.showinfo('تم التعديل', 'تم التحديـــث بنجـاج')
                Display()

                  
        def updatRent():
            if(len(nighrent.get())!=0):
                databasefile.delete_rent(rowm1[15])
                databasefile.insert_rent(nighrent.get(),typerent.get(),landnrent.get(),landbrent.get(),streetrentS.get(),streetrentW.get(),streetrentN.get(),streetrentE.get(),spacerent.get(),pricerent.get(),paymentrent.get(),ownerrent.get(),phonerent.get(),conditionrent.get(), extrarent.get())
                recourd1.delete(*recourd1.get_children())
                result = tkinter.messagebox.showinfo('تم التعديل', 'تم التحديـــث بنجـاج')
                rentDisplay()

                
        def updat3qar():
            if(len(nigh3qar.get())!=0):
                databasefile.delete_3qar(rowm3[14])
                databasefile.insert_3qar(nigh3qar.get(),type3qarr.get(),num3qar.get(),bluk3qar.get(),street3qar.get(),street3qar2.get(),street3qar3.get(),where3qar.get(),taal3qar.get(),price3qar.get(),bid3qar.get(),phone3qar.get(),office3qar.get(), extra3qar.get() )
                recourd3.delete(*recourd3.get_children())
                result = tkinter.messagebox.showinfo('تم التعديل', 'تم التحديـــث بنجـاج')
                Al3qartDisplay()  
        
        def updatorders():
            if(len(nighorders.get())!=0):
                databasefile.delete_orders(rowm4[13])
                databasefile.insert_orders(nighorders.get(),landborders.get(),streetorderS.get(),streetorderW.get(),streetorderN.get(),streetorderE.get(),typeorders.get(),spaceorders.get(),ownerorders.get(),phoneorders.get(),conditionorders.get(),priceorders.get(),extraorders.get())
                recourd4.delete(*recourd4.get_children())
                result = tkinter.messagebox.showinfo('تم التعديل', 'تم التحديـــث بنجـاج')
                ordersDisplay()

                
  
        def updatnote():
            etcN = inputtxt.get("1.0",END)
            if(len(subjecT.get())!=0):
                
                databasefile.delete_note(rowm5[3])
                databasefile.insert_note(subjecT.get(), phonN.get(), etcN)
                recourd5.delete(*recourd5.get_children())
                result = tkinter.messagebox.showinfo('تم التعديل', 'تم التحديـــث بنجـاج')
                Displaynote()  
                
        def updatSQL():
            txt101 = open("resources/n65748382991.skm","r",encoding='utf-8').read()

            if(ownersql.get() == txt101):
                
                databasesconn.delete_sql(rowm6[16])
                databasesconn.addShare(city.get(),typesql.get(),conditionsql.get(),nighSQL.get(),landnSQL.get(),landbSQL.get(),\
                                         northSQL.get(),southSQL.get(),eastSQL.get(),westSQL.get(),spacesql.get(),ownersql.get() ,\
                                         phonesql.get(),pricesql.get(),bidsql.get(),extrasql.get())
                recourd6.delete(*recourd6.get_children())
                result = tkinter.messagebox.showinfo('تم التعديل','تم التحديـــث بنجـاج')
            else:
                result = tkinter.messagebox.showinfo('لم ينم التحديث', "لا تستطيع تحديث عروض غيرك")
            SQLDisplay()
        ################################## END #################################################

        ################################## Frams ###############################################
        
        # create all of the main containers
        MainFrame = Frame(self.root, bg="white", width=1350, height=700, pady=3)
        TitalFrame = Frame(MainFrame,bd=2, padx=25,pady=25, bg="#f4f4fd", relief = RAISED)
        text22 = open("resources/n65748382991.skm","r",encoding='utf-8').read()
            
        self.lbTit = Label(TitalFrame, font=('new roman',50,BOLD),text=text22,bg="White",padx=60,pady=10)
        self.lbTit.grid()
        
        DataFrame = Frame(MainFrame,bd=1, width=1550, height=700, padx=12,pady=12, bg="#f4fdf4", relief = RIDGE )
        
        MainFrame.grid(row=1)
        TitalFrame.grid(row=0)
        
        s = ttk.Style()
        s.configure('TNotebook.Tab' , padding = [4, 4] ,tabposition='ne')
        nb = ttk.Notebook(DataFrame, name = 'nb',width=1550, height=600, style='TNotebook.Tab')
        nb.grid(row=0, column=0) # fill "master" but pad sides

        tab1Frame = Frame(nb, name = 'tab1')
        nb.add(tab1Frame, text = 'تأجير العقـارات')
        
        tab3Frame = Frame(nb, name = 'tab3')
        nb.add(tab3Frame, text = "بيع العقـارات")

        tab2Frame = Frame(nb, name = 'tab2')
        nb.add(tab2Frame, text = 'اراضـــي')
         
        tab4Frame = Frame(nb, name = 'tab4')
        nb.add(tab4Frame, text = 'طلبات الزبائن')
        
        tab5Frame = Frame(nb, name = 'tab5')
        nb.add(tab5Frame, text = 'دفتر الملاحظات')
        
        tab6Frame = Frame(nb, name = 'tab6')
        nb.add(tab6Frame, text = 'مشاركة العروض')

        nb.select(tab2Frame)
        
        #tab5 fram NOTE
        
        DataFramepass = LabelFrame(tab5Frame,bd=4, width=200, height=200, padx=15,pady=3, bg="#DCDCDC", relief =  RAISED, font=('arial',12,'bold'),text='                                                                                                    ضع كلمة المرور')
        DataFrameRIGHT5 = LabelFrame(tab5Frame,bd=4, width=500, height=350, padx=18,pady=3, bg="#DCDCDC", relief =  RAISED, font=('arial',14,'bold'),text=' لوحة الادخال')
        DataFramechange5 = LabelFrame(tab5Frame,bd=4, width=500, height=50, padx=15,pady=3, bg="Ghost White", relief =  RAISED, font=('arial',14,'bold'),text='                                                                                       تغير كلمة المرور')
        DataFrameLEFT5 = LabelFrame(tab5Frame,bd=4, width=500, height=350, padx=15,pady=3, bg="#DCDCDC", relief =  RAISED, font=('arial',14,'bold'),text='                                                                                                                                          لوحة النتائج')
        ButtonFrame5 = Frame(tab5Frame,bd=4, width=500, height=50, padx=15,pady=15, bg="#f4f4fd", relief =  RAISED )
        
        #tab2 fram
        DataFrameRIGHT = LabelFrame(tab2Frame,bd=4, width=500, height=350, padx=15,pady=3, bg="#DCDCDC", relief =  RAISED, font=('arial',14,'bold'))
        DataFrameLEFT = LabelFrame(tab2Frame,bd=4, width=500, height=350, padx=15,pady=3, bg="#DCDCDC", relief =  RAISED, font=('arial',14,'bold'),text='                                                                                                                                                                         لوحة النتائج')
        ButtonFrame = Frame(tab2Frame,bd=4, width=500, height=50, padx=15,pady=15, bg="#f4f4fd", relief =  RAISED )
        #tap1 frame
        DataFrameRIGHT1 = LabelFrame(tab1Frame,bd=4, width=500, height=350, padx=15,pady=3, bg="#DCDCDC", relief =  RAISED, font=('arial',14,'bold'))
        DataFrameLEFT1 = LabelFrame(tab1Frame,bd=4, width=500, height=350, padx=15,pady=3, bg="#DCDCDC", relief =  RAISED, font=('arial',14,'bold'),text='                                                                                                                                                                         لوحة النتائج')
        ButtonFrame1 = Frame(tab1Frame,bd=4, width=500, height=50, padx=15,pady=15, bg="#f4f4fd", relief =  RAISED )
        #tap3qrat 
        
        DataFrameRIGHT3 = LabelFrame(tab3Frame,bd=4, width=500, height=350, padx=15,pady=3, bg="#DCDCDC", relief =  RAISED, font=('arial',14,'bold'))
        DataFrameLEFT3 = LabelFrame(tab3Frame,bd=4, width=500, height=350, padx=15,pady=3, bg="#DCDCDC", relief =  RAISED, font=('arial',14,'bold'),text='                                                                                                                                                                         لوحة النتائج')
        ButtonFrame3 = Frame(tab3Frame,bd=4, width=500, height=50, padx=15,pady=15, bg="#f4f4fd", relief =  RAISED )
        
        #tapORDERS
        
        DataFrameRIGHT4 = LabelFrame(tab4Frame,bd=4, width=500, height=350, padx=15,pady=3, bg="#DCDCDC", relief =  RAISED, font=('arial',14,'bold'))
        DataFrameLEFT4 = LabelFrame(tab4Frame,bd=4, width=500, height=350, padx=15,pady=3, bg="#DCDCDC", relief =  RAISED, font=('arial',14,'bold'),text='                                                                                                                                                                         لوحة النتائج')
        ButtonFrame4 = Frame(tab4Frame,bd=4, width=500, height=50, padx=15,pady=15, bg="#f4f4fd", relief =  RAISED )
        
        #tapSQL
        
        DataFrameRIGHT6 = LabelFrame(tab6Frame,bd=4, width=500, height=350, padx=15,pady=3, bg="#DCDCDC", relief =  RAISED, font=('arial',14,'bold'))
        DataFrameLEFT6 = LabelFrame(tab6Frame,bd=4, width=500, height=350, padx=15,pady=3, bg="#DCDCDC", relief =  RAISED, font=('arial',14,'bold'),text='                                                                                                                                                                         لوحة النتائج')
        ButtonFrame6 = Frame(tab6Frame,bd=4, width=500, height=50, padx=15,pady=15, bg="#f4f4fd", relief =  RAISED )
        
        # layout all of the main containers
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(1, weight=1)
        DataFrame.grid(row=1)
        #tap2 grid frame
        DataFrameRIGHT.grid(row=1,column=1, sticky="en")
        DataFrameLEFT.grid(row=1,column=0, sticky="wn")
        ButtonFrame.grid(row=2,column=0,sticky="wn")
        #tab1
        DataFrameRIGHT1.grid(row=1,column=1, sticky="en")
        DataFrameLEFT1.grid(row=1,column=0, sticky="wn")
        ButtonFrame1.grid(row=2,column=0,sticky="wn")
        #tap3qrat 
        DataFrameRIGHT3.grid(row=1,column=1, sticky="en")
        DataFrameLEFT3.grid(row=1,column=0, sticky="wn")
        ButtonFrame3.grid(row=2,column=0,sticky="wn")
        #taporders 
        DataFrameRIGHT4.grid(row=1,column=1, sticky="en")
        DataFrameLEFT4.grid(row=1,column=0, sticky="wn")
        ButtonFrame4.grid(row=2,column=0,sticky="wn")
        #sql
        DataFrameRIGHT6.grid(row=1,column=1,rowspan = 2,sticky="en")
        DataFrameLEFT6.grid(row=1,column=0,sticky="wn")
        ButtonFrame6.grid(row=2,column=0,sticky="wn")
        #tap NOTE
        DataFramepass.place(relx=0.5, rely=0.40, anchor=CENTER)  #<====== place
        
        
        
        ################################## END #################################################
        #tap 6 sql
        tyor6 = ttk.Combobox(DataFrameRIGHT6,width = 40, state="readonly", textvariable = typesql ,font=('arial',14,'bold'),justify='right')
        pyor6 = ttk.Combobox(DataFrameRIGHT6,width = 40, state="readonly", textvariable = conditionsql ,font=('arial',14,'bold'),justify='right')
        #tap 4 orders
        tyor = ttk.Combobox(DataFrameRIGHT4,width = 40, state="readonly", textvariable = typeorders ,font=('arial',14,'bold'),justify='right')
        pyor = ttk.Combobox(DataFrameRIGHT4,width = 40, state="readonly", textvariable = conditionorders ,font=('arial',14,'bold'),justify='right')
        # tap1
        landtyp = ttk.Combobox(DataFrameRIGHT,width = 40, state="readonly", textvariable = Land_typ,font=('arial',14,'bold'),justify='right')
        #tap 3
        type3qTy = ttk.Combobox(DataFrameRIGHT3,width = 40, state="readonly", textvariable = type3qarr,font=('arial',14,'bold'),justify='right')
        #tap rent
        conditionre = ttk.Combobox(DataFrameRIGHT1,width = 40,state="readonly",  textvariable = conditionrent,font=('arial',14,'bold'),justify='right')
        typerent = ttk.Combobox(DataFrameRIGHT1,width = 40, state="readonly", textvariable = typerent,font=('arial',14,'bold'),justify='right')
        ############################### LABELS  ################################################
        
        #tab6 SQL
   
        self.lblnighSQL = Label(DataFrameRIGHT6, font=('arial',15,'bold'),text='المخطط',padx=2,pady=2,bg='#f4f4fd')
        self.lblnighSQL.grid(row=3,column=1,sticky="en")
        self.txtnighSQL = Entry(DataFrameRIGHT6, font=('arial',15,'bold'),textvariable=nighSQL,width=42, justify='right')
        self.txtnighSQL.grid(row=3,column=0,sticky="e")
        
        self.lbllandnSQL = Label(DataFrameRIGHT6, font=('arial',15,'bold'),text='رقم البلوك',padx=2,pady=2,bg="#dedef9")
        self.lbllandnSQL .grid(row=4,column=1,sticky="en")
        self.txtlandnSQL = Entry(DataFrameRIGHT6, font=('arial',15,'bold'),textvariable=landnSQL,width=42, justify='right')
        self.txtlandnSQL .grid(row=4,column=0,sticky="e")
        
        self.lbllandbSQL = Label(DataFrameRIGHT6, font=('arial',15,'bold'),text='رقم الارض',padx=2,pady=2,bg="#c9c9f5")
        self.lbllandbSQL .grid(row=5,column=1,sticky="en")
        self.txtlandbSQL = Entry(DataFrameRIGHT6, font=('arial',15,'bold'),textvariable=landbSQL,width=42, justify='right')
        self.txtlandbSQL .grid(row=5,column=0,sticky="e")
        
        self.lblnorthSQL  = Label(DataFrameRIGHT6, font=('arial',15,'bold'),text="شارع شمال",padx=2,pady=2,bg='#f4f4fd')
        self.lblnorthSQL .grid(row=6,column=1,sticky="en")
        self.txtnorthSQL  = Entry(DataFrameRIGHT6, font=('arial',15,'bold'),textvariable=northSQL ,width=42, justify='right')
        self.txtnorthSQL .grid(row=6,column=0,sticky="e")
        
        self.lblsouthSQL  = Label(DataFrameRIGHT6, font=('arial',15,'bold'),text="شارع غرب",padx=2,pady=2,bg='#dedef9')
        self.lblsouthSQL .grid(row=7,column=1,sticky="en")
        self.txtsouthSQL  = Entry(DataFrameRIGHT6, font=('arial',15,'bold'),textvariable=southSQL ,width=42, justify='right')
        self.txtsouthSQL .grid(row=7,column=0,sticky="e")
        
        self.lbleastSQL  = Label(DataFrameRIGHT6, font=('arial',15,'bold'),text="شارع جنوب",padx=2,pady=2,bg='#b3b3f1')
        self.lbleastSQL .grid(row=8,column=1,sticky="en")
        self.txteastSQL  = Entry(DataFrameRIGHT6, font=('arial',15,'bold'),textvariable=eastSQL ,width=42, justify='right')
        self.txteastSQL .grid(row=8,column=0,sticky="e")
        
        self.lblwestSQL  = Label(DataFrameRIGHT6, font=('arial',15,'bold'),text="شارع شرق",padx=2,pady=2,bg='#c9c9f5')
        self.lblwestSQL .grid(row=9,column=1,sticky="en")
        self.txtwestSQL  = Entry(DataFrameRIGHT6, font=('arial',15,'bold'),textvariable=westSQL ,width=42, justify='right')
        self.txtwestSQL .grid(row=9,column=0,sticky="e")
        
        self.lbltyor = Label(DataFrameRIGHT6, font=('arial',15,'bold'),text='نوع العرض',padx=2,pady=2,bg='#b3b3f1', justify='right')
        self.lbltyor.grid(row=2,column=1,sticky="en")
        tyor6['values'] = ('ارض سكنية','ارض تجارية','فيلا','بيت دور','دور ارضي','دور علوي','دور وشقتين','عمارة اربع شقق','عمارة شقق عزاب','استراحة','شالية', 'محلات','مخزن','كيربي','مزرعة','محطة','فندق','مصنع')
  
        tyor6.grid(column = 0, row = 2,sticky='w',pady=2) 
        
        self.lblcitySQL  = Label(DataFrameRIGHT6, font=('arial',15,'bold'),text="المدينة",padx=2,pady=2,bg="#f4f4fd")
        self.lblcitySQL .grid(row=0,column=1,sticky="en")
        self.txtcitySQL  = Entry(DataFrameRIGHT6, font=('arial',15,'bold'),textvariable=city ,width=42, justify='right')
        self.txtcitySQL .grid(row=0,column=0,sticky="e")
        
        self.lblspaceSQL  = Label(DataFrameRIGHT6, font=('arial',15,'bold'),text="المساحة",padx=2,pady=2,bg="#f4f4fd")
        self.lblspaceSQL .grid(row=10,column=1,sticky="en")
        self.txtspaceSQL  = Entry(DataFrameRIGHT6, font=('arial',15,'bold'),textvariable=spacesql ,width=42, justify='right')
        self.txtspaceSQL .grid(row=10,column=0,sticky="e")
        
        self.lblownersql = Label(DataFrameRIGHT6, font=('arial',15,'bold'),text="اسم المكتب",padx=2,pady=2,bg='#dedef9')
        self.lblownersql.grid(row=11,column=1,sticky="en")
        self.txtownersql = Entry(DataFrameRIGHT6, font=('arial',15,'bold'),textvariable=ownersql,width=42, justify='right')
        self.txtownersql.grid(row=11,column=0,sticky="e")
        
        self.lblphonesql  = Label(DataFrameRIGHT6, font=('arial',15,'bold'),text="رقم الجوال",padx=2,pady=2,bg="#b3b3f1")
        self.lblphonesql .grid(row=12,column=1,sticky="en")
        self.txtphonesql  = Entry(DataFrameRIGHT6, font=('arial',15,'bold'),textvariable=phonesql ,width=42, justify='right')
        self.txtphonesql .grid(row=12,column=0,sticky="e")
        
        self.lblconditionorders = Label(DataFrameRIGHT6, font=('arial',15,'bold'),text="المطلوب",padx=2,pady=2,bg='#c9c9f5')
        self.lblconditionorders.grid(row=1,column=1,sticky="en")
        pyor6['values'] = ('شراء','بيع',
                          'تأجير') 
        pyor6.grid(column = 0, row = 1,sticky='en',pady=2) 

        self.lblpricesql = Label(DataFrameRIGHT6, font=('arial',15,'bold'),text="الحد",padx=2,pady=2,bg="#f4f4fd")
        self.lblpricesql.grid(row=13,column=1,sticky="en")
        self.txtpricesql = Entry(DataFrameRIGHT6, font=('arial',15,'bold'),textvariable=pricesql,width=42, justify='right')
        self.txtpricesql.grid(row=13,column=0,sticky="e")
        
        self.lblbidsql = Label(DataFrameRIGHT6, font=('arial',15,'bold'),text="السوم",padx=2,pady=2,bg="#b3b3f1")
        self.lblbidsql.grid(row=14,column=1,sticky="en")
        self.txtbidsql = Entry(DataFrameRIGHT6, font=('arial',15,'bold'),textvariable=bidsql,width=42, justify='right')
        self.txtbidsql.grid(row=14,column=0,sticky="e")
        
        self.lblextrasql = Label(DataFrameRIGHT6, font=('arial',15,'bold'),text="اخرى",padx=2,pady=2,bg='#dedef9')
        self.lblextrasql.grid(row=15,column=1,sticky="en")
        self.txtextrasql = Entry(DataFrameRIGHT6, font=('arial',15,'bold'),textvariable=extrasql,width=42, justify='right')
        self.txtextrasql.grid(row=15,column=0,sticky="e")
        
        ### NOTE PASSWORD ###
        NewpassW = StringVar()
        def checkpass():
            for line in open("resources/p65748382991.skm","r").readlines():
                if line == passW.get():

                    DataFramepass.destroy()
                    DataFrameRIGHT5.grid(row=1,column=1, sticky="en")
                    DataFrameLEFT5.grid(row=1,column=0, sticky="wn")
                    ButtonFrame5.grid(row=2,column=0,sticky="wn")
                    DataFramechange5.grid(row=2,column=1, sticky="en")
                else:
                    result = tkinter.messagebox.showinfo('تنبية ', 'كلمة المرور غير صحيحة')
        def chanagepass():
            f = open("resources/p65748382991.skm", "w")
            f.write(NewpassW.get())
            h = NewpassW.get()
            f.close()
            result = tkinter.messagebox.showinfo("تم التغير بنجاح",'\n كلمة المرور الجديدة '+h)
            
            
        #with open('fileresources/n65748382991.skm','w') pass
        self.lblnewpass = Label(DataFramechange5, font=('arial',15,'bold'),text='كلمة المرور الجديدة',padx=2,pady=2,bg='#f4f4fd')
        self.lblnewpass.grid(row=0,column=1,sticky="en")
        self.txtnewpass = Entry(DataFramechange5, font=('arial',15,'bold'),textvariable=NewpassW,width=37, justify='right')
        self.txtnewpass.grid(row=0,column=0,sticky="s")
        #need funct
        self.btnpass = Button(DataFramechange5,text = "تغير",font=('arial',15,'bold'),width =10, height=1,bd=4, command=chanagepass)
        self.btnpass.grid(row=1, column=0)
        
        
        #pass frame
        self.lblpass = Label(DataFramepass, font=('arial',15,'bold'),text='كلمة المرور',padx=2,pady=2,bg='#dedef9')
        self.lblpass.grid(row=0,column=1,sticky="en")
        self.txtpass = Entry(DataFramepass, font=('arial',15,'bold'),textvariable=passW,width=35, justify='right')
        self.txtpass.grid(row=0,column=0,sticky="en")
        ### note butt ###
        self.btnpass = Button(DataFramepass,text = "دخول",font=('arial',15,'bold'),width =10, height=2,bd=4,command = checkpass)
        self.btnpass.grid(row=1, column=0)

        self.btnaddnote = Button(ButtonFrame5,text = "اضافة ملاحظة",font=('arial',15,'bold'),width =10, height=2,bd=4,command = addnote)
        self.btnaddnote.grid(row=0, column=5)
        
        self.btnclearr = Button(ButtonFrame5,text = "مسح الحقول",font=('arial',15,'bold'),width =10, height=2,bd=4,command = clearnote)
        self.btnclearr.grid(row=0, column=3)
        
        self.btnpass = Button(ButtonFrame5,text = "عرض الكل",font=('arial',15,'bold'),width =10, height=2,bd=4,command = Displaynote)
        self.btnpass.grid(row=0, column=4)
        
        self.btnpass = Button(ButtonFrame5,text = "حذف الملاحظة",font=('arial',15,'bold'),width =10, height=2,bd=4,command = DeleteNOTE)
        self.btnpass.grid(row=0, column=2)
        
        self.btnpass = Button(ButtonFrame5,text = "تحديث  الملاحظة",font=('arial',15,'bold'),width =10, height=2,bd=4,command = updatnote)
        self.btnpass.grid(row=0, column=6)
        
        self.btnpass = Button(ButtonFrame5,text = "البحث",font=('arial',15,'bold'),width =10, height=2,bd=4,command = searchNOTE)
        self.btnpass.grid(row=0, column=1)
        
        self.btnExit = Button(ButtonFrame5,text = "الخروج",font=('arial',15,'bold'),width =10, height=2,bd=4, command = iExit)
        self.btnExit.grid(row=0, column=0)
        # note labels
        self.lblsubject = Label(DataFrameRIGHT5, font=('arial',15,'bold'),text='العنوان',padx=2,pady=2,bg='#f4f4fd')
        self.lblsubject.grid(row=0,column=1,sticky="en")
        self.txtsubject = Entry(DataFrameRIGHT5, font=('arial',15,'bold'),textvariable=subjecT,width=42, justify='right')
        self.txtsubject.grid(row=0,column=0,sticky="en")
        self.lblphonN = Label(DataFrameRIGHT5, font=('arial',15,'bold'),text='الرقـم',padx=2,pady=2,bg='#c9c9f5')
        self.lblphonN.grid(row=1,column=1,sticky="en")
        self.txtphonN = Entry(DataFrameRIGHT5, font=('arial',15,'bold'),textvariable=phonN,width=42, justify='right')
        self.txtphonN.grid(row=1,column=0,sticky="en")
        
        self.lbletc = Label(DataFrameRIGHT5, font=('arial',15,'bold'),text='ملاحظات',padx=2,pady=2,bg='#b3b3f1')
        self.lbletc.grid(row=2,column=1,sticky="en")
        inputtxt = Text(DataFrameRIGHT5, height = 25,state=NORMAL,
              width = 58,  
              bg = "#dedef9")
        inputtxt.grid(row=2,column=0,sticky="en")
        inputtxt.tag_configure('tag-center', justify='right')
        inputtxt.insert('end', ' -  ', 'tag-center')

        
        #tab4 Orders
        self.lblnighorders = Label(DataFrameRIGHT4, font=('arial',15,'bold'),text='المخطط',padx=2,pady=2,bg='#f4f4fd')
        self.lblnighorders.grid(row=1,column=1,sticky="en")
        self.txtnighorders = Entry(DataFrameRIGHT4, font=('arial',15,'bold'),textvariable=nighorders,width=42, justify='right')
        self.txtnighorders.grid(row=1,column=0,sticky="e")
        
        self.lbllandborders = Label(DataFrameRIGHT4, font=('arial',15,'bold'),text='رقم البلوك',padx=2,pady=2,bg="#c9c9f5")
        self.lbllandborders .grid(row=2,column=1,sticky="en")
        self.txtlandborders = Entry(DataFrameRIGHT4, font=('arial',15,'bold'),textvariable=landborders,width=42, justify='right')
        self.txtlandborders .grid(row=2,column=0,sticky="e")
        ###work S N W E

        self.lblstreetorderS  = Label(DataFrameRIGHT4, font=('arial',15,'bold'),text="شارع شمال",padx=2,pady=2,bg='#dedef9')
        self.lblstreetorderS.grid(row=3,column=1,sticky="en")
        self.txtstreetorderS  = Entry(DataFrameRIGHT4, font=('arial',15,'bold'),textvariable=streetorderS ,width=42, justify='right')
        self.txtstreetorderS.grid(row=3,column=0,sticky="e")

        self.lblstreetorderW  = Label(DataFrameRIGHT4, font=('arial',15,'bold'),text="شارع غرب",padx=2,pady=2,bg='#f4f4fd')
        self.lblstreetorderW.grid(row=4,column=1,sticky="en")
        self.txtstreetorderW  = Entry(DataFrameRIGHT4, font=('arial',15,'bold'),textvariable=streetorderW ,width=42, justify='right')
        self.txtstreetorderW.grid(row=4,column=0,sticky="e")

        self.lblstreetorderN  = Label(DataFrameRIGHT4, font=('arial',15,'bold'),text="شارع جنوب",padx=2,pady=2,bg='#b3b3f1')
        self.lblstreetorderN.grid(row=5,column=1,sticky="en")
        self.txtstreetorderN  = Entry(DataFrameRIGHT4, font=('arial',15,'bold'),textvariable=streetorderN ,width=42, justify='right')
        self.txtstreetorderN.grid(row=5,column=0,sticky="e")

        self.lblstreetorderE  = Label(DataFrameRIGHT4, font=('arial',15,'bold'),text="شارع شرق",padx=2,pady=2,bg='#c9c9f5')
        self.lblstreetorderE.grid(row=6,column=1,sticky="en")
        self.txtstreetorderE  = Entry(DataFrameRIGHT4, font=('arial',15,'bold'),textvariable=streetorderE ,width=42, justify='right')
        self.txtstreetorderE.grid(row=6,column=0,sticky="e")


        self.lbltyor = Label(DataFrameRIGHT4, font=('arial',15,'bold'),text='نوع الطـلب',padx=2,pady=2,bg='#dedef9')
        self.lbltyor.grid(row=0,column=1,sticky="en")
        tyor['values'] = ('فيلا','بيت دور','دور ارضي','دور علوي','دور وشقتين','عمارة اربع شقق','عمارة شقق عزاب','استراحة','شالية','محلات','مخزن','كيربي','مزرعة','محطة','فندق','مصنع')
  
        tyor.grid(column = 0, row = 0,sticky='w',pady=2) 
        
        self.lblspaceorders  = Label(DataFrameRIGHT4, font=('arial',15,'bold'),text="المساحة",padx=2,pady=2,bg="#f4f4fd")
        self.lblspaceorders .grid(row=7,column=1,sticky="en")
        self.txtspaceorders  = Entry(DataFrameRIGHT4, font=('arial',15,'bold'),textvariable=spaceorders ,width=42, justify='right')
        self.txtspaceorders .grid(row=7,column=0,sticky="e")
        
        self.lblownerorders = Label(DataFrameRIGHT4, font=('arial',15,'bold'),text="راعي الطلب",padx=2,pady=2,bg='#b3b3f1')
        self.lblownerorders.grid(row=8,column=1,sticky="en")
        self.txtownerorders = Entry(DataFrameRIGHT4, font=('arial',15,'bold'),textvariable=ownerorders,width=42, justify='right')
        self.txtownerorders.grid(row=8,column=0,sticky="e")
        
        self.lblphoneorders  = Label(DataFrameRIGHT4, font=('arial',15,'bold'),text="رقم الجوال",padx=2,pady=2,bg="#c9c9f5")
        self.lblphoneorders .grid(row=9,column=1,sticky="en")
        self.txtphoneorders  = Entry(DataFrameRIGHT4, font=('arial',15,'bold'),textvariable=phoneorders ,width=42, justify='right')
        self.txtphoneorders .grid(row=9,column=0,sticky="e")
        
        self.lblconditionorders = Label(DataFrameRIGHT4, font=('arial',15,'bold'),text="طريقة الدفع",padx=2,pady=2,bg='#dedef9')
        self.lblconditionorders.grid(row=10,column=1,sticky="en")
        pyor['values'] = ('كاش',  
                          'قرض بنكي') 
        pyor.grid(column = 0, row = 10,sticky='en',pady=2) 

        self.lblpriceorders = Label(DataFrameRIGHT4, font=('arial',15,'bold'),text="السعر",padx=2,pady=2,bg="#f4f4fd")
        self.lblpriceorders.grid(row=11,column=1,sticky="en")
        self.txtpriceorders = Entry(DataFrameRIGHT4, font=('arial',15,'bold'),textvariable=priceorders,width=42, justify='right')
        self.txtpriceorders.grid(row=11,column=0,sticky="e")
        
        self.lblextraorders = Label(DataFrameRIGHT4, font=('arial',15,'bold'),text="اخرى",padx=2,pady=2,bg='#b3b3f1')
        self.lblextraorders.grid(row=12,column=1,sticky="en")
        self.txtextraorders = Entry(DataFrameRIGHT4, font=('arial',15,'bold'),textvariable=extraorders,width=42, justify='right')
        self.txtextraorders.grid(row=12,column=0,sticky="e")

        #tab2 LAND
        self.lblnighber = Label(DataFrameRIGHT, font=('arial',15,'bold'),text='المخطط',padx=2,pady=2,bg='#c9c9f5')
        self.lblnighber.grid(row=0,column=1,sticky="en")
        self.txtnighber = Entry(DataFrameRIGHT, font=('arial',15,'bold'),textvariable=nighber,width=41, justify='right')
        self.txtnighber.grid(row=0,column=0,sticky="e")
        
        self.lblLand_typ = Label(DataFrameRIGHT, font=('arial',15,'bold'),text='نوع الارض',padx=2,pady=2,bg='#dedef9')
        self.lblLand_typ.grid(row=1,column=1,sticky="en")
        landtyp['values'] = ('سكني','تجاري','استثماري')

  
        landtyp.grid(column = 0, row = 1,sticky='en',pady=2) 
        
        self.lblland_num = Label(DataFrameRIGHT, font=('arial',15,'bold'),text='رقم الارض',padx=2,pady=2,bg="#f4f4fd")
        self.lblland_num.grid(row=2,column=1,sticky="en")
        self.txtland_num = Entry(DataFrameRIGHT, font=('arial',15,'bold'),textvariable=land_num,width=41, justify='right')
        self.txtland_num.grid(row=2,column=0,sticky="e")
        
        self.lblland_bluk = Label(DataFrameRIGHT, font=('arial',15,'bold'),text="البلك",padx=2,pady=2,bg='#b3b3f1')
        self.lblland_bluk.grid(row=3,column=1,sticky="en")
        self.txtland_bluk = Entry(DataFrameRIGHT, font=('arial',15,'bold'),textvariable=land_bluk,width=41, justify='right')
        self.txtland_bluk.grid(row=3,column=0,sticky="e")
        
        self.lblstreetS = Label(DataFrameRIGHT, font=('arial',15,'bold'),text="شارع شمال",padx=2,pady=2,bg="#dedef9")
        self.lblstreetS.grid(row=4,column=1,sticky="en")
        self.txtstreetS = Entry(DataFrameRIGHT, font=('arial',15,'bold'),textvariable=streetS,width=41, justify='right')
        self.txtstreetS.grid(row=4,column=0,sticky="e")
        
        self.lblstreetW = Label(DataFrameRIGHT, font=('arial',15,'bold'),text="شارع غرب",padx=2,pady=2,bg="#c9c9f5")
        self.lblstreetW.grid(row=5,column=1,sticky="en")
        self.txtstreetW = Entry(DataFrameRIGHT, font=('arial',15,'bold'),textvariable=streetW,width=41, justify='right')
        self.txtstreetW.grid(row=5,column=0,sticky="e")
        
        self.lblstreetN = Label(DataFrameRIGHT, font=('arial',15,'bold'),text="شارع جنوب",padx=2,pady=2,bg="#b3b3f1")
        self.lblstreetN.grid(row=6,column=1,sticky="en")
        self.txtstreetN = Entry(DataFrameRIGHT, font=('arial',15,'bold'),textvariable=streetN,width=41, justify='right')
        self.txtstreetN.grid(row=6,column=0,sticky="e")
        
        self.lblstreetE = Label(DataFrameRIGHT, font=('arial',15,'bold'),text="شارع شرق",padx=2,pady=2,bg="#f4f4fd")
        self.lblstreetE.grid(row=7,column=1,sticky="en")
        self.txtstreetE = Entry(DataFrameRIGHT, font=('arial',15,'bold'),textvariable=streetE,width=41, justify='right')
        self.txtstreetE.grid(row=7,column=0,sticky="e")
        
        self.lbltall = Label(DataFrameRIGHT, font=('arial',15,'bold'),text="المساحة",padx=2,pady=2,bg="#dedef9")
        self.lbltall.grid(row=8,column=1,sticky="en")
        self.txttall = Entry(DataFrameRIGHT, font=('arial',15,'bold'),textvariable=tall,width=41, justify='right')
        self.txttall.grid(row=8,column=0,sticky="e")
        
        self.lblbid = Label(DataFrameRIGHT, font=('arial',15,'bold'),text="السوم",padx=2,pady=2,bg='#c9c9f5')
        self.lblbid.grid(row=9,column=1,sticky="en")
        self.txtbid = Entry(DataFrameRIGHT, font=('arial',15,'bold'),textvariable=bid,width=41, justify='right')
        self.txtbid.grid(row=9,column=0,sticky="e")
        
        self.lblprice = Label(DataFrameRIGHT, font=('arial',15,'bold'),text="الحد",padx=2,pady=2,bg="#b3b3f1")
        self.lblprice.grid(row=10,column=1,sticky="en")
        self.txtprice = Entry(DataFrameRIGHT, font=('arial',15,'bold'),textvariable=price,width=41, justify='right')
        self.txtprice.grid(row=10,column=0,sticky="e")
        
        self.lbloffice = Label(DataFrameRIGHT, font=('arial',15,'bold'),text="مكتب",padx=2,pady=2,bg='#dedef9')
        self.lbloffice.grid(row=11,column=1,sticky="en")
        self.txtoffice = Entry(DataFrameRIGHT, font=('arial',15,'bold'),textvariable=office,width=41, justify='right')
        self.txtoffice.grid(row=11,column=0,sticky="e")
        
        self.lblphone = Label(DataFrameRIGHT, font=('arial',15,'bold'),text="رقم الجوال",padx=2,pady=2,bg="#f4f4fd")
        self.lblphone.grid(row=12,column=1,sticky="en")
        self.txtphone = Entry(DataFrameRIGHT, font=('arial',15,'bold'),textvariable=phone,width=41, justify='right')
        self.txtphone.grid(row=12,column=0,sticky="e")
        
        self.lblextra_f = Label(DataFrameRIGHT, font=('arial',15,'bold'),text="ملاحظات",padx=2,pady=2,bg="#dedef9")
        self.lblextra_f.grid(row=13,column=1,sticky="en")
        self.txtextra_f = Entry(DataFrameRIGHT, font=('arial',15,'bold'),textvariable=extra_f,width=41, justify='right')
        self.txtextra_f.grid(row=13,column=0,sticky="e",padx=2,pady=2)

        ###need work
        
        
        #tab1 rent 3qar
        self.lblnighrent = Label(DataFrameRIGHT1, font=('arial',15,'bold'),text='المخطط',padx=2,pady=2,bg='#dedef9')
        self.lblnighrent.grid(row=0,column=1,sticky="en")
        self.txtnighrent = Entry(DataFrameRIGHT1, font=('arial',15,'bold'),textvariable=nighrent,width=42, justify='right')
        self.txtnighrent.grid(row=0,column=0,sticky="e")
        
        
        self.lbltyperent = Label(DataFrameRIGHT1, font=('arial',15,'bold'),text='نوع العقار',padx=2,pady=2,bg='#b3b3f1')
        self.lbltyperent.grid(row=1,column=1,sticky="en")
        
        typerent['values'] = ('فيلا','بيت دور','دور ارضي','دور علوي','دور وشقتين','عمارة اربع شقق','عمارة شقق عزاب','استراحة','شالية','محلات','مخزن','كيربي','مزرعة','محطة','فندق','مصنع')

        typerent.grid(column = 0, row = 1,sticky='e',pady=2) 
        typerent.current() 
        
        self.lbllandnrent = Label(DataFrameRIGHT1, font=('arial',15,'bold'),text='رقم الارض',padx=2,pady=2,bg="#c9c9f5")
        self.lbllandnrent.grid(row=2,column=1,sticky="en")
        self.txtlandnrent = Entry(DataFrameRIGHT1, font=('arial',15,'bold'),textvariable=landnrent,width=42, justify='right')
        self.txtlandnrent.grid(row=2,column=0,sticky="e")
        
        self.lbllandbrent = Label(DataFrameRIGHT1, font=('arial',15,'bold'),text="البلك",padx=2,pady=2,bg='#f4f4fd')
        self.lbllandbrent.grid(row=3,column=1,sticky="en")
        self.txtlandbrent = Entry(DataFrameRIGHT1, font=('arial',15,'bold'),textvariable=landbrent,width=42, justify='right')
        self.txtlandbrent.grid(row=3,column=0,sticky="e")
        
        self.lblstreetrentS = Label(DataFrameRIGHT1, font=('arial',15,'bold'),text="شارع شمال",padx=2,pady=2,bg='#b3b3f1')
        self.lblstreetrentS.grid(row=4,column=1,sticky="en")
        self.txtstreetrentS = Entry(DataFrameRIGHT1, font=('arial',15,'bold'),textvariable=streetrentS,width=42, justify='right')
        self.txtstreetrentS.grid(row=4,column=0,sticky="e")
        
        self.lblstreetrentW = Label(DataFrameRIGHT1, font=('arial',15,'bold'),text="شارع غرب",padx=2,pady=2,bg='#f4f4fd')
        self.lblstreetrentW.grid(row=5,column=1,sticky="en")
        self.txtstreetrentW = Entry(DataFrameRIGHT1, font=('arial',15,'bold'),textvariable=streetrentW,width=42, justify='right')
        self.txtstreetrentW.grid(row=5,column=0,sticky="e")

        self.lblstreetrentN = Label(DataFrameRIGHT1, font=('arial',15,'bold'),text="شارع جنوب",padx=2,pady=2,bg='#c9c9f5')
        self.lblstreetrentN.grid(row=6,column=1,sticky="en")
        self.txtstreetrentN = Entry(DataFrameRIGHT1, font=('arial',15,'bold'),textvariable=streetrentN,width=42, justify='right')
        self.txtstreetrentN.grid(row=6,column=0,sticky="e")

        self.lblstreetrentE = Label(DataFrameRIGHT1, font=('arial',15,'bold'),text="شارع شرق",padx=2,pady=2,bg='#dedef9')
        self.lblstreetrentE.grid(row=7,column=1,sticky="en")
        self.txtstreetrentE = Entry(DataFrameRIGHT1, font=('arial',15,'bold'),textvariable=streetrentE,width=42, justify='right')
        self.txtstreetrentE.grid(row=7,column=0,sticky="e")

        
        self.lblspacerent = Label(DataFrameRIGHT1, font=('arial',15,'bold'),text="المساحة",padx=2,pady=2,bg="#b3b3f1")
        self.lblspacerent.grid(row=8,column=1,sticky="en")
        self.txtspacerent = Entry(DataFrameRIGHT1, font=('arial',15,'bold'),textvariable=spacerent,width=42, justify='right')
        self.txtspacerent.grid(row=8,column=0,sticky="e")
        
        self.lblpricerent = Label(DataFrameRIGHT1, font=('arial',15,'bold'),text="سعر الايجار",padx=2,pady=2,bg='#c9c9f5')
        self.lblpricerent.grid(row=9,column=1,sticky="en")
        self.txtpricerent = Entry(DataFrameRIGHT1, font=('arial',15,'bold'),textvariable=pricerent,width=42, justify='right')
        self.txtpricerent.grid(row=9,column=0,sticky="e")
        
        self.lblpaymentrent = Label(DataFrameRIGHT1, font=('arial',15,'bold'),text="فترة العقد",padx=2,pady=2,bg="#f4f4fd")
        self.lblpaymentrent.grid(row=10,column=1,sticky="en")
        self.txtpaymentrent = Entry(DataFrameRIGHT1, font=('arial',15,'bold'),textvariable=paymentrent,width=42, justify='right')
        self.txtpaymentrent.grid(row=10,column=0,sticky="e")
        
        self.lblownerrent = Label(DataFrameRIGHT1, font=('arial',15,'bold'),text="مكتب/المالك",padx=2,pady=2,bg='#dedef9')
        self.lblownerrent.grid(row=11,column=1,sticky="en")
        self.txtownerrent = Entry(DataFrameRIGHT1, font=('arial',15,'bold'),textvariable=ownerrent,width=42, justify='right')
        self.txtownerrent.grid(row=11,column=0,sticky="e")
        
        self.lblphonerent = Label(DataFrameRIGHT1, font=('arial',15,'bold'),text="رقم الجوال",padx=2,pady=2,bg='#b3b3f1')
        self.lblphonerent.grid(row=12,column=1,sticky="en")
        self.txtphonerent = Entry(DataFrameRIGHT1, font=('arial',15,'bold'),textvariable=phonerent,width=42, justify='right')
        self.txtphonerent.grid(row=12,column=0,sticky="e")
        # Adding combobox drop down list 
        
        conditionre['values'] = ('مواجر',  
                          'غير مواجر',) 
  
        conditionre.grid(column = 0, row = 13,sticky='e',pady=2) 
        
        self.lblconditionrent = Label(DataFrameRIGHT1, font=('arial',15,'bold'),text="حالة العقار",padx=2,pady=2,bg="#f4f4fd")
        self.lblconditionrent.grid(row=13,column=1,sticky="en")
        
        self.lblextrarent = Label(DataFrameRIGHT1, font=('arial',15,'bold'),text="ملاحظات",padx=2,pady=2,bg="#dedef9")
        self.lblextrarent.grid(row=14,column=1,sticky="en")
        self.txtextrarent = Entry(DataFrameRIGHT1, font=('arial',15,'bold'),textvariable=extrarent,width=42, justify='right')
        self.txtextrarent.grid(row=14,column=0,sticky="e")

        
        #tap3 3qar
        self.lblnigh3qar  = Label(DataFrameRIGHT3, font=('arial',15,'bold'),text='المخطط',padx=2,pady=2,bg='#dedef9')
        self.lblnigh3qar.grid(row=0,column=1,sticky="en")
        self.txtnigh3qar  = Entry(DataFrameRIGHT3, font=('arial',15,'bold'),textvariable=nigh3qar ,width=42, justify='right')
        self.txtnigh3qar.grid(row=0,column=0,sticky="e")
        
        self.lbltype3qTy  = Label(DataFrameRIGHT3, font=('arial',15,'bold'),text='نوع العقـار',padx=2,pady=2,bg='#b3b3f1')
        self.lbltype3qTy.grid(row=1,column=1,sticky="en")
        type3qTy ['values'] = ('فيلا','بيت دور','دور علوي','دور ارضي','دور وشقتين','عمارة اربع شقق','عمارة شقق عزاب', 'استراحة','شالية', 'محلات','مخزن','كيربي','مزرعة','محطة','فندق','مصنع')

  
        type3qTy.grid(column = 0, row = 1,sticky='e',pady=2) 
        
        self.lblnum3qar  = Label(DataFrameRIGHT3, font=('arial',15,'bold'),text='رقم الارض',padx=2,pady=2,bg="#c9c9f5")
        self.lblnum3qar.grid(row=2,column=1,sticky="en")
        self.txtnum3qar  = Entry(DataFrameRIGHT3, font=('arial',15,'bold'),textvariable=num3qar ,width=42, justify='right')
        self.txtnum3qar.grid(row=2,column=0,sticky="e")
        
        self.lblbluk3qar  = Label(DataFrameRIGHT3, font=('arial',15,'bold'),text="البلك",padx=2,pady=2,bg='#f4f4fd')
        self.lblbluk3qar.grid(row=3,column=1,sticky="en")
        self.txtbluk3qar  = Entry(DataFrameRIGHT3, font=('arial',15,'bold'),textvariable=bluk3qar ,width=42, justify='right')
        self.txtbluk3qar.grid(row=3,column=0,sticky="e")
        
        self.lblstreet3qar  = Label(DataFrameRIGHT3, font=('arial',15,'bold'),text="شارع شمال",padx=2,pady=2,bg="#dedef9")
        self.lblstreet3qar.grid(row=4,column=1,sticky="en")
        self.txtstreet3qar  = Entry(DataFrameRIGHT3, font=('arial',15,'bold'),textvariable=street3qar ,width=42, justify='right')
        self.txtstreet3qar.grid(row=4,column=0,sticky="e")
        
        self.lblstreet3qar2  = Label(DataFrameRIGHT3, font=('arial',15,'bold'),text="شارع غرب",padx=2,pady=2,bg="#f4f4fd")
        self.lblstreet3qar2.grid(row=5,column=1,sticky="en")
        self.txtstreet3qar2  = Entry(DataFrameRIGHT3, font=('arial',15,'bold'),textvariable=street3qar2 ,width=42, justify='right')
        self.txtstreet3qar2.grid(row=5,column=0,sticky="e")
        
        self.lblstreet3qar3  = Label(DataFrameRIGHT3, font=('arial',15,'bold'),text="شارع جنوب",padx=2,pady=2,bg="#b3b3f1")
        self.lblstreet3qar3.grid(row=6,column=1,sticky="en")
        self.txtstreet3qar3  = Entry(DataFrameRIGHT3, font=('arial',15,'bold'),textvariable=street3qar3 ,width=42, justify='right')
        self.txtstreet3qar3.grid(row=6,column=0,sticky="e")
        
        self.lblwhere3qar  = Label(DataFrameRIGHT3, font=('arial',15,'bold'),text="شارع شرق",padx=2,pady=2,bg='#c9c9f5')
        self.lblwhere3qar.grid(row=7,column=1,sticky="en")
        self.txtwhere3qar  = Entry(DataFrameRIGHT3, font=('arial',15,'bold'),textvariable=where3qar ,width=42, justify='right')
        self.txtwhere3qar.grid(row=7,column=0,sticky="e")
        
        self.lbltaal3qar = Label(DataFrameRIGHT3, font=('arial',15,'bold'),text="المساحة",padx=2,pady=2,bg="#dedef9")
        self.lbltaal3qar.grid(row=8,column=1,sticky="en")
        self.txttaal3qar = Entry(DataFrameRIGHT3, font=('arial',15,'bold'),textvariable=taal3qar,width=42, justify='right')
        self.txttaal3qar.grid(row=8,column=0,sticky="e")
        
        self.lblbid3qar    = Label(DataFrameRIGHT3, font=('arial',15,'bold'),text="الســوم",padx=2,pady=2,bg='#f4f4fd')
        self.lblbid3qar.grid(row=9,column=1,sticky="en")
        self.txtbid3qar    = Entry(DataFrameRIGHT3, font=('arial',15,'bold'),textvariable=bid3qar   ,width=42, justify='right')
        self.txtbid3qar.grid(row=9,column=0,sticky="e")
        
        self.lblprice3qar    = Label(DataFrameRIGHT3, font=('arial',15,'bold'),text="الحــد",padx=2,pady=2,bg='#b3b3f1')
        self.lblprice3qar.grid(row=10,column=1,sticky="en")
        self.txtprice3qar    = Entry(DataFrameRIGHT3, font=('arial',15,'bold'),textvariable=price3qar,width=42, justify='right')
        self.txtprice3qar.grid(row=10,column=0,sticky="e")
        
        self.lbloffice3qar = Label(DataFrameRIGHT3, font=('arial',15,'bold'),text="مكتب/مالك",padx=2,pady=2,bg='#c9c9f5')
        self.lbloffice3qar.grid(row=11,column=1,sticky="en")
        self.txtoffice3qar = Entry(DataFrameRIGHT3, font=('arial',15,'bold'),textvariable=office3qar,width=42, justify='right')
        self.txtoffice3qar.grid(row=11,column=0,sticky="e")
        
        self.lblphone3qar = Label(DataFrameRIGHT3, font=('arial',15,'bold'),text="رقم الجوال",padx=2,pady=2,bg="#f4f4fd")
        self.lblphone3qar.grid(row=12,column=1,sticky="en")
        self.txtphone3qar = Entry(DataFrameRIGHT3, font=('arial',15,'bold'),textvariable=phone3qar,width=42, justify='right')
        self.txtphone3qar.grid(row=12,column=0,sticky="e")
        
        
        self.lblextra3qar = Label(DataFrameRIGHT3, font=('arial',15,'bold'),text="ملاحظات",padx=2,pady=2,bg='#dedef9')
        self.lblextra3qar.grid(row=13,column=1,sticky="en")
        self.txtextra3qar = Entry(DataFrameRIGHT3, font=('arial',15,'bold'),textvariable=extra3qar,width=42, justify='right')
        self.txtextra3qar.grid(row=13,column=0,sticky="e")
        ########################## ListBox & ScrollBar widget for taps lands ##################################
        scroll_y5 = Scrollbar(DataFrameLEFT5)  
        scroll_y5.grid(row=0,column=2, ipady = 210)
        
        
        recourd5 = ttk.Treeview(DataFrameLEFT5,yscrollcommand=scroll_y5.set,height = 22 ,selectmode= "browse", columns=("etcN","phonN","subjecT"))
        scroll_y5.config(command=recourd5.yview)
           
        recourd5.heading("subjecT", text="العنوان", anchor='e')
        recourd5.heading("phonN", text="رقم الجوال", anchor='e')
        recourd5.heading("etcN", text="الملاحظة", anchor='e')
   
        recourd5['show'] = 'headings'
             
        recourd5.column("subjecT", width=160,anchor='e')
        recourd5.column("phonN", width=150,anchor='e')
        recourd5.column("etcN", width=610,anchor='e')

        
             
        recourd5.grid(row=0,column=1)
        recourd5.bind("<ButtonRelease-1>",noteRec)
        Displaynote()
        
        ###sql
        style = ttk.Style()
        style.configure(".", font=('Helvetica', 13,BOLD),foreground='green')
        style.configure("Treeview", foreground='red')
        style.configure("Treeview.Heading",font=('Helvetica', 12), foreground='green') #<----comtrol view 
        scroll_y6 = Scrollbar(DataFrameLEFT6)  
        scroll_y6.grid(row=0,column=2, ipady = 210)
        
        recourd6 = ttk.Treeview(DataFrameLEFT6,yscrollcommand=scroll_y6.set,height = 22 ,selectmode= "browse", columns=("extrasql", "bidsql","pricesql","phonesql","ownersql","spacesql","westSQL","eastSQL","southSQL","northSQL","landnSQL","landbSQL","nighSQL","conditionsql","typesql","city"))
        scroll_y6.config(command=recourd6.yview)
        recourd6.heading("city", text="المدينة", anchor='e')   
        recourd6.heading("typesql", text="نوع العرض", anchor='e')
        recourd6.heading("conditionsql", text="المطلوب", anchor='e')
        recourd6.heading("nighSQL", text="المخطط", anchor='e')
        recourd6.heading("landbSQL", text="رقم البلوك", anchor='e')
        recourd6.heading("landnSQL", text="رقم الارض", anchor='e')
        recourd6.heading("northSQL", text="شارع شمال", anchor='e')
        recourd6.heading("southSQL", text="شارع غرب", anchor='e')
        recourd6.heading("eastSQL", text="شارع جنوب", anchor='e')
        recourd6.heading("westSQL", text="شارع شرق", anchor='e')
        recourd6.heading("spacesql", text="المساحة", anchor='e')
        recourd6.heading("ownersql", text="المكتب", anchor='e')
        recourd6.heading("phonesql", text="الجوال", anchor='e')
        recourd6.heading("pricesql", text="الحد", anchor='e')
        recourd6.heading("bidsql", text="السوم", anchor='e')
        recourd6.heading("extrasql", text="اخرى", anchor='e')
   
        recourd6['show'] = 'headings'
        
        recourd6.column("city", width=65, anchor='e')
        recourd6.column("typesql", width=100, anchor='e')
        recourd6.column("conditionsql",width=45, anchor='e')
        recourd6.column("nighSQL", width=70, anchor='e')
        recourd6.column("landnSQL", width=50, anchor='e')
        recourd6.column("landbSQL", width=40, anchor='e')
        recourd6.column("northSQL", width=40, anchor='e')
        recourd6.column("southSQL", width=40, anchor='e')
        recourd6.column("eastSQL", width=40, anchor='e')
        recourd6.column("westSQL", width=40, anchor='e')
        recourd6.column("spacesql", width=65, anchor='e')
        recourd6.column("ownersql", width=65, anchor='e')
        recourd6.column("phonesql", stretch=NO, minwidth=0, width=0,anchor='e')
        recourd6.column("pricesql", width=50, anchor='e')
        recourd6.column("bidsql", width=50, anchor='e')
        recourd6.column("extrasql", width=155, anchor='e')

             
        recourd6.grid(row=0,column=1)
        recourd6.bind("<ButtonRelease-1>",SQLRec)
        

        
# tap 4 orders
        scroll_y4 = Scrollbar(DataFrameLEFT4)  
        scroll_y4.grid(row=0,column=2, ipady = 210)
        
        recourd4 = ttk.Treeview(DataFrameLEFT4,yscrollcommand=scroll_y4.set,height = 22 ,selectmode= "browse", columns=("extraorders","priceorder","conditionorders","phoneorders","ownerorders",\
                                                     "spaceorders","typeorders","streetorderE","streetorderN","streetorderW","streetorderS","landborders","nighorders"))
        scroll_y4.config(command=recourd4.yview)
           
        recourd4.heading("nighorders", text="الحي", anchor='e')
        recourd4.heading("landborders", text="البلوك", anchor='e')
        recourd4.heading("streetorderS", text="شارع شمال", anchor='e')
        recourd4.heading("streetorderW", text="شارع شرق", anchor='e')
        recourd4.heading("streetorderN", text="شارع جنوب", anchor='e')
        recourd4.heading("streetorderE", text="شارع شرق", anchor='e')
        recourd4.heading("typeorders", text="نوع الطلـب", anchor='e')
        recourd4.heading("spaceorders", text="المساحة", anchor='e')
        recourd4.heading("ownerorders", text="راعي الطلب", anchor='e')
        recourd4.heading("phoneorders", text="رقم الجوال", anchor='e')
        recourd4.heading("conditionorders", text="طريقة الدفع", anchor='e')
        recourd4.heading("priceorder", text="السعر", anchor='e')
        recourd4.heading("extraorders", text="معلومات اضافية" , anchor='e')

             
        recourd4['show'] = 'headings'
             
        recourd4.column("nighorders", width=120,anchor='e')
        recourd4.column("landborders", width=50,anchor='e')
        recourd4.column("streetorderS", width=35,anchor='e')
        recourd4.column("streetorderW", width=35,anchor='e')
        recourd4.column("streetorderN", width=35,anchor='e')
        recourd4.column("streetorderE", width=35,anchor='e')

        recourd4.column("typeorders", width=100,anchor='e')
        recourd4.column("spaceorders", width=100,anchor='e')
        recourd4.column("ownerorders", stretch=NO, minwidth=0, width=0,anchor='e')
        recourd4.column("phoneorders", stretch=NO, minwidth=0, width=0,anchor='e')
        recourd4.column("conditionorders", width=80,anchor='e')
        recourd4.column("priceorder", width=50,anchor='e')
        recourd4.column("extraorders", width=270,anchor='e' )
        
             
        recourd4.grid(row=0,column=1)
        recourd4.bind("<ButtonRelease-1>",ordersRec)
        ordersDisplay()
        
         
        
        # tap 2 land treeview

        scroll_y = Scrollbar(DataFrameLEFT)  
        scroll_y.grid(row=0,column=2, ipady = 210)
        
        recourd = ttk.Treeview(DataFrameLEFT,yscrollcommand=scroll_y.set,height = 22 ,selectmode= "browse", columns=("extra_f","phone","office","tall","bid","price",\
                                                     "streetE","streetN","streetW","streetS","land_num","land_bluk","Land_typ","nighber"))
        scroll_y.config(command=recourd.yview)
           
        recourd.heading("nighber", text="الحي", anchor='e')
        recourd.heading("Land_typ", text="نوع الارض", anchor='e')
        recourd.heading("land_num", text="البلوك", anchor='e')
        recourd.heading("land_bluk", text="رقم الارض", anchor='e')
        recourd.heading("streetS", text="شمال", anchor='e')
        recourd.heading("streetW", text="غرب", anchor='e')
        recourd.heading("streetN", text="جنوب", anchor='e')
        recourd.heading("streetE", text="شرق", anchor='e')
        recourd.heading("tall", text="الحد", anchor='e')
        recourd.heading("bid", text="السوم", anchor='e')
        recourd.heading("price", text="المساحة", anchor='e')
        recourd.heading("office", text="المكتب" )
        recourd.heading("phone", text="الرقم")
        recourd.heading("extra_f", text="ملاحظات")
             
        recourd['show'] = 'headings'
             
        recourd.column("nighber", width=150,anchor='e')
        recourd.column("Land_typ", width=60,anchor='e')
        recourd.column("land_num", width=60,anchor='e')
        recourd.column("land_bluk", width=60,anchor='e')
        recourd.column("streetS", width=45,anchor='e')
        recourd.column("streetW", width=45,anchor='e')
        recourd.column("streetN", width=45,anchor='e')
        recourd.column("streetE", width=45,anchor='e')
        recourd.column("tall", width=62,anchor='e')
        recourd.column("bid", width=62,anchor='e')
        recourd.column("price", width=50,anchor='e')
        recourd.column("office",  stretch=NO, minwidth=0, width=0,anchor='e')
        recourd.column("phone",  stretch=NO, minwidth=0, width=0,anchor='e')
        recourd.column("extra_f",   width=230,anchor='e')
             
        recourd.grid(row=0,column=1)
        recourd.bind("<ButtonRelease-1>",LandRec)
        Display()
        #tab 1 rent treeview
        
        scroll_y1 = Scrollbar(DataFrameLEFT1)  
        scroll_y1.grid(row=0,column=3, ipady = 210) 
        
        recourd1 = ttk.Treeview(DataFrameLEFT1,yscrollcommand=scroll_y1.set,height = 22 , columns=("extrarent","conditionrent","phonerent","ownerrent","paymentrent","pricerent","spacerent",\
                                                     "streetrentE", "streetrentN", "streetrentW", "streetrentS","landbrent","landnrent","typerent","nighrent"))
        scroll_y1.config(command=recourd1.yview)
        
        recourd1.heading("nighrent", text="الحي",anchor='e')
        recourd1.heading("typerent", text="نوع العقار",anchor='e')
        recourd1.heading("landnrent", text="رقم الارض",anchor='e')
        recourd1.heading("landbrent", text="البلوك",anchor='e')
        recourd1.heading("streetrentS", text="شمال",anchor='e')
        recourd1.heading("streetrentW", text="غرب",anchor='e')
        recourd1.heading("streetrentN", text="جنوب",anchor='e')
        recourd1.heading("streetrentE", text="شرق",anchor='e')
        recourd1.heading("spacerent", text="المساحة",anchor='e')
        recourd1.heading("pricerent", text="السعر",anchor='e')
        recourd1.heading("paymentrent", text="فترة العقد",anchor='e')
        recourd1.heading("ownerrent", text="المكتب/المالك",anchor='e')
        recourd1.heading("phonerent", text="الرقم",anchor='e')
        recourd1.heading("conditionrent", text="حالة العقار",anchor='e')
        recourd1.heading("extrarent", text="ملاحظات",anchor='e')
        
             
        recourd1['show'] = 'headings'
             
        recourd1.column("nighrent", width=80,anchor='e')
        recourd1.column("typerent", width=80,anchor='e')
        recourd1.column("landnrent", width=70,anchor='e')
        recourd1.column("landbrent", width=60,anchor='e')
        recourd1.column("streetrentS", width=40,anchor='e')
        recourd1.column("streetrentW", width=40,anchor='e')
        recourd1.column("streetrentN", width=40,anchor='e')
        recourd1.column("streetrentE", width=40,anchor='e')

        recourd1.column("spacerent", width=70,anchor='e')
        recourd1.column("pricerent", width=70,anchor='e')
        recourd1.column("paymentrent", width=100,anchor='e')
        recourd1.column("ownerrent", stretch=NO, minwidth=0, width=0,anchor='e')
        recourd1.column("phonerent", stretch=NO, minwidth=0, width=0,anchor='e')
        recourd1.column("conditionrent", width=70,anchor='e')
        recourd1.column("extrarent", width=150,anchor='e')
             
        recourd1.grid(row=0,column=2)
        recourd1.bind("<ButtonRelease-1>",RentRec)
        rentDisplay()

        ### tree view 3 ###
        scroll_y3 = Scrollbar(DataFrameLEFT3)  
        scroll_y3.grid(row=0,column=2, ipady = 210)
        
        recourd3 = ttk.Treeview(DataFrameLEFT3,yscrollcommand=scroll_y3.set,height = 22 ,selectmode= "browse", columns=( "extra3qar", "office3qar", "phone3qar",\
                                                         "price3qar","bid3qar", "taal3qar", "where3qar","street3qar3","street3qar2","street3qar", "bluk3qar", "num3qar", "type3qarr", "nigh3qar"))
        scroll_y3.config(command=recourd3.yview)
           
        recourd3.heading("nigh3qar", text="المخطط", anchor='e')
        recourd3.heading("type3qarr", text="نوع العقار", anchor='e')
        recourd3.heading("num3qar", text="رقم الارض", anchor='e')
        recourd3.heading("bluk3qar", text="رقم البلوك", anchor='e')
        recourd3.heading("street3qar", text="شمال", anchor='e')
        recourd3.heading("street3qar2", text="غرب", anchor='e')
        recourd3.heading("street3qar3", text="جنوب", anchor='e')
        recourd3.heading("where3qar", text="شرق", anchor='e')
        recourd3.heading("taal3qar", text="المساحة", anchor='e')
        recourd3.heading("bid3qar", text="الحد")
        recourd3.heading("price3qar", text="السوم" )
        recourd3.heading("phone3qar", text="الرقم")
        recourd3.heading("office3qar", text="المكتب")
        recourd3.heading("extra3qar", text="ملاحظات")
             
        recourd3['show'] = 'headings'
             
        recourd3.column("nigh3qar",width=160,anchor='e')
        recourd3.column("type3qarr", width=90,anchor='e')
        recourd3.column("num3qar", width=60,anchor='e')
        recourd3.column("bluk3qar", width=40,anchor='e')
        recourd3.column("street3qar",width=40,anchor='e')
        recourd3.column("street3qar2",width=40,anchor='e')
        recourd3.column("street3qar3",width=40,anchor='e')
        recourd3.column("where3qar",width=40,anchor='e')
        recourd3.column("taal3qar",width=60,anchor='e')
        recourd3.column("bid3qar", width=65,anchor='e')
        recourd3.column("price3qar",width=65,anchor='e')
        recourd3.column("phone3qar",stretch=NO, minwidth=0, width=0,anchor='e')
        recourd3.column("office3qar",stretch=NO, minwidth=0, width=0,anchor='e')
        recourd3.column("extra3qar",width=210,anchor='e')
             
        recourd3.grid(row=0,column=1)
        recourd3.bind("<ButtonRelease-1>",AQR)
        Al3qartDisplay()
    
    
        ################################## END #################################################
        
        ################################ Button widge ##########################################
        #tab4 orders
        self.btnAddData = Button(ButtonFrame4,text = "اضافة طلب",font=('arial',14,'bold'),width =10, height=2,bd=4,command =addorders)
        self.btnAddData.grid(row=0, column=5)
        
        self.btnDisplayData = Button(ButtonFrame4,text = "عرض كل الطلبات",font=('arial',14,'bold'),width =10, height=2,bd=4,command= ordersDisplay)
        self.btnDisplayData.grid(row=0, column=4)

        self.btnclearRent = Button(ButtonFrame4,text = "مسح الحقول",font=('arial',14,'bold'),width =10, height=2,bd=4, command = clearorders)
        self.btnclearRent.grid(row=0, column=3)
        
        self.btnDeleterent = Button(ButtonFrame4,text = "حذف الطلب",font=('arial',14,'bold'),width =10, height=2,bd=4, command= Deleteorders )
        self.btnDeleterent.grid(row=0, column=2)
        
        self.btnsearchrent = Button(ButtonFrame4,text = "البحث",font=('arial',14,'bold'),width =10, height=2,bd=4, command=searchorders)
        self.btnsearchrent.grid(row=0, column=1)
        
        self.btnExit = Button(ButtonFrame4,text = "الخروج",font=('arial',14,'bold'),width =10, height=2,bd=4, command = iExit)
        self.btnExit.grid(row=0, column=0)
        
        self.btnupdate = Button(ButtonFrame4,text = "تحديث الطلب",font=('arial',14,'bold'),width =9, height=2,bd=4, command = updatorders)
        self.btnupdate.grid(row=0, column=6)
        
        #tab2 LAND Button
        self.btnAddData = Button(ButtonFrame,text = "اضافة ارض",font=('arial',14,'bold'),width =10, height=2,bd=4,command =addData)
        self.btnAddData.grid(row=0, column=5)
        
        self.btnDisplayData = Button(ButtonFrame,text = "عرض كل الاراضي",font=('arial',14,'bold'),width =10, height=2,bd=4,command= Display)
        self.btnDisplayData.grid(row=0, column=4)

        self.btnclearRent = Button(ButtonFrame,text = "مسح الحقول",font=('arial',14,'bold'),width =10, height=2,bd=4, command = clearland)
        self.btnclearRent.grid(row=0, column=3)
        
        self.btnDeleterent = Button(ButtonFrame,text = "حذف الارض",font=('arial',14,'bold'),width =10, height=2,bd=4, command=Delete)
        self.btnDeleterent.grid(row=0, column=2)
        
        self.btnsearchrent = Button(ButtonFrame,text = "البحث",font=('arial',14,'bold'),width =10, height=2,bd=4, command=searchrentbase)
        self.btnsearchrent.grid(row=0, column=1)
        
        self.btnExit = Button(ButtonFrame,text = "الخروج",font=('arial',14,'bold'),width =10, height=2,bd=4, command = iExit)
        self.btnExit.grid(row=0, column=0)
        
        self.btnupdate = Button(ButtonFrame,text = "تحديث البيانات",font=('arial',14,'bold'),width =9, height=2,bd=4, command = update)
        self.btnupdate.grid(row=0, column=6)
        #tab1 RENT Button
    
        self.btnaddrent = Button(ButtonFrame1,text = "اضافة",font=('arial',14,'bold'),width =10, height=2,bd=4,command =addrent)
        self.btnaddrent.grid(row=0, column=5)
        
        self.btnrentDisplay = Button(ButtonFrame1,text = "عرض الكل",font=('arial',14,'bold'),width =10, height=2,bd=4,command= rentDisplay)
        self.btnrentDisplay.grid(row=0, column=4)

        self.btnclearRent = Button(ButtonFrame1,text = "مسح الحقول",font=('arial',14,'bold'),width =10, height=2,bd=4, command = clearRent)
        self.btnclearRent.grid(row=0, column=3)
        
        self.btnDeleterent = Button(ButtonFrame1,text = "حذف",font=('arial',14,'bold'),width =10, height=2,bd=4, command=Deleterent)
        self.btnDeleterent.grid(row=0, column=2)
        
        self.btnsearchrent = Button(ButtonFrame1,text = "البحث",font=('arial',14,'bold'),width =10, height=2,bd=4, command=searchrent)
        self.btnsearchrent.grid(row=0, column=1)
        
        self.btnExit = Button(ButtonFrame1,text = "الخروج",font=('arial',14,'bold'),width =10, height=2,bd=4, command = iExit)
        self.btnExit.grid(row=0, column=0)
        
        self.btnupdate = Button(ButtonFrame1,text = "تحديث",font=('arial',14,'bold'),width =9, height=2,bd=4, command = updatRent)
        self.btnupdate.grid(row=0, column=6)
        
        #Button Al3qar
        self.btnAddData = Button(ButtonFrame3,text = "اضافة عقار",font=('arial',14,'bold'),width =10, height=2,bd=4,command =add3qar)
        self.btnAddData.grid(row=0, column=5)
        
        self.btnDisplayData = Button(ButtonFrame3,text = "عرض الكل",font=('arial',14,'bold'),width =10, height=2,bd=4,command= Al3qartDisplay)
        self.btnDisplayData.grid(row=0, column=4)

        self.btnclearRent = Button(ButtonFrame3,text = "مسح الحقول",font=('arial',14,'bold'),width =10, height=2,bd=4, command = clear3qar)
        self.btnclearRent.grid(row=0, column=3)
        
        self.btnDeleterent = Button(ButtonFrame3,text = "حذف عقار",font=('arial',14,'bold'),width =10, height=2,bd=4, command=Delete3qar)
        self.btnDeleterent.grid(row=0, column=2)
        
        self.btnsearchrent = Button(ButtonFrame3,text = "البحث",font=('arial',14,'bold'),width =10, height=2,bd=4, command=search3qar)
        self.btnsearchrent.grid(row=0, column=1)
        
        self.btnExit3 = Button(ButtonFrame3,text = "الخروج",font=('arial',14,'bold'),width =10, height=2,bd=4, command = iExit)
        self.btnExit3.grid(row=0, column=0)
        
        self.btnupdatRent = Button(ButtonFrame3,text = "تحديث العقار",font=('arial',14,'bold'),width =9, height=2,bd=4, command = updat3qar)
        self.btnupdatRent.grid(row=0, column=6)
        #Button Sql
        self.btnAddData = Button(ButtonFrame6,text = "اضافة",font=('arial',14,'bold'),width =10, height=2,bd=4,command =addSQL)
        self.btnAddData.grid(row=0, column=5)
        
        self.btnDisplayData = Button(ButtonFrame6,text = "عرض الكل",font=('arial',14,'bold'),width =10, height=2,bd=4,command= SQLDisplay)
        self.btnDisplayData.grid(row=0, column=4)

        self.btnclearRent = Button(ButtonFrame6,text = "مسح الحقول",font=('arial',14,'bold'),width =10, height=2,bd=4, command = clearSQL)
        self.btnclearRent.grid(row=0, column=3)
        
        self.btnDeleterent = Button(ButtonFrame6,text = "حذف العرض",font=('arial',14,'bold'),width =10, height=2,bd=4, command=DeleteSQL)
        self.btnDeleterent.grid(row=0, column=2)
        
        self.btnsearchrent = Button(ButtonFrame6,text = "البحث",font=('arial',14,'bold'),width =10, height=2,bd=4, command=SQLSearch)
        self.btnsearchrent.grid(row=0, column=1)
        
        self.btnExit3 = Button(ButtonFrame6,text = "الخروج",font=('arial',14,'bold'),width =10, height=2,bd=4, command = iExit)
        self.btnExit3.grid(row=0, column=0)
        
        self.btnupdatRent = Button(ButtonFrame6,text = "تحديث العرض",font=('arial',14,'bold'),width =9, height=2,bd=4, command = updatSQL)
        self.btnupdatRent.grid(row=0, column=6)
        
        ################################## END #################################################
        ################################ CLASS LOGIN ###########################################

if __name__=='__main__': 
    root = Tk()
    application = Land(root)
    root.mainloop()

    def activateTrial():
        trial_key = Key.create_trial_key("WyIyMTMzNDEiLCJiN1JuRzRqK3RaOU0yekQxa1hSWTJYN2RsT2VMWDE4UG1Ibk1yQnc5Il0=", 8703, Helpers.GetMachineCode())

        if trial_key[0] == None:
            print("An error occurred:dcdc {0}".format(trial_key[1]))
            
        RSAPubKey = "<RSAKeyValue><Modulus>1d1jyuGWHA5f767Iu9EEJN3Uy2D1SgO+5vppD8u9alJggeoJDuDNjL+6o5fMEgfacgD4OweEV+eG6IV5EbFrjJe5L2ay9Hidn6bQUt67hA8z2G112imLnN9h6CkRQFBCC6ew+M73rCSO/Phhfzs/XeYx9YeCv2HSz91HNJG/KDEXbv4bPges5ihIq5nW6Jq5MKyy4F9aN3P/HEQrtsNb+dSslkI3j9aEUufBAMoMgbSo0oUvQ1oQlvqovFqTPqwnEee7LDHUkVgV9BnJJYDw9wQUowlWuyIsokVQVRDtyXKMeBADp9L8KWFTYRELAd+EOFr14eHEDw1oGgkm1e5tkw==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>"
        auth = "WyIyMTMzNDEiLCJiN1JuRzRqK3RaOU0yekQxa1hSWTJYN2RsT2VMWDE4UG1Ibk1yQnc5Il0="
        
        result = Key.activate(token=auth,\
                                 rsa_pub_key=RSAPubKey,\
                                 product_id=8703, \
                                 key=trial_key[0],\
                                 machine_code=Helpers.GetMachineCode(),\
                                 friendly_name=socket.gethostname())
        
        if result[0] == None or not Helpers.IsOnRightMachine(result[0]):

            b = False

        else:
            license_key = result[0]
            result = tkinter.messagebox.showinfo('تنتهي الفترة التجريبية في' , str(license_key.expires))
            
            root.mainloop()
            b = True
        return b

    def newactivate():
       
        pubKey = "<RSAKeyValue><Modulus>1d1jyuGWHA5f767Iu9EEJN3Uy2D1SgO+5vppD8u9alJggeoJDuDNjL+6o5fMEgfacgD4OweEV+eG6IV5EbFrjJe5L2ay9Hidn6bQUt67hA8z2G112imLnN9h6CkRQFBCC6ew+M73rCSO/Phhfzs/XeYx9YeCv2HSz91HNJG/KDEXbv4bPges5ihIq5nW6Jq5MKyy4F9aN3P/HEQrtsNb+dSslkI3j9aEUufBAMoMgbSo0oUvQ1oQlvqovFqTPqwnEee7LDHUkVgV9BnJJYDw9wQUowlWuyIsokVQVRDtyXKMeBADp9L8KWFTYRELAd+EOFr14eHEDw1oGgkm1e5tkw==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>"

        USER_code = simpledialog.askstring("تفعيل البرنـامج" , "ضع كود التفعيل الذي تم ارسالة لك ويحتوي على 20 حرف ورقم هنا")
        res = Key.activate(token="WyIyMTMzNDEiLCJiN1JuRzRqK3RaOU0yekQxa1hSWTJYN2RsT2VMWDE4UG1Ibk1yQnc5Il0=",\
                                   rsa_pub_key=pubKey,\
                                   product_id=8704, key=USER_code,machine_code=Helpers.GetMachineCode(),friendly_name=socket.gethostname())
        if res[0] == None or not Helpers.IsOnRightMachine(res[0]):
            print("An error occured: {0}".format(res[1]))
            result = tkinter.messagebox.showinfo('رمز التفعيل غير صالح' , str(format(res[1])))
            a = False

        else:
            
            license_key = res[0]
            l = (str(license_key.expires))
            d = (str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            if l < d:
                    
                result = tkinter.messagebox.showinfo('انتهت رخصك يرجى التجديد' , "تاريخ انتهاء رخصتك " +  "\n" + str(license_key.expires))        
                newactivate()
    
            else:         
                result = tkinter.messagebox.showinfo('تنتهي الرخصة في' , str(license_key.expires))
                root.mainloop()
                if res[0] != None:
                # saving license file to disk
                    with open('resources/licensefile.skm', 'w') as f:
                        f.write(res[0].save_as_string())   
                a = True
            
        return a 
            
    def check():

        file = "resources/licensefile.skm"
        if os.path.isfile(file)==True:
        

            with open('resources/licensefile.skm', 'r') as f:
                pubKey = "<RSAKeyValue><Modulus>1d1jyuGWHA5f767Iu9EEJN3Uy2D1SgO+5vppD8u9alJggeoJDuDNjL+6o5fMEgfacgD4OweEV+eG6IV5EbFrjJe5L2ay9Hidn6bQUt67hA8z2G112imLnN9h6CkRQFBCC6ew+M73rCSO/Phhfzs/XeYx9YeCv2HSz91HNJG/KDEXbv4bPges5ihIq5nW6Jq5MKyy4F9aN3P/HEQrtsNb+dSslkI3j9aEUufBAMoMgbSo0oUvQ1oQlvqovFqTPqwnEee7LDHUkVgV9BnJJYDw9wQUowlWuyIsokVQVRDtyXKMeBADp9L8KWFTYRELAd+EOFr14eHEDw1oGgkm1e5tkw==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>"
                license_key = LicenseKey.load_from_string(pubKey, f.read()) ## you can add How many days you want before function return NoneType
        
            if not Helpers.IsOnRightMachine(license_key):####
                        
                newactivate()
                print("NOTE: This license file does not belong to this machine.")
                
            else: #compare 
                l = (str(license_key.expires))
                d = (str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
                if l < d:
                    
                    result = tkinter.messagebox.showinfo('انتهت رخصك يرجى التجديد' , "تاريخ انتهاء رخصتك " +  "\n" + str(license_key.expires))        
                    newactivate()
    
                else:         
                    result = tkinter.messagebox.showinfo('تنتهي الرخصة في' , str(license_key.expires))
                    root.mainloop()
        elif activateTrial()==True: 
            
            pass
            
        elif newactivate()==True: 
            
            pass
            
        else:
            check()
#check()