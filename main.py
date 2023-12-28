import sys
import os
import time
import cv2
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QMenu
from PySide6.QtGui import QAction, QKeySequence
from ui.main_ui import Ui_MainWindow
from opencv.blend import ImageBlendingOnVideo
from opencv.mask import ImageMask
from opencv.imageOnVideo import ImageOnVideo

class Controller_Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Controller_Window, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Controller')
        
        self.actionclose.setStatusTip('Exit application')
        self.actionclose.setShortcut('Ctrl+Q')
        self.actionclose.triggered.connect(lambda:self.close())
        
        self.options = ('영상 불러오기', '이미지 호출', '도면 마스크 영역 추출', '영상 위에 이미지(+알파) 합성')
        self.comboBox.addItems(self.options)
        self.comboBox.currentTextChanged.connect(self.changeComboBox)
        
        # self.type_first_file = 'Video File (*.mp4 *.avi)'
        # self.type_second_file = 'Video File (*.mp4 *.avi)'
        self.file_first = []
        self.file_second = []
        self.file_save = None
        self.file_first_multy = 0
        self.file_second_multy = 0
        
        self.btn_first.clicked.connect(self.setFirstFile)
        self.btn_second.clicked.connect(self.setSecondFile)
        self.btn_save.clicked.connect(self.setSavePath)
        self.btn_launch.clicked.connect(self.launchDialog)
        
        
    def changeComboBox(self):
        self.btn_first.setStyleSheet('')
        self.btn_second.setStyleSheet('')
        self.btn_first.setEnabled(True)
        self.btn_second.setEnabled(True)
        self.btn_save.setEnabled(True)
        self.file_first_multy = 0
        self.file_second_multy = 0
        option = self.options.index(self.comboBox.currentText())
        if option == 0:
            pass
        elif option == 1:
            self.btn_save.setEnabled(False)
            self.type_second_file = 'Image File (*.png *.jpg)'
            pass
        elif option == 2:
            self.btn_first.setEnabled(False)
            self.textBrowser.setText("▶ 두번째 버튼 이미지 파일 선택, 저장 경로 필수 지정(Select second button image file, specify save path required.)")
        elif option == 3:
            self.btn_save.setEnabled(False)
            self.file_second_multy += 1
            self.textBrowser.setText("▶ 첫번째 버튼 영상 파일 선택, 두번째 버튼 이미지 파일 선택(원본, 알파)*순서 중요, 저장 경로 필수 지정")
        
    def launchDialog(self):
        option = self.options.index(self.comboBox.currentText())
        if option == 0:
            pass
        elif option == 1:
            ImageBlendingOnVideo(self.file_first[0][0], self.file_second[0][0])
        elif option == 2:
            ImageMask(self.file_second[0][0], self.file_save[0])
        elif option == 3:
            video_path = self.file_first[0][0]
            directory = os.path.dirname(video_path) + "/out/"
            filename = os.path.basename(video_path)
            self.createFolder(directory)
            save_path = os.path.splitext(filename)
            save_path = "".join([directory, save_path[0], "_", time.strftime('%Y%m%d%H%M%S'), save_path[1]])
            ImageOnVideo(video_path, self.file_second[0][0], self.file_second[1][0], save_path)
        self.isCheckFile()
        
    def setFirstFile(self):
        response = self.selectFile()
        self.file_first.append(response)
        self.btn_first.setStyleSheet('border: 1px solid #09E65A')
        self.textBrowser.setText('▶' + str(response) +'\n'+ self.textBrowser.toPlainText())
        
    def setSecondFile(self):
        for _ in range(self.file_second_multy+1):
            response = self.selectFile()
            self.file_second.append(response)
        self.btn_second.setStyleSheet('border: 1px solid #09E65A')
        self.textBrowser.setText('▶' + str(response) +'\n'+ self.textBrowser.toPlainText())
        
    def setSavePath(self):
        response = QFileDialog.getSaveFileName(
            parent=self,
            caption='Select a file',
            dir=os.getcwd(),
        )
        self.file_save = response
        self.btn_save.setStyleSheet('border: 1px solid #09E65A')
        self.textBrowser.setText('▶' + str(response) +'\n'+ self.textBrowser.toPlainText())

    def isCheckFile(self):
        if not self.file_first:
            self.btn_first.setStyleSheet('border: 1px solid #EB3F00')
        if not self.file_second:
            self.btn_second.setStyleSheet('border: 1px solid #EB3F00')
            
    def selectFile(self):
        return QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a file',
            dir=os.getcwd(),
            # filter=file_filter,
            # selectedFilter =self.type_first_file
        )
        
    def createFolder(self, directory):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError:
            print("Error: os.makedirs > "+directory)
        
app = QApplication(sys.argv)
windows = Controller_Window()
windows.show()

app.exec_()