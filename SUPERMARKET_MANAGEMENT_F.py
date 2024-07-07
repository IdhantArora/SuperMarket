import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
root=tk.Tk()

canvas=tk.Canvas(root, width=2000, height=1000)
canvas.grid(columnspan=50, rowspan=50)
canvas.configure(bg='#F0F8FF')
db=mysql.connector.connect(host='localhost',user='root',password='tiger')
cursor1=db.cursor()

cursor1.execute('create database if not exists Supermarket_Management;') # For creating Database 
cursor1.execute('Use Supermarket_Management;')
# Creating Tables
cursor1.execute('Create table if not exists Items(Item_ID int not null,Item_Name varchar(20) not null,Cost_Price int not null, Selling_Price int not null);') 
cursor1.execute('Create table if not exists Staff1(ID varchar(7) not null,Name varchar(20) not null,Age int not null,Sex varchar(2) not null,Designation varchar(20)not null,Salary float not null);')
cursor1.execute('Create table if not exists Sales(Date date not null,Total_Sale float not null,Total_Profit float not null);')
cursor1.execute('Create table if not exists Offers(Offer_ID varchar(8) not null, Offers varchar(100) not null);')

# Creating tkinter window
instructions=tk.Label(root, text='ALL IN ONE SUPERMARKET', font=("Bodoni MT",50, 'bold'), fg='blue')
instructions.grid(columnspan=6, column=0, row=0)

#Creating Buttons 
but1_text=tk.StringVar()
but1_btn=tk.Button(root, textvariable=but1_text, command=lambda:Items(), font='Rakeway', bg="#20bebe", fg='black', height=2, width=20)
but1_text.set("ITEMS")#text inside button
but1_btn.grid(column=0, row=1)

but2_text=tk.StringVar()
but2_btn=tk.Button(root, textvariable=but2_text,command=lambda:Staff(), font='Rakeway', bg="#20bebe", fg='black', height=2, width=20)
but2_text.set("STAFF")
but2_btn.grid(column=1, row=1)

but4_text=tk.StringVar()
but4_btn=tk.Button(root, textvariable=but4_text, command=lambda:Offers(), font='Rakeway', bg="#20bebe", fg='black', height=2, width=20)
but4_text.set("OFFERS & DISCOUNT")
but4_btn.grid(column=2, row=1)

but5_text=tk.StringVar()
but5_btn=tk.Button(root, textvariable=but5_text, command=lambda:Sales(), font='Rakeway', bg="#20bebe", fg='black', height=2, width=20)
but5_text.set("SALES & PROFIT")
but5_btn.grid(column=3, row=1)



