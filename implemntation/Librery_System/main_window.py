from PySide2.QtWidgets import QGridLayout, QLayoutItem, QMainWindow
# GUI FILE
from modules.libgui import Ui_MainWindow
# IMPORT FUNCTIONS
from modules.ui_functions import UIFunctions
from modules.Message import myMessage
from modules.BookCardgui import Card 
from modules.DatabaseFetcher import Fetcher
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
                self.books_grid.addWidget(Card(book),i//8,i%8)
        
