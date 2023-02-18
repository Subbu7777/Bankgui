#normal u did done

import sys
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt6 import *
from PyQt6.QtWidgets import QLabel,QApplication,QVBoxLayout,QLineEdit,QWidget,QDialog,QMainWindow,QPushButton,QGridLayout
import PySide6
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
import winsound
import mysql.connector as aa
import pandas as pd
import winsound

FRE_QUENCY = 1000
DUA_RATION = 2000
q = aa.connect(host='localhost', username='root', password='Subbu@123')
w = q.cursor()
w.execute('create database if not exists su')
w.execute('use su')
w.execute('create table detail(id int,  name varchar(20) not null,accbalance  Decimal(10,3),deposit Decimal(10,3) null,withdraw Decimal(10,3) null,transfer_amnt Decimal(10,3) null,transfer_to_id int null)')
w.execute('create table acc(Id int,Name varchar(20),Phone int(10),Place varchar(10))')
q.commit()




class Window(QWidget):
    def __init__(self):
        super().__init__()
        #self.ww=QWidget()
        self.resize(400,400)
        self.setWindowTitle("Bank of Baroda")
        self.layout=QGridLayout()
        self.setLayout(self.layout)

        title=QLabel("WELCOME \n Enter 1.REGISTER 2.LOGIN 0.Exit")
        self.layout.addWidget(title, 0,1,Qt.AlignmentFlag.AlignCenter)

        self.label0=QLabel("Choice",self)
        self.layout.addWidget(self.label0,1,0)
        self.input0=QLineEdit()
        self.layout.addWidget(self.input0,1,1)

        bu2=QPushButton("GO")
        self.layout.addWidget(bu2,2,0,Qt.AlignmentFlag.AlignCenter)
        bu2.setFixedWidth(50)
        bu2.clicked.connect(self.a)

        self.label1=QLabel("Userid: ",self)
        self.label2=QLabel("Name: ",self)
        self.label3=QLabel("Phone: ",self)
        self. label4=QLabel("Place: ",self) 
        self.label11=QLabel("DONE",self)
        self.label5=QLabel('Enter user id')
        self.label18=QLabel("not enough baalnnce")

        self.input1=QLineEdit()
        self.input2=QLineEdit()
        self.input3=QLineEdit()
        self.input4=QLineEdit()



        self.name = ''
        self.nme = ''
        self.accbal = 0.0
        self.oldbal=0.0
       
        #self.ww.setWindowTitle("PyQt MessageBox")
       # bu2=QPushButton("Login")
        #layout.addWidget(bu2,5,2,Qt.AlignmentFlag.AlignLeft)
        #bu2.setFixedWidth(50)
    def a(self):
        ss=self.input0.text()        
        if ss=='0':
            w.execute('drop database su')
            q.commit()

        if ss=='1':
            self.label11.clear()
            self.layout.addWidget(self.label1,3,0) 
            self.layout.addWidget(self.input1,3,1)
            self.layout.addWidget(self.label2,4,0)
            self.layout.addWidget(self.input2,4,1)
            self.layout.addWidget(self.label3,5,0)
            self.layout.addWidget(self.input3,5,1)
            self.layout.addWidget(self.label4,6,0)
            self.layout.addWidget(self.input4,6,1)
            self.label11=QLabel("Done")
            bu=QPushButton('Register')
            bu.setFixedWidth(50)
            bu.clicked.connect(self.display)
            self.layout.addWidget(bu,7,1,Qt.AlignmentFlag.AlignRight)

            
            self.input0.clear()
            self.input1.clear()
            self.input2.clear()
            self.input3.clear()
            self.input4.clear()

            
        if ss=='2':
            self.layout.addWidget(self.label5,8,0)
            self.input5=QLineEdit()
            self.layout.addWidget(self.input5,8,1)
            bu3=QPushButton('Access')
            bu3.setFixedWidth(50)
            bu3.clicked.connect(self.details)
            self.layout.addWidget(bu3,9,0,Qt.AlignmentFlag.AlignRight)
            
            self.label1.clear()
            self.label2.clear()
            self.label3.clear()
            self.label4.clear()
            self.label11.clear()
            self.input1.clear()
            self.input2.clear()
            self.input3.clear()
            self.input4.clear()
            
    def details(self):
        self.label6=QLabel("1.Deposit ")
        self.layout.addWidget(self.label6,10,0)
    
        self.label7=QLabel("2.Withdraw ")
        self.layout.addWidget(self.label7,11,0)
    

        self.label8=QLabel("3.Transfer ")
        self.layout.addWidget(self.label8,12,0)


        self. label9=QLabel("4.Balance ")
        self.layout.addWidget(self.label9,13,0)

        self. label10=QLabel("5.Transactions ")
        self.layout.addWidget(self.label10,14,0)

        self.input6=QLineEdit()
        self.layout.addWidget(self.input6,15,0)
        bu4=QPushButton('Do')
        bu4.setFixedWidth(50)
        bu4.clicked.connect(self.detail)
        self.layout.addWidget(bu4,16,0,Qt.AlignmentFlag.AlignRight)

    def detail(self):
        sk=self.input6.text()
        self.input6.clear()
        self.name = ''
        self.nme = ''
        self.accbal = 0
        self.oldbal=0
        self.id=self.input5.text()
        self.id=int(self.id)
        w.execute(f"select * from acc where id={self.id}")
        self.name = w.fetchone()[1]
        try:
                    w.execute(f"SELECT * FROM detail where id={self.id}")
                    results = w.fetchall()
                    for row in results:
                        self.accbal = row[2]
                        self.accbal=float(self.accbal)
        except ImportError:
                    self.accbal = 0
                    self.accbal=float(self.accbal)
                    # s.wtotal=0
                    # s.transtotal=0
        finally:
                    self.transfered = 0
                    self.withdrawn= 0
                    self.trid = 0
                    self.amount = 0

        if sk=='1':
            self.label12=QLabel("Enter Amount")
            self.layout.addWidget(self.label12,17,0)
            self.input7=QLineEdit()
            self.layout.addWidget(self.input7,17,1)
            bu5=QPushButton('Enter')
            bu5.setFixedWidth(50)
            bu5.clicked.connect(self.sun)
            self.layout.addWidget(bu5,17,2,Qt.AlignmentFlag.AlignRight)
            
            #self.amount=int(self.amount)
            #self.accbal = self.accbal+self.amount
            #self.info()
        elif sk=='2':
            self.label13=QLabel("withdraw amount")
            self.layout.addWidget(self.label13,18,0)
            self.input8=QLineEdit()
            self.layout.addWidget(self.input8,18,1)
            bu6=QPushButton('Enter')
            bu6.setFixedWidth(50)
            bu6.clicked.connect(self.sunn)
            self.layout.addWidget(bu6,18,2,Qt.AlignmentFlag.AlignRight)
        elif sk=='3':
            self.label14=QLabel("Transferid")
            self.layout.addWidget(self.label14,19,0)
            self.input9=QLineEdit()
            self.layout.addWidget(self.input9,19,1)
            self.trid=self.input9.text()
            self.label15=QLabel("Transfer amount")
            self.layout.addWidget(self.label15,20,0)
            self.input10=QLineEdit()
            self.layout.addWidget(self.input10,20,1)
            bu7=QPushButton('Transfer')
            bu7.setFixedWidth(50)
            bu7.clicked.connect(self.sunnn)
            self.layout.addWidget(bu7,21,1,Qt.AlignmentFlag.AlignRight)

            

        elif sk=='4':
            w.execute(f"SELECT * FROM detail where id={self.id}")
            results = w.fetchall()
            for row in results:
                self.accbal = row[2]
            winsound.Beep(FRE_QUENCY, DUA_RATION)
            print('your account balance is',self.accbal)
        elif sk=='5':
            o_d = pd.read_sql_query('select * from detail', q)
            o_d = pd.DataFrame(o_d)
            i = [self.id]
            fi_l = o_d['id'].isin(i)
            m_r = o_d.loc[fi_l]
            print(m_r)
            winsound.Beep(FRE_QUENCY, DUA_RATION)
        else:
            pass
        


        

    def display(self):
        self.layout.addWidget(self.label11, 7,0,Qt.AlignmentFlag.AlignLeft)
        I_D=self.input1.text()
        name=self.input2.text()
        phone=self.input3.text()
        place=self.input4.text()
        print(I_D,name,phone,place)
        W_E= "insert into acc(ID,Name,Phone,Place) values(%s,%s,%s,%s)"
        em=[(I_D,name,phone,place)]
        w.executemany(W_E,em)
        q.commit()
        winsound.Beep(FRE_QUENCY, DUA_RATION)
        #if 5!=6:
         #   time.sleep(5)
            #self.label11.clear()
    def info(self):
                """ insetign """
                listt = [(self.id, self.name, self.accbal, self.amount,
                          self.withdrawn, self.transfered, self.trid)]
                e_e = 'INSERT INTO DETAIL\
                    (id,name,accbalance,deposit,withdraw,\
                        transfer_amnt,transfer_to_id)\
                     VALUES(%s,%s,%s,%s,%s,%s,%s)'
                w.executemany(e_e, listt)
                q.commit()
                self.amount = 0
                self.withdrawn = 0
                self.transfered = 0
                self.trid = 0

    def sun(self):
        w.execute(f"SELECT * FROM detail where id={self.id}")
        results = w.fetchall()
        for row in results:
            self.accbal = row[2]
        self.accbal=float(self.accbal)
        print(self.accbal)
        self.amount =self.input7.text()
        self.amount=float(self.amount)
        self.accbal=self.accbal+self.amount
        print(self.accbal)
        self.info()
        self.layout.addWidget(self.label11, 25,0,Qt.AlignmentFlag.AlignLeft)
        winsound.Beep(FRE_QUENCY, DUA_RATION)
        print("your amount is successfully Deposited")
        self.input7.clear()
        self.label12.clear()




    def sunn(self):
        w.execute(f"SELECT * FROM detail where id={self.id}")
        results = w.fetchall()
        for row in results:
            self.accbal = row[2]
        self.accbal=float(self.accbal)
        self.withdrawn=self.input8.text()
        self.withdrawn=float(self.withdrawn)
        if self.accbal < self.withdrawn:
                self.label17=QLabel("not enough baalnnce")
                self.layout.addWidget(self.label17,21,0)
        else:
            self.accbal = self.accbal-self.withdrawn
            self.info()
            self.layout.addWidget(self.label11, 25,0,Qt.AlignmentFlag.AlignLeft)
            winsound.Beep(FRE_QUENCY, DUA_RATION)
            print("your amount is successfully withdrawn")

            self.label13.clear()
            self.input8.clear()





    def sunnn(self):
        self.trid=self.input9.text()
        self.trid=int(self.trid)
        self.transfered=self.input10.text()
        self.transfered=float(self.transfered)
        w.execute(f"SELECT * FROM detail where id={self.id}")
        results = w.fetchall()
        for row in results:
            self.accbal = row[2]
            self.accbal=float(self.accbal)
        if self.accbal < self.transfered:
                self.layout.addWidget(self.label18,24,0)
        else:
            self.accbal = self.accbal-self.transfered
            try:
                w.execute(f"SELECT * FROM acc where Id={self.trid}")
                results = w.fetchall()
                for rows in results:
                    self.nme = rows[1]
                w.execute(f"SELECT * FROM detail where id={self.trid}")
                results = w.fetchall()
                for rows in results:
                        self.oldbal = rows[2]
                self.oldbal=float(self.oldbal)
                accbala = self.oldbal+self.transfered
                w_e = 'insert into detail(id,name,accbalance) values(%s,%s,%s)'
                k_e = [(self.trid, self.nme, accbala)]
                w.executemany(w_e, k_e)
                print("your amount is successfully Transfered")

                winsound.Beep(FRE_QUENCY, DUA_RATION)
            except ImportError:
                        accbala = self.transfered
                        w_e = 'insert into detail(id,name,accbalance) values(%s,%s,%s)'
                        k_e = [(self.trid, self.nme, accbala)]
                        w.executemany(w_e, k_e)
                        q.commit()
                        
        self.info()
        self.layout.addWidget(self.label11, 25,0,Qt.AlignmentFlag.AlignLeft)

        self.label14.clear()
        self.input9.clear()
        self.label15.clear()
        self.input10.clear()
        self.label18.clear()

                
app=QApplication(sys.argv)
window=Window()
window.show()
sys.exit(app.exec())