###################################################################################((((Items button))))######################################################################################
def Items():        # Defining function to perform operations 
    def addno():
         
           txt11=Entry(root, width=20) #Entry provides single line text box to the user
           txt11.grid(row=4, column=1) #The Grid geometry manager puts the widgets in a 2-dimensional table.
           l11=Label(root, text='Item Code', font=15)
           l11.grid(row=4,column=0)
           but1_text=tk.StringVar()
           btn11=Button(root, text="ENTER", command=lambda:[addname(),getno()], fg="blue")
           btn11.grid(row=4,column=2)

           def getno():
               global ItemNo
               ItemNo=format(txt11.get())
               print(ItemNo)

           def addname():
               txt12=Entry(root, width=20) 
               txt12.grid(row=5, column=1) 
               l12=Label(root, text='Item Name', font=15)
               l12.grid(row=5,column=0)
               but1_text=tk.StringVar()
               btn12=Button(root, text="ENTER",command=lambda:[getname(),addcp()], fg="blue")
               btn12.grid(row=5,column=2)

               def getname():
                   global ItemName
                   ItemName=format(txt12.get())
                   print(ItemName)


               def addcp():
                   txt13=Entry(root, width=20) 
                   txt13.grid(row=6, column=1) 
                   l13=Label(root, text='Cost Price', font=15)
                   l13.grid(row=6,column=0)
                   but1_text=tk.StringVar()
                   btn13=Button(root, text="ENTER",command=lambda:[getcp(),addsp()], fg="blue")
                   btn13.grid(row=6,column=2)

                   def getcp():
                       global cp
                       cp=format(txt13.get())
                       print(cp)

                   def addsp():
                       txt14=Entry(root, width=20) 
                       txt14.grid(row=7, column=1) 
                       l14=Label(root, text='Selling Price', font=15)
                       l14.grid(row=7,column=0)
                       but1_text=tk.StringVar()
                       btn14=Button(root, text="ENTER",command=lambda:getsp(), fg="blue")
                       btn14.grid(row=7,column=2)
  
                       def getsp():
                           global sp
                           sp=format(txt14.get())
                           print(sp)

                           print(ItemNo,ItemName,cp,sp)

                           enter='insert into Items values(%s,%s,%s,%s)' # Entering data in MySql table
                           data=(ItemNo,ItemName,cp,sp)
                           cursor1.execute(enter,data)
                           db.commit()
                           print('Data entered successfully')

                           def delete():                        # To clear buttons after function is performed       
                              l11.destroy()
                              l12.destroy()
                              l13.destroy()
                              l14.destroy()
                              l15.destroy()
                              btn11.destroy()
                              btn12.destroy()
                              btn13.destroy()
                              btn14.destroy()
                              btn15.destroy()
                              txt11.destroy()
                              txt12.destroy()
                              txt13.destroy()
                              txt14.destroy()
                              btnn15.destroy()
                                                            
                           def deleteyes():
                              l11.destroy()
                              l12.destroy()
                              l13.destroy()
                              l14.destroy()
                              l15.destroy()
                              btn11.destroy()
                              btn12.destroy()
                              btn13.destroy()
                              btn14.destroy()
                              btn15.destroy()
                              txt11.destroy()
                              txt12.destroy()
                              txt13.destroy()
                              txt14.destroy()
                              btnn15.destroy()
                              
                           l15=Label(root, text='Want to add more items?', font=15)
                           l15.grid(row=8,column=0)
                           but1_text=tk.StringVar()
                           btn15=Button(root, text="Yes",command=lambda:[deleteyes(),addno()],fg="blue")   
                           btn15.grid(row=8,column=1)
                           btnn15=Button(root, text="No",command=lambda:delete(),fg="blue")
                           btnn15.grid(row=8,column=2)

                         
                                         
    but11_text=tk.StringVar()                           # Creating Sub-Buttons
    but11_btn=tk.Button(root, textvariable=but11_text, command=lambda:addno(), font='Arial', bg="pink", fg='black', height=2, width=15)
    but11_text.set("Add Items")
    but11_btn.grid(column=0, row=2)

    


    def deleit():         # Function to delete data
        txt16=Entry(root, width=20) 
        txt16.grid(row=4, column=1) 
        l16=Label(root, text='Item Code', font=15)
        l16.grid(row=4,column=0)
        but1_text=tk.StringVar()
        btn16=Button(root, text="ENTER",command=lambda:getdeleit(), fg="blue")
        btn16.grid(row=4,column=2)

        def getdeleit():
            dele=format(txt16.get())
            print(dele)
            cursor1.execute("delete from items where Item_ID='"+dele+"'")  
            db.commit()
            print('Data deleted successfully')

            def deleyesit():
                txt16.destroy()
                l16.destroy()
                btn16.destroy()
                l17.destroy()
                btn17.destroy()
                btnn17.destroy()
                
            def delenoit():
                txt16.destroy()
                l16.destroy()
                btn16.destroy()
                l17.destroy()
                btn17.destroy()
                btnn17.destroy()

            l17=Label(root, text='Want to remove more Records?', font=15)
            l17.grid(row=7,column=0)
            but1_text=tk.StringVar()
            btn17=Button(root, text="Yes",command=lambda:[deleit(),deleyesit()],fg="blue")
            btn17.grid(row=7,column=1)
            btnn17=Button(root, text="No",command=lambda:delenoit(),fg="blue")
            btnn17.grid(row=7,column=2)
     
    but12_text=tk.StringVar()
    but12_btn=tk.Button(root, textvariable=but12_text,command=lambda:deleit(), font='Arial', bg="pink", fg='black', height=2, width=15)
    but12_text.set("Delete Item")
    but12_btn.grid(column=1, row=2)


    def dis():
         label=tk.Label(root, text='Item List', font=('Arial',20)).grid(row=12,column=1,columnspan=4)
         cols=('Item_ID','Item_Name','Cost_Price','Selling_Price')
         ListBox=ttk.Treeview(root, columns=cols, show='headings')
         def show():
        
           cursor1.execute('Select Item_ID,Item_Name,Cost_Price,Selling_Price from Items;')
           records=cursor1.fetchall()
           print(records)
        
           for i, (Item_ID,Item_Name,Cost_Price,Selling_Price) in enumerate(records, start=1):
              ListBox.insert("","end",values=(Item_ID,Item_Name,Cost_Price,Selling_Price))

         for col in cols:
           ListBox.heading(col, text=col)
           ListBox.grid(row=12,column=1,columnspan=4)
         
         show()    # To print Table in tkinter window
         
    but13_text=tk.StringVar()
    but13_btn=tk.Button(root, textvariable=but13_text,command=lambda:dis(), font='Arial', bg="pink", fg='black', height=2, width=15)
    but13_text.set("Display Items")
    but13_btn.grid(column=2, row=2)

    but14_text=tk.StringVar()           # Button to clear sub-buttons
    but14_btn=tk.Button(root, textvariable=but14_text,command=lambda:clearkring(), font='Arial', bg="pink", fg='black', height=2, width=15)
    but14_text.set("Clear")
    but14_btn.grid(column=4, row=25)

    def clearkring():                
           but11_btn.destroy()
           but12_btn.destroy()
           but13_btn.destroy()
           but14_btn.destroy()

                  
