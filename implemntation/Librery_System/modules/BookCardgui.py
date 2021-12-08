from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import requests

class Card(QWidget):
    def __init__(self,data):
        name,author,image_path=data.values()
        # self.Layout= QVBoxLayout()
        self.card=QFrame()
        self.image=QLabel()
        self.name=QLabel(name)
        self.author=QLabel(author)
        self.image.setPixmap(self.image_data(image_path))
        self.setup()
        
    def image_data(self,path):
        data= requests.get(path).content
        image=QImage()
        image.loadFromData(data)
        return QPixmap(image)
    def setup(self):
        self.card.setMaximumSize(110,212)
        self.image.setGeometry(QRect(QPoint(0,0),QSize(110,131)))
        self.image.setParent(self.card)
        self.name.setGeometry(QRect(QPoint(0,140),QSize(110,31)))
        self.name.setParent(self.card)
        self.author.setGeometry(QRect(QPoint(0,192),QSize(110,20)))
        self.author.setParent(self.card)
        


    
