import requests
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Card(QWidget):
    def __init__(self, data, parent=None):
        super().__init__()
        name, author, image_path = data['title'], data[
            'authors'], data['image']
        self.card = QFrame(self)

        self.image = QLabel()  # Image
        self.name = QLabel(name)  # Title
        image = QPixmap(128, 193)
        image.fill(Qt.GlobalColor.darkGray)
        self.image.setPixmap(QPixmap(128, 193))
        self.data = data
        self.p = parent
        self.message = myThread(image_path,(128,193))
        self.message.start()
        self.message.update_image.connect(self.call_update_image)

        self.setup()
        self.show()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.p.show_book_info(self.data)
        else:
            super().mousePressEvent(event)

    def setup(self):
        self.card.setGeometry(0, 0, 128, 272)
        self.card.setStyleSheet("QLabel{\
            color:white;\
            }\
            ")
        self.setFixedSize(128, 272)
        self.image.setParent(self.card)
        self.image.setGeometry(QRect(QPoint(0, 0), QSize(128, 193)))
        self.image.setAlignment(Qt.AlignHCenter)
        self.name.setParent(self.card)
        self.name.setWordWrap(True)
        self.name.setGeometry(QRect(QPoint(0, 200), QSize(128, 35)))
        self.name.setAlignment(Qt.AlignHCenter)
        self.author.setParent(self.card)
        self.author.setWordWrap(True)
        self.author.setGeometry(QRect(QPoint(0, 252), QSize(128, 20)))
        self.author.setAlignment(Qt.AlignHCenter)

    def call_update_image(self, image):
        self.image.setPixmap(image)


class myThread(QThread):
    update_image = Signal(QPixmap)

    def __init__(self, path: str,scale:tuple,parent=None):
        super(myThread, self).__init__(parent)
        self.path = path
        self.scale= scale
        
    def run(self):
        data = requests.get(self.path).content
        image = QImage()
        image.loadFromData(data)
        self.update_image.emit(QPixmap(image).scaled(
            self.scale[0], self.scale[1], Qt.KeepAspectRatio))


if __name__ == '__main__':
    path = "https://m.media-amazon.com/images/I/51p-p9etkTL.jpg"
    name = "Lion"
    author = "some lion"

    babylion = {'title': name, 'authors': author, 'image': path}

    app = QApplication([])
    card = Card(babylion)
    sys.exit(app.exec_())