#############################################################################(((STAFF BUTTON)))#########################################################################################################    

def Staff():
    def staffmem():
         
           txt21=Entry(root, width=20) 
           txt21.grid(row=4, column=1) 
           l21=Label(root, text='Name', font=15)
           l21.grid(row=4,column=0)
           but1_text=tk.StringVar()
           btn21=Button(root, text="ENTER", command=lambda:[staffage(),getstaffmem()], fg="blue")
           btn21.grid(row=4,column=2)

           def getstaffmem():
               global Name
               Name=format(txt21.get())
               print(Name)

           def staffage():
               txt22=Entry(root, width=20) 
               txt22.grid(row=5, column=1) 
               l22=Label(root, text='Age', font=15)
               l22.grid(row=5,column=0)
               but1_text=tk.StringVar()
               btn22=Button(root, text="ENTER",command=lambda:[staffdesig(),getstaffage()], fg="blue")
               btn22.grid(row=5,column=2)

               def getstaffage():
                   global Age
                   Age=format(txt22.get())
                   print(Age)

               def staffdesig():
                   txt23=Entry(root, width=20)
                   txt23.grid(row=6, column=1) 
                   l23=Label(root, text='Designation', font=15)
                   l23.grid(row=6,column=0)
                   but1_text=tk.StringVar()
                   btn23=Button(root, text="ENTER",command=lambda:[getstaffdesig(),staffsex()], fg="blue")
                   btn23.grid(row=6,column=2)

                   def getstaffdesig():
                       global Designation
                       Designation=format(txt23.get())
                       print(Designation)

                   def staffsex():
                       txt24=Entry(root, width=20) 
                       txt24.grid(row=7, column=1) 
                       l24=Label(root, text='Sex', font=15)
                       l24.grid(row=7,column=0)
                       but1_text=tk.StringVar()
                       btn24=Button(root, text="ENTER",command=lambda:[getstaffsex(),staffid()], fg="blue")
                       btn24.grid(row=7,column=2)
  
                       def getstaffsex():
                           global Sex
                           Sex=format(txt24.get())
                           print(Sex)

                        
                       def staffid():
                               txt25=Entry(root, width=20) 
                               txt25.grid(row=8, column=1) 
                               l25=Label(root, text='ID', font=15)
                               l25.grid(row=8,column=0)
                               but1_text=tk.StringVar()
                               btn25=Button(root, text="ENTER",command=lambda:[getstaffid(),staffsal()], fg="blue")
                               btn25.grid(row=8,column=2)
  
                               def getstaffid():
                                 global ID
                                 ID=format(txt25.get())
                                 print(ID)

                               def staffsal():
                                 txt26=Entry(root, width=20) 
                                 txt26.grid(row=9, column=1) 
                                 l26=Label(root, text='Salary', font=15)
                                 l26.grid(row=9,column=0)
                                 but1_text=tk.StringVar()
                                 btn26=Button(root, text="ENTER",command=lambda:getstaffsal(), fg="blue")
                                 btn26.grid(row=9,column=2)
  
                                 def getstaffsal():
                                  global Salary
                                  Salary=format(txt26.get())
                                  print(Salary)

                                  print(Name,Age,Designation,Sex,ID,Salary)

                                  enter='insert into Staff1 values(%s,%s,%s,%s,%s,%s)'  
                                  data=(ID,Name,Age,Sex,Designation,Salary)
                                  cursor1.execute(enter,data)
                                  db.commit()
                                  print('Data entered successfully')

                                  def staffdeleteno():
                                      l21.destroy()
                                      l22.destroy()
                                      l23.destroy()
                                      l24.destroy()
                                      l25.destroy()
                                      l26.destroy()
                                      l27.destroy()
                                      btn21.destroy()
                                      btn22.destroy()
                                      btn23.destroy()
                                      btn24.destroy()
                                      btn25.destroy()
                                      btn26.destroy()
                                      btn27.destroy()
                                      txt21.destroy()
                                      txt22.destroy()
                                      txt23.destroy()
                                      txt24.destroy()
                                      txt25.destroy()
                                      txt26.destroy()                                      
                                      btnn27.destroy()

                                  def staffdelyes():
                                      
                                      l21.destroy()
                                      l22.destroy()
                                      l23.destroy()
                                      l24.destroy()
                                      l25.destroy()
                                      l26.destroy()
                                      l27.destroy()
                                      btn21.destroy()
                                      btn22.destroy()
                                      btn23.destroy()
                                      btn24.destroy()
                                      btn25.destroy()
                                      btn26.destroy()
                                      btn27.destroy()
                                      txt21.destroy()
                                      txt22.destroy()
                                      txt23.destroy()
                                      txt24.destroy()
                                      txt25.destroy()
                                      txt26.destroy()                                      
                                      btnn27.destroy()
                                    
                                  l27=Label(root, text='Want to add more Members?', font=15)
                                  l27.grid(row=11,column=0)
                                  but1_text=tk.StringVar()
                                  btn27=Button(root, text="Yes",command=lambda:[staffdelyes(),staffmem()],fg="blue")
                                  btn27.grid(row=11,column=1)
                                  btnn27=Button(root, text="No",command=lambda:staffdeleteno(),fg="blue")
                                  btnn27.grid(row=11,column=2)

    but21_text=tk.StringVar()
    but21_btn=tk.Button(root, textvariable=but21_text, command=lambda:staffmem(), font='Arial', bg="pink", fg='black', height=2, width=18)
    but21_text.set("Add Staff Member")
    but21_btn.grid(column=0, row=2)

    def deles1():
        txt28=Entry(root, width=20) 
        txt28.grid(row=4, column=1) 
        l28=Label(root, text='Staff ID', font=15)
        l28.grid(row=4,column=0)
        but1_text=tk.StringVar()
        btn28=Button(root, text="ENTER",command=lambda:getdeles1(), fg="blue")
        btn28.grid(row=4,column=2)

        def getdeles1():
            deles=format(txt28.get())
            print(deles)
            cursor1.execute("delete from Staff1 where ID='"+deles+"'")  
            db.commit()
            print('Data deleted successfully')

            def deleyes():
                txt28.destroy()
                l28.destroy()
                btn28.destroy()
                l29.destroy()
                btn29.destroy()
                btnn29.destroy()
                
                
            def deleno():
                txt28.destroy()
                l28.destroy()
                btn28.destroy()
                l29.destroy()
                btn29.destroy()
                btnn29.destroy()

            l29=Label(root, text='Want to remove more Records?', font=15)
            l29.grid(row=11,column=0)
            but1_text=tk.StringVar()
            btn29=Button(root, text="Yes",command=lambda:[deles1(),deleyes()],fg="blue")
            btn29.grid(row=11,column=1)
            btnn29=Button(root, text="No",command=lambda:deleno(),fg="blue")
            btnn29.grid(row=11,column=2) 

    but22_text=tk.StringVar()
    but22_btn=tk.Button(root, textvariable=but22_text, command=lambda:deles1(), font='Arial', bg="pink", fg='black', height=2, width=18)
    but22_text.set("Delete Staff Member")
    but22_btn.grid(column=1, row=2)

    def dis():
        label=tk.Label(root, text='Staff List', font=('Arial',20)).grid(row=12,column=0,columnspan=6)
        cols=('ID','Name','Age','Sex','Designation','Salary')
        ListBox=ttk.Treeview(root, columns=cols, show='headings')
        def show():
           cursor1.execute('Select ID,Name,Age,Sex,Designation,Salary from Staff1;')
           records=cursor1.fetchall()
           print(records)
            
           for i, (ID,Name,Age,Sex,Designation,Salary) in enumerate(records, start=1):
              ListBox.insert("","end",values=(ID,Name,Age,Sex,Designation,Salary))
              
        for col in cols:
           ListBox.heading(col, text=col)
           ListBox.grid(row=12,column=0,columnspan=5)
        show()
       
    but23_text=tk.StringVar()
    but23_btn=tk.Button(root, textvariable=but23_text,command=lambda:dis(), font='Arial', bg="pink", fg='black', height=2, width=18)
    but23_text.set("Display Staff")
    but23_btn.grid(column=2, row=2)

    but24_text=tk.StringVar()
    but24_btn=tk.Button(root, textvariable=but24_text,command=lambda:clearkring(), font='Arial', bg="pink", fg='black', height=2, width=15)
    but24_text.set("Clear")
    but24_btn.grid(column=4, row=25)

    def clearkring():
           but21_btn.destroy()
           but22_btn.destroy()
           but23_btn.destroy()
           but24_btn.destroy()


