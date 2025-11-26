

开始收集官网教程中的案例

--2025.11.24 



# 其他资源

- [Qt for Python](https://doc.qt.io/qtforpython-6/)
- [Qt | 软件开发全周期的各阶段工具](https://www.qt.io/zh-cn/)

- [Pycharm配置pyside6 - hbr2 - 博客园](https://www.cnblogs.com/zlongJ/p/18951815)





### pycharm配置pyside工具

[Pycharm配置pyside6 - hbr2 - 博客园](https://www.cnblogs.com/zlongJ/p/18951815)

PyCharm 中 设置-->工具-->外部工具

#### 1.1 Qt Designer

名称：任意即可（建议pyside6-designer）

组：pyside6

程序：$PyInterpreterDirectory$/pyside6-designer.exe

实参：$FilePath$

工作目录：$FileDir$

#### 1.2 pyside6-rcc

名称：任意即可（建议ui2py,这样一目了然）

组：pyside6

程序：$PyInterpreterDirectory$/pyside6-rcc.exe

实参：$FileName$ -o $FileNameWithoutExtension$_rc.py

工作目录：$FileDir$

#### 1.3 pyside6-uic

名称：任意即可（建议pyside2-uic,理由同上）

组：pyside6

程序：$PyInterpreterDirectory$/pyside6-uic.exe

实参：$FileName$ -o $FileNameWithoutExtension$.py

工作目录：$FileDir$

