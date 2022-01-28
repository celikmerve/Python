import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class oturum_acma_bilgisi():

    def __init__(self):
        super().__init__() 
        self.hatalar()
        self.ekrana_yazdirma()
        self.mail_gonderme()
        
    def hatalar(self):
       self.liste=list()
       with open("hatalar.txt","r",encoding="utf-8") as file:
           for satir in file:
               satir=satir[:-1]
               satir_elemanlari=satir.split("\t")
               bilgi=satir_elemanlari[0]
               if(bilgi=="Bilgi"):
                   self.liste.append(satir_elemanlari[1])
       self.liste="\n".join(self.liste)
        
        
    def ekrana_yazdirma(self):
        print("Açık kimlik bilgileri kullanılarak oturum açılmaya çalışıldı.")
        print(self.liste)
        
    def mail_gonderme(self):
        mesaj=MIMEMultipart()
        mesaj["From"]="9890merve9890@gmail.com"
        mesaj["To"]="9890merve9890@gmail.com"
        mesaj["Subject"]="Oturum Açma Bilgisi"
      
        yazi="Açık kimlik bilgileri kullanılarak oturum açılmaya çalışıldı."+"\n"+self.liste
        mesaj_govdesi=MIMEText(yazi,"plain")
        mesaj.attach(mesaj_govdesi)
        try:
            mail=smtplib.SMTP("smtp.gmail.com",587)
            mail.ehlo()
            mail.starttls()
            mail.login("9890merve9890@gmail.com","sifre")
            mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())
            print("Mail başarıyla gönderildi.")
            mail.close()
        except:
            sys.stderr.write("Mail göndermesi başarısız oldu.")
            sys.stderr.flush()


giris = oturum_acma_bilgisi()



        

        
         

        