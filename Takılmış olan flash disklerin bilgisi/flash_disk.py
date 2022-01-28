import sys
from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QPushButton,QVBoxLayout


class flash_disk_bilgisi(QWidget):

    def __init__(self):
        super().__init__() 
        self.icerik()

    def icerik(self):
        self.goruntuleme_butonu=QPushButton("Takılmış olan USB'ler")
        self.takilma_cikarma_zamani=QPushButton("Tarih Ve Zaman Bilgileri")
        self.seri_numara=QPushButton("Seri Numarası")
        self.text1=QTextEdit()  
        v_box=QVBoxLayout()
        v_box.addWidget(self.goruntuleme_butonu)
        v_box.addWidget(self.takilma_cikarma_zamani)
        v_box.addWidget(self.seri_numara)
        v_box.addWidget(self.text1)
        self.setLayout(v_box)
        self.setWindowTitle("USB Bilgilerini Edinme")
        self.goruntuleme_butonu.clicked.connect(self.genel_bilgi)
        self.takilma_cikarma_zamani.clicked.connect(self.giris_cikis_zamanlari)
        self.seri_numara.clicked.connect(self.seri_numarasi)
        self.show()
        
    def genel_bilgi(self):
       self.marka_listesi=list()
       self.tarih_saat_listesi=list()
       with open("takma.txt","r",encoding="utf-8") as file:
           for satir in file:
               satir=satir[:-1]
               satir_elemanlari=satir.split("\t")
               if(satir_elemanlari[0]=="Bilgi"):
                   self.yeni_liste=satir_elemanlari[5].split("VEN")
                   self.yeni_liste=self.yeni_liste[1]
                   self.yeni_liste=self.yeni_liste.lstrip("_")
                   self.yeni_liste=self.yeni_liste.lstrip("USB&PROD")
                   self.yeni_liste=self.yeni_liste.lstrip("_")
                   self.yeni_liste=self.yeni_liste.split("&REV")
                   self.yeni_liste=self.yeni_liste[0]
                   self.marka_listesi.append(self.yeni_liste)
                   self.tarih_saat_listesi.append(satir_elemanlari[1])
       self.ortak_liste=list()
       n=0
       for i in self.marka_listesi:
           self.ortak_liste.append(i+"             "+self.tarih_saat_listesi[n])
           n=n+1
       self.ortak_liste="\n".join(self.ortak_liste)
       self.text1.setPlainText(self.ortak_liste)
     
       
    def giris_cikis_zamanlari(self):
        self.giris_listesi=list()
        self.cikis_listesi=list()
        with open("takma.txt","r",encoding="utf-8") as file:
            for satir in file:
                satir=satir[:-1]
                satir_elemanlari=satir.split("\t") 
                self.giris_listesi.append(satir_elemanlari[1])
        self.giris_listesi.remove("Tarih ve Saat")
        self.giris_listesi.insert(0,"USB Giriş Zamanları")
        
        with open("çıkarma.txt","r",encoding="utf-8") as file:
            for satir in file:
                satir=satir[:-1]
                satir_elemanlari=satir.split("\t") 
                if(satir_elemanlari[0]=="Bilgi"):
                    self.liste=satir_elemanlari[5].split(")")
                    if(self.liste[0]=="Bitmiş bir Pnp veya Güç işlemi (27, 23"):
                        self.cikis_listesi.append(satir_elemanlari[1])          
              
        self.cikis_listesi.insert(0,"USB Çıkış Zamanları")  
        
        self.ortak_liste=list()
        n=0
        for i in self.giris_listesi:
            self.ortak_liste.append(i+"    "+self.cikis_listesi[n])
            n=n+1
        self.ortak_liste="\n".join(self.ortak_liste)
        self.text1.setPlainText(self.ortak_liste)
                
                    
       
    def seri_numarasi(self):
        self.liste=list()
        self.seri_nu=list()
        with open("takma.txt","r",encoding="utf-8") as file:
            for satir in file:
                satir=satir[:-1]
                satir_elemanlari=satir.split("\t")
                if(satir_elemanlari[0]=="Bilgi"):
                    self.liste=satir_elemanlari[5].split("#")
                    self.liste=self.liste[2]     
                    self.seri_nu.append(self.liste)
            self.seri_nu="\n".join(self.seri_nu)
            self.text1.setPlainText(self.seri_nu)
            
        
       
app = QApplication(sys.argv)
usb_bilgi = flash_disk_bilgisi()
sys.exit(app.exec())
