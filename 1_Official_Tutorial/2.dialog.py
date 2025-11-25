import sys
from PySide6.QtWidgets import (QLineEdit, QPushButton, QApplication,
    QVBoxLayout, QDialog)
from PySide6.QtCore import Slot

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.edit = QLineEdit("Write my name here")
        self.button = QPushButton("Show Greetings")
        # 创建layout 并添加widget进入
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        # Set dialog layout
        self.setLayout(layout)

        self.button.clicked.connect(self.greetings)

    @Slot()
    def greetings(self):
        print(f"Hello {self.edit.text()}")

if __name__ == '__main__':

    app = QApplication(sys.argv)

    form = Form()
    form.show()

    sys.exit(app.exec())