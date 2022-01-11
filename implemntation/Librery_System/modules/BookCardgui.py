import requests
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Card(QWidget):
    def __init__(self, data, parent=None):
        super().__init__()
        name, image_path = data['title'], data['image']
        self.card = QFrame(self)

        self.image = QLabel()  # Image
        self.name = QLabel(name)  # Title
        image = QPixmap(128, 193)
        image.fill(Qt.GlobalColor.darkGray)
        self.image.setPixmap(QPixmap(128, 193))

        self.data = data  # Book data
        self.p = parent  # Parent

        self.message = myThread(image_path)
        self.message.start()
        self.message.update_image.connect(self.call_update_image)

        self.setup()
        self.show()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.p.ui.title.setText(self.data['title'])
            self.p.ui.description.setText(self.data['description'])
            self.p.ui.authors.setText(self.data['authors'])
            self.p.ui.publisher.setText(self.data['publisher'])
            self.p.ui.date.setText(self.data['publishing_date'])
            self.p.ui.isbn.setText(self.data['ISBN'])

            self.p.ui.back.mousePressEvent = lambda x: self.p.ui.pages_Widget.setCurrentWidget(self.p.ui.home_page)  # Back to parent

            self.p.ui.message = myThread2(self.data['image'])
            self.p.ui.message.start()
            self.p.ui.message.update_image.connect(self.call_update_book_image)

            self.p.ui.image.setPixmap(QPixmap())

            self.p.ui.pages_Widget.setCurrentWidget(self.p.ui.book_page)

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
        self.name.setGeometry(QRect(QPoint(0, 200), QSize(128, 50)))
        self.name.setAlignment(Qt.AlignHCenter)

    def call_update_image(self, image):
        self.image.setPixmap(image)

    def call_update_book_image(self, image):
        self.p.ui.image.setPixmap(image)


class myThread(QThread):
    update_image = Signal(QPixmap)

    def __init__(self, url: str, parent=None):
        super(myThread, self).__init__(parent)
        self.url = url

    def run(self):
        data = requests.get(self.url).content
        image = QImage()
        image.loadFromData(data)
        self.update_image.emit(QPixmap(image).scaled(128, 193, Qt.KeepAspectRatio))


class myThread2(QThread):
    update_image = Signal(QPixmap)

    def __init__(self, url: str, parent=None):
        super(myThread2, self).__init__(parent)
        self.url = url

    def run(self):
        try :
            data = requests.get(self.url).content
            image = QImage()
            image.loadFromData(data)
            self.update_image.emit(QPixmap(image).scaled(250, 321, Qt.KeepAspectRatio))
        except :
            print(self.url)


if __name__ == '__main__':
    path = "https://m.media-amazon.com/images/I/51p-p9etkTL.jpg"
    name = "Lion"
    author = "some lion"

    babylion = {'title': name, 'authors': author, 'image': path}

    app = QApplication([])
    card = Card(babylion)
    sys.exit(app.exec_())

