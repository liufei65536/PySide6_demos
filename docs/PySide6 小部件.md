# PySide6 QtWidgets Qt小部件

`QtWidgets`是Qt创建用户界面的主要组成，它们可以显示数据，接收输入......。

## 窗口

窗口window：窗口是顶层widget，上面没有父组件（parent）了。通常窗口包含边框（frame）和标题栏(title bar)。在Qt中，`QMainWindow`和各种`QDialog` 子类是最常见的窗口类型。

- 程序的主窗口一般通过集成`QMainWindow`创建，`QMainWindow`拥有自己的布局，可以添加`menu bar`, `tool bars`, `dockable widgets`和 `status bar`。中心区域可以由任何类型的`QWidget`占据。
- 各种弹出窗口一般通过`QDialog`实现，Qt提供了多个标准对话框，可以用于选择文件或字体等标准任务。



[窗口和对话框组件 - Qt for Python](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-application-windows.html#window-and-dialog-widgets)

[PySide6.QtWidgets - Qt for Python](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/index.html#widgets)

[应用程序主窗口 - Qt for Python](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-mainwindow.html#application-main-window)

## 输入小部件

### 单行文本框 QLineEdit

[PySide6.QtWidgets.QLineEdit - Qt for Python](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QLineEdit.html#more)

QLineEdit是单行文本框，可以让用户输入一行文本。QLineEdit自带了一些编辑功能，可以进行复制、粘贴等。





```py
basic_edit = QLineEdit()

basic_edit.setPlaceholderText("请输入任意内容（基础输入框）") # 设置占位符
basic_edit.setText("123") # 设置文本
basic_edit.text() # 获取文本
basic_edit.setEchoMode(QLineEdit.Password)  # 密码隐藏模式（显示圆点）
```



**LineEdit总结**

| 功能类型   | 关键 API / 知识点                                            |
| ---------- | ------------------------------------------------------------ |
| 文本设置   | 设置文本 `setText()` 、获取文本 `text()`                     |
| 基础配置   | 占位提示 `setPlaceholderText()`、清除按钮`setClearButtonEnabled(True)` |
| 输入验证   | 整数范围`QIntValidator(i,j,lineEdit)`、`QDoubleValidator`（浮点数）、`QRegularExpressionValidator`（正则） <br />注：要在`PySide6.QtGui`中导入 |
| 合法性校验 | 验证输入符合规则`valid = hasAcceptableInput()`               |
| 格式限制   | 掩码`setInputMask()`<br />例：手机号分隔符`phone_edit.setInputMask("999-9999-9999;_") ` <br />注： 9 表示数字，;_ 表示占位符为下划线） |
| 密码模式   | 隐藏回显`setEchoMode(QLineEdit.EchoMode.Password)` 可以配合btn设置显示/隐藏。 |
| 信号绑定   | `textChanged`（文本变化）、                                  |
| 样式美化   | `setStyleSheet()`（边框、背景色）                            |





### 多行文本 QTextEdit

[PySide6.QtWidgets.QTextEdit - Qt for Python](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTextEdit.html#more)

`QTextEdit`是一个多行文本编辑器，支持HTML/Markdown格式，还可以显示图像、表格。

