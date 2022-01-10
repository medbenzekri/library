# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'libgui.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1007, 700)
        MainWindow.setMinimumSize(QSize(45, 700))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"\n"
"QFrame>QPushButton{\n"
"    background-position:  left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 18px solid transparent ;\n"
"	background-color: rgb(255, 0, 0);\n"
"	text-align: left;\n"
"	padding-left: 48px;	\n"
"\n"
"}\n"
"/*\n"
"//////////////////*/\n"
"#top_bar:hover{\n"
"background-color: rgb(46, 52, 54) ;\n"
"}\n"
" #centralwidget *{\n"
"background-color: rgb(46, 52, 54);\n"
"}\n"
"QLabel{\n"
"color :white;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.topbar = QFrame(self.centralwidget)
        self.topbar.setObjectName(u"topbar")
        self.topbar.setMinimumSize(QSize(0, 40))
        self.topbar.setMaximumSize(QSize(16777215, 40))
        self.topbar.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.topbar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.topbar.setFrameShape(QFrame.NoFrame)
        self.topbar.setFrameShadow(QFrame.Raised)
        self.frame_top = QFrame(self.topbar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setGeometry(QRect(422, 0, 400, 40))
        self.frame_top.setMaximumSize(QSize(400, 40))
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.topbar)

        self.content = QFrame(self.centralwidget)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.content)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(60, 0))
        self.frame_left_menu.setMaximumSize(QSize(60, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setStyleSheet(u"\n"
"QPushButton:hover{\n"
"background-color: rgb(46, 52, 54);\n"
"}")
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_menus)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.menu_toggle = QPushButton(self.frame_menus)
        self.menu_toggle.setObjectName(u"menu_toggle")
        self.menu_toggle.setMinimumSize(QSize(0, 45))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(35, 35, 35, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 128))
        brush2.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush3 = QBrush(QColor(255, 255, 255, 128))
        brush3.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush4 = QBrush(QColor(255, 255, 255, 128))
        brush4.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.menu_toggle.setPalette(palette)
        self.menu_toggle.setStyleSheet(u"background-image: url(:/icons/icons/menu.png);")
        self.menu_toggle.setCheckable(False)
        self.menu_toggle.setAutoDefault(False)
        self.menu_toggle.setFlat(False)

        self.verticalLayout_3.addWidget(self.menu_toggle)

        self.home_btn = QPushButton(self.frame_menus)
        self.home_btn.setObjectName(u"home_btn")
        self.home_btn.setMinimumSize(QSize(0, 45))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush5 = QBrush(QColor(255, 255, 255, 128))
        brush5.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush6 = QBrush(QColor(255, 255, 255, 128))
        brush6.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush7 = QBrush(QColor(255, 255, 255, 128))
        brush7.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.home_btn.setPalette(palette1)
        self.home_btn.setStyleSheet(u"background-image: url(:/icons/icons/icons8-home-24.png);")
        self.home_btn.setCheckable(False)
        self.home_btn.setAutoDefault(False)
        self.home_btn.setFlat(False)

        self.verticalLayout_3.addWidget(self.home_btn)

        self.search_btn = QPushButton(self.frame_menus)
        self.search_btn.setObjectName(u"search_btn")
        self.search_btn.setMinimumSize(QSize(0, 45))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush8 = QBrush(QColor(255, 255, 255, 128))
        brush8.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush9 = QBrush(QColor(255, 255, 255, 128))
        brush9.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush10 = QBrush(QColor(255, 255, 255, 128))
        brush10.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        self.search_btn.setPalette(palette2)
        self.search_btn.setStyleSheet(u"background-image: url(:/icons/icons/icons8-search-24.png);")
        self.search_btn.setCheckable(False)
        self.search_btn.setAutoDefault(False)
        self.search_btn.setFlat(False)

        self.verticalLayout_3.addWidget(self.search_btn)

        self.wishlist_btn = QPushButton(self.frame_menus)
        self.wishlist_btn.setObjectName(u"wishlist_btn")
        self.wishlist_btn.setMinimumSize(QSize(0, 45))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush11 = QBrush(QColor(255, 255, 255, 128))
        brush11.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush12 = QBrush(QColor(255, 255, 255, 128))
        brush12.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush13 = QBrush(QColor(255, 255, 255, 128))
        brush13.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush13)
