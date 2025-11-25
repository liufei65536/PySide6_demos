import sys
from PySide6.QtWidgets import QApplication, QLabel

# 创建QApplication
app = QApplication(sys.argv)
# label，显示文字
label = QLabel("Hello World!")
label.show()
# main loop  程序入口
app.exec()