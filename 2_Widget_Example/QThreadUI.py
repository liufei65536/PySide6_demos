from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QProgressBar, QPushButton, QVBoxLayout, QLabel)
from PySide6.QtCore import QThread, Signal, Qt, Slot
import sys
import time


# -------------------------- 1. 后台线程类（执行耗时任务，不碰 UI! QThread里改动UI会让程序崩溃）--------------------------
class BackgroundWorker(QThread):
    # 定义信号：用于向主线程发送进度更新（int 类型参数）和任务完成信号
    progress_updated = Signal(int)  # 进度信号（0-100）
    task_finished = Signal(str)  # 完成信号（返回结果）

    def run(self):
        total = 100  # 模拟任务总量
        for i in range(total + 1):
            # 模拟耗时操作（如网络请求、数据处理）
            time.sleep(0.05)
            # 发送进度信号（通过信号间接通知主线程更新 UI）
            self.progress_updated.emit(i)
        # 任务完成后发送结果信号
        self.task_finished.emit("后台任务执行完成！")


# -------------------------- 2. 主窗口类（UI 线程，接收信号并更新 UI）--------------------------
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.worker = None  # 存储后台线程实例

    def initUI(self):
        self.setWindowTitle("后台更新 UI 示例")
        self.resize(400, 200)

        #  UI 控件
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)  # 进度条范围 0-100
        self.status_label = QLabel("就绪状态")
        self.start_btn = QPushButton("启动后台任务")
        self.start_btn.clicked.connect(self.start_background_task)  # 绑定按钮点击事件

        # 布局
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.status_label, alignment=Qt.AlignCenter)
        layout.addWidget(self.start_btn)

    def start_background_task(self):
        # 1. 重置 UI 状态
        self.progress_bar.setValue(0)
        self.status_label.setText("任务执行中...")
        self.start_btn.setEnabled(False)  # 禁用按钮，防止重复点击

        # 2. 创建后台线程实例，绑定信号与槽
        self.worker = BackgroundWorker()
        self.worker.progress_updated.connect(self.update_progress_bar)
        self.worker.task_finished.connect(self.on_task_finished)
        # 线程结束后自动回收（避免内存泄漏）
        self.worker.finished.connect(self.worker.deleteLater)

        # 3. 启动线程（调用 run 方法）
        self.worker.start()

    @Slot()
    def update_progress_bar(self, progress):
        """接收进度信号，更新进度条（运行在主线程）"""
        self.progress_bar.setValue(progress)
        self.status_label.setText(f"进度：{progress}%")
    @Slot()
    def on_task_finished(self, result):
        """接收完成信号，更新状态（运行在主线程）"""
        self.status_label.setText(result)
        self.start_btn.setEnabled(True)  # 恢复按钮可用


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())