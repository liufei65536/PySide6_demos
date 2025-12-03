import PySide6
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                               QLineEdit, QLabel, QPushButton, QMenu)
from PySide6.QtCore import Qt, Slot, QRegularExpression, QPoint
from PySide6.QtGui import (QRegularExpressionValidator, QIntValidator,
                           QDoubleValidator, QAction)
import sys

class LineEditDemoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QLineEdit 全面功能示例")
        self.resize(500, 400)

        # 中心部件与主布局
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(30, 30, 30, 20)
        main_layout.setSpacing(20)

        # -------------------------- 1. 基础输入框（带占位符）--------------------------
        self.add_section_label("1. 基础输入框")
        basic_edit = QLineEdit()
        basic_edit.setPlaceholderText("请输入任意内容（基础输入框）")
        basic_edit.setClearButtonEnabled(True)  # 显示清除按钮（右侧×）
        main_layout.addWidget(basic_edit)
        #basic_edit.setText("123")

        # -------------------------- 2. 整数输入框（范围限制）--------------------------
        self.add_section_label("2. 整数输入框（1-100）")
        int_edit = QLineEdit()
        int_edit.setPlaceholderText("只能输入 1-100 的整数")
        # 设置整数验证器（范围 1-100）
        int_validator = QIntValidator(1, 100, self)
        int_edit.setValidator(int_validator)
        # 绑定文本变化信号（实时反馈）
        int_edit.textChanged.connect(lambda text: self.on_text_changed(int_edit, text))
        main_layout.addWidget(int_edit)

        # -------------------------- 3. 浮点数输入框（精度限制）--------------------------
        self.add_section_label("3. 浮点数输入框（0.00-100.00）")
        double_edit = QLineEdit()
        double_edit.setPlaceholderText("保留 2 位小数的浮点数")
        # 设置浮点数验证器（范围 0.00-100.00，精度 2 位）
        double_validator = QDoubleValidator(0.00, 100.00, 2, self)
        double_validator.setNotation(QDoubleValidator.Notation.StandardNotation)  # 标准表示法（不显示科学计数法）
        double_edit.setValidator(double_validator)
        double_edit.textChanged.connect(lambda text: self.on_text_changed(double_edit, text))
        main_layout.addWidget(double_edit)

        # -------------------------- 4. 手机号输入框（正则验证+掩码）--------------------------
        self.add_section_label("4. 手机号输入框（正则+掩码）")
        phone_edit = QLineEdit()
        # 方法1：掩码（强制格式，自动补全分隔符）
        phone_edit.setInputMask("999-9999-9999;_")  # 9 表示数字，;_ 表示占位符为下划线
        # 方法2：正则验证（补充格式校验，可选）
        #phone_re = QRegularExpression(r"^\d{3}-\d{4}-\d{4}$")
        #phone_validator = QRegularExpressionValidator(phone_re, self)
        #phone_edit.setValidator(phone_validator)
        main_layout.addWidget(phone_edit)

        # -------------------------- 5. 密码输入框 --------------------------
        self.add_section_label("5. 密码输入框")
        pwd_edit = QLineEdit()
        pwd_edit.setPlaceholderText("请输入密码（8-16位，含字母和数字）")
        pwd_edit.setEchoMode(QLineEdit.EchoMode.Password)  # 密码隐藏模式（显示圆点）
        # 密码正则验证（8-16位，字母+数字）
        pwd_re = QRegularExpression(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,16}$")
        pwd_validator = QRegularExpressionValidator(pwd_re, self)
        pwd_edit.setValidator(pwd_validator)
        # 切换密码可见性按钮
        self.pwd_visible_action = QAction("显", self)  #
        self.pwd_visible_action.setCheckable(True)
        self.pwd_visible_action.toggled.connect(lambda checked: self.toggle_pwd_visible(pwd_edit, checked))
        pwd_edit.addAction(self.pwd_visible_action, QLineEdit.ActionPosition.TrailingPosition)  # 按钮在输入框右侧
        main_layout.addWidget(pwd_edit)

        # -------------------------- 6. 带右键菜单的输入框 --------------------------
        self.add_section_label("6. 自定义右键菜单")
        custom_edit = QLineEdit()
        custom_edit.setPlaceholderText("右键点击查看自定义菜单")
        custom_edit.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)  # 启用自定义右键菜单
        custom_edit.customContextMenuRequested.connect(lambda pos: self.show_custom_menu(custom_edit, pos))
        main_layout.addWidget(custom_edit)

        # -------------------------- 7. 按钮触发获取输入内容 --------------------------
        self.result_label = QLabel("输入结果将显示在这里...", alignment=Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.result_label)

        get_value_btn = QPushButton("获取所有输入框内容")
        get_value_btn.clicked.connect(lambda: self.get_all_values(
            basic_edit, int_edit, double_edit, phone_edit, pwd_edit, custom_edit
        ))
        main_layout.addWidget(get_value_btn)

    def add_section_label(self, text):
        """添加分区标签（美化界面）"""
        label = QLabel(text)
        label.setStyleSheet("font-weight: bold; color: #2c3e50;")
        self.centralWidget().layout().addWidget(label)

    @Slot(QLineEdit, str)
    def on_text_changed(self, edit, text):
        """文本变化时实时校验（示例：整数/浮点数输入反馈）"""
        if not edit.validator():
            return
        # 验证输入是否合法
        valid = edit.hasAcceptableInput()
        # 合法则设置正常样式，非法则标红
        if valid:
            edit.setStyleSheet("border: 1px solid #ccc; padding: 5px;")
        else:
            edit.setStyleSheet("border: 1px solid red; padding: 5px; background-color: #fff8f8;")

    @Slot(QLineEdit, bool)
    def toggle_pwd_visible(self, pwd_edit, checked):
        """切换密码可见性"""
        if checked:
            pwd_edit.setEchoMode(QLineEdit.EchoMode.Normal)  # 显示明文
            self.pwd_visible_action.setText("隐")
            #self.pwd_visible_action.setText("🙈")  # 切换为“隐藏”表情
        else:
            pwd_edit.setEchoMode(QLineEdit.EchoMode.Password)  # 隐藏密码
            self.pwd_visible_action.setText("显")

    @Slot(QLineEdit,QPoint)
    def show_custom_menu(self, edit, pos):
        """显示自定义右键菜单"""
        menu = QMenu()
        # 添加默认菜单项（复制/粘贴/剪切）
        menu.addAction(QAction("复制", self, triggered=edit.copy))
        menu.addAction(QAction("粘贴", self, triggered=edit.paste))
        menu.addAction(QAction("剪切", self, triggered=edit.cut))
        menu.addSeparator()
        # 添加自定义菜单项
        clear_action = QAction("清空内容", self, triggered=edit.clear)
        menu.addAction(clear_action)
        # 在鼠标位置显示菜单
        menu.exec(edit.mapToGlobal(pos))

    def get_all_values(self, basic_edit, int_edit, double_edit, phone_edit, pwd_edit, custom_edit):
        """获取所有输入框内容并显示"""
        result = f"""
基础输入：{basic_edit.text() or '未输入'}
整数输入：{int_edit.text() or '未输入'}（合法：{int_edit.hasAcceptableInput()}）
浮点数输入：{double_edit.text() or '未输入'}（合法：{double_edit.hasAcceptableInput()}）
手机号输入：{phone_edit.text() or '未输入'}（合法：{phone_edit.hasAcceptableInput()}）
密码输入：{'*' * len(pwd_edit.text())}（合法：{pwd_edit.hasAcceptableInput()}）
自定义菜单输入：{custom_edit.text() or '未输入'}
        """
        self.result_label.setText(result.strip())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LineEditDemoWindow()
    window.show()
    sys.exit(app.exec())