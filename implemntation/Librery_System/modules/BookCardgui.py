from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import requests
import sys
class Card(QWidget):
    def __init__(self,data):
        super().__init__()
        name,author,image_path=data.values()
        self.card=QFrame(self)
        self.image=QLabel()
        self.name=QLabel(name)
        self.author=QLabel(author)
        self.image.setPixmap(self.image_data(image_path))
        self.setup()
        self.show()
        
    def image_data(self,path):
        data= requests.get(path).content
        image=QImage()
        image.loadFromData(data)
        return QPixmap(image).scaled(110, 131, Qt.KeepAspectRatio)
    def setup(self):   
        self.card.setGeometry(0,0,110,212)
        self.setFixedSize(110,212)
        self.image.setParent(self.card)
        self.image.setGeometry(QRect(QPoint(0,0),QSize(110,131)))
        self.name.setParent(self.card)
        self.name.setGeometry(QRect(QPoint(0,140),QSize(110,31)))
        self.name.setAlignment(Qt.AlignHCenter)
        self.author.setParent(self.card)
        self.author.setGeometry(QRect(QPoint(0,192),QSize(110,20)))
        self.author.setAlignment(Qt.AlignHCenter)
        

path="https://m.media-amazon.com/images/I/51p-p9etkTL.jpg"
babylion={"name":"Lion","author":"some lion","image":path}
app = QApplication([])
card=Card(babylion)
sys.exit(app.exec_())
    
