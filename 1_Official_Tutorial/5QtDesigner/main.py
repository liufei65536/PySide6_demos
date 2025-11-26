import sys

from PySide6.QtWidgets import QMainWindow, QApplication

from ui_mainwindow import Ui_DesignedWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_DesignedWindow() #加载
        self.ui.setupUi(self)     #设置ui

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())