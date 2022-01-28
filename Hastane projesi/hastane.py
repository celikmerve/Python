import sqlite3
import sys
from PyQt5.QtWidgets import QTableWidget,QCheckBox,QTableWidgetItem,QMainWindow,QWidget,QLabel,QApplication,QTextEdit,QLineEdit,QPushButton,QVBoxLayout,QHBoxLayout,QComboBox,QAction,qApp
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
class pencere2(QWidget):
    def baglanti_olustur(self):
        self.baglanti=sqlite3.connect("hastane_veritabani.db")
        self.cursor=self.baglanti.cursor() 
        self.cursor.execute("Create Table If not exists KAYITLI_KULLANICILAR(Kullanici_Adi INT,İsim TEXT,Telefon_Numarasi INT,Mail_Adresi TEXT,Dogum_Tarihi TEXT,Sifre TEXT,Vasfi TEXT,Durum TEXT,Onceki_islemler TEXT,Yeni_islem TEXT)")
        self.baglanti.commit()
    
    def __init__(self):
        super().__init__() 
        self.baglanti_olustur()
        self.cursor.execute("Select Vasfi From KAYITLI_KULLANICILAR where Kullanici_Adi=?",(window.kullanici_adi.text(),))
        liste=self.cursor.fetchall()
        self.a=liste[0][0]
        
        
        if(self.a=="Hasta"):
            self.init_uii()
        else:
            self.init_uiii()

    def init_uii(self):
        
        self.yazi1=QLabel("HOŞGELDİNİZ",self)
        self.yazi2=QLabel("Hastane durumunuz için",self)
        self.yazi3=QLabel()
        self.yazi4=QLabel()
        self.yazi5=QLabel("RANDEVU MU ALMAK İSTİYORSUNUZ ?")
        self.yazi6=QLabel("Randevu almak istediğiniz doktoru seçiniz:")
        self.yazi7=QLabel("Geliş Amacınızı Belirtiniz:")
        self.yazi8=QLabel("Uygun olduğunuz saat aralığını seçiniz:")
        self.buton1=QPushButton("tıklayınız")
        self.randevu=QPushButton("Randevu Bilgisi")
        self.randevu_al=QPushButton("Randevuyu Kesinleştir")
        self.label=QLabel()
        self.label1=QLabel()
        self.gecmis=QPushButton("Önceden Yapılan Cerrahi İşlemler")
        self.label2=QLabel()
        self.label3=QLabel()
        self.label4=QLabel()
        self.label5=QLabel()
        self.label6=QLabel()
        self.label7=QLabel()
        self.sec=QComboBox()
        self.cursor.execute("Select İsim From KAYITLI_KULLANICILAR where Vasfi='Doktor'")
        liste1=self.cursor.fetchall()
        g_liste=liste1[0]
        g_liste1=liste1[1]
        self.sec.addItem("Seçiniz")
        self.sec.addItems(g_liste)
        self.sec.addItems(g_liste1)
        
        self.sec2=QComboBox()
        self.sec2.addItem("Seçiniz")
        self.sec2.addItem("Genel muayene ve gözlem")
        self.sec2.addItem("Kontrol")
        self.sec2.addItem("20lik diş ağrısı")
        self.sec2.addItem("20lik diş harici ağrı")
        self.sec2.addItem("Dolguda düşme veya kırılma")
        
        self.sec3=QComboBox()
        self.sec3.addItem("Seçiniz")
        self.sec3.addItem("9.00-11.00 arası")
        self.sec3.addItem("11.00-13.00 arası")
        self.sec3.addItem("13.00-15.00 arası")
        self.sec3.addItem("15.00-17.00 arası")

    
        h_box1=QHBoxLayout()
        h_box1.addWidget(self.yazi2)
        h_box1.addWidget(self.buton1)
        h_box2=QHBoxLayout()
        h_box2.addWidget(self.yazi3)
        h_box2.addWidget(self.yazi4)
        h_box3=QHBoxLayout()
        h_box3.addWidget(self.yazi6)
        h_box3.addWidget(self.yazi7)
        h_box3.addWidget(self.yazi8)
        h_box4=QHBoxLayout()
        h_box4.addWidget(self.sec)
        h_box4.addWidget(self.sec2)
        h_box4.addWidget(self.sec3)
        
        
        v_box1=QVBoxLayout()
        v_box1.addWidget(self.yazi1)
        v_box1.addLayout(h_box1)
        v_box1.addLayout(h_box2)
        v_box1.addWidget(self.randevu)
        v_box1.addWidget(self.label)
        v_box1.addWidget(self.label1)
        v_box1.addWidget(self.label2)
        v_box1.addWidget(self.label3)
        v_box1.addWidget(self.label5)
        v_box1.addWidget(self.label6)
        v_box1.addWidget(self.label7)
        v_box1.addWidget(self.yazi5)
        v_box1.addLayout(h_box3)
        v_box1.addLayout(h_box4)
        v_box1.addWidget(self.randevu_al)
        v_box1.addWidget(self.gecmis)
        v_box1.addWidget(self.label4)
        self.setLayout(v_box1)
        self.setWindowTitle("Hasta Penceresi")
        
        self.buton1.clicked.connect(self.durum)
        self.randevu.clicked.connect(self.randevu_bilgisi)
        self.gecmis.clicked.connect(self.gecmis_islemler)
        self.randevu_al.clicked.connect(self.randevu_kesinlestir)
    def durum(self):
       
        self.cursor.execute("Select Durum From KAYITLI_KULLANICILAR where Kullanici_Adi=?",(window.kullanici_adi.text(),))
        liste=self.cursor.fetchall()
        
    
        self.a=liste[0][0]
        self.yazi2.hide()
        self.buton1.hide()
        self.yazi3.setText("Hastane Durumunuz:")
        self.yazi4.setText(self.a)
        
    def randevu_kesinlestir(self):
        if(self.sec.currentText()!="Seçiniz" and self.sec2.currentText()!="Seçiniz" and self.sec3.currentText()!="Seçiniz" and self.label1.text()=="-" ):
            liste=(self.sec.currentText()+","+self.sec2.currentText()+","+self.sec3.currentText()+","+";")

            self.cursor.execute("Update KAYITLI_KULLANICILAR set Yeni_islem=? where Kullanici_Adi=?",(liste,window.kullanici_adi.text()))
            self.baglanti.commit()
        
        
    def randevu_bilgisi(self):
        self.cursor.execute("Select Yeni_islem From KAYITLI_KULLANICILAR where Kullanici_Adi=?",(window.kullanici_adi.text(),))
        liste=self.cursor.fetchall()
        self.randev=liste[0][0]
        self.randev=self.randev.split(",")

        self.label.setText("Randevunuzun olduğu doktor:")
        self.label2.setText("Geliş Amacınız:")
        self.label5.setText("Randevu Saatiniz:")
        
        self.label1.setText(self.randev[0])
        self.label3.setText(self.randev[1])
        self.label6.setText(self.randev[2])
        
        
        self.label7.setText("Doktorumuz seçtiğiniz saati değerlendirip sizi bilgilendirecektir.")
        self.label7.setStyleSheet("color:red")
        
       
        
        self.cursor.execute("Update KAYITLI_KULLANICILAR set Durum='Aktif' where Kullanici_Adi=?",(window.kullanici_adi.text(),))
        self.baglanti.commit()
        
    def gecmis_islemler(self):
        self.cursor.execute("Select Onceki_islemler From KAYITLI_KULLANICILAR where Kullanici_Adi=?",(window.kullanici_adi.text(),))
        liste=self.cursor.fetchall()
        self.label4.setText(liste[0][0])
        
    def kabul_bekleyenler(self):
        self.cursor.execute("Select İsim From KAYITLI_KULLANICILAR where Kullanici_Adi=?",(window.kullanici_adi.text(),))
        liste1=self.cursor.fetchall()
        self.isim=liste1[0][0]
        
        self.cursor.execute("Select Yeni_islem From KAYITLI_KULLANICILAR where Vasfi='Hasta'")
        liste2=self.cursor.fetchall()

      
        indks=0
        self.li=[self.text3,self.text6,self.text9,self.text12,self.text15]
        for im in self.li:
            x=-1
            for i in liste2:  
                x=x+1
                if(indks==x):
                    self.parcala=i[0].split(",")  
                    if(self.parcala[0]==self.isim):
                        self.yazilacak="Doktor Adı:"+self.parcala[0]+"\n"+"Geliş Amacı:"+self.parcala[1]+"\n"+"Hastanın Uygun Olduğu Saat:"+self.parcala[2]
                        im.setPlainText(self.yazilacak)
                    else:
                        indks=indks+1
            indks=indks+1       
            
                    
    def hastanin_bilgileri(self):      
        self.cursor.execute("Select İsim From KAYITLI_KULLANICILAR where Kullanici_Adi=?",(window.kullanici_adi.text(),))
        liste1=self.cursor.fetchall()
        self.isim=liste1[0][0]  
        
        self.cursor.execute("Select Yeni_islem From KAYITLI_KULLANICILAR where Vasfi='Hasta'")
        liste2=self.cursor.fetchall()

        self.cursor.execute("Select İsim,Mail_Adresi,Dogum_Tarihi From KAYITLI_KULLANICILAR where Vasfi='Hasta'")
        liste3=self.cursor.fetchall()    
        
            
        n=0
        indks=0
        self.li=[self.text2,self.text5,self.text8,self.text11,self.text14]
        for yazilacakyer in self.li:
            x=-1
            for i in liste3: 
                x=x+1
                if(indks==x):             
                    self.parcala=liste3[x] 
                    self.parcala2=liste2[n][0].split(",")
                    if(self.isim==self.parcala2[0]):
                        self.yazilacak="Hasta Adı:"+self.parcala[0]+"\n"+"Hastanın Mail Adresi:"+self.parcala[1]+"\n"+"Hastanın Dogum Tarihi:"+self.parcala[2]
                        yazilacakyer.setPlainText(self.yazilacak)
                    else:
                        indks=indks+1
                        n=n+1
            indks=indks+1 
            n=n+1

                

      
    def hastanin_gecmisi(self):
        self.cursor.execute("Select İsim From KAYITLI_KULLANICILAR where Kullanici_Adi=?",(window.kullanici_adi.text(),))
        liste1=self.cursor.fetchall()
        self.isim=liste1[0][0]
        
        self.cursor.execute("Select Yeni_islem From KAYITLI_KULLANICILAR where Vasfi='Hasta'")
        liste2=self.cursor.fetchall()
        
        self.cursor.execute("Select Onceki_islemler From KAYITLI_KULLANICILAR where Vasfi='Hasta'")
        liste3=self.cursor.fetchall()

        n=0
        indks=0
        self.li=[self.text1,self.text4,self.text7,self.text10,self.text13]
        for yazilacakyer in self.li:
            x=-1
            for i in liste3:  
                x=x+1
                if(indks==x):
                    self.parcala2=liste2[n][0].split(",")
                    if(self.isim==self.parcala2[0]):
                        self.yazilacak="Hastanın geçmiş işlemi:"+i[0]
                        yazilacakyer.setPlainText(self.yazilacak)
                    else:
                        indks=indks+1
                        n=n+1
            indks=indks+1  
            n=n+1
            
    def sonlandirma(self):
        self.cursor.execute("Select Yeni_islem From KAYITLI_KULLANICILAR where Mail_Adresi=?",(self.line.text(),))
        liste=self.cursor.fetchall()
        self.parcala=liste[0][0].split(",")
   

        self.cursor.execute("Update KAYITLI_KULLANICILAR set Onceki_islemler=? where Mail_Adresi=?",(self.parcala[1],self.line.text(),))
        self.baglanti.commit()
        
        self.cursor.execute("Update KAYITLI_KULLANICILAR set Yeni_islem=? where Mail_Adresi=?",("-,-,-,;",self.line.text(),))
        self.baglanti.commit()

        self.cursor.execute("Update KAYITLI_KULLANICILAR set Durum=? where Mail_Adresi=?",("Pasif",self.line.text(),))
        self.baglanti.commit()
        
    def kesinlestirme(self):
        mesaj=MIMEMultipart()
        kime=self.line.text()
        mesaj["From"]="mercelik.2328@gmail.com"
        mesaj["To"]=kime
        mesaj["Subject"]="Randevu Bilgisi"
      
        saat=self.line1.text()
        isim=self.yazi2.text()
        yazi="Saat"+" "+saat+" "+"da"+" "+isim+" "+"doktoruna randevunuz bulunmaktadır."
        mesaj_gövdesi=MIMEText(yazi,"plain")
        mesaj.attach(mesaj_gövdesi)
        try:
            mail=smtplib.SMTP("smtp.gmail.com",587)
            mail.ehlo()
            mail.starttls()
            mail.login("mercelik.2328@gmail.com","sifre")
            mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())
            print("Mail başarıyla gönderildi..")
            mail.close()
        except:
            sys.stderr.write("Mail göndermesi başarısız oldu..")
            sys.stderr.flush()
        
        
        
    def init_uiii(self):
        self.yazi1=QLabel("HOŞGELDİNİZ",self)
        self.yazi3=QLabel("Hangi hasta için işlem yapmak istiyorsanız mail adresini giriniz:")
        self.line=QLineEdit()
        self.line1=QLineEdit()
        self.kesinlestir=QPushButton("Kesinleştir")#mesaj yollayacak
        self.sonlandir=QPushButton("Sonlandır")#geçmişe atacak
        self.yazi4=QLabel("Randevu vermek istediğiniz saat:")
        self.kayit_gecmisi=QPushButton("Hasta Geçmişi")
        self.hasta_bilgileri=QPushButton("Kayıttaki Hasta Bilgileri")
        self.bekleyen_hastalar=QPushButton("Kabul Bekleyen Hasta Bilgileri")
        self.text1=QTextEdit()
        self.text2=QTextEdit()
        self.text3=QTextEdit()
        self.text4=QTextEdit()
        self.text5=QTextEdit()
        self.text6=QTextEdit()
        self.text7=QTextEdit()
        self.text8=QTextEdit()
        self.text9=QTextEdit()
        self.text10=QTextEdit()
        self.text11=QTextEdit()
        self.text12=QTextEdit()
        self.text13=QTextEdit()
        self.text14=QTextEdit()
        self.text15=QTextEdit()
        
        self.cursor.execute("Select İsim From KAYITLI_KULLANICILAR where Kullanici_Adi=?",(window.kullanici_adi.text(),))
        liste1=self.cursor.fetchall()
        self.isim=liste1[0][0]
        self.yazi2=QLabel(self.isim)
        
        h_box1=QHBoxLayout()
        h_box1.addWidget(self.yazi1)
        h_box1.addWidget(self.yazi2)
        
        h_box2=QHBoxLayout()
        h_box2.addWidget(self.kayit_gecmisi)
        h_box2.addWidget(self.hasta_bilgileri)
        h_box2.addWidget(self.bekleyen_hastalar)
        
        h_box3=QHBoxLayout()
        h_box3.addWidget(self.text1)
        h_box3.addWidget(self.text2)
        h_box3.addWidget(self.text3)
        
        h_box4=QHBoxLayout()
        h_box4.addWidget(self.text4)
        h_box4.addWidget(self.text5)
        h_box4.addWidget(self.text6)
        
        h_box5=QHBoxLayout()
        h_box5.addWidget(self.text7)
        h_box5.addWidget(self.text8)
        h_box5.addWidget(self.text9)
        
        h_box6=QHBoxLayout()
        h_box6.addWidget(self.text10)
        h_box6.addWidget(self.text11)
        h_box6.addWidget(self.text12)
        
        h_box7=QHBoxLayout()
        h_box7.addWidget(self.text13)
        h_box7.addWidget(self.text14)
        h_box7.addWidget(self.text15)
        
        h_box8=QHBoxLayout()
        h_box8.addWidget(self.yazi3)
        h_box8.addWidget(self.yazi4)
        
        h_box9=QHBoxLayout()
        h_box9.addWidget(self.line)
        h_box9.addWidget(self.line1)
        
        
        v_box1=QVBoxLayout()
        v_box1.addLayout(h_box1)
        v_box1.addLayout(h_box2)
        v_box1.addLayout(h_box3)
        v_box1.addLayout(h_box4)
        v_box1.addLayout(h_box5)
        v_box1.addLayout(h_box6)
        v_box1.addLayout(h_box7)
        v_box1.addLayout(h_box8)
        v_box1.addLayout(h_box9)
        v_box1.addWidget(self.kesinlestir)
        v_box1.addWidget(self.sonlandir)
        self.setLayout(v_box1)
        self.setWindowTitle("Doktor Penceresi")
        self.bekleyen_hastalar.clicked.connect(self.kabul_bekleyenler)
        self.hasta_bilgileri.clicked.connect(self.hastanin_bilgileri)
        self.kayit_gecmisi.clicked.connect(self.hastanin_gecmisi)
        self.sonlandir.clicked.connect(self.sonlandirma)
        self.kesinlestir.clicked.connect(self.kesinlestirme)
       
