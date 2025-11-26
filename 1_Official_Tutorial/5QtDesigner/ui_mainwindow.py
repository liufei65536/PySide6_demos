# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_DesignedWindow(object):
    def setupUi(self, DesignedWindow):
        if not DesignedWindow.objectName():
            DesignedWindow.setObjectName(u"DesignedWindow")
        DesignedWindow.resize(800, 600)
        self.centralwidget = QWidget(DesignedWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        DesignedWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(DesignedWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        self.menuHello = QMenu(self.menubar)
        self.menuHello.setObjectName(u"menuHello")
        DesignedWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(DesignedWindow)
        self.statusbar.setObjectName(u"statusbar")
        DesignedWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuHello.menuAction())

        self.retranslateUi(DesignedWindow)

        QMetaObject.connectSlotsByName(DesignedWindow)
    # setupUi

    def retranslateUi(self, DesignedWindow):
        DesignedWindow.setWindowTitle(QCoreApplication.translate("DesignedWindow", u"MainWindow", None))
        self.menuHello.setTitle(QCoreApplication.translate("DesignedWindow", u"Hello", None))
    # retranslateUi

