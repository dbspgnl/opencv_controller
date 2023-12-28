# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(243, 304)
        MainWindow.setStyleSheet(u"")
        self.actionversion = QAction(MainWindow)
        self.actionversion.setObjectName(u"actionversion")
        self.actionclose = QAction(MainWindow)
        self.actionclose.setObjectName(u"actionclose")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setFocusPolicy(Qt.ClickFocus)
        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(u"formLayout")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.comboBox)

        self.btn_first = QPushButton(self.centralwidget)
        self.btn_first.setObjectName(u"btn_first")

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.btn_first)

        self.btn_second = QPushButton(self.centralwidget)
        self.btn_second.setObjectName(u"btn_second")

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.btn_second)

        self.btn_launch = QPushButton(self.centralwidget)
        self.btn_launch.setObjectName(u"btn_launch")

        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.btn_launch)

        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setStyleSheet(u"background-color: white;")
        self.textBrowser.setFrameShape(QFrame.StyledPanel)

        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.textBrowser)

        self.btn_save = QPushButton(self.centralwidget)
        self.btn_save.setObjectName(u"btn_save")

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.btn_save)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 243, 22))
        self.menuinfo = QMenu(self.menubar)
        self.menuinfo.setObjectName(u"menuinfo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuinfo.menuAction())
        self.menuinfo.addAction(self.actionclose)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionversion.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionclose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.btn_first.setText(QCoreApplication.translate("MainWindow", u"First Select File", None))
        self.btn_second.setText(QCoreApplication.translate("MainWindow", u"Second Select File", None))
        self.btn_launch.setText(QCoreApplication.translate("MainWindow", u"Launch", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"Save Path", None))
        self.menuinfo.setTitle(QCoreApplication.translate("MainWindow", u"info", None))
    # retranslateUi

