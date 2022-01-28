import sys
import os
import smtplib
from PyQt5.QtWidgets import QWidget,QTextEdit,QApplication,QPushButton,QVBoxLayout,QHBoxLayout,QFileDialog
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Mail(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.yazi_alani=QTextEdit()
        self.gonder=QPushButton("GÖNDER")
        self.ac=QPushButton("AÇ")
        self.sil=QPushButton("SİL")
        h_box=QHBoxLayout()
        h_box.addWidget(self.ac)
        h_box.addWidget(self.gonder)
        h_box.addWidget(self.sil)
        
        v_box=QVBoxLayout()
        v_box.addWidget(self.yazi_alani)
        v_box.addLayout(h_box)
        self.setLayout(v_box)
        self.setWindowTitle("MailGönderme")
        self.gonder.clicked.connect(self.maili_gonder)
        self.ac.clicked.connect(self.dosya_ac)
        self.sil.clicked.connect(self.yaziyi_temizle)
        self.show()
    def yaziyi_temizle(self):
        self.yazi_alani.clear()
        
    def dosya_ac(self):
        dosya_ismi=QFileDialog.getOpenFileName(self,"DOSYA AÇ",os.getenv("HOME"))
        with open(dosya_ismi[0],"r")as file:
            self.yazi_alani.setText(file.read())
            
    def maili_gonder(self):
        mesaj=MIMEMultipart()
        liste=list()
        liste.append(self.yazi_alani.toPlainText())
        mesaj["From"]="mail-adresi"
        mesaj["To"]=liste[0]
        mesaj["Subject"]="Smtp Mail Gönderme"
        yazi="""
        Merhaba PyQt5 butonumla smtp sayesinde mail gönderiyorum..
        """
        mesaj_gövdesi=MIMEText(yazi,"plain")
        mesaj.attach(mesaj_gövdesi)
        try:
            mail=smtplib.SMTP("smtp.gmail.com",587)
            mail.ehlo()
            mail.starttls()
            mail.login("mail-adresi","sifre")
            mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())
            print("Mail başarıyla gönderildi..")
        except:
            sys.stderr.write("Mail gndermesi başarısız oldu..")
            sys.stderr.flush()
            
app=QApplication(sys.argv)
mail=Mail()
sys.exit(app.exec_())