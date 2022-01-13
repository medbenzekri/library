import requests
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QGridLayout, QMainWindow
# GUI FILE
from library.implemntation.Librery_System.Login_window import LoginWindow
from library.implemntation.Librery_System.modules.libgui import Ui_MainWindow
# IMPORT FUNCTIONS
from library.implemntation.Librery_System.modules.ui_functions import UIFunctions
from library.implemntation.Librery_System.modules.Message import myMessage
from library.implemntation.Librery_System.modules.BookCardgui import Card, myThread
from library.implemntation.Librery_System.modules.DatabaseFetcher import get_books
from library.implemntation.Librery_System.modules.Layout import FlowLayout
import re


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.menu_toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self))
        self.ui.home_btn.clicked.connect(lambda: self.ui.pages_Widget.setCurrentWidget(self.ui.home_page))
        self.ui.search_btn.clicked.connect(lambda: self.ui.pages_Widget.setCurrentWidget(self.ui.search_page))

        self.ui.searchbtn.clicked.connect(lambda: self.book_search(self.ui.searchtext.text()))
        self.ui.add_book_btn.hide()
        self.ui.add_user_btn.hide()
        self.message = myMessage(self)
        self.books_grid = FlowLayout(self.ui.scrollAreaWidgetContents)
        self.books_grid.setSpacing(10)
        self.show_books(500)
        
    def show_books(self,num="NULL",name=""):
            books= Fetcher.get_books(num,name)
            for i,book in enumerate(books):
                self.books_grid.addWidget(Card(book,self))

    def show_book_info(self, data: dict):
        self.ui.title.setText(data["title"])
        imagepath = re.sub("&zoom=1", "", data["image"])
        self.ui.image.setPixmap(QPixmap(250, 321))
        self.imagefetcher = myThread(imagepath, (250, 321))
        self.imagefetcher.start()
        self.imagefetcher.update_image.connect(self.ui.image.setPixmap)
        self.ui.description.setText(data["description"])
        self.ui.authors.setText(data["authors"])
        self.ui.publisher.setText(data["publisher"])
        self.ui.date.setText(data["publishing_date"])
        self.ui.isbn.setText(data["ISBN"])
        self.ui.geners.setText(data['categories'])
        self.ui.pages_Widget.setCurrentWidget(
            self.ui.book_page)
    def book_search(self,name:str):
        for i in reversed(range(self.books_grid.count())): 
            self.books_grid.itemAt(i).widget().setParent(None)
        self.show_books(name)

        def pick():
            z = requests.get(
                "http://20.111.12.142/rente.php?user=" + LoginWindow.username + "&&book=" + data["Id"]).text
            self.message.success(z)

        def reserve():
            z = requests.get(
                "http://20.111.12.142/reserve.php?user=" + LoginWindow.username + "&&book=" + data["Id"]).text
            self.message.success(z)

        self.ui.pick.clicked.connect(lambda z: pick())
        self.ui.reserve.clicked.connect(lambda z: reserve())
        self.ui.pages_Widget.setCurrentWidget(
            self.ui.book_page)




