import sys
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import Slot

# 将函数作为槽
@Slot()
def say_hello():
 print("Button clicked, Hello!")


app = QApplication(sys.argv)

button = QPushButton("Click me")
button.clicked.connect(say_hello) # button.clicked是信号，调用connect连接到槽
button.show()

app.exec()