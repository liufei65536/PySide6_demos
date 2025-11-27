from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QLabel, QLineEdit, QSpinBox, QDateEdit,
                               QGridLayout, QPushButton)
import sys

class BuddyDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("setBuddy 示例 - 注册表单")
        self.resize(400, 200)

        # 中心部件和布局（用 QGridLayout 让标签与输入框对齐）
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QGridLayout(central_widget)
        layout.setSpacing(10)  # 控件间距
        layout.setContentsMargins(20, 20, 20, 20)  # 内边距

        # -------------------------- 1. 标签 + QLineEdit（文本输入）--------------------------
        name_label = QLabel("&Name（姓名）：")  # 快捷键 Alt+N
        name_edit = QLineEdit()
        name_label.setBuddy(name_edit)  # 绑定标签与输入框

        # -------------------------- 2. 标签 + QSpinBox（数字输入）--------------------------
        age_label = QLabel("&Age（年龄）：")  # 快捷键 Alt+A
        age_spin = QSpinBox()
        age_spin.setRange(0, 120)  # 年龄范围
        age_label.setBuddy(age_spin)  # 绑定

        # -------------------------- 3. 标签 + QDateEdit（日期选择）--------------------------
        birth_label = QLabel("&Birth（生日）：")  # 快捷键 Alt+B
        birth_edit = QDateEdit()
        birth_edit.setCalendarPopup(True)  # 弹出日历选择
        birth_label.setBuddy(birth_edit)  # 绑定

        # 提交按钮（非绑定控件，仅作演示）
        submit_btn = QPushButton("提交")

        # 添加控件到布局（行号，列号，跨行数，跨列数）
        layout.addWidget(name_label, 0, 0, 1, 1)
        layout.addWidget(name_edit, 0, 1, 1, 2)  # 输入框跨 2 列，更美观
        layout.addWidget(age_label, 1, 0, 1, 1)
        layout.addWidget(age_spin, 1, 1, 1, 2)
        layout.addWidget(birth_label, 2, 0, 1, 1)
        layout.addWidget(birth_edit, 2, 1, 1, 2)
        layout.addWidget(submit_btn, 3, 1, 1, 1)  # 按钮居中

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BuddyDemo()
    window.show()
    sys.exit(app.exec())