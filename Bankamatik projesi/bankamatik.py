import sqlite3
import sys
from PyQt5.QtWidgets import QWidget,QLabel,QApplication,QTextEdit,QLineEdit,QPushButton,QVBoxLayout,QHBoxLayout

class bankamatik(QWidget):
    def __init__(self):
        super().__init__()
        self.baglantı_olustur()
        self.init_ui()
        
    def baglantı_olustur(self):
        self.baglanti=sqlite3.connect("databasee.db")
        self.cursor=self.baglanti.cursor()
        self.cursor.execute("Create Table If not exists müşteriler(isim TEXT,parola TEXT,bakiye INT,iban TEXT)")
        self.baglanti.commit()
        
    def init_ui(self):
        self.yazi=QLabel("Kullanıcı Adı:      ")
        self.kullanici_adi=QLineEdit()
        self.yazi1=QLabel("Şifre:                ")
        self.sifre=QLineEdit()
        self.yazi2=QLabel("İban:                 ")
        self.iban=QLineEdit()
        self.bakiye=QPushButton("Bakiye Sorgulama")
        self.para_cek=QPushButton("Para çekme")
        self.para_yatir=QPushButton("Para yatırma")
        self.baska_yatir=QPushButton("Başka Hesaba Para Yatırma")  
        self.yazi_alani=QTextEdit()
        self.yazi3=QLabel("Parayı Girin:            ")
        self.islemler=QLineEdit()
        self.yazi4=QLabel("Göndereceğiniz İban:")
        self.baskahesap_iban=QLineEdit()
        h_box=QHBoxLayout()
        h_box.addWidget(self.bakiye)
        h_box.addWidget(self.para_cek)
        h_box.addWidget(self.para_yatir)
        h_box.addWidget(self.baska_yatir)
        
        h_box2=QHBoxLayout()
        h_box2.addWidget(self.yazi)
        h_box2.addWidget(self.kullanici_adi)
        
        h_box3=QHBoxLayout()
        h_box3.addWidget(self.yazi1)
        h_box3.addWidget(self.sifre)
        
        h_box4=QHBoxLayout()
        h_box4.addWidget(self.yazi2)
        h_box4.addWidget(self.iban)
        
        h_box5=QHBoxLayout()
        h_box5.addWidget(self.yazi3)
        h_box5.addWidget(self.islemler)
        
        h_box6=QHBoxLayout()
        h_box6.addWidget(self.yazi4)
        h_box6.addWidget(self.baskahesap_iban)
        
        v_box=QVBoxLayout()
        v_box.addLayout(h_box2)
        v_box.addLayout(h_box3)
        v_box.addLayout(h_box4)
        v_box.addLayout(h_box)
        v_box.addWidget(self.yazi_alani)
        v_box.addLayout(h_box5)
        v_box.addLayout(h_box6)
        
      
        self.setLayout(v_box)
        self.setWindowTitle("Bankamatik")
        self.bakiye.clicked.connect(self.bakiye_ogren)
        self.para_cek.clicked.connect(self.para_cekme)
        self.para_yatir.clicked.connect(self.para_yatirma)
        self.baska_yatir.clicked.connect(self.baska_yatirma)
        self.show()
    def bakiye_ogren(self,liste):
        self.cursor.execute("Select isim,parola From müşteriler where iban=?",(self.iban.text(),))
        liste2=self.cursor.fetchall()
        for j in liste2:
            demet=j
            
        if(self.kullanici_adi.text()!=demet[0] and self.sifre.text()==demet[1]):
            self.yazi_alani.setText("Kullanıcı adı hatalı!")
        elif(self.kullanici_adi.text()==demet[0] and self.sifre.text()!=demet[1]):
            self.yazi_alani.setText("Parola hatalı!")
        elif(self.kullanici_adi.text()!=demet[0] and self.sifre.text()!=demet[1]):
            self.yazi_alani.setText("Kullanıcı adı ve parola hatalı!")
        else:
            self.cursor.execute("Select bakiye From müşteriler where iban=?",(self.iban.text(),))
            liste=self.cursor.fetchall()
            for i in liste:
                self.yazi_alani.setText(str(i[0]))
  
    def para_cekme(self):
        self.cursor.execute("Select isim,parola From müşteriler where iban=?",(self.iban.text(),))
        liste2=self.cursor.fetchall()
        for j in liste2:
            demet=j
            
        if(self.kullanici_adi.text()!=demet[0] and self.sifre.text()==demet[1]):
            self.yazi_alani.setText("Kullanıcı adı hatalı!")
        elif(self.kullanici_adi.text()==demet[0] and self.sifre.text()!=demet[1]):
            self.yazi_alani.setText("Parola hatalı!")
        elif(self.kullanici_adi.text()!=demet[0] and self.sifre.text()!=demet[1]):
            self.yazi_alani.setText("Kullanıcı adı ve parola hatalı!")
        else:   
            self.cursor.execute("Select bakiye From müşteriler where iban=?",(self.iban.text(),))
            liste=self.cursor.fetchall()
            for i in liste:
                yeni_para=i[0]-int(self.islemler.text())  
            if(yeni_para<0):
                self.yazi_alani.setText("Yetersiz bakiye..")
            else:   
                self.cursor.execute("Update müşteriler set bakiye=? where iban=?",(yeni_para,self.iban.text()))
                self.baglanti.commit()
        
    def para_yatirma(self):
        self.cursor.execute("Select isim,parola From müşteriler where iban=?",(self.iban.text(),))
        liste2=self.cursor.fetchall()
        for j in liste2:
            demet=j
            
        if(self.kullanici_adi.text()!=demet[0] and self.sifre.text()==demet[1]):
            self.yazi_alani.setText("Kullanıcı adı hatalı!")
        elif(self.kullanici_adi.text()==demet[0] and self.sifre.text()!=demet[1]):
            self.yazi_alani.setText("Parola hatalı!")
        elif(self.kullanici_adi.text()!=demet[0] and self.sifre.text()!=demet[1]):
            self.yazi_alani.setText("Kullanıcı adı ve parola hatalı!")
        else:    
            self.cursor.execute("Select bakiye From müşteriler where iban=?",(self.iban.text(),))
            liste=self.cursor.fetchall()
            for i in liste:
                yeni_para=i[0]+int(self.islemler.text())
            self.cursor.execute("Update müşteriler set bakiye=? where iban=?",(yeni_para,self.iban.text()))
            self.baglanti.commit()
        
    def baska_yatirma(self):
        self.cursor.execute("Select isim,parola From müşteriler where iban=?",(self.iban.text(),))
        liste2=self.cursor.fetchall()
        for j in liste2:
            demet=j
            
        if(self.kullanici_adi.text()!=demet[0] and self.sifre.text()==demet[1]):
            self.yazi_alani.setText("Kullanıcı adı hatalı!")
        elif(self.kullanici_adi.text()==demet[0] and self.sifre.text()!=demet[1]):
            self.yazi_alani.setText("Parola hatalı!")
        elif(self.kullanici_adi.text()!=demet[0] and self.sifre.text()!=demet[1]):
            self.yazi_alani.setText("Kullanıcı adı ve parola hatalı!")
        else:   
         
            self.cursor.execute("Select bakiye From müşteriler where iban=?",(self.iban.text(),))
            liste=self.cursor.fetchall()
            for i in liste:
                yeni_para=i[0]-int(self.islemler.text())
            if(yeni_para<0):
               self.yazi_alani.setText("Yetersiz bakiye")
            else:
                self.cursor.execute("Update müşteriler set bakiye=? where iban=?",(yeni_para,self.iban.text()))
                self.baglanti.commit()
         
                self.cursor.execute("Select bakiye From müşteriler where iban=?",(self.baskahesap_iban.text(),))
                liste2=self.cursor.fetchall()
                for i in liste2:
                    yeni_para2=i[0]+int(self.islemler.text())
                self.cursor.execute("Update müşteriler set bakiye=? where iban=?",(yeni_para2,self.baskahesap_iban.text()))
                self.baglanti.commit()
         
app=QApplication(sys.argv)
bankamatikk=bankamatik()
sys.exit(app.exec_())
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        