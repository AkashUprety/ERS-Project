import tkinter
import datetime
import smtplib
import random
from tkinter import*
from tkinter import ttk
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import messagebox
import pymysql
import os
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import(
    FigureCanvasTkAgg,
    NavigationToolbar2Tk)

def sign():
    t=tkinter.Tk()
    t.geometry('1600x1600')
    t.configure(bg='White')
    t.title("Home")
    
    def ins():
#Canvas3
        mid_canvas=Canvas(t,width=1600,height=1600,bg='white',border=-10)
        mid_canvas.place(x=163,y=110)
        
        def plotcor():
            tb=tkinter.Tk()
            tb.geometry('700x500')
            tb.configure(bg='white')
            tb.resizable(False,False)

            
            db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
            cur=db.cursor()
            sql="select ins_name,City from Institute"
            a=[]
            b=[]
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                a.append(res[0])
                b.append(res[1])
            languages = a
            Duration = b
            
            figure=Figure(figsize=(6, 4), dpi=100)
            figure_canvas=FigureCanvasTkAgg(figure, tb)
            NavigationToolbar2Tk(figure_canvas, tb)
            axes=figure.add_subplot()
            axes.bar(languages, Duration)
            axes.set_title('Institute Name and City')
            axes.set_ylabel('City...')
            figure_canvas.get_tk_widget().place(x=0,y=0)
            
        
        #heading
        heading=Label(mid_canvas,text='Institute Insert',fg='light green',bg='white',font=('arial',45,'bold'),width=45)
        heading.place(x=-160,y=10)
    
        def savedata():
            p=InstuteId.get()
            r=Instutename.get()
            t=Instuteaddress.get()
            u=Instutecity.get()
            y=Instutemail.get() 
            x=Instutephone.get()
            z=Instuteregs.get()
            db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
            cur=db.cursor()
            if len(p)==0 or len(r)==0 or len(t)==0 or len(u)==0 or len(y)==0 or len(x)==0 or len(z)==0:
                        messagebox.showerror('Error','Check All values first')
            else:
                sql="insert into Institute values('%s','%s','%s','%s','%s','%s','%s')"%(p,r,t,u,y,x,z)
                cur.execute(sql)
                messagebox.showinfo('Saved','Data Saved')
                InstuteId.delete(0,100)
                Instutename.delete(0,100)
                Instuteaddress.delete(0,100)
                Instutecity.delete(0,100)
                Instutemail.delete(0,100)
                Instutephone.delete(0,100)
                Instuteregs.delete(0,100)
                db.commit()
                db.close()
        def cleardata():
            InstuteId.delete(0,100)
            Instutename.delete(0,100)
            Instuteaddress.delete(0,100)
            Instutecity.delete(0,100)
            Instutemail.delete(0,100)
            Instutephone.delete(0,100)
            Instuteregs.delete(0,100)
        
         #Institute Field
        def on_id(e):
            InstuteId.delete(0,100)
               
            
        def on_levid(e):
            num=InstuteId.get()
            if num==' ':
                InstuteId.insert(0,InstId)
        
        
        InstuteId=Entry(mid_canvas,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        InstuteId.place(x=430,y=100)
        InstuteId.insert(0,'INSTITUTE ID')
        InstuteId.bind('<FocusIn>',on_id)
        InstuteId.bind('<FocusOut>',on_levid)
        
        def on_nam(e):
            Instutename.delete(0,100)
            
        def on_levnam(e):
            num=Instutename.get()
            if num==' ':
                Instutename.insert(0,Instutename)
        
        Instutename=Entry(mid_canvas,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        Instutename.place(x=430,y=150)
        Instutename.insert(0,'INSTITUTE NAME')
        Instutename.bind('<FocusIn>',on_nam)
        Instutename.bind('<FocusOut>',on_levnam)
        
        def on_add(e):
            Instuteaddress.delete(0,100)
            
        def on_levadd(e):
            num=Instuteaddress.get()
            if num==' ':
                Instuteaddress.insert(0,Instuteaddress)
        
        Instuteaddress=Entry(mid_canvas,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        Instuteaddress.place(x=430,y=200)
        Instuteaddress.insert(0,'ADDRESS')
        Instuteaddress.bind('<FocusIn>',on_add)
        Instuteaddress.bind('<FocusOut>',on_levadd)
        
        def on_cit(e):
            Instutecity.delete(0,100)
            
        def on_levcit(e):
            num=Instutecity.get()
            if num==' ':
                Instutecity.insert(0,Instutecity)
        
        Instutecity=Entry(mid_canvas,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        Instutecity.place(x=430,y=250)
        Instutecity.insert(0,'CITY')
        Instutecity.bind('<FocusIn>',on_cit)
        Instutecity.bind('<FocusOut>',on_levcit)
        
        def on_mal(e):
            Instutemail.delete(0,100)
            
        def on_levmal(e):
            num=Instutemail.get()
            if num==' ':
                Instutemail.insert(0,Instutemail)
        
        Instutemail=Entry(mid_canvas,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        Instutemail.place(x=430,y=300)
        Instutemail.insert(0,'Email')
        Instutemail.bind('<FocusIn>',on_mal)
        Instutemail.bind('<FocusOut>',on_levmal)
        
        def on_pho(e):
            Instutephone.delete(0,100)
            
        def on_levpho(e):
            num=Instutephone.get()
            if num==' ':
                Instutephone.insert(0,Instutephone)
        
        Instutephone=Entry(mid_canvas,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        Instutephone.place(x=430,y=350)
        Instutephone.insert(0,'Phone no')
        Instutephone.bind('<FocusIn>',on_pho)
        Instutephone.bind('<FocusOut>',on_levpho)
        
        
        def on_pho(e):
            Instuteregs.delete(0,100)
            
        def on_levpho(e):
            num=Instuteregs.get()
            if num==' ':
                Instuteregs.insert(0,Instuteregs)
        
        Instuteregs=Entry(mid_canvas,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        Instuteregs.place(x=430,y=400)
        Instuteregs.insert(0,'REGISTRATION NO')
        Instuteregs.bind('<FocusIn>',on_pho)
        Instuteregs.bind('<FocusOut>',on_levpho)
        
        
        
        
        #Buttons
        button_ins=Button(mid_canvas,width=40,pady=7,text='Save',bg='#57a1f8',fg='white',border=0,command=savedata)
        button_ins.place(x=500,y=470)
        button1_ins=Button(mid_canvas,width=40,pady=7,text='Clear',bg='#BA55D3',fg='white',border=0,font=('Nirmala UI',10),command=cleardata)
        button1_ins.place(x=500,y=530)
        def close():
            mid_canvas.destroy()
        button_close=Button(mid_canvas,width=2,pady=2,text='X',bg='green',fg='white',border=0,font=('Nirmala UI',13),command=close)
        button_close.place(x=1170,y=0)
        button_plot=Button(mid_canvas,width=4,pady=5,text='Plot',bg='#57a1f8',fg='white',border=0,command=plotcor)
        button_plot.place(x=950,y=250)
        
        
    def update():
#Canvas4
        mid_canvas2=Canvas(t,width=1600,height=1600,bg='white',border=-10)
        mid_canvas2.place(x=163,y=110)
        
        #heading
        heading=Label(mid_canvas2,text='Institute Update',fg='light green',bg='white',font=('arial',45,'bold'),width=45)
        heading.place(x=-160,y=10)  
        def finddata():
            a=InstuteId.get()
            db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
            cur=db.cursor()
            if len(a)==0:
                 messagebox.showerror('Error','Check All values first')
            else:
                sql="select*from Institute where ins_id='%s'"%(a) 
                cur.execute(sql)
                data=cur.fetchone()
                if data==None:
                    messagebox.showinfo('Not found','No found')
                else:
                   Instutename.insert(0,data[1])
                   Instuteaddress.insert(0,data[2])
                   Instutecity.insert(0,data[3])
                   Instutemail.insert(0,data[4])
                   Instutephone.insert(0,data[5])
                   Instuteregs.insert(0,data[6])
                db.close()
        def updatedata():
            a=InstuteId.get()
            b=Instutename.get()
            c=Instuteaddress.get()
            d=Instutecity.get()
            e=Instutemail.get() 
            f=Instutephone.get()
            g=Instuteregs.get()
            db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
            cur=db.cursor()
            if len(a)==0 or len(b)==0 or len(c)==0 or len(d)==0 or len(e)==0 or len(f)==0 or len(g)==0:
                        messagebox.showerror('Error','Check All values first')
            else:
                sql="update Institute set ins_name='%s',address='%s',city='%s',email='%s',phone='%s',reg_no='%s' where ins_id='%s'" %(b,c,d,e,f,g,a)
                cur.execute(sql)
                messagebox.showinfo('Update','Update Done')
                db.commit()    
                db.close()
                InstuteId.delete(0,100)
                Instutename.delete(0,100)
                Instuteaddress.delete(0,100)
                Instutecity.delete(0,100)
                Instutemail.delete(0,100)
                Instutephone.delete(0,100)
                Instuteregs.delete(0,100)
        def cleardata():
            InstuteId.delete(0,100)
            Instutename.delete(0,100)
            Instuteaddress.delete(0,100)
            Instutecity.delete(0,100)
            Instutemail.delete(0,100)
            Instutephone.delete(0,100)
            Instuteregs.delete(0,100)
          #Institute Field
        def on_id(e):
            InstuteId.delete(0,100)
               
            
        def on_levid(e):
            num=InstuteId.get()
            if num==' ':
                InstuteId.insert(0,InstuteId)
        
        
        InstuteId=Entry(mid_canvas2,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        InstuteId.place(x=430,y=100)
        InstuteId.insert(0,'INSTITUTE ID')
        InstuteId.bind('<FocusIn>',on_id)
        InstuteId.bind('<FocusOut>',on_levid)
        
        
        
        Instutename=Entry(mid_canvas2,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        Instutename.place(x=430,y=150)
       
        
        
        
        Instuteaddress=Entry(mid_canvas2,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        Instuteaddress.place(x=430,y=200)
        
        
       
        
        Instutecity=Entry(mid_canvas2,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        Instutecity.place(x=430,y=250)
        
        
        
        
        Instutemail=Entry(mid_canvas2,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        Instutemail.place(x=430,y=300)
        
        
        
        
        Instutephone=Entry(mid_canvas2,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        Instutephone.place(x=430,y=350)
        
        
        
        
        Instuteregs=Entry(mid_canvas2,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        Instuteregs.place(x=430,y=400)
        
        
        #Buttons
        button_ins=Button(mid_canvas2,width=40,pady=7,text='Update',bg='#57a1f8',fg='white',border=0,command=updatedata)
        button_ins.place(x=500,y=470)
        button1_ins=Button(mid_canvas2,width=40,pady=7,text='Clear',bg='#BA55D3',fg='white',border=0,font=('Nirmala UI',10),command=cleardata)
        button1_ins.place(x=500,y=530)
        button1_ins=Button(mid_canvas2,width=10,pady=3,text='Find',bg='#BA55D3',fg='white',border=0,font=('Nirmala UI',10),command= finddata)
        button1_ins.place(x=350,y=100)
        def close():
            mid_canvas2.destroy()
        button_close=Button(mid_canvas2,width=2,pady=2,text='X',bg='green',fg='white',border=0,font=('Nirmala UI',13),command=close)
        button_close.place(x=1170,y=0)
        
    def find():
#Canvas5
        mid_canvas3=Canvas(t,width=1600,height=1600,bg='white',border=-10)
        mid_canvas3.place(x=163,y=110)
        
        #heading
        heading=Label(mid_canvas3,text='Institute Find',fg='light green',bg='white',font=('arial',45,'bold'),width=45)
        heading.place(x=-160,y=10)
        
        def finddata():
            a=InstuteId.get()
            db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
            cur=db.cursor()
            if len(a)==0:
                 messagebox.showerror('Error','Check All values first')
            else:
            
                
                sql="select*from Institute where ins_id='%s'"%(a) 
                cur.execute(sql)
                data=cur.fetchone()
                if data==None:
                    messagebox.showinfo('Not found','No found')
                else:
                   Instutename.insert(0,data[1])
                   Instuteaddress.insert(0,data[2])
                   Instutecity.insert(0,data[3])
                   Instutemail.insert(0,data[4])
                   Instutephone.insert(0,data[5])
                   Instuteregs.insert(0,data[6])
                db.close()
                
        def cleardata():
            InstuteId.delete(0,100)
            Instutename.delete(0,100)
            Instuteaddress.delete(0,100)
            Instutecity.delete(0,100)
            Instutemail.delete(0,100)
            Instutephone.delete(0,100)
            Instuteregs.delete(0,100)
            
    
            
        
             #Institute Field
        def on_id(e):
            InstuteId.delete(0,100)
               
            
        def on_levid(e):
            num=InstuteId.get()
            if num==' ':
                InstuteId.insert(0,InstuteId)
        
        
        InstuteId=Entry(mid_canvas3,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        InstuteId.place(x=430,y=100)
        InstuteId.insert(0,'INSTITUTE ID')
        InstuteId.bind('<FocusIn>',on_id)
        InstuteId.bind('<FocusOut>',on_levid)
        
        
        
        Instutename=Entry(mid_canvas3,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        Instutename.place(x=430,y=150)
        
        
        
        
        Instuteaddress=Entry(mid_canvas3,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        Instuteaddress.place(x=430,y=200)
        
        
        
        
        Instutecity=Entry(mid_canvas3,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        Instutecity.place(x=430,y=250)
       
        
       
        
        Instutemail=Entry(mid_canvas3,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        Instutemail.place(x=430,y=300)
       
        
        
        
        Instutephone=Entry(mid_canvas3,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        Instutephone.place(x=430,y=350)
        
        
       
        
        Instuteregs=Entry(mid_canvas3,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        Instuteregs.place(x=430,y=400)
       
        
        #Buttons
        button_ins=Button(mid_canvas3,width=40,pady=7,text='Find',bg='#57a1f8',fg='white',border=0,command=finddata)
        button_ins.place(x=500,y=470)
        button1_ins=Button(mid_canvas3,width=40,pady=7,text='Clear',bg='#BA55D3',fg='white',border=0,font=('Nirmala UI',10),command=cleardata)
        button1_ins.place(x=500,y=530)
        def close():
            mid_canvas3.destroy()
        button_close=Button(mid_canvas3,width=2,pady=2,text='X',bg='green',fg='white',border=0,font=('Nirmala UI',13),command=close)
        button_close.place(x=1170,y=0)
    def dele():
#Canvas6
        mid_canvas4=Canvas(t,width=1600,height=1600,bg='white',border=-10)
        mid_canvas4.place(x=163,y=110)
        
        #heading
        heading=Label(mid_canvas4,text='INSTUTE DELETE',fg='light green',bg='white',font=('arial',45,'bold'),width=45)
        heading.place(x=-160,y=10)
        insidlist=[]
        def deletedata():
            a=InstuteId.get()
            db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
            cur=db.cursor()
            if len(a)==0:
                messagebox.showerror('Error','Check All values first')
            else:
                
                sql="delete from Institute where ins_id='%s'"%(a) 
                cur.execute(sql)
                messagebox.showinfo('Delete','Data Delete')
                db.commit()
                db.close()
        def filldatains():
              db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
              cur=db.cursor()
              sql="select ins_id from Institute"
              cur.execute(sql)
              data= cur.fetchall()
              for res in data:
                  insidlist.append(res[0])
              db.close() 
       
                
        InstuteId=ttk.Combobox(mid_canvas4,width=45,font=('Microsoft YaHei UI Light',15))
        InstuteId.place(x=430,y=100)
        filldatains()
        InstuteId['values']=insidlist
         
        #Buttons
        button_ins=Button(mid_canvas4,width=40,pady=7,text='Delete',bg='#57a1f8',fg='white',border=0,command=deletedata)
        button_ins.place(x=500,y=190)
        def close():
            mid_canvas4.destroy()
        button_close=Button(mid_canvas4,width=2,pady=2,text='X',bg='green',fg='white',border=0,font=('Nirmala UI',13),command=close)
        button_close.place(x=1170,y=0) 
        
        
    def insc():
#Canvas7
        mid_canvas5=Canvas(t,width=1600,height=1600,bg='white',border=-10)
        mid_canvas5.place(x=163,y=110)
        
        
        def plotcorcour():  
            ta=tkinter.Tk()
            ta.geometry('700x500')
            ta.configure(bg='white')
            ta.resizable(False,False)

            
            db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
            cur=db.cursor()
            sql="select cour_name,duration from cour"
            a=[]
            b=[]
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                a.append(res[0])
                b.append(res[1])
            languages = a
            Duration = b
            
            figure=Figure(figsize=(6, 4), dpi=100)
            figure_canvas=FigureCanvasTkAgg(figure, ta)
            NavigationToolbar2Tk(figure_canvas, ta)
            axes=figure.add_subplot()
            axes.bar(languages, Duration)
            axes.set_title('Course Name and Duration')
            axes.set_ylabel('Duration(in Hrs...)')
            figure_canvas.get_tk_widget().place(x=0,y=0)
        
        
        
        #heading
        heading=Label(mid_canvas5,text='COURSE INSERT',fg='light green',bg='white',font=('arial',45,'bold'),width=45)
        heading.place(x=-160,y=10)
        
        def savedata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
            cur=db.cursor()
            p=courseId.get()
            r=coursename.get()
            t=duration.get()
            u=fee.get()
            y=description.get()
            if len(p)==0 or len(r)==0 or len(t)==0 or len(u)==0 or len(y)==0:
                messagebox.showerror('Error','Check All values first')
            else:
                sql="insert into cour values('%s','%s','%s','%s','%s')"%(p,r,t,u,y)
                cur.execute(sql)
                messagebox.showinfo('Saved','Data Saved')
                courseId.delete(0,100)
                coursename.delete(0,100)
                duration.delete(0,100)
                fee.delete(0,100)
                description.delete(0,100)
                db.commit()
                db.close()
        def cleardata():
            courseId.delete(0,100)
            coursename.delete(0,100)
            duration.delete(0,100)
            fee.delete(0,100)
            description.delete(0,100)
            
            
            
         #Institute Field
        def on_id(e):
            courseId.delete(0,100)
               
            
        def on_levid(e):
            num=courseId.get()
            if num==' ':
                courseId.insert(0,courseId)
        
        
        courseId=Entry(mid_canvas5,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        courseId.place(x=430,y=100)
        courseId.insert(0,'COURSE ID')
        courseId.bind('<FocusIn>',on_id)
        courseId.bind('<FocusOut>',on_levid)
        
        def on_nam(e):
            coursename.delete(0,100)
            
        def on_levnam(e):
            num=coursename.get()
            if num=='':
                coursename.insert(0,coursename)
        
        coursename=Entry(mid_canvas5,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        coursename.place(x=430,y=150)
        coursename.insert(0,'COURSE NAME')
        coursename.bind('<FocusIn>',on_nam)
        coursename.bind('<FocusOut>',on_levnam)
        
        def on_add(e):
            duration.delete(0,100)
            
        def on_levadd(e):
            num=duration.get()
            if num=='':
                duration.insert(0,duration)
        
        duration=Entry(mid_canvas5,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        duration.place(x=430,y=200)
        duration.insert(0,'DURATION')
        duration.bind('<FocusIn>',on_add)
        duration.bind('<FocusOut>',on_levadd)
        
        def on_cit(e):
            fee.delete(0,100)
            
        def on_levcit(e):
            num=fee.get()
            if num==' ':
                fee.insert(0,fee)
        
        fee=Entry(mid_canvas5,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        fee.place(x=430,y=250)
        fee.insert(0,'FEES')
        fee.bind('<FocusIn>',on_cit)
        fee.bind('<FocusOut>',on_levcit)
        
        def on_mal(e):
            description.delete(0,100)
            
        def on_levmal(e):
            num=description.get()
            if num==' ':
                description.insert(0,description)
        
        description=Entry(mid_canvas5,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        description.place(x=430,y=300)
        description.insert(0,'DESCRIPTION')
        description.bind('<FocusIn>',on_mal)
        description.bind('<FocusOut>',on_levmal)
        
        #Buttons
        button_ins=Button(mid_canvas5,width=40,pady=7,text='Save',bg='#57a1f8',fg='white',border=0,command=savedata)
        button_ins.place(x=500,y=400)
        button1_ins=Button(mid_canvas5,width=40,pady=7,text='Clear',bg='#BA55D3',fg='white',border=0,font=('Nirmala UI',10),command=cleardata)
        button1_ins.place(x=500,y=450)
        def close():
            mid_canvas5.destroy()
        button_close=Button(mid_canvas5,width=2,pady=2,text='X',bg='green',fg='white',border=0,font=('Nirmala UI',13),command=close)
        button_close.place(x=1170,y=0) 
        button_plot=Button(mid_canvas5,width=4,pady=5,text='Plot',bg='#57a1f8',fg='white',border=0,command=plotcorcour)
        button_plot.place(x=950,y=250)
        
        
    def updatec():
#Canvas8
        mid_canvas6=Canvas(t,width=1600,height=1600,bg='white',border=-10)
        mid_canvas6.place(x=163,y=110)
        
        #heading
        heading=Label(mid_canvas6,text='COURSE UPDATE',fg='light green',bg='white',font=('arial',45,'bold'),width=45)
        heading.place(x=-160,y=10)
        
        def finddata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
            cur=db.cursor()
            a=courseId.get()
            if len(a)==0:
                messagebox.showerror('Error','Check All values first')
            else:
                
                sql="select*from cour where cour_id='%s'"%(a) 
                cur.execute(sql)
                data=cur.fetchone()
                if data==None:
                    messagebox.showinfo('Not found','No found')
                else:
                   coursename.insert(0,data[1])
                   duration.insert(0,data[2])
                   fee.insert(0,data[3])
                   description.insert(0,data[4])
                db.close()
        def updatedata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
            cur=db.cursor()
            a=courseId.get()
            b=coursename.get()
            c=duration.get()
            d=fee.get()
            e=description.get()
            if len(a)==0 or len(b)==0 or len(c)==0 or len(d)==0 or len(e)==0:
                messagebox.showerror('Error','Check All values first')
            else:
                
                sql="update cour set cour_name='%s',duration='%s',fee='%s',description='%s' where cour_id='%s'" %(b,c,d,e,a)
                cur.execute(sql)
                messagebox.showinfo('Update','Update Done')
                db.commit()    
                db.close()
                courseId.delete(0,100)
                coursename.delete(0,100)
                duration.delete(0,100)
                fee.delete(0,100)
                description.delete(0,100)
        def cleardata():
            courseId.delete(0,100)
            coursename.delete(0,100)
            duration.delete(0,100)
            fee.delete(0,100)
            description.delete(0,100)
     #Institute Field
        def on_id(e):
            courseId.delete(0,100)
               
            
        def on_levid(e):
            num=courseId.get()
            if num==' ':
                courseId.insert(0,courseId)
        
        
        courseId=Entry(mid_canvas6,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        courseId.place(x=430,y=100)
        courseId.insert(0,'COURSE ID')
        courseId.bind('<FocusIn>',on_id)
        courseId.bind('<FocusOut>',on_levid)
        
        
        
        coursename=Entry(mid_canvas6,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        coursename.place(x=430,y=150)
        
        
       
        
        duration=Entry(mid_canvas6,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        duration.place(x=430,y=200)
        
        
       
        
        fee=Entry(mid_canvas6,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        fee.place(x=430,y=250)
        
        
        
        
        description=Entry(mid_canvas6,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        description.place(x=430,y=300)
        
        
        #Buttons
        button_ins=Button(mid_canvas6,width=40,pady=7,text='Update',bg='#57a1f8',fg='white',border=0,command=updatedata)
        button_ins.place(x=500,y=400)
        button1_ins=Button(mid_canvas6,width=40,pady=7,text='Cancel',bg='#BA55D3',fg='white',border=0,font=('Nirmala UI',10),command=cleardata)
        button1_ins.place(x=500,y=450)
        button1_ins=Button(mid_canvas6,width=10,pady=3,text='Find',bg='#BA55D3',fg='white',border=0,font=('Nirmala UI',10),command=finddata)
        button1_ins.place(x=350,y=100)
        def close():
            mid_canvas6.destroy()
        button_close=Button(mid_canvas6,width=2,pady=2,text='X',bg='green',fg='white',border=0,font=('Nirmala UI',13),command=close)
        button_close.place(x=1170,y=0) 
    def findc():
#Canvas9
        mid_canvas7=Canvas(t,width=1600,height=1600,bg='white',border=-10)
        mid_canvas7.place(x=163,y=110)
        
        #heading
        heading=Label(mid_canvas7,text='COURSE FIND',fg='light green',bg='white',font=('arial',45,'bold'),width=45)
        heading.place(x=-160,y=10)
        
        def finddata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
            cur=db.cursor()
            a=courseId.get()
            if len(a)==0:
                messagebox.showerror('Error','Check All values first')
            else:
                
                sql="select*from cour where cour_id='%s'"%(a) 
                cur.execute(sql)
                data=cur.fetchone()
                if data==None:
                    messagebox.showinfo('Not found','No found')
                else:
                   coursename.insert(0,data[1])
                   duration.insert(0,data[2])
                   fee.insert(0,data[3])
                   description.insert(0,data[4])
                db.close()
        def cleardata():
            courseId.delete(0,100)
            coursename.delete(0,100)
            duration.delete(0,100)
            fee.delete(0,100)
            description.delete(0,100)
     #Institute Field
        def on_id(e):
            courseId.delete(0,100)
               
            
        def on_levid(e):
            num=courseId.get()
            if num==' ':
                courseId.insert(0,courseId)
        
        
        courseId=Entry(mid_canvas7,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        courseId.place(x=430,y=100)
        courseId.insert(0,'COURSE ID')
        courseId.bind('<FocusIn>',on_id)
        courseId.bind('<FocusOut>',on_levid)
        
        
        
        coursename=Entry(mid_canvas7,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        coursename.place(x=430,y=150)
        
        
       
        
        duration=Entry(mid_canvas7,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        duration.place(x=430,y=200)
        
        
       
        
        fee=Entry(mid_canvas7,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        fee.place(x=430,y=250)
        
        
        
        
        description=Entry(mid_canvas7,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        description.place(x=430,y=300)
        
        
        #Buttons
        button_ins=Button(mid_canvas7,width=40,pady=7,text='Find',bg='#57a1f8',fg='white',border=0,command=finddata)
        button_ins.place(x=500,y=400)
        button1_ins=Button(mid_canvas7,width=40,pady=7,text='Clear',bg='#BA55D3',fg='white',border=0,font=('Nirmala UI',10),command=cleardata)
        button1_ins.place(x=500,y=450)
        def close():
            mid_canvas7.destroy()
        button_close=Button(mid_canvas7,width=2,pady=2,text='X',bg='green',fg='white',border=0,font=('Nirmala UI',13),command=close)
        button_close.place(x=1170,y=0)
    def delec():
#Canvas10
        mid_canvas8=Canvas(t,width=1600,height=1600,bg='white',border=-10)
        mid_canvas8.place(x=163,y=110)
        
        #heading
        heading=Label(mid_canvas8,text='COURSE DELETE',fg='light green',bg='white',font=('arial',45,'bold'),width=45)
        heading.place(x=-160,y=10)
        
        def deletedata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
            cur=db.cursor()
            a=courseId.get()
            if len(a)==0:
                messagebox.showerror('Error','Check All values first')
            else:
                
                sql="delete from cour where cour_id='%s'"%(a) 
                cur.execute(sql)
                messagebox.showinfo('Delete','Data Delete')
                db.commit()
                db.close()
        courseId=ttk.Combobox(mid_canvas8,width=45,font=('Microsoft YaHei UI Light',15))
        courseId.place(x=430,y=100)
        
         #Buttons
        button_ins=Button(mid_canvas8,width=40,pady=7,text='Delete',bg='#57a1f8',fg='white',border=0,command=deletedata)
        button_ins.place(x=500,y=190)
        def close():
            mid_canvas8.destroy()
        button_close=Button(mid_canvas8,width=2,pady=2,text='X',bg='green',fg='white',border=0,font=('Nirmala UI',13),command=close)
        button_close.place(x=1170,y=0) 
        
    def insf():
#Canvas11
        mid_canvas9=Canvas(t,width=1600,height=1600,bg='white',border=-10)
        mid_canvas9.place(x=163,y=110)
        
        #heading
        heading=Label(mid_canvas9,text='FEE INSERT',fg='light green',bg='white',font=('arial',45,'bold'),width=45)
        heading.place(x=-160,y=10)
        def receipt():
            c55=Frame(mid_canvas9,width=500,height=900,bg='gray',border=10)
            c55.place(x=100,y=0)
            re=Label(c55,text='FEE RECEIPT',width=10,fg='black',bg='gray',font=('bold',10))
            re.place(x=200,y=20)
            re=Label(c55,text='............................................................................................',width=40,fg='black',bg='gray',font=('bold',20))
            re.place(x=0,y=40)
            a=Label(c55,text='FEE ID  = ',width=10,fg='black',bg='gray',font=('bold',10))
            a.place(x=10,y=90)
            b=Label(c55,text='Amount = ',width=10,fg='black',bg='gray',font=('bold',10))
            b.place(x=10,y=130)
            c=Label(c55,text='Installment = ',width=10,fg='black',bg='gray',font=('bold',10))
            c.place(x=10,y=170)
            p=feeId.get()
            
        
        def savedata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
            cur=db.cursor()
            p=feeId.get()
            r=amount.get()
            t=instalment.get()
            if len(p)==0 or len(r)==0 or len(t)==0:
                messagebox.showerror('Error','Check All values first')
            else:
                
                sql="insert into feeplan values('%s','%s','%s')"%(p,r,t)
                cur.execute(sql)
                messagebox.showinfo('Saved','Data Saved')
                feeId.delete(0,100)
                amount.delete(0,100)
                instalment.delete(0,100)
                db.commit()
                db.close()
        
        def cleardata():
            feeId.delete(0,100)
            amount.delete(0,100)
            instalment.delete(0,100)
        
        
        
         
        fee_id=Label(mid_canvas9,text='FEE ID',width=10,fg='black',bg='white',font=('Microsoft YaHei UI Light',15))
        fee_id.place(x=30,y=70)
        feeId=Entry(mid_canvas9,width=30,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        feeId.place(x=60,y=100)
        
        amo=Label(mid_canvas9,text='AMOUNT',width=10,fg='black',bg='white',font=('Microsoft YaHei UI Light',15))
        amo.place(x=680,y=70)
        amount=Entry(mid_canvas9,width=30,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        amount.place(x=680,y=100)
        
        inst=Label(mid_canvas9,text='INSTALMENT',width=10,fg='black',bg='white',font=('Microsoft YaHei UI Light',15))
        inst.place(x=200,y=180)
        instalment=ttk.Combobox(mid_canvas9,font=('Microsoft YaHei UI Light',15),width=30)
        instalment['values']=['1','2','3']
        instalment.place(x=200,y=210)
         
         #Buttons
        button_ins=Button(mid_canvas9,width=30,pady=7,text='Save',bg='#57a1f8',fg='white',border=0,command=savedata)
        button_ins.place(x=250,y=300)
        button1_ins=Button(mid_canvas9,width=30,pady=7,text='Clear',bg='#BA55D3',fg='white',border=0,font=('Nirmala UI',10),command=cleardata)
        button1_ins.place(x=700,y=300)
        button_print=Button(mid_canvas9,width=30,pady=7,text='Receipt',bg='red',fg='white',border=0,font=('Nirmala UI',10),command=receipt)
        button_print.place(x=500,y=400)
        
        def close():
            mid_canvas9.destroy()
        button_close=Button(mid_canvas9,width=2,pady=2,text='X',bg='green',fg='white',border=0,font=('Nirmala UI',13),command=close)
        button_close.place(x=1170,y=0)
        
    def updatef():
#Canvas12
        mid_canvas10=Canvas(t,width=1600,height=1600,bg='white',border=-10)
        mid_canvas10.place(x=163,y=110)
        
        #heading
        heading=Label(mid_canvas10,text='FEE UPDATE',fg='light green',bg='white',font=('arial',45,'bold'),width=45)
        heading.place(x=-160,y=10)
        
        def finddata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
            cur=db.cursor()
            a=feeId.get()
            if len(a)==0:
                messagebox.showerror('Error','Check All values first')
            else:
                
                sql="select*from feeplan where fee_id='%s'"%(a) 
                cur.execute(sql)
                data=cur.fetchone()
                if data==None:
                    messagebox.showinfo('Not found','No found')
                else:
                   amount.insert(0,data[1])
                   instalment.insert(0,data[2])
                db.close()
        def updatedata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
            cur=db.cursor()
            a=feeId.get()
            b=amount.get()
            c=instalment.get()
            if len(a)==0 or len(b)==0 or len(c)==0:
                messagebox.showerror('Error','Check All values first')
            else:
                
                sql="update feeplan set amount='%s',installment='%s' where fee_id='%s'" %(b,c,a)
                cur.execute(sql)
                messagebox.showinfo('Update','Update Done')
                db.commit()    
                db.close()
                feeId.delete(0,100)
                amount.delete(0,100)
                instalment.delete(0,100)
        def cleardata():
            feeId.delete(0,100)
            amount.delete(0,100)
            instalment.delete(0,100)
        
         #Institute Field
        def on_id(e):
            feeId.delete(0,100)
               
            
        def on_levid(e):
            num=feeId.get()
            if num==' ':
                feeId.insert(0,feeId)
        
        
        feeId=Entry(mid_canvas10,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        feeId.place(x=430,y=100)
        feeId.insert(0,'FEE ID')
        feeId.bind('<FocusIn>',on_id)
        feeId.bind('<FocusOut>',on_levid)
        
        
        
        amount=Entry(mid_canvas10,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        amount.place(x=430,y=150)
        
        instalment=Entry(mid_canvas10,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        instalment.place(x=430,y=200)
        
        
        
         #Buttons
        button_ins=Button(mid_canvas10,width=40,pady=7,text='Update',bg='#57a1f8',fg='white',border=0,command=updatedata)
        button_ins.place(x=500,y=300)
        button1_ins=Button(mid_canvas10,width=40,pady=7,text='Clear',bg='#BA55D3',fg='white',border=0,font=('Nirmala UI',10),command=cleardata)
        button1_ins.place(x=500,y=350)
        button1_ins=Button(mid_canvas10,width=10,pady=3,text='Find',bg='#BA55D3',fg='white',border=0,font=('Nirmala UI',10),command=finddata)
        button1_ins.place(x=350,y=100)
        def close():
            mid_canvas10.destroy()
        button_close=Button(mid_canvas10,width=2,pady=2,text='X',bg='green',fg='white',border=0,font=('Nirmala UI',13),command=close)
        button_close.place(x=1170,y=0)
        
        
    def findf():
#Canvas13
        mid_canvas11=Canvas(t,width=1600,height=1600,bg='white',border=-10)
        mid_canvas11.place(x=163,y=110)
        
        #heading
        heading=Label(mid_canvas11,text='FEE FIND',fg='light green',bg='white',font=('arial',45,'bold'),width=45)
        heading.place(x=-160,y=10)
        
        def finddata():
            db=pymysql.connect(host='localhost',user='root',password='ankurroot',database='ERS')
            cur=db.cursor()
            a=feeId.get()
            sql="select*from feeplan where fee_id='%s'"%(a) 
            cur.execute(sql)
            data=cur.fetchone()
            if data==None:
                messagebox.showinfo('Not found','No found')
            else:
               amount.insert(0,data[1])
               instalment.insert(0,data[2])
            db.close()
            
        def cleardata():
            feeId.delete(0,100)
            amount.delete(0,100)
            instalment.delete(0,100)
        
        
        
         #Institute Field
        def on_id(e):
            feeId.delete(0,100)
               
            
        def on_levid(e):
            num=feeId.get()
            if num==' ':
                feeId.insert(0,feeId)
        
        
        feeId=Entry(mid_canvas11,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        feeId.place(x=430,y=100)
        feeId.insert(0,'FEE ID')
        feeId.bind('<FocusIn>',on_id)
        feeId.bind('<FocusOut>',on_levid)
        
        
        
        amount=Entry(mid_canvas11,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        amount.place(x=430,y=150)
        
        instalment=Entry(mid_canvas11,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        instalment.place(x=430,y=200)
        
        
        
         #Buttons
        button_ins=Button(mid_canvas11,width=40,pady=7,text='Find',bg='#57a1f8',fg='white',border=0,command=finddata)
        button_ins.place(x=500,y=300)
        button1_ins=Button(mid_canvas11,width=40,pady=7,text='Clear',bg='#BA55D3',fg='white',border=0,font=('Nirmala UI',10),command=cleardata)
        button1_ins.place(x=500,y=350)  
        def close():
            mid_canvas11.destroy()
        button_close=Button(mid_canvas11,width=2,pady=2,text='X',bg='green',fg='white',border=0,font=('Nirmala UI',13),command=close)
        button_close.place(x=1170,y=0) 
        
    def delef():
#Canvas14
        mid_canvas12=Canvas(t,width=1600,height=1600,bg='white',border=-10)
        mid_canvas12.place(x=163,y=110)
        
        #heading
        heading=Label(mid_canvas12,text='FEE DELETE',fg='light green',bg='white',font=('arial',45,'bold'),width=45)
        heading.place(x=-160,y=10)
        
        def deletedata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
            cur=db.cursor()
            a=feeId.get()
            if len(a)==0:
                messagebox.showerror('Error','Check All values first')
            else:
                
                sql="delete from feeplan where fee_id='%s'"%(a) 
                cur.execute(sql)
                messagebox.showinfo('Delete','Data Delete')
                db.commit()
                db.close()
            
        
        
        
         #Institute Field
        def on_id(e):
            feeId.delete(0,100)
               
            
        def on_levid(e):
            num=feeId.get()
            if num==' ':
                feeId.insert(0,feeId)
        
        
        feeId=Entry(mid_canvas12,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        feeId.place(x=430,y=100)
        feeId.insert(0,'FEE ID')
        feeId.bind('<FocusIn>',on_id)
        feeId.bind('<FocusOut>',on_levid)
        
        
         #Buttons
        button_ins=Button(mid_canvas12,width=40,pady=7,text='Find',bg='#57a1f8',fg='white',border=0,command=deletedata)
        button_ins.place(x=500,y=200) 
        def close():
            mid_canvas12.destroy()
        button_close=Button(mid_canvas12,width=2,pady=2,text='X',bg='green',fg='white',border=0,font=('Nirmala UI',13),command=close)
        button_close.place(x=1170,y=0) 
    def inse():
#Canvas15
        mid_canvas13=Canvas(t,width=1600,height=1600,bg='white',border=-10)
        mid_canvas13.place(x=163,y=110)
        
        #heading
        heading=Label(mid_canvas13,text='ENQUIRY INSERT',fg='light green',bg='white',font=('arial',45,'bold'),width=45)
        heading.place(x=-160,y=10)
        
        def savedata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
            cur=db.cursor()
            p=enqId.get()
            r=enqname.get()
            t=enqaddress.get()
            s=enqcity.get()
            v=enqmail.get()
            w=enqphone.get()
            x=enqcourseid.get()
            z=enqdate.get()
            if len(p)==0 or len(r)==0 or len(t)==0 or len(s)==0 or len(v)==0 or len(w)==0 or len(x)==0 or len(z)==0:
                messagebox.showerror('Error','Check All values first')
            else:
                
                sql="insert into enquiry values('%s','%s','%s','%s','%s','%s','%s','%s')"%(p,r,t,s,v,w,x,z)
                cur.execute(sql)
                messagebox.showinfo('Saved','Data Saved')
                enqId.delete(0,100)
                enqname.delete(0,100)
                enqaddress.delete(0,100)
                enqcity.delete(0,100)
                enqmail.delete(0,100)
                enqphone.delete(0,100)
                enqcourseid.delete(0,100)
                enqdate.delete(0,100)
                db.commit()
                db.close()
        def cleardata():
            enqId.delete(0,100)
            enqname.delete(0,100)
            enqaddress.delete(0,100)
            enqcity.delete(0,100)
            enqmail.delete(0,100)
            enqphone.delete(0,100)
            enqcourseid.delete(0,100)
            enqdate.delete(0,100)
        
        
        
        
         #Institute Field
        def on_id(e):
            enqId.delete(0,100)
               
            
        def on_levid(e):
            num=enqId.get()
            if num==' ':
                enqId.insert(0,enqId)
        
        
        enqId=Entry(mid_canvas13,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        enqId.place(x=430,y=100)
        enqId.insert(0,'Enquiry no')
        enqId.bind('<FocusIn>',on_id)
        enqId.bind('<FocusOut>',on_levid)
        
        
        def on_nam(e):
            enqname.delete(0,100)
            
        def on_levnam(e):
            num=enqname.get()
            if num==' ':
                enqname.insert(0,enqname)
        
        enqname=Entry(mid_canvas13,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        enqname.place(x=430,y=150)
        enqname.insert(0,'NAME')
        enqname.bind('<FocusIn>',on_nam)
        enqname.bind('<FocusOut>',on_levnam)
        
        def on_add(e):
            enqaddress.delete(0,100)
            
        def on_levadd(e):
            num=enqaddress.get()
            if num=='':
                enqaddress.insert(0,enqaddress)
        
        enqaddress=Entry(mid_canvas13,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        enqaddress.place(x=430,y=200)
        enqaddress.insert(0,'ADDRESS')
        enqaddress.bind('<FocusIn>',on_add)
        enqaddress.bind('<FocusOut>',on_levadd)
        
        def on_cit(e):
            enqcity.delete(0,100)
            
        def on_levcit(e):
            num=enqcity.get()
            if num==' ':
                enqcity.insert(0,enqcity)
        
        enqcity=Entry(mid_canvas13,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        enqcity.place(x=430,y=250)
        enqcity.insert(0,'CITY')
        enqcity.bind('<FocusIn>',on_cit)
        enqcity.bind('<FocusOut>',on_levcit)
        
        def on_mal(e):
            enqmail.delete(0,100)
            
        def on_levmal(e):
            num=enqmail.get()
            if num==' ':
                enqmail.insert(0,enqmail)
        
        enqmail=Entry(mid_canvas13,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        enqmail.place(x=430,y=300)
        enqmail.insert(0,'Email')
        enqmail.bind('<FocusIn>',on_mal)
        enqmail.bind('<FocusOut>',on_levmal)
        
        def on_pho(e):
            enqphone.delete(0,100)
            
        def on_levpho(e):
            num=enqphone.get()
            if num==' ':
                enqphone.insert(0,enqphone)
        
        enqphone=Entry(mid_canvas13,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        enqphone.place(x=430,y=350)
        enqphone.insert(0,'Phone no')
        enqphone.bind('<FocusIn>',on_pho)
        enqphone.bind('<FocusOut>',on_levpho)
        
        def on_pho(e):
            enqcourseid.delete(0,100)
            
        def on_levpho(e):
            num=enqcourseid.get()
            if num==' ':
                enqcourseid.insert(0,enqcourseid)
        
        enqcourseid=Entry(mid_canvas13,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        enqcourseid.place(x=430,y=400)
        enqcourseid.insert(0,'COURSE ID')
        enqcourseid.bind('<FocusIn>',on_pho)
        enqcourseid.bind('<FocusOut>',on_levpho)
        
        enqdate=Entry(mid_canvas13,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        enqdate.place(x=430,y=450)
        dt=datetime.datetime.now()
        ats=str(dt.day)+'-'+str(dt.month)+'-'+str(dt.year)
        enqdate.insert(0,ats)
        
        #Buttons
        button_ins=Button(mid_canvas13,width=40,pady=7,text='Save',bg='#57a1f8',fg='white',border=0,command=savedata)
        button_ins.place(x=500,y=490)
        button1_ins=Button(mid_canvas13,width=40,pady=7,text='Clear',bg='#BA55D3',fg='white',border=0,font=('Nirmala UI',10),command=cleardata)
        button1_ins.place(x=500,y=550)
        def close():
            mid_canvas13.destroy()
        button_close=Button(mid_canvas13,width=2,pady=2,text='X',bg='green',fg='white',border=0,font=('Nirmala UI',13),command=close)
        button_close.place(x=1170,y=0) 
    def updatee():
#Canvas16
        mid_canvas14=Canvas(t,width=1600,height=1600,bg='white',border=-10)
        mid_canvas14.place(x=163,y=110)
        
        #heading
        heading=Label(mid_canvas14,text='ENQUIRY UPDATE',fg='light green',bg='white',font=('arial',45,'bold'),width=45)
        heading.place(x=-160,y=10)
        
        def finddata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
            cur=db.cursor()
            a=enqId.get()
            if len(a)==0:
                messagebox.showerror('Error','Check All values first')
            else:
                
                sql="select*from enquiry where enq_no='%s'"%(a) 
                cur.execute(sql)
                data=cur.fetchone()
                if data==None:
                    messagebox.showinfo('Not found','No found')
                else:
                   enqname.insert(0,data[1])
                   enqaddress.insert(0,data[2])
                   enqcity.insert(0,data[3])
                   enqmail.insert(0,data[4])
                   enqphone.insert(0,data[5])
                   enqcourseid.insert(0,data[6])
                   enqdate.insert(0,data[7])
                db.close()
        def updatedata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
            cur=db.cursor()
            p=enqId.get()
            r=enqname.get()
            t=enqaddress.get()
            s=enqcity.get()
            v=enqmail.get()
            w=enqphone.get()
            x=enqcourseid.get()
            z=enqdate.get()
            if len(p)==0 or len(r)==0 or len(t)==0 or len(s)==0 or len(v)==0 or len(w)==0 or len(x)==0 or len(z)==0:
                messagebox.showerror('Error','Check All values first')
            else:
                
                sql="update enquiry set name='%s',address='%s',city='%s',email='%s',phone='%s',course_id='%s',dateofenquiry='%s' where enq_no='%s'" %(r,t,s,v,w,x,z,p)
                cur.execute(sql)
                messagebox.showinfo('Update','Update Done')
                db.commit()    
                db.close()
                enqId.delete(0,100)
                enqname.delete(0,100)
                enqaddress.delete(0,100)
                enqcity.delete(0,100)
                enqmail.delete(0,100)
                enqphone.delete(0,100)
                enqcourseid.delete(0,100)
                enqdate.delete(0,100)
        def cleardata():
            enqId.delete(0,100)
            enqname.delete(0,100)
            enqaddress.delete(0,100)
            enqcity.delete(0,100)
            enqmail.delete(0,100)
            enqphone.delete(0,100)
            enqcourseid.delete(0,100)
            enqdate.delete(0,100)
        
        
        
         #Institute Field
        def on_id(e):
            enqId.delete(0,100)
               
            
        def on_levid(e):
            num=enqId.get()
            if num==' ':
                enqId.insert(0,enqId)
        
        
        enqId=Entry(mid_canvas14,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        enqId.place(x=430,y=100)
        enqId.insert(0,'Enquiry no')
        enqId.bind('<FocusIn>',on_id)
        enqId.bind('<FocusOut>',on_levid)
        
        enqname=Entry(mid_canvas14,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        enqname.place(x=430,y=150)
        
        enqaddress=Entry(mid_canvas14,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        enqaddress.place(x=430,y=200)
        
        enqcity=Entry(mid_canvas14,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        enqcity.place(x=430,y=250)
        
        enqmail=Entry(mid_canvas14,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        enqmail.place(x=430,y=300)
        
        enqphone=Entry(mid_canvas14,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        enqphone.place(x=430,y=350)
        
        enqcourseid=Entry(mid_canvas14,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        enqcourseid.place(x=430,y=400)
        
        enqdate=Entry(mid_canvas14,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        enqdate.place(x=430,y=450)
       
        #Buttons
        button_ins=Button(mid_canvas14,width=40,pady=7,text='Update',bg='#57a1f8',fg='white',border=0,command=updatedata)
        button_ins.place(x=500,y=490)
        button1_ins=Button(mid_canvas14,width=40,pady=7,text='Clear',bg='#BA55D3',fg='white',border=0,font=('Nirmala UI',10),command=cleardata)
        button1_ins.place(x=500,y=550)
        button1_ins=Button(mid_canvas14,width=10,pady=3,text='Find',bg='#BA55D3',fg='white',border=0,font=('Nirmala UI',10),command=finddata)
        button1_ins.place(x=350,y=100)
        def close():
            mid_canvas14.destroy()
        button_close=Button(mid_canvas14,width=2,pady=2,text='X',bg='green',fg='white',border=0,font=('Nirmala UI',13),command=close)
        button_close.place(x=1170,y=0)
    def finde():
#Canvas17
        mid_canvas15=Canvas(t,width=1600,height=1600,bg='white',border=-10)
        mid_canvas15.place(x=163,y=110)
        
        #heading
        heading=Label(mid_canvas15,text='ENQUIRY FIND',fg='light green',bg='white',font=('arial',45,'bold'),width=45)
        heading.place(x=-160,y=10)
        
        def finddata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
            cur=db.cursor()
            a=enqId.get()
            if len(a)==0:
                messagebox.showerror('Error','Check All values first')
            else:
                
                sql="select*from enquiry where enq_no='%s'"%(a) 
                cur.execute(sql)
                data=cur.fetchone()
                if data==None:
                    messagebox.showinfo('Not found','No found')
                else:
                   enqname.insert(0,data[1])
                   enqaddress.insert(0,data[2])
                   enqcity.insert(0,data[3])
                   enqmail.insert(0,data[4])
                   enqphone.insert(0,data[5])
                   enqcourseid.insert(0,data[6])
                   enqdate.insert(0,data[7])
                db.close()
        def cleardata():
            enqId.delete(0,100)
            enqname.delete(0,100)
            enqaddress.delete(0,100)
            enqcity.delete(0,100)
            enqmail.delete(0,100)
            enqphone.delete(0,100)
            enqcourseid.delete(0,100)
            enqdate.delete(0,100)
         #Institute Field
        def on_id(e):
            enqId.delete(0,100)
               
            
        def on_levid(e):
            num=enqId.get()
            if num==' ':
                enqId.insert(0,enqId)
        
        
        enqId=Entry(mid_canvas15,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        enqId.place(x=430,y=100)
        enqId.insert(0,'Enquiry no')
        enqId.bind('<FocusIn>',on_id)
        enqId.bind('<FocusOut>',on_levid)
        
        enqname=Entry(mid_canvas15,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        enqname.place(x=430,y=150)
        
        enqaddress=Entry(mid_canvas15,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        enqaddress.place(x=430,y=200)
        
        enqcity=Entry(mid_canvas15,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        enqcity.place(x=430,y=250)
        
        enqmail=Entry(mid_canvas15,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        enqmail.place(x=430,y=300)
        
        enqphone=Entry(mid_canvas15,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        enqphone.place(x=430,y=350)
        
        enqcourseid=Entry(mid_canvas15,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        enqcourseid.place(x=430,y=400)
        
        enqdate=Entry(mid_canvas15,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        enqdate.place(x=430,y=450)
       
        #Buttons
        button_ins=Button(mid_canvas15,width=40,pady=7,text='Find',bg='#57a1f8',fg='white',border=0,command=finddata)
        button_ins.place(x=500,y=490)
        button1_ins=Button(mid_canvas15,width=40,pady=7,text='Clear',bg='#BA55D3',fg='white',border=0,font=('Nirmala UI',10),command=cleardata)
        button1_ins.place(x=500,y=550)
        def close():
            mid_canvas15.destroy()
        button_close=Button(mid_canvas15,width=2,pady=2,text='X',bg='green',fg='white',border=0,font=('Nirmala UI',13),command=close)
        button_close.place(x=1170,y=0)
       
    def delee():
#Canvas18
        mid_canvas16=Canvas(t,width=1600,height=1600,bg='white',border=-10)
        mid_canvas16.place(x=163,y=110)
        
        #heading
        heading=Label(mid_canvas16,text='ENQUIRY DELETE',fg='light green',bg='white',font=('arial',45,'bold'),width=45)
        heading.place(x=-160,y=10)
        
        def deletedata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
            cur=db.cursor()
            a=enqId.get()
            if len(a)==0:
                messagebox.showerror('Error','Check All values first')
            else:
                
                sql="delete from enquiry where enq_no='%s'"%(a) 
                cur.execute(sql)
                messagebox.showinfo('Delete','Data Delete')
                db.commit()
                db.close()
        
         #Institute Field
        def on_id(e):
            enqId.delete(0,100)
               
            
        def on_levid(e):
            num=enqId.get()
            if num==' ':
                enqId.insert(0,enqId)
        
        
        enqId=Entry(mid_canvas16,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        enqId.place(x=430,y=100)
        enqId.insert(0,'Enquiry no')
        enqId.bind('<FocusIn>',on_id)
        enqId.bind('<FocusOut>',on_levid) 
        
        #Buttons
        button_ins=Button(mid_canvas16,width=40,pady=7,text='Delete',bg='#57a1f8',fg='white',border=0,command=deletedata)
        button_ins.place(x=500,y=200)
        def close():
            mid_canvas16.destroy()
        button_close=Button(mid_canvas16,width=2,pady=2,text='X',bg='green',fg='white',border=0,font=('Nirmala UI',13),command=close)
        button_close.place(x=1170,y=0)
        
    def insb():
#Canvas19
        mid_canvas17=Canvas(t,width=1600,height=1600,bg='white',border=-10)
        mid_canvas17.place(x=163,y=110)
        
        #heading
        heading=Label(mid_canvas17,text='BATCH INSERT',fg='light green',bg='white',font=('arial',45,'bold'),width=45)
        heading.place(x=-160,y=10)
        
        def savedata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
            cur=db.cursor()
            p=batId.get()
            r=fromtime.get()
            t=totime.get()
            s=startend.get()
            if len(p)==0 or len(r)==0 or len(t)==0 or len(s)==0:
                messagebox.showerror('Error','Check All values first')
            else:
                 
                sql="insert into Batch values('%s','%s','%s','%s')"%(p,r,t,s)
                cur.execute(sql)
                messagebox.showinfo('Saved','Data Saved')
                batId.delete(0,100)
                fromtime.delete(0,100)
                totime.delete(0,100)
                startend.delete(0,100)
                db.commit()
                db.close()
        def cleardata():
            batId.delete(0,100)
            fromtime.delete(0,100)
            totime.delete(0,100)
            startend.delete(0,100)
        
        
         #Institute Field
        def on_id(e):
            batId.delete(0,100)
               
            
        def on_levid(e):
            num=batId.get()
            if num==' ':
                batId.insert(0,batId)
        
        
        batId=Entry(mid_canvas17,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        batId.place(x=430,y=100)
        batId.insert(0,'BATCH ID')
        batId.bind('<FocusIn>',on_id)
        batId.bind('<FocusOut>',on_levid)
        
        def on_nam(e):
            fromtime.delete(0,100)
            
        def on_levnam(e):
            num=fromtime.get()
            if num==' ':
                fromtime.insert(0,fromtime)
        
        fromtime=Entry(mid_canvas17,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        fromtime.place(x=430,y=150)
        fromtime.insert(0,'FROM TIME')
        fromtime.bind('<FocusIn>',on_nam)
        fromtime.bind('<FocusOut>',on_levnam)
        
        def on_nam(e):
            totime.delete(0,100)
            
        def on_levnam(e):
            num=totime.get()
            if num=='':
                totime.insert(0,totime)
        
        totime=Entry(mid_canvas17,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        totime.place(x=430,y=200)
        totime.insert(0,'TO TIME')
        totime.bind('<FocusIn>',on_nam)
        totime.bind('<FocusOut>',on_levnam)
        
        def on_nam(e):
            startend.delete(0,100)
            
        def on_levnam(e):
            num=startend.get()
            if num=='':
               startend.insert(0,startend)
        
        startend=Entry(mid_canvas17,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        startend.place(x=430,y=250)
        startend.insert(0,'START END')
        startend.bind('<FocusIn>',on_nam)
        startend.bind('<FocusOut>',on_levnam)
       
        #Buttons
        button_ins=Button(mid_canvas17,width=40,pady=7,text='Save',bg='#57a1f8',fg='white',border=0,command=savedata)
        button_ins.place(x=500,y=350)
        button1_ins=Button(mid_canvas17,width=40,pady=7,text='Clear',bg='#BA55D3',fg='white',border=0,font=('Nirmala UI',10),command=cleardata)
        button1_ins.place(x=500,y=400)
        def close():
            mid_canvas17.destroy()
        button_close=Button(mid_canvas17,width=2,pady=2,text='X',bg='green',fg='white',border=0,font=('Nirmala UI',13),command=close)
        button_close.place(x=1170,y=0)
    def updateb():
#Canvas20
        mid_canvas18=Canvas(t,width=1600,height=1600,bg='white',border=-10)
        mid_canvas18.place(x=163,y=110)
        
        #heading
        heading=Label(mid_canvas18,text='BATCH UPDATE',fg='light green',bg='white',font=('arial',45,'bold'),width=45)
        heading.place(x=-160,y=10)
        
        def finddata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
            cur=db.cursor()
            a=batId.get()
            if len(a)==0:
                messagebox.showerror('Error','Check All values first')
            else:
                sql="select*from Batch where batch_id='%s'"%(a) 
                cur.execute(sql)
                data=cur.fetchone()
                if data==None:
                    messagebox.showinfo('Not found','No found')
                else:
                   fromtime.insert(0,data[1])
                   totime.insert(0,data[2])
                   startend.insert(0,data[3])
                db.close()
        def updatedata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
            cur=db.cursor()
            p=batId.get()
            r=fromtime.get()
            t=totime.get()
            s=startend.get()
            if len(p)==0 or len(r)==0 or len(t)==0 or len(s)==0:
                messagebox.showerror('Error','Check All values first')
            else:
                 
                sql="update Batch set fromtime='%s',totime='%s',startend='%s' where batch_id='%s'" %(r,t,s,p)
                cur.execute(sql)
                messagebox.showinfo('Update','Update Done')
                db.commit()    
                db.close()
                batId.delete(0,100)
                fromtime.delete(0,100)
                totime.delete(0,100)
                startend.delete(0,100)
               
        def cleardata():
            batId.delete(0,100)
            fromtime.delete(0,100)
            totime.delete(0,100)
            startend.delete(0,100)
        
         #Institute Field
        def on_id(e):
            batId.delete(0,100)
               
            
        def on_levid(e):
            num=batId.get()
            if num==' ':
                batId.insert(0,batId)
        
        
        batId=Entry(mid_canvas18,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        batId.place(x=430,y=100)
        batId.insert(0,'BATCH ID')
        batId.bind('<FocusIn>',on_id)
        batId.bind('<FocusOut>',on_levid)
        
       
        
        fromtime=Entry(mid_canvas18,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        fromtime.place(x=430,y=150)
        
        totime=Entry(mid_canvas18,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        totime.place(x=430,y=200)
        
        
        startend=Entry(mid_canvas18,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        startend.place(x=430,y=250)
       
       
        #Buttons
        button_ins=Button(mid_canvas18,width=40,pady=7,text='Update',bg='#57a1f8',fg='white',border=0,command=updatedata)
        button_ins.place(x=500,y=350)
        button1_ins=Button(mid_canvas18,width=40,pady=7,text='Clear',bg='#BA55D3',fg='white',border=0,font=('Nirmala UI',10),command=cleardata)
        button1_ins.place(x=500,y=400)
        button1_ins=Button(mid_canvas18,width=10,pady=3,text='Find',bg='#BA55D3',fg='white',border=0,font=('Nirmala UI',10),command=finddata)
        button1_ins.place(x=350,y=100)
        def close():
            mid_canvas18.destroy()
        button_close=Button(mid_canvas18,width=2,pady=2,text='X',bg='green',fg='white',border=0,font=('Nirmala UI',13),command=close)
        button_close.place(x=1170,y=0) 
    def findb():
#Canvas21
        mid_canvas19=Canvas(t,width=1600,height=1600,bg='white',border=-10)
        mid_canvas19.place(x=163,y=110)
        
        #heading
        heading=Label(mid_canvas19,text='BATCH FIND',fg='light green',bg='white',font=('arial',45,'bold'),width=45)
        heading.place(x=-160,y=10)
        
        def finddata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
            cur=db.cursor()
            a=batId.get()
            if len(a)==0:
                messagebox.showerror('Error','Check All values first')
            else:
                sql="select*from Batch where batch_id='%s'"%(a) 
                cur.execute(sql)
                data=cur.fetchone()
                if data==None:
                    messagebox.showinfo('Not found','No found')
                else:
                   fromtime.insert(0,data[1])
                   totime.insert(0,data[2])
                   startend.insert(0,data[3])
                   
        def cleardata():
            batId.delete(0,100)
            fromtime.delete(0,100)
            totime.delete(0,100)
            startend.delete(0,100)
        
         #Institute Field
        def on_id(e):
            batId.delete(0,100)
               
            
        def on_levid(e):
            num=batId.get()
            if num==' ':
                batId.insert(0,batId)
        
        
        batId=Entry(mid_canvas19,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        batId.place(x=430,y=100)
        batId.insert(0,'BATCH ID')
        batId.bind('<FocusIn>',on_id)
        batId.bind('<FocusOut>',on_levid)
        
       
        
        fromtime=Entry(mid_canvas19,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        fromtime.place(x=430,y=150)
        
        totime=Entry(mid_canvas19,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        totime.place(x=430,y=200)
        
        
        startend=Entry(mid_canvas19,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        startend.place(x=430,y=250)
       
       
        #Buttons
        button_ins=Button(mid_canvas19,width=40,pady=7,text='Find',bg='#57a1f8',fg='white',border=0,command=finddata)
        button_ins.place(x=500,y=350)
        button1_ins=Button(mid_canvas19,width=40,pady=7,text='Clear',bg='#BA55D3',fg='white',border=0,font=('Nirmala UI',10),command=cleardata)
        button1_ins.place(x=500,y=400)
        def close():
            mid_canvas19.destroy()
        button_close=Button(mid_canvas19,width=2,pady=2,text='X',bg='green',fg='white',border=0,font=('Nirmala UI',13),command=close)
        button_close.place(x=1170,y=0)  
        
    def deleb():
#Canvas21
        mid_canvas20=Canvas(t,width=1600,height=1600,bg='white',border=-10)
        mid_canvas20.place(x=163,y=110)
        
        #heading
        heading=Label(mid_canvas20,text='BATCH DELETE',fg='light green',bg='white',font=('arial',45,'bold'),width=45)
        heading.place(x=-160,y=10)
        
        def deletedata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
            cur=db.cursor()
            a=batId.get()
            if len(a)==0:
                messagebox.showerror('Error','Check All values first')
            else:
                
                sql="delete from Batch where batch_id='%s'"%(a) 
                cur.execute(sql)
                messagebox.showinfo('Delete','Data Delete')
                db.commit()
                db.close() 
         #Institute Field
        def on_id(e):
            batId.delete(0,100)
               
            
        def on_levid(e):
            num=batId.get()
            if num==' ':
                batId.insert(0,batId)
        
        
        batId=Entry(mid_canvas20,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        batId.place(x=430,y=100)
        batId.insert(0,'BATCH ID')
        batId.bind('<FocusIn>',on_id)
        batId.bind('<FocusOut>',on_levid)
        
         #Buttons
        button_ins=Button(mid_canvas20,width=40,pady=7,text='Delete',bg='#57a1f8',fg='white',border=0,command=deletedata)
        button_ins.place(x=500,y=200)
        def close():
            mid_canvas20.destroy()
        button_close=Button(mid_canvas20,width=2,pady=2,text='X',bg='green',fg='white',border=0,font=('Nirmala UI',13),command=close)
        button_close.place(x=1170,y=0)
        
    def insreg():
        def emailotp():
              OTP="".join([str(random.randint(0,9)) for i in range(4)])
              from_address = "akashuprety2510@gmail.com"
              to_address = w=regmail.get()
          
               # Create message container - the correct MIME type is multipart/alternative.
              msg = MIMEMultipart('alternative')
              msg['Subject'] = "OTP verification"
              msg['From'] = from_address
              msg['To'] = to_address
          
               # Create the message (HTML).
              html =  'Hello, your OTP is ' +str( OTP )
              """We are sending an email using Python and Gmail, how fun! We can fill this with html, and gmail supports a decent range of css style attributes too - https://developers.google.com/gmail/design/css#example.
               """
          
               # Record the MIME type - text/html.
              part1 = MIMEText(html, 'html')
          
               # Attach parts into message container
              msg.attach(part1)
          
               # Credentials
              username = 'akashuprety2510@gmail.com'  
              password = 'wncrmrdivojbzvjg'
          
               # Sending the email
               ## note - this smtp config worked for me, I found it googling around, you may have to tweak the # (587) to get yours to work
              server = smtplib.SMTP('smtp.gmail.com', 587) 
              server.ehlo()
              server.starttls()
              server.login(username,password)  
              server.sendmail(from_address, to_address, msg.as_string())  
              server.quit()
              messagebox.showinfo("OTP Send",'Send')
      
        
        
      
         #Mail fun for registration
        def EmailSending(p,r,t,s,v,w,x,z,b,c):
            d=regotp.get()
            if d==OTP:
                    messagebox.showinfo("Verified",'Verified')
            elif d!=OTP:
                 messagebox.showinfo("Check your otp agian.",'Error')
                 if d==OTP:
                    messagebox.showinfo("Verified",'Verified')
                 else:
                     messagebox.showinfo("Check your otp agian.",'Error')
               
            elif d==OTP:
                 from_address = "akashuprety2510@gmail.com"
                 to_address = str(w)
                 msg = MIMEMultipart('alternative')
                 msg['Subject'] = "Run Email Code"
                 msg['From'] = from_address
                 msg['To'] = to_address
                 # Create the message (HTML).
                 html = "Reg no:- "+str( p )+'\n' + "Name :-"+str( r )+'\n' + "Address:-"+str( t )+'\n' + "City:-"+str( s ) +'\n'+ "Phone no:-"+str( v )+'\n' + "Email:-"+str( w ) +'\n'+ "Course:-"+str( x )+'\n' + "BatchId:-"+str( z ) +'\n'+ "feeid:-"+str( b )+'\n' + "date of joining:-"+str( c ) 
                 part1 = MIMEText(html, 'html')
                 msg.attach(part1)
                 # Credentials
                 username = 'akashuprety2510@gmail.com'  
                 password = 'wncrmrdivojbzvjg'
                 server = smtplib.SMTP('smtp.gmail.com', 587) 
                 server.ehlo()
                 server.starttls()
                 server.login(username,password)  
                 server.sendmail(from_address, to_address, msg.as_string())  
                 server.quit()
                 messagebox.showinfo('Mail','Mail Sent')
          
            
        
      
          
#Canvas22
        mid_canvas21=Canvas(t,width=1600,height=1600,bg='white',border=-10)
        mid_canvas21.place(x=163,y=110)
        
        #heading
        heading=Label(mid_canvas21,text='REGISTRATION INSERT',fg='light green',bg='white',font=('arial',45,'bold'),width=45)
        heading.place(x=-160,y=10)
        
        def savedata():
            p=regno.get()
            r=regname.get()
            t=regaddress.get()
            s=regcity.get()
            v=regphone.get()
            w=regmail.get()
            x=regcourse.get()
            z=regbatchid.get()
            b=regfeeid.get()
            c=regdoj.get()
            db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
            cur=db.cursor()
            if len(p)==0 or len(r)==0 or len(t)==0 or len(s)==0 or len(v)==0 or len(w)==0 or len(x)==0 or len(z)==0 or len(b)==0 or len(c)==0:
                          messagebox.showerror('Error','Check All values first')
            else:
                
                sql="insert into registration values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(p,r,t,s,v,w,x,z,b,c)
                cur.execute(sql)
                messagebox.showinfo('Saved','Data Saved')
                regno.delete(0,100)
                regname.delete(0,100)
                regaddress.delete(0,100)
                regcity.delete(0,100)
                regphone.delete(0,100)
                regmail.delete(0,100)
                regcourse.delete(0,100)
                regbatchid.delete(0,100)
                regotp.delete(0,100)
                regfeeid.delete(0,100)
                regdoj.delete(0,100)
                db.commit()
                messagebox.showinfo('Status','Thankyou for registration')
                EmailSending(p,r,t,s,v,w,x,z,b,c)
        def cleardata():
            regno.delete(0,100)
            regname.delete(0,100)
            regaddress.delete(0,100)
            regcity.delete(0,100)
            regphone.delete(0,100)
            regmail.delete(0,100)
            regcourse.delete(0,100)
            regbatchid.delete(0,100)
            regotp.delete(0,100)
            regfeeid.delete(0,100)
            regdoj.delete(0,100)
        
        
        
        reg_no=Label(mid_canvas21,text='REGISTRATION NO',width=15,fg='black',bg='white',font=('Microsoft YaHei UI Light',15))
        reg_no.place(x=30,y=70)
        regno=Entry(mid_canvas21,width=30,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        regno.place(x=30,y=100)
        
        reg_name=Label(mid_canvas21,text='NAME',width=15,fg='black',bg='white',font=('Microsoft YaHei UI Light',15))
        reg_name.place(x=370,y=70)
        regname=Entry(mid_canvas21,width=30,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        regname.place(x=400,y=100)
       
        
        reg_add=Label(mid_canvas21,text='ADDRESS',width=15,fg='black',bg='white',font=('Microsoft YaHei UI Light',15))
        reg_add.place(x=750,y=70) 
        regaddress=Entry(mid_canvas21,width=30,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        regaddress.place(x=780,y=100)
        
        reg_city=Label(mid_canvas21,text='CITY',width=15,fg='black',bg='white',font=('Microsoft YaHei UI Light',15))
        reg_city.place(x=0,y=170)
        regcity=Entry(mid_canvas21,width=30,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        regcity.place(x=30,y=200)
        
        reg_phone=Label(mid_canvas21,text='PHONE NO',width=15,fg='black',bg='white',font=('Microsoft YaHei UI Light',15))
        reg_phone.place(x=370,y=170)
        regphone=Entry(mid_canvas21,width=30,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        regphone.place(x=400,y=200)
        
        #mail otp send button
        reg_mail=Label(mid_canvas21,text='Email',width=15,fg='black',bg='white',font=('Microsoft YaHei UI Light',15))
        reg_mail.place(x=720,y=170)
        regmail=Entry(mid_canvas21,width=30,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        regmail.place(x=780,y=200)
        reg_otp=Label(mid_canvas21,text='ENTER OTP',width=15,fg='black',bg='white',font=('Microsoft YaHei UI Light',15))
        reg_otp.place(x=750,y=270)
        regotp=Entry(mid_canvas21,width=30,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        regotp.place(x=780,y=300)
        
       
        reg_course=Label(mid_canvas21,text='COURSE',width=15,fg='black',bg='white',font=('Microsoft YaHei UI Light',15))
        reg_course.place(x=2,y=270)
        regcourse=Entry(mid_canvas21,width=30,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        regcourse.place(x=30,y=300)
        
        reg_batchid=Label(mid_canvas21,text='BATCH ID',width=15,fg='black',bg='white',font=('Microsoft YaHei UI Light',15))
        reg_batchid.place(x=370,y=270)
        regbatchid=Entry(mid_canvas21,width=30,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        regbatchid.place(x=400,y=300)
        
        reg_feeid=Label(mid_canvas21,text='FEE ID',width=15,fg='black',bg='white',font=('Microsoft YaHei UI Light',15))
        reg_feeid.place(x=2,y=370)
        regfeeid=Entry(mid_canvas21,width=30,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        regfeeid.place(x=30,y=400)
        
        reg_doj=Label(mid_canvas21,text='DATE OF JOINING',width=15,fg='black',bg='white',font=('Microsoft YaHei UI Light',15))
        reg_doj.place(x=400,y=370)
        regdoj=Entry(mid_canvas21,width=30,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        regdoj.place(x=400,y=400)
        dt=datetime.datetime.now()
        ats=str(dt.day)+'-'+str(dt.month)+'-'+str(dt.year)
        regdoj.insert(0,ats)
        
        
        
       
       
        #Buttons
        button_ins=Button(mid_canvas21,width=40,pady=5,text='Save',bg='#57a1f8',fg='white',border=0,command=savedata)
        button_ins.place(x=300,y=500)
        button1_ins=Button(mid_canvas21,width=40,pady=5,text='Clear',bg='#BA55D3',fg='white',border=0,font=('Nirmala UI',10),command=cleardata)
        button1_ins.place(x=850,y=500)
        def close():
            mid_canvas21.destroy()
        button_close=Button(mid_canvas21,width=2,pady=2,text='X',bg='green',fg='white',border=0,font=('Nirmala UI',13),command=close)
        button_close.place(x=1170,y=0) 
    def updatereg():
#Canvas23
        mid_canvas22=Canvas(t,width=1600,height=1600,bg='white',border=-10)
        mid_canvas22.place(x=163,y=110)
        
        #heading
        heading=Label(mid_canvas22,text='REGISTRATION UPDATE',fg='light green',bg='white',font=('arial',45,'bold'),width=45)
        heading.place(x=-160,y=10)
        
        def finddata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
            cur=db.cursor()
            a=regno.get()
            if len(a)==0:
                messagebox.showerror('Error','Check All values first')
            else:
                
                sql="select*from registration where reg_no='%s'"%(a) 
                cur.execute(sql)
                data=cur.fetchone()
                if data==None:
                    messagebox.showinfo('Not found','No found')
                else:
                   regname.insert(0,data[1])
                   regaddress.insert(0,data[2])
                   regcity.insert(0,data[3])
                   regphone.insert(0,data[4])
                   regmail.insert(0,data[5])
                   regcourse.insert(0,data[6])
                   regbatchid.insert(0,data[7])
                   regfeeid.insert(0,data[8])
                   regdoj.insert(0,data[9])
                db.close()
        def updatedata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
            cur=db.cursor()
            p=regno.get()
            r=regname.get()
            t=regaddress.get()
            s=regcity.get()
            v=regphone.get()
            w=regmail.get()
            x=regcourse.get()
            z=regbatchid.get()
            b=regfeeid.get()
            c=regdoj.get()
            if len(p)==0 or len(r)==0 or len(t)==0 or len(s)==0 or len(v)==0 or len(w)==0 or len(x)==0 or len(z)==0 or len(b)==0 or len(c)==0:
                messagebox.showerror('Error','Check All values first')
            else:
                
                sql="update registration set name='%s',address='%s',city='%s',phone='%s',email='%s',course='%s',batchid='%s',feeid='%s',dateofjoining='%s' where reg_no='%s'" %(r,t,s,v,w,x,z,b,c,p)
                cur.execute(sql)
                messagebox.showinfo('Update','Update Done')
                db.commit()    
                db.close()
                regno.delete(0,100)
                regname.delete(0,100)
                regaddress.delete(0,100)
                regcity.delete(0,100)
                regphone.delete(0,100)
                regmail.delete(0,100)
                regcourse.delete(0,100)
                regbatchid.delete(0,100)
                regfeeid.delete(0,100)
                regdoj.delete(0,100)
                
        def cleardata():
            regno.delete(0,100)
            regname.delete(0,100)
            regaddress.delete(0,100)
            regcity.delete(0,100)
            regphone.delete(0,100)
            regmail.delete(0,100)
            regcourse.delete(0,100)
            regbatchid.delete(0,100)
            regfeeid.delete(0,100)
            regdoj.delete(0,100)
        
         #Institute Field
        def on_id(e):
            regno.delete(0,100)
               
            
        def on_levid(e):
            num=regno.get()
            if num==' ':
                regno.insert(0,regno)
        
        
        regno=Entry(mid_canvas22,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',10))
        regno.place(x=430,y=100)
        regno.insert(0,'REGISTRATION NO')
        regno.bind('<FocusIn>',on_id)
        regno.bind('<FocusOut>',on_levid)
        
        
        regname=Entry(mid_canvas22,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',10))
        regname.place(x=430,y=140)
        
        regaddress=Entry(mid_canvas22,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',10))
        regaddress.place(x=430,y=180)
        
        regcity=Entry(mid_canvas22,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',10))
        regcity.place(x=430,y=220)
        
        regphone=Entry(mid_canvas22,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',10))
        regphone.place(x=430,y=260)
        
        regmail=Entry(mid_canvas22,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',10))
        regmail.place(x=430,y=300)
        
        regcourse=Entry(mid_canvas22,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',10))
        regcourse.place(x=430,y=340)
        
        regbatchid=Entry(mid_canvas22,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',10))
        regbatchid.place(x=430,y=380)
        
        regfeeid=Entry(mid_canvas22,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',10))
        regfeeid.place(x=430,y=420)
        
        regdoj=Entry(mid_canvas22,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',10))
        regdoj.place(x=430,y=460)
       
       
        #Buttons
        button_ins=Button(mid_canvas22,width=40,pady=5,text='Update',bg='#57a1f8',fg='white',border=0,command=updatedata)
        button_ins.place(x=450,y=500)
        button1_ins=Button(mid_canvas22,width=40,pady=5,text='Clear',bg='#BA55D3',fg='white',border=0,font=('Nirmala UI',10),command=cleardata)
        button1_ins.place(x=450,y=550)
        button1_ins=Button(mid_canvas22,width=10,pady=3,text='Find',bg='#BA55D3',fg='white',border=0,font=('Nirmala UI',10),command=finddata)
        button1_ins.place(x=350,y=100)
        def close():
            mid_canvas22.destroy()
        button_close=Button(mid_canvas22,width=2,pady=2,text='X',bg='green',fg='white',border=0,font=('Nirmala UI',13),command=close)
        button_close.place(x=1170,y=0) 
    def findreg():
#Canvas24
        mid_canvas23=Canvas(t,width=1600,height=1600,bg='white',border=-10)
        mid_canvas23.place(x=163,y=110)
        
        #heading
        heading=Label(mid_canvas23,text='REGISTRATION FIND',fg='light green',bg='white',font=('arial',45,'bold'),width=45)
        heading.place(x=-160,y=10)
        
        def finddata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
            cur=db.cursor()
            a=regno.get()
            if len(a)==0:
                messagebox.showerror('Error','Check All values first')
            else:
                
                sql="select*from registration where reg_no='%s'"%(a) 
                cur.execute(sql)
                data=cur.fetchone()
                if data==None:
                    messagebox.showinfo('Not found','No found')
                else:
                   regname.insert(0,data[1])
                   regaddress.insert(0,data[2])
                   regcity.insert(0,data[3])
                   regphone.insert(0,data[4])
                   regmail.insert(0,data[5])
                   regcourse.insert(0,data[6])
                   regbatchid.insert(0,data[7])
                   regfeeid.insert(0,data[8])
                   regdoj.insert(0,data[9])
                db.close()
                
        def cleardata():
            regno.delete(0,100)
            regname.delete(0,100)
            regaddress.delete(0,100)
            regcity.delete(0,100)
            regphone.delete(0,100)
            regmail.delete(0,100)
            regcourse.delete(0,100)
            regbatchid.delete(0,100)
            regfeeid.delete(0,100)
            regdoj.delete(0,100)
        
         #Institute Field
        def on_id(e):
            regno.delete(0,100)
               
            
        def on_levid(e):
            num=regno.get()
            if num==' ':
                regno.insert(0,regno)
        
        
        regno=Entry(mid_canvas23,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',10))
        regno.place(x=430,y=100)
        regno.insert(0,'REGISTRATION NO')
        regno.bind('<FocusIn>',on_id)
        regno.bind('<FocusOut>',on_levid)
        
        
        regname=Entry(mid_canvas23,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',10))
        regname.place(x=430,y=140)
        
        regaddress=Entry(mid_canvas23,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',10))
        regaddress.place(x=430,y=180)
        
        regcity=Entry(mid_canvas23,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',10))
        regcity.place(x=430,y=210)
        
        regphone=Entry(mid_canvas23,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',10))
        regphone.place(x=430,y=250)
        
        regmail=Entry(mid_canvas23,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',10))
        regmail.place(x=430,y=290)
        
        regcourse=Entry(mid_canvas23,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',10))
        regcourse.place(x=430,y=330)
        
        regbatchid=Entry(mid_canvas23,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',10))
        regbatchid.place(x=430,y=370)
        
        regfeeid=Entry(mid_canvas23,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',10))
        regfeeid.place(x=430,y=410)
        
        regdoj=Entry(mid_canvas23,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',10))
        regdoj.place(x=430,y=450)
        
         #Buttons
        button_ins=Button(mid_canvas23,width=40,pady=5,text='Find',bg='#57a1f8',fg='white',border=0,command=finddata)
        button_ins.place(x=450,y=500)
        button1_ins=Button(mid_canvas23,width=40,pady=5,text='Clear',bg='#BA55D3',fg='white',border=0,font=('Nirmala UI',10),command=cleardata)
        button1_ins.place(x=450,y=530)
        def close():
            mid_canvas23.destroy()
        button_close=Button(mid_canvas23,width=2,pady=2,text='X',bg='green',fg='white',border=0,font=('Nirmala UI',13),command=close)
        button_close.place(x=1170,y=0)
    def delereg():
#Canvas25
        mid_canvas24=Canvas(t,width=1600,height=1600,bg='white',border=-10)
        mid_canvas24.place(x=163,y=110)
        
        #heading
        heading=Label(mid_canvas24,text='REGISTRATION DELETE',fg='light green',bg='white',font=('arial',45,'bold'),width=45)
        heading.place(x=-160,y=10)
        
          
        def deletedata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
            cur=db.cursor()
            a=regno.get()
            if len(a)==0:
                messagebox.showerror('Error','Check All values first')
            else:
                
                sql="delete from registration where reg_no='%s'"%(a) 
                cur.execute(sql)
                messagebox.showinfo('Delete','Data Delete')
                db.commit()
                db.close() 
            
         #Institute Field
        def on_id(e):
            regno.delete(0,100)
               
            
        def on_levid(e):
            num=regno.get()
            if num=='':
               regno.insert(0,regno)
        
        
        regno=Entry(mid_canvas24,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
        regno.place(x=430,y=100)
        regno.insert(0,'REGISTRATION NO')
        regno.bind('<FocusIn>',on_id)
        regno.bind('<FocusOut>',on_levid)
        
         #Buttons
        button_ins=Button(mid_canvas24,width=40,pady=7,text='Delete',bg='#57a1f8',fg='white',border=0,command=deletedata)
        button_ins.place(x=500,y=200)
        def close():
            mid_canvas24.destroy()
        button_close=Button(mid_canvas24,width=2,pady=2,text='X',bg='green',fg='white',border=0,font=('Nirmala UI',13),command=close)
        button_close.place(x=1170,y=0) 
        
        
    def inscorcom():
#Canvas26
         mid_canvas25=Canvas(t,width=1600,height=1600,bg='white',border=-10)
         mid_canvas25.place(x=163,y=110)
            
            #heading
         heading=Label(mid_canvas25,text='COURSECOMPLETE INSERT',fg='light green',bg='white',font=('arial',45,'bold'),width=45)
         heading.place(x=-160,y=10)
         regidlist=[]
         def savedata():
             db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
             cur=db.cursor()
             p=regno.get()
             r=batchid.get()
             t=courid.get()
             s=doc.get()
             if len(p)==0 or len(r)==0 or len(t)==0 or len(s)==0:
                 messagebox.showerror('Error','Check All values first')
             else:
                
                sql="insert into coursecomplete values('%s','%s','%s','%s')"%(p,r,t,s)
                cur.execute(sql)
                messagebox.showinfo('Saved','Data Saved')
                regno.delete(0,100)
                batchid.delete(0,100)
                courid.delete(0,100)
                doc.delete(0,100)
                db.commit()
                db.close()
         def cleardata():
             regno.delete(0,100)
             batchid.delete(0,100)
             courid.delete(0,100)
             doc.delete(0,100)
         def filldata():
             db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
             cur=db.cursor()
             sql="select reg_no from registraction"
             cur.execute(sql)
             data= cur.fetchall()
             for res in data:
                 regidlist.append(res[0])
             db.close() 
       
         
       
         regnoa=Label(mid_canvas25,text='REGISTRATION NO',width=25,fg='black',bg='white',font=('Microsoft YaHei UI Light',15))
         regnoa.place(x=380,y=100)
         regno=ttk.Combobox(mid_canvas25,width=45,font=('Microsoft YaHei UI Light',15))
         regno.place(x=430,y=130)
         filldata()
         regno['values']=regidlist
          
         def on_nam(e):
             batchid.delete(0,100)
                
         def on_levnam(e):
             num=batchid.get()
             if num=='':
                batchid.insert(0,batchid)
            
         batchid=Entry(mid_canvas25,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
         batchid.place(x=430,y=180)
         batchid.insert(0,'BATCH ID')
         batchid.bind('<FocusIn>',on_nam)
         batchid.bind('<FocusOut>',on_levnam)
            
         def on_nam(e):
             courid.delete(0,100)
                
         def on_levnam(e):
            num=courid.get()
            if num==' ':
               courid.insert(0,courid)
            
         courid=Entry(mid_canvas25,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
         courid.place(x=430,y=230)
         courid.insert(0,'COURSE ID')
         courid.bind('<FocusIn>',on_nam)
         courid.bind('<FocusOut>',on_levnam)
            
            
         doc=Entry(mid_canvas25,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
         doc.place(x=430,y=280)
         dt=datetime.datetime.now()
         ats=str(dt.day)+'-'+str(dt.month)+'-'+str(dt.year)
         doc.insert(0,ats)
           
         #Buttons
         button_ins=Button(mid_canvas25,width=40,pady=7,text='Save',bg='#57a1f8',fg='white',border=0,command=savedata)
         button_ins.place(x=500,y=400)
         button1_ins=Button(mid_canvas25,width=40,pady=7,text='Clear',bg='#BA55D3',fg='white',border=0,font=('Nirmala UI',10),command=cleardata)
         button1_ins.place(x=500,y=440)
         def close():
            mid_canvas25.destroy()
         button_close=Button(mid_canvas25,width=2,pady=2,text='X',bg='green',fg='white',border=0,font=('Nirmala UI',13),command=close)
         button_close.place(x=1170,y=0)
         
    def updatecorcom():
#Canvas27
         mid_canvas26=Canvas(t,width=1600,height=1600,bg='white',border=-10)
         mid_canvas26.place(x=163,y=110)
            
            #heading
         heading=Label(mid_canvas26,text='COURSECOMPLETE UPDATE',fg='light green',bg='white',font=('arial',45,'bold'),width=45)
         heading.place(x=-160,y=10)
         
         def finddata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
            cur=db.cursor()
            a=regno.get()
            if len(a)==0:
                messagebox.showerror('Error','Check All values first')
            else:
                
                sql="select*from coursecomplete where reg_no='%s'"%(a) 
                cur.execute(sql)
                data=cur.fetchone()
                if data==None:
                    messagebox.showinfo('Not found','No found')
                else:
                   batchid.insert(0,data[1])
                   courid.insert(0,data[2])
                   doc.insert(0,data[3])
                db.close()
         def updatedata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
            cur=db.cursor()
            p=regno.get()
            r=batchid.get()
            t=courid.get()
            s=doc.get()
            if len(p)==0 or len(r)==0 or len(t)==0 or len(s)==0:
                messagebox.showerror('Error','Check All values first')
            else:
                
                sql="update coursecomplete set batch_id='%s',course_id='%s',dateofcomplete='%s' where reg_no='%s'" %(r,t,s,p)
                cur.execute(sql)
                messagebox.showinfo('Update','Update Done')
                db.commit()    
                db.close()
                regno.delete(0,100)
                batchid.delete(0,100)
                courid.delete(0,100)
                doc.delete(0,100)
               
         def cleardata():
            regno.delete(0,100)
            batchid.delete(0,100)
            courid.delete(0,100)
            doc.delete(0,100)
            
              #Institute Field
         def on_id(e):
             regno.delete(0,100)
                   
                
         def on_levid(e):
              num=regno.get()
              if num==' ':
                 regno.insert(0,regno)
            
            
         regno=Entry(mid_canvas26,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
         regno.place(x=430,y=100)
         regno.insert(0,'REGISTRATION NO')
         regno.bind('<FocusIn>',on_id)
         regno.bind('<FocusOut>',on_levid)
            
        
            
         batchid=Entry(mid_canvas26,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
         batchid.place(x=430,y=150)
         
            
        
            
         courid=Entry(mid_canvas26,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
         courid.place(x=430,y=200)
        
            
       
            
         doc=Entry(mid_canvas26,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
         doc.place(x=430,y=250)
        
           
         #Buttons
         button_ins=Button(mid_canvas26,width=40,pady=7,text='Update',bg='#57a1f8',fg='white',border=0,command=updatedata)
         button_ins.place(x=500,y=350)
         button1_ins=Button(mid_canvas26,width=40,pady=7,text='Clear',bg='#BA55D3',fg='white',border=0,font=('Nirmala UI',10),command=cleardata)
         button1_ins.place(x=500,y=400)
         button1_ins=Button(mid_canvas26,width=10,pady=3,text='Find',bg='#BA55D3',fg='white',border=0,font=('Nirmala UI',10),command=finddata)
         button1_ins.place(x=350,y=100)
         def close():
             mid_canvas26.destroy()
         button_close=Button(mid_canvas26,width=2,pady=2,text='X',bg='green',fg='white',border=0,font=('Nirmala UI',13),command=close)
         button_close.place(x=1170,y=0)
    def findcorcom():
#Canvas28
         mid_canvas27=Canvas(t,width=1600,height=1600,bg='white',border=-10)
         mid_canvas27.place(x=163,y=110)
            
            #heading
         heading=Label(mid_canvas27,text='COURSECOMPLETE FIND',fg='light green',bg='white',font=('arial',45,'bold'),width=45)
         heading.place(x=-160,y=10)
         
         def finddata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
            cur=db.cursor()
            a=regno.get()
            if len(a)==0:
                messagebox.showerror('Error','Check All values first')
            else:
                
                sql="select*from coursecomplete where reg_no='%s'"%(a) 
                cur.execute(sql)
                data=cur.fetchone()
                if data==None:
                    messagebox.showinfo('Not found','No found')
                else:
                   batchid.insert(0,data[1])
                   courid.insert(0,data[2])
                   doc.insert(0,data[3])
                db.close()
                
         def cleardata():
            regno.delete(0,100)
            batchid.delete(0,100)
            courid.delete(0,100)
            doc.delete(0,100)



            
              #Institute Field
         def on_id(e):
             regno.delete(0,100)
                   
                
         def on_levid(e):
              num=regno.get()
              if num==' ':
                 regno.insert(0,regno)
            
            
         regno=Entry(mid_canvas27,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
         regno.place(x=430,y=100)
         regno.insert(0,'REGISTRATION NO')
         regno.bind('<FocusIn>',on_id)
         regno.bind('<FocusOut>',on_levid)
            
        
            
         batchid=Entry(mid_canvas27,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
         batchid.place(x=430,y=150)
         
            
        
            
         courid=Entry(mid_canvas27,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
         courid.place(x=430,y=200)
        
            
       
            
         doc=Entry(mid_canvas27,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
         doc.place(x=430,y=250)
        
           
         #Buttons
         button_ins=Button(mid_canvas27,width=40,pady=7,text='Find',bg='#57a1f8',fg='white',border=0,command=finddata)
         button_ins.place(x=500,y=350)
         button1_ins=Button(mid_canvas27,width=40,pady=7,text='Clear',bg='#BA55D3',fg='white',border=0,font=('Nirmala UI',10),command=cleardata)
         button1_ins.place(x=500,y=400)
         def close():
             mid_canvas27.destroy()
         button_close=Button(mid_canvas27,width=2,pady=2,text='X',bg='green',fg='white',border=0,font=('Nirmala UI',13),command=close)
         button_close.place(x=1170,y=0) 
    def deletecorcom():
#Canvas29
         mid_canvas28=Canvas(t,width=1600,height=1600,bg='white',border=-10)
         mid_canvas28.place(x=163,y=110)
            
            #heading
         heading=Label(mid_canvas28,text='COURSECOMPLETE DELETE',fg='light green',bg='white',font=('arial',45,'bold'),width=45)
         heading.place(x=-160,y=10)
         
         def deletedata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
            cur=db.cursor()
            a=regno.get()
            if len(a)==0:
                messagebox.showerror('Error','Check All values first')
            else:
                
                sql="delete from coursecomplete where reg_no='%s'"%(a) 
                cur.execute(sql)
                messagebox.showinfo('Delete','Data Delete')
                db.commit()
                db.close() 
             
            
              #Institute Field
         def on_id(e):
             regno.delete(0,100)
                   
                
         def on_levid(e):
              num=regno.get()
              if num=='':
                 regno.insert(0,regno)
            
            
         regno=Entry(mid_canvas28,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
         regno.place(x=430,y=100)
         regno.insert(0,'REGISTRATION NO')
         regno.bind('<FocusIn>',on_id)
         regno.bind('<FocusOut>',on_levid)
         
          #Buttons
         button_ins=Button(mid_canvas28,width=40,pady=7,text='Delete',bg='#57a1f8',fg='white',border=0,command=deletedata)
         button_ins.place(x=500,y=200)
         def close():
             mid_canvas28.destroy()
         button_close=Button(mid_canvas28,width=2,pady=2,text='X',bg='green',fg='white',border=0,font=('Nirmala UI',13),command=close)
         button_close.place(x=1170,y=0)
         
    def inscertifi():
#Canvas30
         mid_canvas29=Canvas(t,width=1600,height=1600,bg='white',border=-10)
         mid_canvas29.place(x=163,y=110)
            
            #heading
         heading=Label(mid_canvas29,text='CERTIFICATEISSUE INSERT',fg='light green',bg='white',font=('arial',45,'bold'),width=45)
         heading.place(x=-160,y=10)
         regidlist=[]
         batchidlist=[]
         courselist=[]
         def savedata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
            cur=db.cursor()
            p=regno.get()
            r=batchid.get()
            t=courtxt.get()
            s=cerissue.get()
            if len(p)==0 or len(r)==0 or len(t)==0 or len(s)==0:
                messagebox.showerror('Error','Check All values first')
            else:
                
                sql="insert into certificateissue values('%s','%s','%s','%s')"%(p,r,t,s)
                cur.execute(sql)
                messagebox.showinfo('Saved','Data Saved')
                sql="delete from registration where reg_no='%s'"%(p)
                cur.execute(sql)
                messagebox.showinfo('Delete','Registration No Removed')    
                db.commit()
                db.close()
         def cleardata():
            regno.delete(0,100)
            batchid.delete(0,100)
            courtxt.delete(0,100)
            cerissue.delete(0,100)
         def filldata():
             db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
             cur=db.cursor()
             sql="select reg_no from registration"
             cur.execute(sql)
             data= cur.fetchall()
             for res in data:
                 regidlist.append(res[0])
             db.close() 
         def filldatabatch():
             db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
             cur=db.cursor()
             sql="select batch_id from batch"
             cur.execute(sql)
             data= cur.fetchall()
             for res in data:
                 batchidlist.append(res[0])
             db.close()
         def filldatacourse():
             db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
             cur=db.cursor()
             sql="select cour_name from Cour"
             cur.execute(sql)
             data= cur.fetchall()
             for res in data:
                 courselist.append(res[0])
             db.close()
         regnoa=Label(mid_canvas29,text='REGISTRATION NO',width=25,fg='black',bg='white',font=('Microsoft YaHei UI Light',15))
         regnoa.place(x=380,y=100)
         regno=ttk.Combobox(mid_canvas29,width=45,font=('Microsoft YaHei UI Light',15))
         regno.place(x=430,y=130)
         filldata()
         regno['values']=regidlist
                
         
         batchidn=Label(mid_canvas29,text='BATCH ID',width=25,fg='black',bg='white',font=('Microsoft YaHei UI Light',15))       
         batchidn.place(x=340,y=180)
         batchid=ttk.Combobox(mid_canvas29,width=45,font=('Microsoft YaHei UI Light',15))
         batchid.place(x=430,y=210)
         filldatabatch()
         batchid['values']=batchidlist
         
         
         courlabel=Label(mid_canvas29,text='COURSE',width=25,fg='black',bg='white',font=('Microsoft YaHei UI Light',15))
         courlabel.place(x=330,y=250)
         courtxt=ttk.Combobox(mid_canvas29,width=45,font=('Microsoft YaHei UI Light',15))
         courtxt.place(x=430,y=280)
         filldatacourse()
         courtxt['values']=courselist
         
         
         cerissued=Label(mid_canvas29,text='CERTIFICATE ISSUE DATE',width=25,fg='black',bg='white',font=('Microsoft YaHei UI Light',15))      
         cerissued.place(x=400,y=330)
         cerissue=Entry(mid_canvas29,width=45,border=1,bg='white',fg='black',font=('Microsoft YaHei UI Light',15))
         cerissue.place(x=430,y=380)
         dt=datetime.datetime.now()
         ats=str(dt.day)+'-'+str(dt.month)+'-'+str(dt.year)
         cerissue.insert(0,ats)
        
         
         
         #Buttons
         button_ins=Button(mid_canvas29,width=40,pady=7,text='Save',bg='#57a1f8',fg='white',border=0,command=savedata)
         button_ins.place(x=500,y=440)
         button1_ins=Button(mid_canvas29,width=40,pady=7,text='Clear',bg='#BA55D3',fg='white',border=0,font=('Nirmala UI',10),command=cleardata)
         button1_ins.place(x=500,y=480)
         def close():
             mid_canvas29.destroy()
         button_close=Button(mid_canvas29,width=2,pady=2,text='X',bg='green',fg='white',border=0,font=('Nirmala UI',13),command=close)
         button_close.place(x=1170,y=0)
         
    def updatecertifi():
#Canvas31
         mid_canvas30=Canvas(t,width=1600,height=1600,bg='white',border=-10)
         mid_canvas30.place(x=163,y=110)
            
            #heading
         heading=Label(mid_canvas30,text='CERTIFICATEISSUE UPDATE',fg='light green',bg='white',font=('arial',45,'bold'),width=45)
         heading.place(x=-160,y=10)
         
         def finddata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
            cur=db.cursor()
            a=regno.get()
            if len(a)==0:
                messagebox.showerror('Error','Check All values first')
            else:
                
                sql="select*from certificateissue where reg_no='%s'"%(a) 
                cur.execute(sql)
                data=cur.fetchone()
                if data==None:
                    messagebox.showinfo('Not found','No found')
                else:
                   batchid.insert(0,data[1])
                   cour.insert(0,data[2])
                   cerissue.insert(0,data[3])
                db.close()
         def updatedata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
            cur=db.cursor()
            p=regno.get()
            r=batchid.get()
            t=cour.get()
            s=cerissue.get()
            if len(p)==0 or len(r)==0 or len(t)==0 or len(s)==0:
                messagebox.showerror('Error','Check All values first')
            else:
                p1=int(regno.get())
                sql="update certificateissue set batch_id='%s',course='%s', certificate_issuedate='%s' where reg_no='%s'" %(r,t,s,p)
                cur.execute(sql)
                messagebox.showinfo('Update','Update Done')
                db.commit()    
                db.close()
                regno.delete(0,100)
                batchid.delete(0,100)
                cour.delete(0,100)
                cerissue.delete(0,100)
               
         def cleardata():
            regno.delete(0,100)
            batchid.delete(0,100)
            cour.delete(0,100)
            cerissue.delete(0,100)
         
            
           #Institute Field
         def on_id(e):
             regno.delete(0,100)
                       
                    
         def on_levid(e):
             num=regno.get()
             if num==' ':
                 regno.insert(0,regno)
                
                
         regno=Entry(mid_canvas30,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
         regno.place(x=430,y=100)
         regno.insert(0,'REGISTRATION NO')
         regno.bind('<FocusIn>',on_id)
         regno.bind('<FocusOut>',on_levid)
                
    
                
         batchid=Entry(mid_canvas30,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
         batchid.place(x=430,y=150)
        
                
        
                
         cour=Entry(mid_canvas30,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
         cour.place(x=430,y=200)
        
                
        
                
         cerissue=Entry(mid_canvas30,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
         cerissue.place(x=430,y=250)
        
           
         #Buttons
         button_ins=Button(mid_canvas30,width=40,pady=7,text='Update',bg='#57a1f8',fg='white',border=0,command=updatedata)
         button_ins.place(x=500,y=350)
         button1_ins=Button(mid_canvas30,width=40,pady=7,text='Clear',bg='#BA55D3',fg='white',border=0,font=('Nirmala UI',10),command=cleardata)
         button1_ins.place(x=500,y=400)
         button1_ins=Button(mid_canvas30,width=10,pady=3,text='Find',bg='#BA55D3',fg='white',border=0,font=('Nirmala UI',10),command=finddata)
         button1_ins.place(x=350,y=100)
         def close():
             mid_canvas30.destroy()
         button_close=Button(mid_canvas30,width=2,pady=2,text='X',bg='green',fg='white',border=0,font=('Nirmala UI',13),command=close)
         button_close.place(x=1170,y=0)
    
    def findcertifi():
#Canvas32
         mid_canvas31=Canvas(t,width=1600,height=1600,bg='white',border=-10)
         mid_canvas31.place(x=163,y=110)
            
            #heading
         heading=Label(mid_canvas31,text='CERTIFICATEISSUE FIND',fg='light green',bg='white',font=('arial',45,'bold'),width=45)
         heading.place(x=-160,y=10)
         
         def finddata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
            cur=db.cursor()
            a=regno.get()
            if len(a)==0:
                messagebox.showerror('Error','Check All values first')
            else:
                
                sql="select*from certificateissue where reg_no='%s'"%(a) 
                cur.execute(sql)
                data=cur.fetchone()
                if data==None:
                    messagebox.showinfo('Not found','No found')
                else:
                   batchid.insert(0,data[1])
                   cour.insert(0,data[2])
                   cerissue.insert(0,data[3])
                db.close()
                
         def cleardata():
                regno.delete(0,100)
                batchid.delete(0,100)
                cour.delete(0,100)
                cerissue.delete(0,100)
            
           #Institute Field
         def on_id(e):
             regno.delete(0,100)
                       
                    
         def on_levid(e):
             num=regno.get()
             if num==' ':
                 regno.insert(0,regno)
                
                
         regno=Entry(mid_canvas31,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
         regno.place(x=430,y=100)
         regno.insert(0,'REGISTRATION NO')
         regno.bind('<FocusIn>',on_id)
         regno.bind('<FocusOut>',on_levid)
                
    
                
         batchid=Entry(mid_canvas31,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
         batchid.place(x=430,y=150)
        
                
        
                
         cour=Entry(mid_canvas31,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
         cour.place(x=430,y=200)
        
                
        
                
         cerissue=Entry(mid_canvas31,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
         cerissue.place(x=430,y=250)
        
           
         #Buttons
         button_ins=Button(mid_canvas31,width=40,pady=7,text='Find',bg='#57a1f8',fg='white',border=0,command=finddata)
         button_ins.place(x=500,y=350)
         button1_ins=Button(mid_canvas31,width=40,pady=7,text='Clear',bg='#BA55D3',fg='white',border=0,font=('Nirmala UI',10),command=cleardata)
         button1_ins.place(x=500,y=400)  
         def close():
             mid_canvas31.destroy()
         button_close=Button(mid_canvas31,width=2,pady=2,text='X',bg='green',fg='white',border=0,font=('Nirmala UI',13),command=close)
         button_close.place(x=1170,y=0)
         
    def deletecertifi():
#Canvas33
         mid_canvas32=Canvas(t,width=1600,height=1600,bg='white',border=-10)
         mid_canvas32.place(x=163,y=110)
            
            #heading
         heading=Label(mid_canvas32,text='CERTIFICATEISSUE DELETE',fg='light green',bg='white',font=('arial',45,'bold'),width=45)
         heading.place(x=-160,y=10)
            
         def deletedata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
            cur=db.cursor()
            a=regno.get()
            if len(a)==0:
                messagebox.showerror('Error','Check All values first')
            else:
                
                sql="delete from certificateissue where reg_no='%s'"%(a) 
                cur.execute(sql)
                messagebox.showinfo('Delete','Data Delete')
                db.commit()
                db.close() 
            
         
           #Institute Field
         def on_id(e):
             regno.delete(0,100)
                       
                    
         def on_levid(e):
             num=regno.get()
             if num==' ':
                 regno.insert(0,regno)
                
                
         regno=Entry(mid_canvas32,width=45,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',15))
         regno.place(x=430,y=100)
         regno.insert(0,'REGISTRATION NO')
         regno.bind('<FocusIn>',on_id)
         regno.bind('<FocusOut>',on_levid)
         
          #Buttons
         button_ins=Button(mid_canvas32,width=40,pady=7,text='Delete',bg='#57a1f8',fg='white',border=0,command=deletedata)
         button_ins.place(x=500,y=200)
         def close():
             mid_canvas32.destroy()
         button_close=Button(mid_canvas32,width=2,pady=2,text='X',bg='green',fg='white',border=0,font=('Nirmala UI',13),command=close)
         button_close.place(x=1170,y=0)  
    
    
    def insr():
         button_insrt=Button(Top_canvas,width=28,pady=9,text='INSERT',bg='sky blue',fg='black',border=0,command=ins)
         button_insrt.place(x=30,y=35)
                
         button_update=Button(Top_canvas,width=28,pady=9,text='UPDATE',bg='sky blue',fg='black',border=0,command=update)
         button_update.place(x=330,y=35)
                
         button_find=Button(Top_canvas,width=28,pady=9,text='FIND',bg='sky blue',fg='black',border=0,command=find)
         button_find.place(x=730,y=35)
                
         button_delete=Button(Top_canvas,width=28,pady=9,text='DELETE',bg='sky blue',fg='black',border=0,command=dele)
         button_delete.place(x=1000,y=35)
    def cour():
         button_insrt=Button(Top_canvas,width=28,pady=9,text='INSERT',bg='sky blue',fg='black',border=0,command=insc)
         button_insrt.place(x=30,y=35)
                
         button_update=Button(Top_canvas,width=28,pady=9,text='UPDATE',bg='sky blue',fg='black',border=0,command=updatec)
         button_update.place(x=330,y=35)
                
         button_find=Button(Top_canvas,width=28,pady=9,text='FIND',bg='sky blue',fg='black',border=0,command=findc)
         button_find.place(x=730,y=35)
                
         button_delete=Button(Top_canvas,width=28,pady=9,text='DELETE',bg='sky blue',fg='black',border=0,command=delec)
         button_delete.place(x=1000,y=35)
         
    def fee():
         button_insrt=Button(Top_canvas,width=28,pady=9,text='INSERT',bg='sky blue',fg='black',border=0,command=insf)
         button_insrt.place(x=30,y=35)
                
         button_update=Button(Top_canvas,width=28,pady=9,text='UPDATE',bg='sky blue',fg='black',border=0,command=updatef)
         button_update.place(x=330,y=35)
                
         button_find=Button(Top_canvas,width=28,pady=9,text='FIND',bg='sky blue',fg='black',border=0,command=findf)
         button_find.place(x=730,y=35)
                
         button_delete=Button(Top_canvas,width=28,pady=9,text='DELETE',bg='sky blue',fg='black',border=0,command=delef)
         button_delete.place(x=1000,y=35)
   
    def enq():
         button_insrt=Button(Top_canvas,width=28,pady=9,text='INSERT',bg='sky blue',fg='black',border=0,command=inse)
         button_insrt.place(x=30,y=35)
                
         button_update=Button(Top_canvas,width=28,pady=9,text='UPDATE',bg='sky blue',fg='black',border=0,command=updatee)
         button_update.place(x=330,y=35)
                
         button_find=Button(Top_canvas,width=28,pady=9,text='FIND',bg='sky blue',fg='black',border=0,command=finde)
         button_find.place(x=730,y=35)
                
         button_delete=Button(Top_canvas,width=28,pady=9,text='DELETE',bg='sky blue',fg='black',border=0,command=delee)
         button_delete.place(x=1000,y=35)
         
    def batc():
         button_insrt=Button(Top_canvas,width=28,pady=9,text='INSERT',bg='skyblue',fg='black',border=0,command=insb)
         button_insrt.place(x=30,y=35)
                
         button_update=Button(Top_canvas,width=28,pady=9,text='UPDATE',bg='sky blue',fg='black',border=0,command=updateb)
         button_update.place(x=330,y=35)
                
         button_find=Button(Top_canvas,width=28,pady=9,text='FIND',bg='sky blue',fg='black',border=0,command=findb)
         button_find.place(x=730,y=35)
                
         button_delete=Button(Top_canvas,width=28,pady=9,text='DELETE',bg='sky blue',fg='black',border=0,command=deleb)
         button_delete.place(x=1000,y=35)
         
    def reg():
         button_insrt=Button(Top_canvas,width=28,pady=9,text='INSERT',bg='sky blue',fg='black',border=0,command=insreg)
         button_insrt.place(x=30,y=35)
                
         button_update=Button(Top_canvas,width=28,pady=9,text='UPDATE',bg='sky blue',fg='black',border=0,command=updatereg)
         button_update.place(x=330,y=35)
                
         button_find=Button(Top_canvas,width=28,pady=9,text='FIND',bg='sky blue',fg='black',border=0,command=findreg)
         button_find.place(x=730,y=35)
                
         button_delete=Button(Top_canvas,width=28,pady=9,text='DELETE',bg='sky blue',fg='black',border=0,command=delereg)
         button_delete.place(x=1000,y=35)
         
    def corcom():
         button_insrt=Button(Top_canvas,width=28,pady=9,text='INSERT',bg='sky blue',fg='black',border=0,command=inscorcom)
         button_insrt.place(x=30,y=35)
                
         button_update=Button(Top_canvas,width=28,pady=9,text='UPDATE',bg='sky blue',fg='black',border=0,command=updatecorcom)
         button_update.place(x=330,y=35)
                
         button_find=Button(Top_canvas,width=28,pady=9,text='FIND',bg='sky blue',fg='black',border=0,command=findcorcom)
         button_find.place(x=730,y=35)
                
         button_delete=Button(Top_canvas,width=28,pady=9,text='DELETE',bg='sky blue',fg='black',border=0,command=deletecorcom)
         button_delete.place(x=1000,y=35)
         
    def certissue():
         button_insrt=Button(Top_canvas,width=28,pady=9,text='INSERT',bg='sky blue',fg='black',border=0,command=inscertifi)
         button_insrt.place(x=30,y=35)
                
         button_update=Button(Top_canvas,width=28,pady=9,text='UPDATE',bg='sky blue',fg='black',border=0,command=updatecertifi)
         button_update.place(x=330,y=35)
                
         button_find=Button(Top_canvas,width=28,pady=9,text='FIND',bg='sky blue',fg='black',border=0,command=findcertifi)
         button_find.place(x=730,y=35)
                
         button_delete=Button(Top_canvas,width=28,pady=9,text='DELETE',bg='sky blue',fg='black',border=0,command=deletecertifi)
         button_delete.place(x=1000,y=35)
         
           
        
#Canvas2
    Top_canvas=Canvas(t,width=1600,height=130,bg='light green',border=-10)
    Top_canvas.place(x=163,y=0)
    
#Canvas
    first_canvas=Canvas(t,width=180,height=1600,bg="silver",border=-10)
    first_canvas.place(x=0,y=0)
    
    ers_label=Label(first_canvas,text='ERS!',font=('arial',50),bg="silver",fg="light green")
    ers_label.place(x=1,y=80)
    
    button_reg=Button(first_canvas,width=23,font=7,text='Registration',bg='light green',fg='white',border=0,command=reg)
    button_reg.place(x=-20,y=250)
    
            
    button_course=Button(first_canvas,width=23,font=7,text='COURSE',bg='light green',fg='white',border=0,command=cour)
    button_course.place(x=-20,y=300)
            
    button_feeplan=Button(first_canvas,width=23,font=7,text='FeePlans',bg='light green',fg='white',border=0,command=fee)
    button_feeplan.place(x=-20,y=350)
            
    button_enquiry=Button(first_canvas,width=23,font=7,text='Enquiry',bg='light green',fg='white',border=0,command=enq)
    button_enquiry.place(x=-20,y=400)
   
    button_batch=Button(first_canvas,width=23,font=7,text='BATCH',bg='light green',fg='white',border=0,command=batc)
    button_batch.place(x=-20,y=450)
    
    button_institute=Button(first_canvas,width=23,font=7,text='INSTITUTE',bg='light green',fg='white',border=0,command=insr)
    button_institute.place(x=-10,y=500)
   
            
    button_com=Button(first_canvas,width=20,font=5,text='COURSE COMPLETE',bg='light green',fg='white',border=0,command=corcom)
    button_com.place(x=-10,y=550)
            
    button_cer=Button(first_canvas,width=20,font=5,text='CERTIFICATE ISSUE',bg='light green',fg='white',border=0,command=certissue)
    button_cer.place(x=-10,y=600)
    
    def logout():
         t.withdraw()
         os.system("python log.py")
         t.destroy()
    button_out=Button(first_canvas,width=20,font=5,text='log out',bg='light green',fg='white',border=0,command=logout)
    button_out.place(x=-20,y=650)
    
    

    t.mainloop()