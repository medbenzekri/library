from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QGridLayout, QLayoutItem, QMainWindow
# GUI FILE
from modules.libgui import Ui_MainWindow
# IMPORT FUNCTIONS
from modules.ui_functions import UIFunctions
from modules.Message import myMessage
from modules.BookCardgui import Card,myThread 
from modules.DatabaseFetcher import Fetcher
import re
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.menu_toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self))
        self.ui.home_btn.clicked.connect(lambda: self.ui.pages_Widget.setCurrentWidget(self.ui.home_page))
        self.ui.search_btn.clicked.connect(lambda: self.ui.pages_Widget.setCurrentWidget(self.ui.search_page))
        self.message = myMessage(self,self)
        self.books_grid=QGridLayout(self.ui.scrollAreaWidgetContents)
        self.books_grid.setVerticalSpacing(10)
        self.show_books()
        
    def show_books(self):
            
            books= Fetcher.get_books(500)
            for i,book in enumerate(books):
                self.books_grid.addWidget(Card(book,self),i//8,i%8)

    def show_book_info(self,data:dict):
        self.ui.title.setText(data["title"])
        imagepath= re.sub("&edge=curl","",data["image"])
        self.ui.image.setPixmap(QPixmap(250,321))
        self.imagefetcher= myThread(imagepath,(250,321))
        self.imagefetcher.start()
        self.imagefetcher.update_image.connect(self.ui.image.setPixmap)
        self.ui.description.setText(data["description"])
        self.ui.authors.setText(data["GROUP_CONCAT(author_book.name)"])
        self.ui.publisher.setText(data["publisher"])
        self.ui.date.setText(data["publishing_date"])
        self.ui.isbn.setText(data["ISBN"])
        self.ui.pages_Widget.setCurrentWidget(
            self.ui.book_page)

        
