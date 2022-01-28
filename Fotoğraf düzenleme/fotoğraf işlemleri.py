from PIL import Image,ImageFilter
import sys


from PyQt5.QtWidgets import QWidget,QCheckBox,QApplication,QPushButton,QVBoxLayout

class Pencere(QWidget):
    def __init__(self):
        super(). __init__()
        self.init_ui()
    
    def init_ui(self):
        self.checkbox1=QCheckBox("Resmi 180 derece döndürmek istermisin?")
        self.checkbox2=QCheckBox("Resmi 90 derece döndürmek ister misin?")
        self.checkbox3=QCheckBox("Resmi siyah beyaz renge dönüştürmek ister misin?")
        self.checkbox4=QCheckBox("Resmin boyutunu değiştirmek ister misin?")
        self.checkbox5=QCheckBox("Resmi bulanıklaştırmak ister misin?")
        self.checkbox6=QCheckBox("Resmi kırpmak ister misin?") 
        self.buton=QPushButton("OK")
        
        v_box=QVBoxLayout()
        v_box.addWidget(self.checkbox1)
        v_box.addWidget(self.checkbox2)
        v_box.addWidget(self.checkbox3)
        v_box.addWidget(self.checkbox4)
        v_box.addWidget(self.checkbox5)
        v_box.addWidget(self.checkbox6)
        v_box.addWidget(self.buton)
        self.setLayout(v_box)
        self.setWindowTitle("Fotoğraf İşlemleri")
        self.buton.clicked.connect(lambda: self.fnk1(self.checkbox1.isChecked()))
        self.buton.clicked.connect(lambda: self.fnk2(self.checkbox2.isChecked()))
        self.buton.clicked.connect(lambda: self.fnk3(self.checkbox3.isChecked()))
        self.buton.clicked.connect(lambda: self.fnk4(self.checkbox4.isChecked()))
        self.buton.clicked.connect(lambda: self.fnk5(self.checkbox5.isChecked()))
        self.buton.clicked.connect(lambda: self.fnk6(self.checkbox6.isChecked()))
       
        self.show()
        
    def fnk1(self,checkbox1):
        if checkbox1:
            image=Image.open("biz.jpg")
            image.rotate(180).save("biz.jpg")
        
    def fnk2(self,value):
        if value:
            image=Image.open("biz.jpg")
            image.rotate(90).save("biz.jpg")
        
    def fnk3(self,value):
        if value:
            image=Image.open("biz.jpg")
            image.convert(mode="L").save("biz.jpg")
        
    def fnk4(self,value):
        if value:
            image=Image.open("biz.jpg")
            image.thumbnail((400,400))
            image.save("biz.jpg")
        
    def fnk5(self,value):
        if value:
            image=Image.open("biz.jpg")
            image.filter(ImageFilter.GaussionBlur(500)).save("biz.jpg")
        
        
    def fnk6(self,value):
        if value:
            image=Image.open("biz.jpg")
    
            image.crop((340,0,950,600)).save("biz.jpg")
        
        
app=QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec_())       
        