#endif
        self.wishlist_btn.setPalette(palette3)
        self.wishlist_btn.setStyleSheet(u"background-image: url(:/icons/icons/icons8-bookmark-24.png);")
        self.wishlist_btn.setCheckable(False)
        self.wishlist_btn.setAutoDefault(False)
        self.wishlist_btn.setFlat(False)

        self.verticalLayout_3.addWidget(self.wishlist_btn)


        self.verticalLayout_2.addWidget(self.frame_menus, 0, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.NoFrame)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pages_Widget = QStackedWidget(self.frame_pages)
        self.pages_Widget.setObjectName(u"pages_Widget")
        self.pages_Widget.setMinimumSize(QSize(3, 0))
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.searchbar = QFrame(self.home_page)
        self.searchbar.setObjectName(u"searchbar")
        self.searchbar.setGeometry(QRect(220, 10, 221, 28))
        self.searchbar.setMaximumSize(QSize(221, 28))
        self.searchbar.setStyleSheet(u"background-color:white;\n"
"border-radius:13px;")
        self.searchbar.setFrameShape(QFrame.StyledPanel)
        self.searchbar.setFrameShadow(QFrame.Raised)
        self.searchbtn = QPushButton(self.searchbar)
        self.searchbtn.setObjectName(u"searchbtn")
        self.searchbtn.setGeometry(QRect(190, 0, 31, 28))
        self.searchbtn.setLayoutDirection(Qt.LeftToRight)
        self.searchbtn.setStyleSheet(u"background-image: url(:/icons/icons/icons8-search-16.png);\n"
"background-repeat: no-repeat;\n"
"border: none;\n"
"background-position:  center;\n"
"")
        self.searchtext = QLineEdit(self.searchbar)
        self.searchtext.setObjectName(u"searchtext")
        self.searchtext.setGeometry(QRect(12, 0, 181, 28))
        font = QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.searchtext.setFont(font)
        self.scrollArea = QScrollArea(self.home_page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 130, 921, 511))
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 921, 511))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label = QLabel(self.home_page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 96, 131, 21))
        font1 = QFont()
        font1.setFamilies([u"DejaVu Sans Mono"])
        font1.setBold(True)
        self.label.setFont(font1)
        self.pages_Widget.addWidget(self.home_page)
        self.search_page = QWidget()
        self.search_page.setObjectName(u"search_page")
        self.pages_Widget.addWidget(self.search_page)
        self.wishlist_page = QWidget()
        self.wishlist_page.setObjectName(u"wishlist_page")
        self.pages_Widget.addWidget(self.wishlist_page)
        self.book_page = QWidget()
        self.book_page.setObjectName(u"book_page")
        self.book_page.setStyleSheet(u"QWidget{\n"
"                     background-color: rgb(46, 52, 54);\n"
"                 }\n"
"                 QWidget > QLabel{\n"
"                     color : rgb(240,240,240);\n"
"                 }\n"
"                 QWidget > QPushButton{\n"
"                     color : rgb(255,255,255);\n"
"                    background-color : gb(240,200,240);\n"
"                 }")
        self.image = QLabel(self.book_page)
        self.image.setObjectName(u"image")
        self.image.setGeometry(QRect(30, 60, 250, 321))
        self.image.setStyleSheet(u"")
        self.image.setFrameShape(QFrame.NoFrame)
        self.image.setPixmap(QPixmap(u":/icons/icons/test.jpg"))
        self.image.setScaledContents(True)
        self.title = QLabel(self.book_page)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(310, 50, 381, 91))
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"FreeSans"])
        font2.setPointSize(22)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setStrikeOut(False)
        font2.setKerning(True)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.title.setFont(font2)
        self.title.setStyleSheet(u"")
        self.title.setLineWidth(1)
        self.title.setScaledContents(False)
        self.title.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.title.setWordWrap(True)
        self.title.setIndent(0)
        self.title.setOpenExternalLinks(False)
        self.description = QLabel(self.book_page)
        self.description.setObjectName(u"description")
        self.description.setGeometry(QRect(310, 190, 611, 241))
        font3 = QFont()
        font3.setFamilies([u"Ubuntu Condensed"])
        font3.setPointSize(13)
        font3.setBold(False)
        font3.setItalic(False)
        self.description.setFont(font3)
        self.description.setTextFormat(Qt.PlainText)
        self.description.setScaledContents(False)
        self.description.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.description.setWordWrap(True)
        self.pick = QPushButton(self.book_page)
        self.pick.setObjectName(u"pick")
        self.pick.setGeometry(QRect(310, 150, 89, 25))
        self.reserve = QPushButton(self.book_page)
        self.reserve.setObjectName(u"reserve")
        self.reserve.setGeometry(QRect(420, 150, 89, 25))
        self.label_6 = QLabel(self.book_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 10, 201, 31))
        font4 = QFont()
        font4.setFamilies([u"Ubuntu Condensed"])
        font4.setPointSize(16)
        font4.setBold(True)
        self.label_6.setFont(font4)
        self.label_6.setStyleSheet(u"QLabel {\n"
"                     color : #C3DDE6;\n"
"                 }")
        self.widget = QWidget(self.book_page)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 430, 781, 211))
        self.widget.setStyleSheet(u"")
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 0, 61, 31))
        self.label_7.setFont(font4)
        self.label_7.setStyleSheet(u"QLabel {\n"
"                     color : #C3DDE6;\n"
"                 }")
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(40, 40, 61, 31))
        self.label_8.setFont(font4)
        self.label_8.setStyleSheet(u"QLabel {\n"
"                     color : rgb(89, 89, 89);\n"
"                 }")
        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(270, 40, 91, 31))
        self.label_9.setFont(font4)
        self.label_9.setStyleSheet(u"QLabel {\n"
"                     color : rgb(89, 89, 89);\n"
"                 }")
        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(40, 120, 111, 31))
        self.label_10.setFont(font4)
        self.label_10.setStyleSheet(u"QLabel {\n"
"                     color : rgb(89, 89, 89);\n"
"                 }")
        self.authors = QLabel(self.widget)
        self.authors.setObjectName(u"authors")
        self.authors.setGeometry(QRect(40, 80, 211, 41))
        font5 = QFont()
        font5.setFamilies([u"Ubuntu Condensed"])
        font5.setPointSize(10)
        font5.setBold(True)
        self.authors.setFont(font5)
        self.authors.setStyleSheet(u"QLabel {\n"
"                     color : rgb(240,240,240);\n"
"                 }")
        self.authors.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.authors.setWordWrap(True)
        self.publisher = QLabel(self.widget)
        self.publisher.setObjectName(u"publisher")
        self.publisher.setGeometry(QRect(270, 80, 211, 41))
        self.publisher.setFont(font5)
        self.publisher.setStyleSheet(u"QLabel {\n"
"                     color : rgb(240,240,240);\n"
"                 }")
        self.publisher.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.publisher.setWordWrap(True)
        self.date = QLabel(self.widget)
        self.date.setObjectName(u"date")
        self.date.setGeometry(QRect(40, 160, 211, 21))
        font6 = QFont()
        font6.setFamilies([u"Ubuntu Condensed"])
        font6.setPointSize(15)
        font6.setBold(True)
        self.date.setFont(font6)
        self.date.setStyleSheet(u"QLabel {\n"
"                     color : rgb(240,240,240);\n"
"                 }")
        self.date.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.date.setWordWrap(True)
        self.label_14 = QLabel(self.widget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(520, 40, 91, 31))
        self.label_14.setFont(font4)
        self.label_14.setStyleSheet(u"QLabel {\n"
"                     color : rgb(89, 89, 89);\n"
"                 }")
        self.isbn = QLabel(self.widget)
        self.isbn.setObjectName(u"isbn")
        self.isbn.setGeometry(QRect(520, 80, 211, 41))
        font7 = QFont()
        font7.setFamilies([u"Ubuntu Condensed"])
        font7.setPointSize(13)
        font7.setBold(True)
        self.isbn.setFont(font7)
        self.isbn.setStyleSheet(u"QLabel {\n"
"                     color : rgb(240,240,240);\n"
"                 }")
        self.isbn.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.isbn.setWordWrap(True)
        self.label_11 = QLabel(self.book_page)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(310, 10, 61, 31))
        self.label_11.setFont(font4)
        self.label_11.setStyleSheet(u"QLabel {\n"
"                     color : #C3DDE6;\n"
"                 }")
        self.pages_Widget.addWidget(self.book_page)

        self.verticalLayout_5.addWidget(self.pages_Widget)


        self.horizontalLayout.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.content)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.menu_toggle, self.search_btn)
        QWidget.setTabOrder(self.search_btn, self.wishlist_btn)

        self.retranslateUi(MainWindow)

        self.menu_toggle.setDefault(False)
        self.home_btn.setDefault(False)
        self.search_btn.setDefault(False)
        self.wishlist_btn.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"library", None))
        self.menu_toggle.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.home_btn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.search_btn.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.wishlist_btn.setText(QCoreApplication.translate("MainWindow", u"My Books", None))
        self.searchbtn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Books", None))
        self.book_page.setWindowTitle(QCoreApplication.translate("MainWindow", u"Form", None))
        self.image.setText("")
        self.title.setText("")
        self.description.setText("")
        self.pick.setText(QCoreApplication.translate("MainWindow", u"Pick", None))
        self.reserve.setText(QCoreApplication.translate("MainWindow", u"Reserve", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Book Details", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Details", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Authors", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Publisher", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Released Date", None))
        self.authors.setText("")
        self.publisher.setText("")
        self.date.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"ISBN", None))
        self.isbn.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Title", None))
    # retranslateUi