"""
    class menuler(QMainWindow):
        def __init__(self):
            super().__init__()
            self.pencere=pencere2()
                
            self.setCentralWidget(self.pencere)
            menubar=self.menuBar()
            self.hasta_gecmisi=menubar.addMenu("Hasta_Geçmişi")
            self.setWindowTitle("Menüler")   
            self.show()

    app = QApplication(sys.argv)
    menule=menuler()
    sys.exit(app.exec_())
"""

class pencere3(QWidget):
    def baglanti_olustur(self):
        self.baglanti=sqlite3.connect("hastane_veritabani.db")
        self.cursor=self.baglanti.cursor() 
        self.cursor.execute("Create Table If not exists KAYITLI_KULLANICILAR(Kullanici_Adi INT,İsim TEXT,Telefon_Numarasi INT,Mail_Adresi TEXT,Dogum_Tarihi TEXT,Sifre TEXT,Vasfi TEXT,Durum TEXT,Onceki_islemler TEXT,Yeni_islem TEXT)")
        self.baglanti.commit()
    
    def __init__(self):
        super().__init__()       
        self.baglanti_olustur()
        self.init_ui()
        
      
    def init_ui(self):
        self.yazi1=QLabel("İsim Soyisim:")
        self.ad=QLineEdit()
        self.yazi2=QLabel("TC kimlik numarası:")
        self.kimlik=QLineEdit()
        self.yazi3=QLabel("Doğum Tarihi:")
        self.dogum_tarihi=QLineEdit()
        self.yazi4=QLabel("E-Posta Adresi:")
        self.eposta=QLineEdit()
        self.yazi5=QLabel("Telefon Numarası:")
        self.telefon_numarasi=QLineEdit()
        self.yazi6=QLabel("Şifre Oluşturun:")
        self.sifre=QLineEdit()
        self.checkbox1=QCheckBox("Doktor")
        self.checkbox2=QCheckBox("Hasta")
        self.buton1=QPushButton("Kayıt Ol")

        h_box=QHBoxLayout()
        h_box.addWidget(self.checkbox1)
        h_box.addWidget(self.checkbox2)
        v_box=QVBoxLayout()
        v_box.addWidget(self.yazi1)
        v_box.addWidget(self.ad)
        v_box.addWidget(self.yazi2)
        v_box.addWidget(self.kimlik)
        v_box.addWidget(self.yazi3)
        v_box.addWidget(self.dogum_tarihi)
        v_box.addWidget(self.yazi4)
        v_box.addWidget(self.eposta)
        v_box.addWidget(self.yazi5)
        v_box.addWidget(self.telefon_numarasi)
        v_box.addWidget(self.yazi6)
        v_box.addWidget(self.sifre)
        v_box.addLayout(h_box)
        v_box.addWidget(self.buton1)
        self.setLayout(v_box)       
        self.setWindowTitle("Kayıt Penceresi")      
        self.buton1.clicked.connect(lambda: self.kayit1(self.checkbox1.isChecked()))
        self.buton1.clicked.connect(lambda: self.kayit2(self.checkbox2.isChecked()))

    def kayit1(self,checkbox1):
        if checkbox1:
            self.cursor.execute("Insert Into KAYITLI_KULLANICILAR(Kullanici_Adi,İsim,Telefon_Numarasi,Mail_Adresi,Dogum_Tarihi,Sifre,Vasfi,Yeni_islem) values(?,?,?,?,?,?,?,?)",(self.kimlik.text(),self.ad.text(),self.telefon_numarasi.text(),self.eposta.text(),self.dogum_tarihi.text(),self.sifre.text(),self.checkbox1.text(),'-,-,-,;',))
            self.baglanti.commit()

    def kayit2(self,checkbox2):
        if checkbox2:
            self.cursor.execute("Insert Into KAYITLI_KULLANICILAR(Kullanici_Adi,İsim,Telefon_Numarasi,Mail_Adresi,Dogum_Tarihi,Sifre,Vasfi,Yeni_islem) values(?,?,?,?,?,?,?,?)",(self.kimlik.text(),self.ad.text(),self.telefon_numarasi.text(),self.eposta.text(),self.dogum_tarihi.text(),self.sifre.text(),self.checkbox2.text(),'-,-,-,;',
                                                                                                                                                                                 ))
            self.baglanti.commit()
            
