from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import requests,sys

class Card(QWidget):
    def __init__(self,data):
        super().__init__()
        name,author,image_path=data
        self.card=QFrame(self)
        self.image=QLabel()
        self.name=QLabel(name)
        self.author=QLabel(author)
        self.image.setPixmap(QPixmap(110, 131))
        
        self.message = myThread(image_path)
        self.message.start()
        self.message.update_image.connect(self.call_update_image)
                
        self.setup()
        self.show()
        
        
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
        
    def call_update_image(self,image):
            self.image.setPixmap(image)
        
class myThread(QThread):
                update_image = Signal(QPixmap)
                
                def __init__(self,path : str,parent = None):
                        super(myThread, self).__init__(parent)
                        self.path = path
                
                def run(self): 
                        data = requests.get(self.path).content
                        image = QImage()
                        image.loadFromData(data)
                        self.update_image.emit( QPixmap(image).scaled(110, 131, Qt.KeepAspectRatio) )

if __name__ == '__main__':
    path="https://m.media-amazon.com/images/I/51p-p9etkTL.jpg"
    name = "Lion"
    author = "some lion"

    babylion=(name,author,path)

    app = QApplication([])
    card=Card(babylion)
    sys.exit(app.exec_())

