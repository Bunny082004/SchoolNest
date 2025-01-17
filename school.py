from tkinter import *
from tkinter import messagebox as msg
import pymysql as p
from tkinter import ttk
mydb=p.connect(host='localhost',user='root',password='root',port=3306,database='school')
cursor=mydb.cursor()
class School:
    def __init__(self):
        r=Tk()
        r.geometry('520x500')
        r.config(bg='#85929E')
        r.resizable(False,False)
        img=PhotoImage(file="schl.png")
        Label(r,image=img,bg='#85929E',).place(x=-800,y=-100)
        Button(r,text='New Admission',bg='#CED7D7',fg='#17202A',font=('bold',30),command=self.apage).place(x=100,y=60)
        Button(r,text='Staff update',bg='#CED7D7',fg='#17202A',font=('bold',30),command=self.tpage).place(x=130,y=150)
        Button(r,text='Student List',bg='#CED7D7',fg='#17202A',font=('bold',30),command=self.lpage).place(x=130,y=240)
        Button(r,text="Fee payment",bg="#CED7D7",fg="#17202A",font=('bold',30),command=self.fpage).place(x=120,y=330)
        Button(r,text="Student Status",bg="#CED7D7",fg="#17202A",font=('bold',30),command=self.spage2).place(x=120,y=410)
        r.mainloop()
    def spage2(self):
        y=Toplevel()
        y.geometry('800x630')
        y.config(bg='#85929E')
        y.resizable(False,False)
        img=PhotoImage(file='schlimg2.png')
        Label(y,image=img).place(x=0,y=0)
        Label(y,text='Student Name',bg='#CED7D7',fg='#17202A',font=('bold',30)).place(x=20,y=30)
        Label(y,text='Class',bg='#CED7D7',fg='#17202A',font=('bold',30)).place(x=20,y=110)
        Label(y,text='Roll no',bg='#CED7D7',fg='#17202A',font=('bold',30)).place(x=20,y=190)
        self.sname=Entry(y,bg='#CED7D7',fg='#17202A',font=('bold',30))
        self.sname.place(x=300,y=30)
        self.Class=Entry(y,bg='#CED7D7',fg='#17202A',font=('bold',30))
        self.Class.place(x=300,y=110)
        self.sroll=Entry(y,bg='#CED7D7',fg='#17202A',font=('bold',30))
        self.sroll.place(x=300,y=190)
        Button(y,text='Pay',bg='#CED7D7',fg='#17202A',font=('bold',20),command=self.sdisplay).place(x=380,y=270)
        y.mainloop()
    def fpage(self):
        y=Toplevel()
        y.geometry('800x630')
        y.config(bg='#85929E')
        y.resizable(False,False)
        img=PhotoImage(file='schlimg2.png')
        Label(y,image=img).place(x=0,y=0)
        Label(y,text='Student Name',bg='#CED7D7',fg='#17202A',font=('bold',30)).place(x=20,y=30)
        Label(y,text='Class',bg='#CED7D7',fg='#17202A',font=('bold',30)).place(x=20,y=110)
        Label(y,text='Roll no',bg='#CED7D7',fg='#17202A',font=('bold',30)).place(x=20,y=190)
        Label(y,text='Amount',bg='#CED7D7',fg='#17202A',font=('bold',30)).place(x=20,y=270)
        self.sname=Entry(y,bg='#CED7D7',fg='#17202A',font=('bold',30))
        self.sname.place(x=300,y=30)
        self.sclass=Entry(y,bg='#CED7D7',fg='#17202A',font=('bold',30))
        self.sclass.place(x=300,y=110)
        self.sroll=Entry(y,bg='#CED7D7',fg='#17202A',font=('bold',30))
        self.sroll.place(x=300,y=190)
        self.samt=Entry(y,bg='#CED7D7',fg='#17202A',font=('bold',30))
        self.samt.place(x=300,y=270)
        Button(y,text='Pay',bg='#CED7D7',fg='#17202A',font=('bold',20),command=self.payfee).place(x=380,y=350)
        y.mainloop()
    def apage(self):
        y=Toplevel()
        y.geometry('800x630')
        y.config(bg='#85929E')
        y.resizable(False,False)
        img=PhotoImage(file="schlimg2.png")
        Label(y,image=img,bg='#85929E',).place(x=0,y=0)
        Label(y,text='Student Name',bg='#CED7D7',fg='#17202A',font=('bold',30)).place(x=20,y=30)
        Label(y,text='Parent Name',bg='#CED7D7',fg='#17202A',font=('bold',30)).place(x=20,y=110)
        Label(y,text='Contact',bg='#CED7D7',fg='#17202A',font=('bold',30)).place(x=20,y=190)
        Label(y,text='Roll No',bg='#CED7D7',fg='#17202A',font=('bold',30)).place(x=20,y=270)
        Label(y,text='Class',bg='#CED7D7',fg='#17202A',font=('bold',30)).place(x=20,y=350)
        Label(y,text='Total Fee',bg='#CED7D7',fg='#17202A',font=('bold',30)).place(x=20,y=430)
        Label(y,text='Paid',bg='#CED7D7',fg='#17202A',font=('bold',30)).place(x=20,y=510)
        self.sname=Entry(y,bg='#CED7D7',fg='#17202A',font=('bold',30))
        self.sname.place(x=300,y=30)
        self.pname=Entry(y,bg='#CED7D7',fg='#17202A',font=('bold',30))
        self.pname.place(x=300,y=110)
        self.scontact=Entry(y,bg='#CED7D7',fg='#17202A',font=('bold',30))
        self.scontact.place(x=300,y=190)
        self.sroll=Entry(y,bg='#CED7D7',fg='#17202A',font=('bold',30))
        self.sroll.place(x=300,y=270)
        self.sclass=Entry(y,bg='#CED7D7',fg='#17202A',font=('bold',30))
        self.sclass.place(x=300,y=350)
        self.sfee=Entry(y,bg='#CED7D7',fg='#17202A',font=('bold',30))
        self.sfee.place(x=300,y=430)
        self.spaid=Entry(y,bg='#CED7D7',fg='#17202A',font=('bold',30))
        self.spaid.place(x=300,y=510)
        Button(y,text='admit',bg='#CED7D7',fg='#17202A',font=('bold',20),command=self.addstudent).place(x=380,y=570)
        y.mainloop()
    def tpage(self):
        y=Toplevel()
        y.geometry('800x630')
        y.config(bg='#85929E')
        y.resizable(False,False)
        img=PhotoImage(file="schlimg2.png")
        Label(y,image=img,bg='#85929E',).place(x=0,y=0)
        Label(y,text='Teacher Name',bg='#CED7D7',fg='#17202A',font=('bold',30)).place(x=20,y=30)
        Label(y,text='Contact',bg='#CED7D7',fg='#17202A',font=('bold',30)).place(x=20,y=110)
        Label(y,text='Class From',bg='#CED7D7',fg='#17202A',font=('bold',30)).place(x=20,y=190)
        Label(y,text='Class to',bg='#CED7D7',fg='#17202A',font=('bold',30)).place(x=20,y=270)
        Label(y,text='Salary',bg='#CED7D7',fg='#17202A',font=('bold',30)).place(x=20,y=350)
        self.tname=Entry(y,bg='#CED7D7',fg='#17202A',font=('bold',30))
        self.tname.place(x=300,y=30)
        self.tcontact=Entry(y,bg='#CED7D7',fg='#17202A',font=('bold',30))
        self.tcontact.place(x=300,y=110)
        self.tclassfrom=Entry(y,bg='#CED7D7',fg='#17202A',font=('bold',30))
        self.tclassfrom.place(x=300,y=190)
        self.tclassto=Entry(y,bg='#CED7D7',fg='#17202A',font=('bold',30))
        self.tclassto.place(x=300,y=270)
        self.tsalary=Entry(y,bg='#CED7D7',fg='#17202A',font=('bold',30))
        self.tsalary.place(x=300,y=350)
        Button(y,text='Save',bg='#CED7D7',fg='#17202A',font=('bold',20),command=self.addteacher).place(x=380,y=470)
        y.mainloop()
    def lpage(self):
        y=Toplevel()
        y.geometry('400x300')
        y.config(bg='#85929E')
        y.resizable(False,False)
        img=PhotoImage(file="schlimg2.png")
        Label(y,image=img,bg='#85929E',).place(x=0,y=0)
        Button(y,text='Due',bg='#CED7D7',fg='#17202A',font=('bold',30),command=self.Duestudents).place(x=150,y=10)
        Button(y,text='No Due',bg='#CED7D7',fg='#17202A',font=('bold',30),command=self.NoDuestudents).place(x=120,y=100)
        Button(y,text='All',bg='#CED7D7',fg='#17202A',font=('bold',30),command=self.Allstudents).place(x=170,y=190)
        y.mainloop()
    def Allstudents(self):
        y=Tk()
        # y.geometry('900x600')
        # y.config(bg='#85929E')
        # y.resizable(False,False)
        cursor.execute('select * from students')
        t=1
        for i in cursor:
            t+=1
        tv=ttk.Treeview(y,columns=(1,2,3,4,5,6,7),show="headings",height=t)
        tv.pack()
        tv.heading(1,text="Name")
        tv.heading(2,text="Parent")
        tv.heading(3,text="Contact")
        tv.heading(4,text="Roll no")
        tv.heading(5,text="Class")
        tv.heading(6,text="Fee total")
        tv.heading(7,text="Paid")
        cursor.execute('select * from students')
        for i in cursor:
            tv.insert('','end',values=i)
        y.mainloop()
    def Duestudents(self):
        y=Tk()
        # y.geometry('900x600')
        # y.config(bg='#85929E')
        # y.resizable(False,False)
        cursor.execute('select * from students')
        t=1
        for i in cursor:
            if i[6]<i[5]:
                t+=1
        tv=ttk.Treeview(y,columns=(1,2,3,4,5,6,7),show="headings",height=t)
        tv.pack()
        tv.heading(1,text="Name")
        tv.heading(2,text="Parent")
        tv.heading(3,text="Contact")
        tv.heading(4,text="Roll no")
        tv.heading(5,text="Class")
        tv.heading(6,text="Fee total")
        tv.heading(7,text="Paid")
        cursor.execute('select * from students')
        for i in cursor:
            if i[6]<i[5]:
                tv.insert('','end',values=i)
        y.mainloop()
    def NoDuestudents(self):
        y=Tk()
        # y.geometry('900x600')
        # y.config(bg='#85929E')
        # y.resizable(False,False)
        cursor.execute('select * from students')
        t=1
        for i in cursor:
            if i[6]==i[5]:
                t+=1
        tv=ttk.Treeview(y,columns=(1,2,3,4,5,6,7),show="headings",height=t)
        tv.pack()
        tv.heading(1,text="Name")
        tv.heading(2,text="Parent")
        tv.heading(3,text="Contact")
        tv.heading(4,text="Roll no")
        tv.heading(5,text="Class")
        tv.heading(6,text="Fee total")
        tv.heading(7,text="Paid")
        cursor.execute('select * from students')
        for i in cursor:
            if i[6]==i[5]:
                tv.insert('','end',values=i)
        y.mainloop()
    def sdisplay(self):
        Class=int(self.Class.get())
        roll=self.sroll.get()
        self.u=int(self.sroll.get())
        y=Tk()
        # y.geometry('900x600')
        # y.config(bg='#85929E')
        # y.resizable(False,False)
        cursor.execute('select * from students')
        t=2
        tv=ttk.Treeview(y,columns=(1,2,3,4,5,6,7),show="headings",height=t)
        tv.pack()
        tv.heading(1,text="Name")
        tv.heading(2,text="Parent")
        tv.heading(3,text="Contact")
        tv.heading(4,text="Roll no")
        tv.heading(5,text="Class")
        tv.heading(6,text="Fee total")
        tv.heading(7,text="Paid")
        cursor.execute('select * from students')
        for i in cursor:
            if i[3]==self.u and i[4]==Class:
                tv.insert('','end',values=i)
        y.mainloop()

    def addstudent(self):
        name=self.sname.get()
        pname=self.pname.get()
        contact=self.scontact.get()
        roll=self.sroll.get()
        Class=self.sclass.get()
        Tfee=self.sfee.get()
        pfee=self.spaid.get()
        cursor.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(name,pname,contact,roll,Class,Tfee,pfee))
        mydb.commit()
    def addteacher(self):
        name=self.tname.get()
        contact=self.tcontact.get()
        classfrom=self.tclassfrom.get()
        Classto=self.tclassto.get()
        salary=self.tsalary.get()
        cursor.execute("insert into teachers values(%s,%s,%s,%s,%s)",(name,contact,classfrom,Classto,salary))
        mydb.commit()
    def payfee(self):
        Class=self.sclass.get()
        roll=self.sroll.get()
        fee=self.samt.get()
        cursor.execute("update students set paid=paid+%s where class=%s AND roll=%s ",(fee,Class,roll))
        mydb.commit()


s=School()