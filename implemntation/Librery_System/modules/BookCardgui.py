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
        self.image.setPixmap(QPixmap(128, 193))
        
        self.message = myThread(image_path)
        self.message.start()
        self.message.update_image.connect(self.call_update_image)
                
        self.setup()
        self.show()
        
        
    def setup(self):   
        self.card.setGeometry(0,0,128,272)
        self.card.setStyleSheet("QLabel{\
            color:white;\
            }\
            ")
        self.setFixedSize(128,272)
        self.image.setParent(self.card)
        self.image.setGeometry(QRect(QPoint(0,0),QSize(128,193)))
        self.image.setAlignment(Qt.AlignHCenter)
        self.name.setParent(self.card)
        self.name.setWordWrap(True)
        self.name.setGeometry(QRect(QPoint(0,200),QSize(128,35)))
        self.name.setAlignment(Qt.AlignHCenter)
        self.author.setParent(self.card)
        self.author.setWordWrap(True)
        self.author.setGeometry(QRect(QPoint(0,252),QSize(128,20)))
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
                        self.update_image.emit( QPixmap(image).scaled(128, 193, Qt.KeepAspectRatio) )

if __name__ == '__main__':
    path="https://m.media-amazon.com/images/I/51p-p9etkTL.jpg"
    name = "Lion"
    author = "some lion"

    babylion=(name,author,path)

    app = QApplication([])
    card=Card(babylion)
    sys.exit(app.exec_())

