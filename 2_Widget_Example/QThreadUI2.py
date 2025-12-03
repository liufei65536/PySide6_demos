from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QProgressBar, QPushButton, QVBoxLayout, QLabel)
from PySide6.QtCore import QObject, QThread, Signal, Qt, Slot
import sys
import time


# -------------------------- 1. 任务逻辑类（封装耗时操作，继承 QObject）--------------------------
# QObject + moveToThread
class BackgroundTask(QObject):
    # 定义信号：与原版本一致（进度更新、任务完成）
    progress_updated = Signal(int)  # 进度信号（0-100）
    task_finished = Signal(str)  # 完成信号（返回结果）
    # 控制信号：用于外部触发任务开始
    start_task = Signal()  # 触发任务启动的信号

    def __init__(self, parent=None):
        super().__init__(parent)
        self.is_running = True  # 任务运行标记（用于优雅退出）

    @Slot()
    def run_task(self):
        """耗时任务的核心逻辑（被 start_task 信号触发，运行在子线程）"""
        self.is_running = True
        total = 100  # 模拟任务总量
        for i in range(total + 1):
            if not self.is_running:  # 检查是否需要退出
                self.task_finished.emit("任务已取消！")
                return

            # 模拟耗时操作（如网络请求、数据处理）
            time.sleep(0.05)
            # 发送进度信号（间接通知主线程更新 UI）
            self.progress_updated.emit(i)

        # 任务完成后发送结果信号
        self.task_finished.emit("后台任务执行完成！")

    def stop_task(self):
        """停止任务（优雅退出，运行在主线程）"""
        self.is_running = False


# -------------------------- 2. 主窗口类（UI 线程，管理线程和任务对象）--------------------------
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.init_thread_and_task()  # 初始化线程和任务对象

    def initUI(self):
        self.setWindowTitle("QObject+moveToThread 后台更新 UI 示例")
        self.resize(400, 200)

        # UI 控件（与原版本一致）
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.status_label = QLabel("就绪状态")
        self.start_btn = QPushButton("启动后台任务")
        self.stop_btn = QPushButton("取消任务")  # 新增取消按钮
        self.start_btn.clicked.connect(self.on_start_clicked)
        self.stop_btn.clicked.connect(self.on_stop_clicked)
        self.stop_btn.setEnabled(False)  # 初始禁用取消按钮

        # 布局
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.status_label, alignment=Qt.AlignCenter)
        # 按钮横向布局
        btn_layout = QVBoxLayout()
        btn_layout.addWidget(self.start_btn)
        btn_layout.addWidget(self.stop_btn)
        layout.addLayout(btn_layout)

    def init_thread_and_task(self):
        """初始化线程和任务对象（核心：分离线程与任务）"""
        # 1. 创建任务对象（封装耗时逻辑）
        self.background_task = BackgroundTask()
        # 2. 创建线程对象（仅负责提供线程执行环境，不写任务逻辑）
        self.worker_thread = QThread(self)  # 父对象绑定窗口，自动回收

        # 3. 关键：将任务对象移动到子线程（线程未启动时移动）
        self.background_task.moveToThread(self.worker_thread)

        # 4. 信号绑定（核心逻辑关联）
        # - 主线程：点击启动按钮 → 触发任务对象的 start_task 信号
        # - 任务对象：start_task 信号 → 执行 run_task 方法（子线程中）
        self.background_task.start_task.connect(self.background_task.run_task)

        # - 任务对象：进度/完成信号 → 主线程槽函数（更新 UI）
        self.background_task.progress_updated.connect(self.update_progress_bar)
        self.background_task.task_finished.connect(self.on_task_finished)

        # - 线程结束信号 → 线程自动回收（避免内存泄漏）
        self.worker_thread.finished.connect(self.worker_thread.deleteLater)

        # 5. 启动线程（此时线程是空闲的，需触发 start_task 才会执行任务）
        self.worker_thread.start()

    @Slot()
    def on_start_clicked(self):
        """启动任务（主线程执行）"""
        # 重置 UI 状态
        self.progress_bar.setValue(0)
        self.status_label.setText("任务执行中...")
        self.start_btn.setEnabled(False)
        self.stop_btn.setEnabled(True)

        # 触发任务开始（通过信号通知子线程执行 run_task）
        self.background_task.start_task.emit()

    @Slot()
    def on_stop_clicked(self):
        """停止任务（主线程执行）"""
        self.background_task.stop_task()  # 通知任务对象退出
        self.status_label.setText("正在取消任务...")
        self.stop_btn.setEnabled(False)

    @Slot(int)
    def update_progress_bar(self, progress):
        """接收进度信号，更新 UI（主线程执行）"""
        self.progress_bar.setValue(progress)
        self.status_label.setText(f"进度：{progress}%")

    @Slot(str)
    def on_task_finished(self, result):
        """接收完成信号，恢复 UI 状态（主线程执行）"""
        self.status_label.setText(result)
        self.start_btn.setEnabled(True)
        self.stop_btn.setEnabled(False)

    def closeEvent(self, event):
        """窗口关闭时，优雅停止线程（关键）"""
        # 停止任务
        self.background_task.stop_task()
        # 退出线程（等待任务完成后线程终止）
        self.worker_thread.quit()
        # 等待线程结束（最多等 1 秒）
        self.worker_thread.wait(1000)
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())