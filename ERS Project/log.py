import tkinter
import pymysql
from tkinter import*
from PIL import ImageTk
from Hom import*
t=tkinter.Tk()
t.geometry('950x500+280+180')
t.configure(bg='white')
t.resizable(False,False)
t.title("Sign in")
def top():
    t.withdraw()
    sign()
    t.destroy()
def che():
    db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
    cur=db.cursor()
    a=usern.get()
    b=passn_En.get()
    sql="select password from login where user='%s'"%(a)
    cur.execute(sql)
    data= cur.fetchone()
    d=data[0]
    if d==b:
        messagebox.showinfo('hi','Success')
        top()
    else:
        messagebox.showerror('Hi','Login Failed')
    db.close()  
    

      
def forgetpass():
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
        cur=db.cursor()
        a=mail.get()
        sql="select  user from login where email='%s'"%(a)
        cur.execute(sql)
        data= cur.fetchone()
        if data==None:
            messagebox.showerror('Not found','No Found')
        else:
            usern.insert(0,data[0])
        db.close()    
    def updatedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
        cur=db.cursor()
        a=usern.get()
        c=newpassn_En.get()
        sql="update login set password='%s' where user='%s'" %(c,a)
        cur.execute(sql)
        messagebox.showinfo('Forgot Password','Done')
        db.commit()    
        db.close()
     #Frame3
    c3=Frame(t,width=350,height=350,bg='white',border=0)
    c3.place(x=480,y=70)
    #heading
    heading=Label(c3,text='New Password',fg='green',bg='white',font=('Microsoft YaHei UI Light',25,'bold'))
    heading.place(x=60,y=5)
    
    
    #user Field
    def on_enter(e):
        mail.delete(0,100)
        
    def on_leave(e):
        name=mail.get()
        if name==' ':
            mail.insert(0,mail)    

    
    
    mail=Entry(c3,width=29,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',13))
    mail.place(x=30,y=80)
    mail.insert(0,'Email')
    mail.bind('<FocusIn>',on_enter)
    mail.bind('<FocusOut>',on_leave)
    Canvas(c3,width=295,height=2,bg='black').place(x=25,y=110)
    
   
    usern=Entry(c3,width=29,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',13))
    usern.place(x=30,y=150)
    Canvas(c3,width=295,height=2,bg='black').place(x=25,y=175)
    
    
    #Email Field
    def on_enter(e):
        newpassn_En.delete(0,100)
        
    def on_leave(e):
        name=newpassn_En.get()
        if name==' ':
           newpassn_En.insert(0,newpassn_En)
    
    
    newpassn_En=Entry(c3,width=29,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',13))
    newpassn_En.place(x=30,y=200)
    newpassn_En.insert(0,'New Password')
    newpassn_En.bind('<FocusIn>',on_enter)
    newpassn_En.bind('<FocusOut>',on_leave)
    Canvas(c3,width=295,height=2,bg='black').place(x=25,y=230)
    
    
    #Buttons
    button=Button(c3,width=39,pady=7,text='Save Password',bg='green',fg='white',border=0,command=updatedata)
    button.place(x=35,y=250)
    btn_find=Button(c3,width=5,height=0,text='find',fg='white',bg='green',border=0,command=finddata)
    btn_find.place(x=250,y=140)
    label=Label(c3,text="Back to login page.",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label.place(x=70,y=290)
    back_up=Button(c3,width=8,text='Back',border=-10,bg='white',cursor='hand2',fg='green',command=showlog)
    back_up.place(x=180,y=290)


#set img
img=PhotoImage(file='Ers.png')
Label(t,image=img,bg='white').place(x=50,y=50)  
#frame
c=Frame(t,width=350,height=350,bg='white',border=0)
c.place(x=480,y=70)
def showlog():
    def che():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
        cur=db.cursor()
        a=usern.get()
        b=passn_En.get()
        sql="select password from login where user='%s'"%(a)
        cur.execute(sql)
        data= cur.fetchone()
        d=data[0]
        if d==b:
            messagebox.showinfo('hi','Success')
            sign()
        else:
            messagebox.showerror('Hi','Login Failed')
        db.close()  
    c=Frame(t,width=350,height=350,bg='white',border=0)
    c.place(x=480,y=70)
    #heading
    heading=Label(c,text='Sign in',fg='green',bg='white',font=('Microsoft YaHei UI Light',35,'bold'))
    heading.place(x=100,y=3)
    #user Field
    def on_ent(e):
        usern.delete(0,100)
            
    def on_leve(e):
        name=usern.get()
        if name==' ':
            usern.insert(0,usern)
        
        
    usern=Entry(c,width=15,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',13))
    usern.place(x=30,y=80)
    usern.insert(0,'username')
    usern.bind('<FocusIn>',on_ent)
    usern.bind('<FocusOut>',on_leve)
    Canvas(c,width=295,height=2,bg='black').place(x=25,y=110)
        
        #password Field
    def on_click(e):
        passn_En.delete(0,100)
            
    def on_lea(e):
        name=passn_En.get()
        if name==' ':
            passn_En.insert(0,passn_En)
        
        
    passn_En=Entry(c,width=15,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',13))
    passn_En.place(x=30,y=150)
    passn_En.insert(0,'password')
    passn_En.bind('<FocusIn>',on_click)
    passn_En.bind('<FocusOut>',on_lea)
    Canvas(c,width=295,height=2,bg='black').place(x=25,y=180)
        
        #Buttons
    button=Button(c,width=39,pady=7,text='Sign in',bg='green',fg='white',border=-10,command=che)
    button.place(x=35,y=204)
    fot_up=Button(c,width=0,text='Forgot Password',border=-10,bg='white',cursor='hand2',fg='green',command=forgetpass)
    fot_up.place(x=150,y=250)    
    label=Label(c,text="Don't have an account.?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label.place(x=75,y=270)
    sign_up=Button(c,width=6,text='Sign up',border=-10,bg='white',cursor='hand2',fg='green',command=sinup)
    sign_up.place(x=230,y=270)
    

def sinup():
    def signsave():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ERS')
        cur=db.cursor()
        a=usern.get()
        b=passn_En.get() 
        c=mail.get()
        sql="select count(*) from login where user='%s'" %(a)
        cur.execute(sql)
        data=cur.fetchone()
        if data[0]==0:
                    sql="insert into login values ('%s','%s','%s')" %(a,b,c)
                    cur.execute(sql)
                    messagebox.showinfo('saved','New Id Registered')
        else:
            messagebox.showerror('Not available','Try new name')       
        db.commit()    
        db.close()
    #Frame2
    c2=Frame(t,width=350,height=350,bg='white',border=0)
    c2.place(x=480,y=70)
    #heading
    heading=Label(c2,text='Create Account',fg='green',bg='white',font=('Microsoft YaHei UI Light',25,'bold'))
    heading.place(x=40,y=3)
    
    
    #user Field
    def on_enter(e):
        usern.delete(0,100)
        
    def on_leave(e):
        name=usern.get()
        if name==' ':
            usern.insert(0,usern)    

    
    
    usern=Entry(c2,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',13))
    usern.place(x=30,y=80)
    usern.insert(0,'Username')
    usern.bind('<FocusIn>',on_enter)
    usern.bind('<FocusOut>',on_leave)
    Canvas(c2,width=295,height=2,bg='black').place(x=25,y=107)
    
    #password Field
    def on_enter(e):
        passn_En.delete(0,100)
        
    def on_leave(e):
        name=passn_En.get()
        if name==' ':
            passn_En.insert(0,passn_En)
    
    
    passn_En=Entry(c2,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',13))
    passn_En.place(x=30,y=150)
    passn_En.insert(0,'Password')
    passn_En.bind('<FocusIn>',on_enter)
    passn_En.bind('<FocusOut>',on_leave)
    Canvas(c2,width=295,height=2,bg='black').place(x=25,y=177)
    
    
    #Email Field
    def on_enter(e):
        mail.delete(0,100)
        
    def on_leave(e):
        name=mail.get()
        if name==' ':
            mail.insert(0,mail)
    
    
    mail=Entry(c2,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',13))
    mail.place(x=30,y=220)
    mail.insert(0,'Email')
    mail.bind('<FocusIn>',on_enter)
    mail.bind('<FocusOut>',on_leave)
    Canvas(c2,width=295,height=2,bg='black').place(x=25,y=247)
    
    
    #Buttons
    button=Button(c2,width=39,pady=7,text='Sign up',bg='green',fg='white',border=0,command=signsave)
    button.place(x=35,y=270)
    label=Label(c2,text="Back to login page.",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label.place(x=75,y=320)
    back_up=Button(c2,width=6,text='Back',border=-10,bg='white',cursor='hand2',fg='green',command=showlog)
    back_up.place(x=180,y=320)
   

#heading
heading=Label(c,text='Sign in',fg='green',bg='white',font=('Microsoft YaHei UI Light',35,'bold'))
heading.place(x=100,y=0)



#user Field
def on_ent(e):
    usern.delete(0,100)
        
def on_leve(e):
    name=usern.get()
    if name==' ':
        usern.insert(0,usern)
    
    
usern=Entry(c,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',13))
usern.place(x=30,y=80)
usern.insert(0,'username')
usern.bind('<FocusIn>',on_ent)
usern.bind('<FocusOut>',on_leve)
Canvas(c,width=295,height=2,bg='black').place(x=25,y=110)
    
    #password Field
def on_click(e):
    passn_En.delete(0,100)
        
def on_lea(e):
    name=passn_En.get()
    if name==' ':
        passn_En.insert(0,passn_En)
        
passn_En=Entry(c,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',10),show='*')
passn_En.place(x=30,y=150)
passn_En.insert(0,'password')
passn_En.bind('<FocusIn>',on_click)
passn_En.bind('<FocusOut>',on_lea)
Canvas(c,width=295,height=2,bg='black').place(x=25,y=180)
    
    #Buttons
button=Button(c,width=39,pady=9,text='Sign in',bg='green',fg='white',border=-10,command=che)
button.place(x=35,y=204)
fot_up=Button(c,width=0,text='Forgot Password',border=-10,bg='white',cursor='hand2',fg='green',command=forgetpass)
fot_up.place(x=150,y=250)
label=Label(c,text="Don't have an account.?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=75,y=270)
sign_up=Button(c,width=8,text='Sign up',border=-10,bg='white',cursor='hand2',fg='green',command=sinup)
sign_up.place(x=219,y=270)


t.mainloop() 