class pencere1(QWidget):
    def __init__(self):
        super().__init__()
        self.baglanti_olustur()
        self.init_ui()
        
    def baglanti_olustur(self):
        self.baglanti=sqlite3.connect("hastane_veritabani.db")
        self.cursor=self.baglanti.cursor()
        self.cursor.execute("Create Table If not exists KAYITLI_KULLANICILAR(Kullanici_Adi INT,İsim TEXT,Telefon_Numarasi INT,Mail_Adresi TEXT,Dogum_Tarihi TEXT,Sifre TEXT,Vasfi TEXT,Durum TEXT,Onceki_islemler TEXT,Yeni_islem TEXT)")     
        self.baglanti.commit()
        
    def init_ui(self):
        self.yazi=QLabel("             ÖZEL MERVE HASTANESİ")
        self.yazi1=QLabel("Kullanıcı Adı:      ")
        self.kullanici_adi=QLineEdit()
        self.buton=QPushButton("Giriş Yap")
        self.yazi2=QLabel("Şifre:                ")
        self.sifre=QLineEdit()
        self.label=QLabel()
        self.yazi3=QLabel("                 Kayıtlı değil misiniz?")
        self.yazi3.setStyleSheet("color:blue")
        self.buton1=QPushButton("Kayıt Ol")
        
        
        h_box1=QHBoxLayout()
        h_box1.addWidget(self.yazi1)
        h_box1.addWidget(self.kullanici_adi)
        h_box2=QHBoxLayout()
        h_box2.addWidget(self.yazi2)
        h_box2.addWidget(self.sifre) 
        v_box=QVBoxLayout()
        v_box.addWidget(self.yazi)
        v_box.addLayout(h_box1)
        v_box.addLayout(h_box2)
        v_box.addWidget(self.label)
        v_box.addWidget(self.buton)
        v_box.addWidget(self.yazi3)
        v_box.addWidget(self.buton1)
        self.setLayout(v_box)
        self.setWindowTitle("Kullanıcı Girişi")
        self.buton.clicked.connect(self.giris)
        self.buton1.clicked.connect(self.kayit)
        self.show()
       
    

    def giris(self):
        self.cursor.execute("Select Sifre From KAYITLI_KULLANICILAR where Kullanici_Adi=?",(window.kullanici_adi.text(),))
        liste=self.cursor.fetchall()
        print(liste[0][0])
        if(liste[0][0]==self.sifre.text()):
            self.window2 =pencere2()
            self.window2.show()
            self.hide()
        else:
            self.label.setText("              Şifrenizi yanlış girdiniz.")
            self.label.setStyleSheet("color:red")
        
    
    def kayit(self):
        self.window3=pencere3()
        self.window3.show()
        self.hide()
        
app = QApplication(sys.argv)
window = pencere1()
sys.exit(app.exec())


        

        
         

        