#######################################################################(((OFFERS AND DISCOUNT)))############################################################################################

def Offers():
    def offerIDadd():
         
           txt31=Entry(root, width=15) 
           txt31.grid(row=4, column=1) 
           l31=Label(root, text='Offer  ID', font=15)
           l31.grid(row=4,column=0)
           but1_text=tk.StringVar()
           btn31=Button(root, text="ENTER", command=lambda:[getofferIDadd(),offerr()], fg="blue")
           btn31.grid(row=4,column=2)

           def getofferIDadd():
               global offerrid
               offerrid=format(txt31.get())
               print(offerrid)

           def offerr():
                    txt32=Entry(root, width=15) 
                    txt32.grid(row=7, column=1) 
                    l32=Label(root, text='Offer', font=15)
                    l32.grid(row=7,column=0)
                    but1_text=tk.StringVar()
                    btn32=Button(root, text="ENTER",command=lambda:getofferr(), fg="blue")
                    btn32.grid(row=7,column=2)
  
                    def getofferr():
                         global offerrr
                         offerrr=format(txt32.get())
                         print(offerrr)

                         print(offerrid,offerrr)
                       
                         enter1='insert into Offers values(%s,%s)'  
                         data1=(offerrid,offerrr)
                         cursor1.execute(enter1,data1)
                         db.commit()
                         print('Data entered successfully')

                         def nooffer():
                            txt31.destroy()
                            l31.destroy()
                            btn31.destroy()
                            txt32.destroy()
                            l32.destroy()
                            btn32.destroy()
                            l33.destroy()
                            btn33.destroy()
                            btnn33.destroy()

                         def yesoffer():
                            txt31.destroy()
                            l31.destroy()
                            btn31.destroy()
                            txt32.destroy()
                            l32.destroy()
                            btn32.destroy()
                            l33.destroy()
                            btn33.destroy()
                            btnn33.destroy()            

                         l33=Label(root, text='Want to add more?', font=15)
                         l33.grid(row=11,column=0)
                         but1_text=tk.StringVar()
                         btn33=Button(root, text="Yes",command=lambda:[yesoffer(),offerIDadd()],fg="blue")
                         btn33.grid(row=11,column=1)
                         btnn33=Button(root, text="No",command=lambda:nooffer(),fg="blue")
                         btnn33.grid(row=11,column=2)

    but31_text=tk.StringVar()
    but31_btn=tk.Button(root, textvariable=but31_text, command=lambda:offerIDadd(), font='Arial', bg="pink", fg='black', height=2, width=18)
    but31_text.set("Add Offers")
    but31_btn.grid(column=0, row=2)

    def deleoffer():
        txt32=Entry(root, width=20) 
        txt32.grid(row=4, column=1) 
        l32=Label(root, text='Offer ID', font=15)
        l32.grid(row=4,column=0)
        but1_text=tk.StringVar()
        btn32=Button(root, text="ENTER",command=lambda:getdeleoffer(), fg="blue")
        btn32.grid(row=4,column=2)

        def getdeleoffer():
            deles=format(txt32.get())
            print(deles)
            cursor1.execute("delete from Offers where Offer_ID='"+deles+"'")  
            db.commit()
            print('Data deleted successfully')
          
            def deleofyes():
                txt32.destroy()
                l32.destroy()
                btn32.destroy()
                l35.destroy()
                btn35.destroy()
                btnn35.destroy()
                               
            def deleofno():
                txt32.destroy()
                l32.destroy()
                btn32.destroy()
                l35.destroy()
                btn35.destroy()
                btnn35.destroy()

            l35=Label(root, text='Want to remove more Records?', font=15)
            l35.grid(row=11,column=0)
            but1_text=tk.StringVar()
            btn35=Button(root, text="Yes",command=lambda:[deleoffer(),deleofyes()],fg="blue")
            btn35.grid(row=11,column=1)
            btnn35=Button(root, text="No",command=lambda:deleofno(),fg="blue")
            btnn35.grid(row=11,column=2)


    but32_text=tk.StringVar()
    but32_btn=tk.Button(root, textvariable=but32_text, command=lambda:deleoffer(), font='Arial', bg="pink", fg='black', height=2, width=18)
    but32_text.set("Delete Offer")
    but32_btn.grid(column=1, row=2)

    def dis():
        label=tk.Label(root, text='Offer List', font=('Arial',20)).grid(row=12,column=0,columnspan=6)
        cols=('Offer_ID','Offers')
        ListBox=ttk.Treeview(root, columns=cols, show='headings')
        def show():
           cursor1.execute('Select Offer_ID,Offers from Offers;')
           records=cursor1.fetchall()
           print(records)
            
           for i, (Offer_ID,Offers) in enumerate(records, start=1):
              ListBox.insert("","end",values=(Offer_ID,Offers))
              
        for col in cols:
           ListBox.heading(col, text=col)
           ListBox.grid(row=12,column=0,columnspan=5)
        show()
       
    but33_text=tk.StringVar()
    but33_btn=tk.Button(root, textvariable=but33_text,command=lambda:dis(), font='Arial', bg="pink", fg='black', height=2, width=18)
    but33_text.set("Display Offers")
    but33_btn.grid(column=2, row=2)

    but34_text=tk.StringVar()
    but34_btn=tk.Button(root, textvariable=but34_text,command=lambda:clearkring(), font='Arial', bg="pink", fg='black', height=2, width=15)
    but34_text.set("Clear")
    but34_btn.grid(column=10, row=30)

    def clearkring():
           but31_btn.destroy()
           but32_btn.destroy()
           but33_btn.destroy()
           but34_btn.destroy()


