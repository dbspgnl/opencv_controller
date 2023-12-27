import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QMenu
from PySide6.QtGui import QAction, QKeySequence
from ui.main_ui import Ui_MainWindow
import os
import cv2
from opencv.blend import ImageBlendingOnVideo

class Controller_Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Controller_Window, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Controller')
        
        self.options = ('영상 불러오기', '이미지 호출')
        self.comboBox.addItems(self.options)
        self.comboBox.currentTextChanged.connect(self.changeComboBox)
        
        self.type_first_file = 'Video File (*.mp4 *.avi)'
        self.type_second_file = 'Video File (*.mp4 *.avi)'
        self.file_first = None
        self.file_second = None
        
        self.btn_first.clicked.connect(self.setFirstFile)
        self.btn_second.clicked.connect(self.setSecondFile)
        self.btn_launch.clicked.connect(self.launchDialog)
        
        
    def changeComboBox(self):
        print(self.type_second_file)
        self.type_second_file = 'Image File (*.png *.jpg)'
        print(self.type_second_file)
        
    def launchDialog(self):
        option = self.options.index(self.comboBox.currentText())
        if option == 0:
            pass
        elif option == 1:
            ImageBlendingOnVideo(self.file_first[0], self.file_second[0])
            pass
        else:
            print('Got Nothing')
        self.isCheckFile()
        
    def setFirstFile(self):
        file_filter = self.type_first_file
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a file',
            dir=os.getcwd(),
            filter=file_filter,
            selectedFilter =self.type_first_file
        )
        self.file_first = response
        self.btn_first.setStyleSheet('border: 1px solid #09E65A')
        self.textBrowser.setText(str(response) + '\n' + self.textBrowser.toPlainText())
        
    def setSecondFile(self):
        file_filter = self.type_second_file
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a file',
            dir=os.getcwd(),
            filter=file_filter,
            selectedFilter =self.type_second_file
        )
        self.file_second = response
        self.btn_second.setStyleSheet('border: 1px solid #09E65A')
        self.textBrowser.setText(str(response) + '\n' + self.textBrowser.toPlainText())

    def isCheckFile(self):
        if self.file_first is None:
            self.btn_first.setStyleSheet('border: 1px solid #EB3F00')
        if self.file_second is None:
            self.btn_second.setStyleSheet('border: 1px solid #EB3F00')
        
app = QApplication(sys.argv)
windows = Controller_Window() #QWidget()
windows.show()

app.exec_()