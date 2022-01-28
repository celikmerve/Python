import sqlite3
import sys
from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QPushButton,QVBoxLayout


class pencere1(QWidget):
    def __init__(self):
        super().__init__()
        self.baglanti_olustur()
        self.icerik()
    
    def baglanti_olustur(self):
         self.baglanti=sqlite3.connect("C:\Documents and Settings\Asus\AppData\Local\Google\Chrome\\User Data\Default\History")
         self.cursor=self.baglanti.cursor()
         self.baglanti.commit()   

    def icerik(self):
        self.goruntuleme_butonu=QPushButton("Geçmişi görüntüle")
        self.text1=QTextEdit()  
        v_box=QVBoxLayout()
        v_box.addWidget(self.goruntuleme_butonu)
        v_box.addWidget(self.text1)
        self.setLayout(v_box)
        self.setWindowTitle("İnternet Geçmişini Görüntüleme")
        self.goruntuleme_butonu.clicked.connect(self.internet_gecmisi)
        self.show()

    def internet_gecmisi(self):
        self.cursor.execute("Select url From urls")     
        self.gecmis=self.cursor.fetchall()
        
        for i in self.gecmis:#Ekrana yazdırma.
            print(i[0])
            print("************************************")
            

        self.gecmis=str(self.gecmis)#setPlainText'e list türünde parametre verilmez.
        self.text1.setPlainText(self.gecmis)#self.text1'e yazdırma.



app = QApplication(sys.argv)
window = pencere1()
sys.exit(app.exec())