###################################################################################(((SALES)))##############################################################################################

def Sales():
    def sales_date():
         
           txt41=Entry(root, width=15) 
           txt41.grid(row=4, column=1) 
           l41=Label(root, text='Sales Date in YYYY-MM-DD', font=15)
           l41.grid(row=4,column=0)
           but1_text=tk.StringVar()
           btn41=Button(root, text="ENTER", command=lambda:[getsalesdate(),salestotal()], fg="blue")
           btn41.grid(row=4,column=2)

           def getsalesdate():
               global salesdate
               salesdate=format(txt41.get())
               print(salesdate)

           def salestotal():
                    txt42=Entry(root, width=15) 
                    txt42.grid(row=6, column=1) 
                    l42=Label(root, text='Sales', font=15)
                    l42.grid(row=6,column=0)
                    but1_text=tk.StringVar()
                    btn42=Button(root, text="ENTER",command=lambda:[getsalestotal(),profittotal()], fg="blue")
                    btn42.grid(row=6,column=2)
  
                    def getsalestotal():
                         global saless
                         saless=format(txt42.get())
                         print(saless)

                    def profittotal():
                            txt43=Entry(root, width=15)
                            txt43.grid(row=8, column=1) 
                            l43=Label(root, text='Profit', font=15)
                            l43.grid(row=8,column=0)
                            but1_text=tk.StringVar()
                            btn43=Button(root, text="ENTER",command=lambda:getprofittotal(), fg="blue")
                            btn43.grid(row=8,column=2)
  
                            def getprofittotal():
                              global profitt
                              profitt=format(txt43.get())
                              print(profitt)

                              enter2='insert into Sales values(%s,%s,%s)'  
                              data2=(salesdate,saless,profitt)
                              cursor1.execute(enter2,data2)
                              db.commit()
                              print('Data entered successfully')

                              def nosales():
                                  txt41.destroy()
                                  txt42.destroy()
                                  txt43.destroy()
                                  l41.destroy()
                                  l42.destroy()
                                  l43.destroy()
                                  btn41.destroy()
                                  btn42.destroy()
                                  btn43.destroy()
                                  btnn44.destroy()

                              btnn44=Button(root, text="CLEAR",command=lambda:nosales(),fg="blue")
                              btnn44.grid(row=11,column=2)

    but41_text=tk.StringVar()
    but41_btn=tk.Button(root, textvariable=but41_text, command=lambda:sales_date(), font='Arial', bg="pink", fg='black', height=2, width=18)
    but41_text.set("Add Sales")
    but41_btn.grid(column=0, row=2)

    def tble():
        label=tk.Label(root, text='DAILY SALES AND PROFIT', font=('Arial',20)).grid(row=12,column=0,columnspan=6)
        cols=('Date','Total_Sale','Total_Profit')
        ListBox=ttk.Treeview(root, columns=cols, show='headings')
        def show():
           cursor1.execute('Select Date, Total_sale, Total_Profit from Sales;')
           records1=cursor1.fetchall()
           print(records1)
            
           for i, (Date, Total_sale, Total_Profit) in enumerate(records1, start=1):
              ListBox.insert("","end",values=(Date, Total_sale, Total_Profit))
              
        for col in cols:
           ListBox.heading(col, text=col)
           ListBox.grid(row=12,column=0,columnspan=5)
        show()

    but42_text=tk.StringVar()
    but42_btn=tk.Button(root, textvariable=but42_text, command=lambda:tble(), font='Arial', bg="pink", fg='black', height=2, width=18)
    but42_text.set("Display")
    but42_btn.grid(column=1, row=2)

    but43_text=tk.StringVar()
    but43_btn=tk.Button(root, textvariable=but43_text,command=lambda:clearkrings(), font='Arial', bg="pink", fg='black', height=2, width=15)
    but43_text.set("Clear")
    but43_btn.grid(column=10, row=25)

    def clearkrings():
           but41_btn.destroy()
           but42_btn.destroy()
           but43_btn.destroy()
           

root.mainloop()

############################################################################################################################################################################################


