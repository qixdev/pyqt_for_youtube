from pytube import YouTube
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import sys
from ui import Ui_MainWindow

class MainUI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainUI, self).__init__()

        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.Download)

    
    def Download(self):
        url = self.lineEdit.text() 
        exit_path = self.lineEdit_2.text()
        video = YouTube(url)
        if self.radioButton.isChecked() == True:
            res_dl = 0
            if self.radioButton_5.isChecked() == True:
                res = '480p'
                res_dl = 1
            elif self.radioButton_7.isChecked() == True:
                res = '720p'
                res_dl = 1
            elif self.radioButton_6.isChecked() == True:
                res = '1080p'
                res_dl = 1
            if res_dl == 1:
                stream = video.streams.filter(res=res).first()
            else:
                pass
            if self.radioButton_3.isChecked == True:
                stream = video.streams.get_highest_resolution()
            elif self.radioButton_3.isChecked == True:
                stream = video.streams.get_lowest_resolution()
        if self.radioButton_2.isChecked() == True:
            stream = video.streams.get_audio_only()
        if stream:
            stream.download(output_path = exit_path)
    
if __name__=='__main__':
    app = QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    app.exec_()
