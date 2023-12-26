import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
from ui.ui_main import Ui_MainWindow
import os
import cv2
import time

class Controller_Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Controller_Window, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Controller')
        
        self.options = ('이미지 호출', '영상 불러오기')
        self.comboBox.addItems(self.options)
        
        btn =  self.file_button
        btn.clicked.connect(self.launchDialog)
        
        
    def launchDialog(self):
        option = self.options.index(self.comboBox.currentText())
        if option == 0:
            response = self.getImageFileName()
        elif option == 1:
            response = self.getVideoFileName()
        else:
            print('Got Nothing')
            
    def getImageFileName(self):
        # file_filter = 'Data File (*.xlsx *.csv *.dat);; Excel File (*.xlsx *.xls);; Image File (*.png *.jpg)'
        file_filter = 'Image File (*.png *.jpg)'
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a file',
            dir=os.getcwd(),
            filter=file_filter,
            selectedFilter ='Image File (*.png *.jpg)'
        )
        self.textEdit.setText(str(response))
        img_bgr = cv2.imread(response[0])
        cv2.namedWindow('img_bgr', flags=cv2.WINDOW_NORMAL)
        cv2.resizeWindow(winname='img_bgr', width=600, height=300)
        cv2.imshow("img_bgr", img_bgr)
        pause()
        
    def getVideoFileName(self):
        file_filter = 'Video File (*.mp4 *.avi)'
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a file',
            dir=os.getcwd(),
            filter=file_filter,
            selectedFilter ='Video File (*.mp4 *.avi)'
        )
        self.textEdit.setText(str(response))
        
        start_time = time.time()
        
        video1 = cv2.VideoCapture(response[0])
        # width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
        # height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = video1.get(cv2.CAP_PROP_FPS)
        delay = int(1000/fps)-10 #오차
        
        while True:
            ret1, frame1 = video1.read()
            if not ret1:
                break
            cv2.imshow("ImageP",frame1)

            k = cv2.waitKey(delay)
            if k == 27:
                break
            
        end_time = time.time()
        print(round(end_time-start_time,3))
        cv2.destroyAllWindows()

        
    def pause():
        keycode = cv2.waitKey(0)
        if keycode == 27:         
            cv2.destroyAllWindows()
        
app = QApplication(sys.argv)
windows = Controller_Window() #QWidget()
windows.show()

app.exec_()